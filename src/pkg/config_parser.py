import yaml, os


class ConfigParser:

    def __init__(self):
        return

    def yaml2Dict(self, file_path):
        if file_path == "":
            return {}
        with open(file_path,'rb') as f:
            date = yaml.load(f, yaml.Loader)
            return date

confSingleton = ConfigParser()