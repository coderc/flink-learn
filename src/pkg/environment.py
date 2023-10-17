import os

class Environment:
    env =  ""
    region = ""
    work_name = ""
    work_path = ""
    conf_path = ""


    def __init__(self):
        self.env = os.getenv("ENVIRONMENT", "Dev")
        self.region = os.getenv("REGION", "local")
        self.work_name = os.getenv("WORK_NAME", "invalid work name")
        self.work_path = os.path.abspath("")
        self.conf_path = os.path.join(self.work_path[:self.work_path.find(self.work_name)], self.work_name, 'configs')

    def getConfPath(self, file_name):
        return os.path.join(self.conf_path, file_name)


envSingleton = Environment()