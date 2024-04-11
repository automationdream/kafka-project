from confluent_kafka import Producer
from dotenv import load_dotenv
import os
import argparse

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
}

# Get topic from environment variable
topic = os.getenv("KAFKA_TOPIC")

def produce(topic, config, value):
  # creates a new producer instance
  producer = Producer(config)

  # produces a sample message
  key = os.getenv("MESSAGE_KEY")
  producer.produce(topic, key=key, value=value)
  print(f"Produced message to topic {topic}: key = {key:12} value = {value:12}")

  # send any outstanding or buffered messages to the Kafka broker
  producer.flush()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Produce a message to a Kafka topic.')
  parser.add_argument('--message', type=str, required=True, help='The value of the message.')

  args = parser.parse_args()
  produce(topic, config, value=args.message)