# Traffic of Barcelona city

This is an extended project of 2-day technical challenge (5-6 Sep 2020) I was given during my 6-month Data Analytics Bootcamp (CodeOp, Barcelona).



## Collect data
All data files were saved under "./data" directory.

*Data 1: Traffic state information by sections of Barcelona city. Available at [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/trams)

*Data 2: Coordinates of traffic sections of Barcelona. Available at [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/es/dataset/transit-relacio-trams)



## Tools
* Software used to visualize, query, retrieve, analyze geospatial data: [QGIS](https://www.qgis.org/en/site/)
 
* Two docker containers for a PostGIS database and Jupyter notebook were created using a docker compose. To build the docker images, run the command below in your terminal.

```
docker-compse up
```


## TO DO
[X] Integrate a database and SQL to the previous project -> perform ETL

[] Improve the intepretation of the coordinates (dots -> lines)

[] Broaden the focus of spatial analysis (not only Av.Diagonal)
