# Spark 3.5.4 and Kafka 3.9.0 Docker Environment

This repository provides a ready-to-use Docker environment combining Apache Spark and Kafka clusters for data streaming and processing applications. Perfect for development, testing, and learning distributed data processing architectures.

## Overview

This Docker setup includes:
- Apache Spark cluster (version 3.5.4) with:

  - Spark Master 

  - Spark History Server

  - Configurable number of Spark Workers

- Two Kafka clusters (version 3.9.0) with:

  - Two independent brokers

  - Kafbat UI for cluster management

## Prerequisites

- Docker and Docker Compose installed
- Python 3.11 or higher
- At least 4GB of available RAM
- 2GB of free disk space


## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/dnjfr/spark-kafka-docker
cd spark-kafka-docker
```

### 2. Set Up Python Environment
```bash
python -m venv .venv 
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Launch the Clusters

Start Spark master:
```bash
docker compose -f docker-compose-spark-master.yml up -d
```

Start first Kafka broker:
```bash
docker compose -f docker-compose-kafka-broker-1.yml up -d
```

Get the cluster ID for broker-1:
```bash
docker exec kafka-broker-1 cat /bitnami/kafka/data/meta.properties
```
Copy the cluster.id value to `kafka/conf/workaround.sh`

Start second Kafka broker:
```bash
docker compose -f docker-compose-kafka-broker-2.yml up -d
```

Launch remaining services:
```bash
docker compose up -d
```

### 4. Configure Kafbat UI

1. Access Kafbat UI at `http://localhost:8080`
2. Click "Configure new cluster"
3. For Broker 1:
   - Cluster name: `kafka-broker-1`
   - Bootstrap Servers: `kafka-broker-1`
   - Port: `9092`
4. Repeat for Broker 2 with appropriate values

## Usage Examples

### Running Spark Applications

Execute the sample script:
```bash
docker exec -it spark-master python /opt/spark/scripts/sample.py
```

Or submit a Spark job:
```bash
docker exec -it spark-master spark-submit --master spark://spark-master:7077 /opt/spark/scripts/sample.py
```

### Managing Kafka Topics

Create a topic via CLI:
```bash
docker exec -it kafka-broker-1 opt/bitnami/kafka/bin/kafka-topics.sh \
    --bootstrap-server localhost:9092 \
    --topic topic_1 \
    --create \
    --partitions 3 \
    --replication-factor 2
```

Alternatively, use Kafbat UI to create and manage topics.

### Working with Kafka Messages

#### Produce Messages (without key)
```bash
docker exec -it kafka-broker-1 opt/bitnami/kafka/bin/kafka-console-producer.sh \
    --bootstrap-server localhost:9092 \
    --topic topic_1
```
Example input:
```
Hello World
This is a test message
```

#### Produce Messages (with key)
```bash
docker exec -it kafka-broker-1 opt/bitnami/kafka/bin/kafka-console-producer.sh \
    --bootstrap-server localhost:9092 \
    --topic topic_1 \
    --property "parse.key=true" \
    --property "key.separator=;"
```
Example input:
```
1;First message
2;Second message
```

#### Consume Messages
```bash
docker exec -it kafka-broker-1 opt/bitnami/kafka/bin/kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic topic_1
```

## Troubleshooting

### Common Issues

1. **Spark Workers Not Connecting**
   - Verify network connectivity
   - Check logs: `docker logs spark-worker-1`
   - Ensure sufficient memory allocation

2. **Kafka Broker Communication Issues**
   - Verify cluster.id in workaround.sh
   - Check network settings in docker-compose files
   - Inspect broker logs: `docker logs kafka-broker-1`

### Health Checks

Check cluster status:
- Spark Master: `http://localhost:4040`
- Spark History: `http://localhost:18080`
- Spark UI (when running): `http://localhost:4040`
- Kafbat UI: `http://localhost:8080`


## Configuration

### Customizing Spark

Modify `sparkInit.py` for Spark settings:
```properties
spark.executor.memory=2g
spark.driver.memory=2g
```

### Scaling Workers

To add more Spark workers, update the `docker-compose.yml` by uncommenting workers


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Inspired by the work of:
- karlchris
- codersee-blog
- MaximeGillot

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.