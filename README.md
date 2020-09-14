# CodeOp-DA1-TechChallenge (5-6, Sep2020)

## Collect data

Data 1: Traffic state information by sections of the city of Barcelona. Available at [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/dataset/trams)

Data 2: Coordinates of traffic sections of Barcelona. Available at [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/es/dataset/transit-relacio-trams)

To visualize, query, retrieve, analyze geospatial data: [QGIS](https://www.qgis.org/en/site/)


## Build the docker image

```
docker build -t da-traffic .
```

## Run notebook server in docker

```bash
docker run -it --rm \
    -p 8888:8888 \
    -v $(pwd)/notebooks:/home/jovyan/notebooks \
    -v $(pwd)/data:/data/ \
    da-nlp-1 \
    jupyter notebook --notebook-dir /home/jovyan/notebooks
```
