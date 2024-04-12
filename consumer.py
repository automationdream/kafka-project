from confluent_kafka import Consumer
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Kafka config
config = {
    "bootstrap.servers": os.getenv("BOOTSTRAP_SERVERS"),
    "security.protocol": os.getenv("SECURITY_PROTOCOL"),
    "sasl.mechanisms": os.getenv("SASL_MECHANISMS"),
    "sasl.username": os.getenv("SASL_USERNAME"),
    "sasl.password": os.getenv("SASL_PASSWORD"),
    "session.timeout.ms": os.getenv("SESSION_TIMEOUT_MS"),
    "group.id": "mygroup",
    "auto.offset.reset": "earliest",
}

# Get topic from environment variable
topic = os.getenv("KAFKA_TOPIC")

def consume(topic, config):
    # creates a new consumer instance
    consumer = Consumer(config)

    # subscribes to the topic
    consumer.subscribe([topic])

    # consumes the message
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print('Received message: {}'.format(msg.value().decode('utf-8')))

    consumer.close()

if __name__ == "__main__":
    consume(topic, config)