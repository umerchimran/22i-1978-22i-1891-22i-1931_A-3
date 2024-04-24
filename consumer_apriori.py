from confluent_kafka import Consumer, KafkaError

def consume_messages(consumer, topic):

    consumer.subscribe([topic])
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            else:
                print(f"Apriori: Received message: {msg.value

().decode('utf-8')}")

                #  Apriori algorithm here
    finally:
        consumer.close()

if __name__ == "__main__":
    # Kafka configuration
    kafka_config = {
        'bootstrap.servers': 'localhost:9092',  

        'group.id': 'apriori_consumer_group',

        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(kafka_config)

    
    topic = 'amazon_metadata'

    
    consume_messages(consumer, topic)

