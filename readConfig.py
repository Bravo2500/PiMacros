__author__ = 'imacros'
from Utilities import ConfigManager

#read config file
getConfig = ConfigManager()
emailSubject  = getConfig.readConfigFile("config/config.cfg","email","subject")
print emailSubject

