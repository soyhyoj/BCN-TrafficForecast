import psycopg2

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


###########################################################3
# Functions for EDA

# A function to retrieve data from database using queries
# and save the result as a gdf (geodataframe)
def db_to_df(table_name, column_names):
    
    conn = connect_to_db()
    
    query = f"""
            select * from {table_name}
            limit 100
            """
    try:
        cur = conn.cursor()
        cur.execute(query)
        
    except psycopg2.DatabaseError: # print error if fails
        print ("Failed to create the dataframe")
    
    tupples = cur.fetchall() # a list of tupples
    cur.close()
    conn.close () # Close connection
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df