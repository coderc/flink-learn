from pyflink.table import EnvironmentSettings
from pyflink.common import configuration
from pkg.environment import envSingleton
from pkg.config_parser import confSingleton
from pkg.kafka.consumer import Consumer as KafkaConsumer

def init():
    kafka_config = confSingleton.yaml2Dict(envSingleton.getConfPath('kafka_config.yaml'))
    consumer = KafkaConsumer(kafka_config)
    for con in consumer.getConsumer():
        print (con)

def main():
    init()

# def f1():
#     config = configuration.Configuration()
#     config.set_string("parallelism.default", "128") \
#         .set_string("pipeline.auto-watermark-interval", "800ms") \
#         .set_string("execution.checkpointing.interval", "30s")

#     env_setting = EnvironmentSettings.new_instance() \
#         .in_streaming_mode() \
#         .with_built_in_catalog_name("my_catalog") \
#         .with_built_in_database_name("my_database") \
#         .with_configuration(config) \
#         .build()

#     print(env_setting.get_configuration())




if __name__=='__main__':
    main()