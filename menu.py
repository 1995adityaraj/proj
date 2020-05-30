import os
import getpass

os.system("tput setaf 8")
print("\t\t\t Welcome to my TUI ")
os.system("tput setaf 7")
print("\t\t\t------------------------------------------------------")

passwd = getpass.getpass("Enter your Password:")
apass = "rhel"

if passwd != apass:
    print("authentication incorrect")
    exit()


print("where would you like to perform your job(local/remote): ",end='')
location = input()
print(location)

if location == "remote":
    remoteIP = input("enter your IP :")

while True:
        print("""press 1:To see Date
        press 2: To open Calculator
        press 3: To configure Web Server
        press 4: To create File
        press 5: To setup Network
        press 6: To Exit
        """)
        print("enter your  choice :",end ='')
        ch=input()
        print(ch)
        
        if location == "local":
            if int(ch) == 1:
                os.system("date")
            elif int(ch) == 2:
                os.system("cal")
            elif int(ch) == 3:
                os.system("yum install httpd")
            elif int(ch) == 4:
                os.system("can you enter name :" , end ='')
                create_user = input()
                os.system("useradd {}".format(create_user))
            elif int(ch) == 6:
                os.system("exit")
            else:
                print("option not supported")
            input("enter to continue . . . . . ")
            os.sytem("clear")
        elif location == "remote":
            if int(ch) == 1:
                os.system("ssh {0} date".format(remoteIP))
            elif int(ch) == 2:
                os.system("ssh {0} cal".format(remoteIP))
            elif int(ch) == 3:
                os.system("yum install httpd")
            elif int(ch) == 4:
                os.system("can you enter name :" , end ='')
                create_user = input()
                os.system("ssh {0} useradd {1}".format(remoteIP,create_user))
            elif int(ch) == 6:
                os.system("ssh {0}  exit".format(remoteIP))
            else:
                print("option not supported")
else:
    print("location doesnot supported")


