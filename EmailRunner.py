__author__ = 'imacros'
import sys
from config import *
from Utilities import send_email_base, send_email


# from Utilities import ConfigManager
#get param value from config file
#####################################
# #set varialbles
# configFile = "config.cfg"
# configEmailSection = "email"
# subjParam = "subject"
# messageParam = "message"
# senderParam = "sender"
# recipientParam = "recipient"
# hostParam = "host"
# portParam = "port"
# usernameParam = "username"
# passwordParam = "password"
# #create object to get config file values
# configParamGetter = ConfigManager()
#
# #get email subject
# emailSubj = configParamGetter.readConfigFile(configFile, configEmailSection, subjParam)
# #get host
# host = configParamGetter.readConfigFile(configFile, configEmailSection, hostParam)
# #get message
# message = configParamGetter.readConfigFile(configFile, configEmailSection, messageParam)
# #get sender
# sender = configParamGetter.readConfigFile(configFile, configEmailSection, senderParam)




print 'Sending...'
server = send_email(subject, message, attachments,email_from, email_to, None, None, mail_server, port,email_from,password, usetsl)





