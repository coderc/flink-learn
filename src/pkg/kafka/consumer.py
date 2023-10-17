import time
from kafka import KafkaConsumer

consumer = KafkaConsumer("my-topic", group_id='my-consumer-group_id-0',bootstrap_servers=['localhost:9093'])

for msg in consumer:
    print (msg)


class Consumer:
    config = {}
    consumer_id = ""
    consumer
    
    def __init__(self, config):
        self.setup(config)

    def setup(self, config):
        self.config = config
        self.consumer_id = self.config.topic.name + time.time_ns()
        self.consumer = KafkaConsumer(self.config.topic.name,
            group_id='group_id' + self.consumer_id,
            bootstrap_servers = self.config.bootstrap_servers)
    
    def getConsumer(self) -> consumer:
        return self.consumer
