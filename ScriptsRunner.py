__author__ = 'imacros'
# from Utilities import ImacrosRunner
import win32com.client
import os
import shutil
from Utilities import FileManager
from iMacrosVARS import *
from Utilities import EmailManager
from config import *
from Utilities import ZipFiles

def runImacros():
    imacrosAPP = win32com.client.Dispatch("imacros")
    #open IE browser
    imacrosInterface = imacrosAPP.iimOpen(browser)
    #get the scripts
    fileListsObj = FileManager()
    #auto translate the path
    fileList = fileListsObj.getFileNames(scriptFolder.replace('\\','\\\\') + "\\")

    #play imacros
    try:
        #if exist screenshot folder remove
        if os.path.isdir(screenshotFolder.replace('\\','\\\\')):
            try:
                shutil.rmtree(screenshotFolder.replace('\\','\\\\'))
            except IOError, e:
                print "Error NO.: " + e.errno
                print "OS error: " + e

        #if not exists make the folder
        os.mkdir(screenshotFolder.replace('\\','\\\\'))

        #loop the scripts folder and fun all scripts
        for file in fileList:
            #get the vars
            imacrosAPP.iimSet("USER_NAME", USER_NAME)
            imacrosAPP.iimSet("PASS_WORD", PASS_WORD)
            imacrosAPP.iimSet("APP_SERVER", APP_SERVER)
            imacrosInterface = imacrosAPP.iimPlay(scriptFolder.replace('\\','\\\\') + "\\" + file)
            #check success
            if imacrosInterface > 0:
                print "File: {} ran successfully.".format(file)
            else:
                imacrosError = imacrosAPP.iimGetErrorText()
                screenshot = imacrosAPP.iimTakeBrowserScreenshot(screenshotFolder.replace('\\','\\\\')+'\\' + file.translate(None,".iim")+".png",0)
                if screenshot == -1:
                    print "The file: {} Could not take screenshot".format(file)
                elif screenshot == -2:
                    print "Screenshot path is not correct"
                elif screenshot == -3:
                    print "System locked."
                print "iMacros Error: {}.".format(imacrosError)

          #if exist, delete
        if os.path.isfile("C:\\Users\\imacros\\Desktop\\imacrosFailed.zip"):
            try:
                os.remove("C:\\Users\\imacros\\Desktop\\imacrosFailed.zip")

            except Exception:
                print "cannot zip file"
        #zip files
        zipFolderObj = ZipFiles()
        zipFolderObj.zip(screenshotFolder, "C:\\Users\\imacros\\Desktop\\imacrosFailed")

    except Exception, e:
        print "Some error happened. PiMacros stopped for some reasons."
        print e
    #close the browser
    imacrosInterface = imacrosAPP.iimClose()
#------------------------end of  runImacros --------------------
#run imacros
runImacros();

#send email
pushEmail = EmailManager(message, sender, recipient, host, port, username, password, subject)
pushEmail.sendEmail(zipFolder)

