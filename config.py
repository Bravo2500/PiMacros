__author__ = 'imacros'
from getpass import getpass
import sys
browser = "-ie"
cmdTimeout = 60
scriptFolder = "C:\Users\imacros\Desktop\imacros\Temp"
screenshotFolder = "C:\Users\imacros\Desktop\screenshots"
zipFolder = "C:\Users\imacros\Desktop\imacrosFailed.zip"

#email vars
name = "Jason Z"
email_from = "3231174@student.rmit.edu.au"
password = 'W0rkfl0w5'
mail_server = "smtp.gmail.com"
port = 587
email_to = "3231174@student.rmit.edu.au"
to_name = "joydesigner"
subject = 'Sending mail easily with Python'
message = 'here is the message body python test2'
attachments = [sys.argv[0]]
usetsl ="true"
email_cc = None
email_bcc = None



