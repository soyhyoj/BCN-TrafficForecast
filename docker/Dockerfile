# Start from a basic image.
FROM jupyter/base-notebook:python-3.7.6


# Install requirements. No cache to lower the image size.
RUN pip install --no-cache psycopg2-binary \
	sqlalchemy \
	geoalchemy2==0.8.4\
	geopandas==0.8.0\
	geojson==2.5.0\
	geopy==2.0.0 \
	shapely \
	fiona \
	pyproj==3.0.0\
	descartes==1.1.0 \
	contextily==1.0.1 \
	mapclassify==2.3.0\
	pandas==1.1.1 \
	numpy==1.19.1 \
	scipy==1.4.1 \
	matplotlib==3.3 \
	seaborn==0.10.0 \
	scikit-learn==0.23.2

VOLUME /notebooks
WORKDIR /notebooks