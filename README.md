# Spark 3.5.4 and Kafka 3.9.0 Docker ready to use

## Getting Started

**1.** Clone the repository:
```bash
git clone https://github.com/dnjfr/spark-kafka-docker
cd spark-kafka-docker
```

**2.** Create and activate virtual environment:
```bash
python -m venv .venv 
source .venv/bin/activate  # On Windows: .venv/Scripts/activate
```

**3.** Launch these two docker compose :
```bash
docker compose -f docker-compose-spark-master.yml up -d   

docker compose -f docker-compose-kafka-broker-1.yml up -d 
```

**4.** Retrieve the cluster.id of broker-1
```bash
docker exec kafka-broker-1 cat /bitnami/kafka/data/meta.properties
```
Paste it into the `workaround.sh` file in `kafka/conf` dir

**5.** Then launch the docker compose broker-2
```bash
docker compose -f docker-compose-kafka-broker-2.yml up -d 
```

**6.** Finally, on project root, launch docker compose to create spark-history-server, spark-worker-1 (or more), kafbat-ui
```bash
docker compose up -d
```

## Commands

### Run spark inside container
```bash
docker exec -it spark-master python /opt/spark/scripts/script_sample.py
 or
docker exec -it spark-master spark-submit --master spark://spark-master:7077 /opt/spark
```

### Create Kafka topics

### Create Kakfa messages


## Greetings
Inspired by the work of karlchris, codersee-blog and MaximeGillot, thanks to them