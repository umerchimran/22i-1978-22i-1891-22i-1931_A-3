from confluent_kafka import Producer
import json
import time

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def _messages(producer, topic, data):
    for entry in data:
        producer.produce(topic, json.dumps(entry), callback=delivery_report)
        time.sleep(0.1)  
    producer.flush()


if __name__ == "__main__":
    kafka_config = {
        'bootstrap.servers': 'localhost:9092',   address
    }

    producer = Producer(kafka_config)

    with open('preprocessed_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    topic = 'amazon_metadata'
    _messages(producer, topic, data)


    producer.flush()


