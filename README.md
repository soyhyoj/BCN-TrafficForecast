# Traffic of Barcelona city

This is an extended project of 2-day technical challenge (5-6 Sep 2020) I was given during my 6-month Data Analytics Bootcamp (CodeOp, Barcelona).

-----------------------------

## Collect data

Data 1: Traffic state information by sections of the city of Barcelona. Available at [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/trams)

Data 2: Coordinates of traffic sections of Barcelona. Available at [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/es/dataset/transit-relacio-trams)

Software used to visualize, query, retrieve, analyze geospatial data: [QGIS](https://www.qgis.org/en/site/)

All csv files were saved in a folder called 'data' under this directory
```
./data
```

--------------------------

## Build the docker image

```
docker-compse up
```

## TO DO
[X] Integrate a database and SQL to the previous project -> perform ETL

[] Improve the intepretation of the coordinates (dots -> lines)

[] Broaden the focus of spatial analysis (not only Av.Diagonal)
