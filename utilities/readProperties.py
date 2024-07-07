import configparser
config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
class ReadConfig:
    @staticmethod
    def getAppurl():
        url=config.get("commoninfo","baseUrl")
        return str(url)

    @staticmethod
    def getAdminemail():
        email = config.get("commoninfo", "userName")
        return str(email)

    @staticmethod
    def getAdminPassword():
        adpassword = config.get("commoninfo", "password")
        return str(adpassword)