import os
import getpass
os.system("tput setaf 6")
print("\t\t\t\tWelcome to my project this is menu of linux")
print("\t\t\t\t--------------------------------------------")
passwd=getpass.getpass("Enter your Password : ")
if passwd == "ayush":
    user=input("Which user you want to go local/remote :")
    if user == "local":   
        print(""" 
                Press 1: To create a file
                Press 2: To Create a folder
                Press 3: To show your date
                Press 4: To show cal
                Press 5: To install your software
                Press 6: To exit
                Press 7: To go Networking
            """)
        while True:
            ch=input("Enter your choice: ")
            if int(ch) == 1:
                file_name=input("Enter your file name :")
                os.system("touch {0}".format(file_name))
            elif int(ch) == 2:
                fold_name=input("Enter your folder name :")
                os.system("mkdir {0}".format(fold_name))
            elif int(ch) == 3:
                os.system("date")
            elif int(ch) == 4:
                os.system("cal")
            elif int(ch) == 5:
                soft_name=input("Enter your software name: ")
                os.system("yum install {0}".format(soft_name))
            elif int(ch) == 6:
                exit()
            elif int(ch) == 7:
                print("""
                    Press 1: To show your IP 
                    Press 2: To go to ssh
                    Press 3: To go to scp
                    Press 4: To go to NAS storage
                    """)
                networking=input("Choose your option: ")
                if int(networking) == 1:
                    os.system("ifconfig")
                elif int(networking) == 2:
                    print(""" 
                    Press 1: To Send your cmd to remote system
                    Press 2: To login your remote system 
                    """)
                    ssh_remote_system=input("Enter your choice :")
                    if int(ssh_remote_system) == 1:
                        ssh_remote_user=input("Enter your user name : ")
                        ssh_remote_ip=input("Enter your IP : ")
                        ssh_remote_cmd=input("Enter your CMD :")
                        os.system("ssh {0}@{1} {2}".format(ssh_remote_user, ssh_remote_ip, ssh_remote_cmd))
                    elif int(ssh_remote_system) == 2:
                        ssh_remote_login_user=input("Enter your user name :")
                        ssh_remote_login_IP=input("Enter your IP :")
                        os.system("ssh -l {0} {1} ".format(ssh_remote_login_user, ssh_remote_login_IP))
                        print("something")
            else:
                print("Option not support")
    elif user == "remote":
        ip=input("Enter your IP :")
        print("""
                Press 1: To create a file
                Press 2: To Create a folder
                Press 3: To show your date
                Press 4: To show cal
                Press 5: To install your software
                Press 6: To exit
                """)
        ch=input("Enter your choice: ")
        if int(ch) == 1:
            file_name=input("Enter your file name :")
            os.system("ssh {0} touch {1}".format(ip,file_name))
        elif int(ch) == 2:
            fold_name=input("Enter your folder name :")
            os.system("ssh {0} mkdir {1}".format(ip,fold_name))
        elif int(ch) == 3:
            os.system("ssh {0} date".format(ip))
        elif int(ch) == 4:
            os.system("cal {0}".format(ip))
        elif int(ch) == 5:
            soft_name=input("Enter your software name: ")
            os.system("ssh {0} yum install {1}".format(ip,soft_name))
        elif int(ch) == 6:
            exit()
        else:
            print("Option not support")
    else:
            print("Option not support")
else:
    print("authentication failed")
    exit()
