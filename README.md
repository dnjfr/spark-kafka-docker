# Spark 3.5.4 and Kafka 3.9.0 Docker ready to use

## First time setup

git clone https://github.com/dnjfr/spark-kafka-docker
cd spark-kafka-docker

Launch these two docker compose :

docker compose -f docker-compose-spark-master.yml up -d   
docker compose -f docker-compose-kafka-broker-1.yml up -d 

Retrieve the cluster.id of broker-1
docker exec kafka-broker-1 cat /bitnami/kafka/data/meta.properties

Paste it into the workaround.sh file in kafka/conf dir

Then launch the docker compose broker-2
docker compose -f docker-compose-kafka-broker-2.yml up -d 


Finally, on project root, launch docker compose to create spark-history-server, spark-worker-1 (or more), kafbat-ui 
docker compose up -d


## Commands

## Run spark inside container

docker exec -it spark-master python /opt/spark/scripts/script_sample.py
 or
docker exec -it spark-master spark-submit --master spark://spark-master:7077 /opt/spark

## Greetings
Inspired by the work of karlchris, codersee-blog and MaximeGillot, thanks to them