import psycopg2
import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine

########################################################################
# Functions for ETL #
########################################################################

# Define a function connect to the database 'bcn_traffic'
# In case the connecting attempt fails, print the error message
def connect_to_db():
    try:
        #conn for connection
        conn =  psycopg2.connect(dbname='bcn_traffic',
                                 user='bcn',
                                 password='bcn',
                                 host='postgis',
                                 port='5432')

    except psycopg2.DatabaseError:
        print ("I am unable to connect the database")
    return conn

# Function to create a table inside the PostGIS database
def create_table(query):
    # connect to the db
    conn = connect_to_db()

    try:
        cur = conn.cursor()  # initiate cursor (communication with db)
        #print('Connected')
        cur.execute(query)   # execute the query
        #print('Query executed')
        conn.commit()

    except psycopg2.DatabaseError: # print error if fails
        print ("Failed to create the table")

    # Close the communication & connection with the postgis
    finally:
        cur.close()
        conn.close ()

# Function to fill the previously created tables
def fill_table_with_data(query, filepath):
    # connect to the db
    conn = connect_to_db()

    try:
        cur = conn.cursor()
        
        with open(filepath, 'r') as file:
           
            next(file) # Skip header

            cur.copy_expert(query, file)
            
            conn.commit() # commit the changes to the db

    # Print error message if query fails
    except psycopg2.DatabaseError:
        print ("Failed to copy data to the table")

    finally:
        cur.close()
        conn.close ()
        #print('Connection closed')

# Function to create connection using SQLALchemy
def prepare_engine():
    return create_engine('postgresql://bcn:bcn@postgis:5432/bcn_traffic')


### End of ETL ###
# To check the database using terminal:
# 1. docker exec -it bcn-trafficforecast_postgis_1 bash
# 2. psql postgresql://bcn:bcn@postgis:5432/bcn_traffic


########################################################################
# Functions for EDA #
########################################################################

# A function to retrieve data from database using queries
# and save the result as a df 
def db_to_df(query, column_names):
    conn = connect_to_db()

    try:
        cur = conn.cursor()
        cur.execute(query)
        
    except psycopg2.DatabaseError: # print error if fails
        print ("Failed to execute the query")
    
    tupples = cur.fetchall() # a list of tupples
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    cur.close()
    conn.close () # Close connection
    return df

# Function to retrieve data from database using queries
# and save the result as a gdf (geodataframe)
def db_to_gdf(query, geometry):
    conn = connect_to_db()
    
    try:
        # Save the query result as a geodataframe
        gdf = gpd.read_postgis(query, conn, geom_col=geometry)

    except psycopg2.DatabaseError: # print error if fails
        print ("Failed to execute the query")

    conn.close () # Close connection
    return gdf