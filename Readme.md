# Kafka Producer and Consumer

This project contains a Kafka producer and consumer implemented in Python. The producer sends messages to a Kafka topic, and the consumer reads those messages.

## Requirements

This project requires Python 3.9 or later. The required Python packages are:

- `confluent-kafka==2.3.0`
- `python-dotenv==1.0.1`

You can install these packages with pip:

```bash
pip install -r requirements.txt
```

## Running the Producer and Consumer with Docker Compose

```bash
docker-compose up
```

### Environment Variables
This project uses the following environment variables:

* BOOTSTRAP_SERVERS: The address of the Kafka.
* SECURITY_PROTOCOL: The security protocol to use. - SASL_MECHANISMS: The SASL mechanism to use.
* SASL_USERNAME: The SASL username.
* SASL_PASSWORD: The SASL password.
* SESSION_TIMEOUT_MS: The session timeout, in milliseconds.
* KAFKA_TOPIC: The Kafka topic to produce to and consume from.
* MESSAGE_KEY: The key of the message to produce.
* MESSAGE_VALUE: The value of the message to produce.

You can set these environment variables in a .env file.

## License
This project is licensed under the MIT License - see the LICENSE file for details.