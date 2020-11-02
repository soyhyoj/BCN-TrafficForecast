# CodeOp-DA1-TechChallenge (5-6, Sep 2020)

This is a 2-day technical challenge I was given during my 6-month Data Analytics Bootcamp (CodeOp).
Results are summarized as presentation format in the ['BCN_traffic_report.pdf'](https://github.com/soyhyoj/BCN-TrafficForecast/blob/master/BCN_traffic_report.pdf) file of this repo.


## Collect data

Data 1: Traffic state information by sections of the city of Barcelona. Available at [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/trams)

Data 2: Coordinates of traffic sections of Barcelona. Available at [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/es/dataset/transit-relacio-trams)

Software used to visualize, query, retrieve, analyze geospatial data: [QGIS](https://www.qgis.org/en/site/)

All csv files were saved in a folder called 'data' under this directory
```
./data
```

## Build the docker image

```
docker build -t da-traffic .
```

## Run notebook server in docker

```bash
docker run -it --rm \
    -p 8888:8888 \
    -v $(pwd):/home/jovyan/notebooks \
    -v $(pwd)/data:/data/ \
    da-traffic \
    jupyter notebook --notebook-dir /home/jovyan/notebooks
```

## TO DO
[] Integrate a database and SQL to the project

[] Improve the intepretation of the coordinates

[] Broaden the focus of analysis (not only Av.Diagonal)
