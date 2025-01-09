#!/bin/bash

# Wait for the data folder to be created
while [ ! -d "/bitnami/kafka/data" ]; do
    mkdir -p /bitnami/kafka/data
    sleep 1
done

# Edit the meta.properties file with the correct cluster.id
cat > /bitnami/kafka/data/meta.properties << EOF
#
#$(date)
node.id=1
version=1
cluster.id=<enter cluster id from broker 1 here>
EOF

# Start the Kafka process normally
exec /opt/bitnami/scripts/kafka/entrypoint.sh /opt/bitnami/scripts/kafka/run.sh