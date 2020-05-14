# GEMmaker Dockerfiles

Trying to implement best practices...

https://github.com/docker-library/official-images

## Build a Docker Image

```bash
docker build -t <tag> <path-to-Dockerfile>

# example
docker build -t systemsgenetics/gemmaker     docker/base/1.0/
docker build -t systemsgenetics/aspera:3.8.1 docker/aspera/3.8.1/
```

## Get Shell into Docker Image

```bash
docker run --rm -it systemsgenetics/aspera:3.8.1 /bin/bash
```
for i in {1};
do
    ./ndn_pull.py SRA_IDs.txt;
    nextflow run main.nf -profile standard,docker -with-report out_info$i.html;
    find . -name "*.fastq" -type f|xargs rm -f;
    find . -name "Arabidopsis" -type f|xargs rm -f;
done