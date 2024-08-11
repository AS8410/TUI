import os
import getpass
import subprocess

def main_menu():
    print("\n\t\t\t\tWelcome to my project, this is the menu of Linux")
    print("\t\t\t\t--------------------------------------------")
    passwd = getpass.getpass("Enter your Password: ")
    if passwd == "ayush":
        user = input("Which user you want to go local/remote: ").strip().lower()
        if user == "local":
            local_menu()
        elif user == "remote":
            remote_menu()
        else:
            print("Invalid option. Please choose 'local' or 'remote'.")
    else:
        print("Authentication failed.")
        exit()

def local_menu():
    while True:
        print("""
            Press 1: To create a file
            Press 2: To create a folder
            Press 3: To show the date
            Press 4: To show the calendar
            Press 5: To install software
            Press 6: To exit
            Press 7: To go to Networking
        """)
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            create_file()
        elif choice == '2':
            create_folder()
        elif choice == '3':
            show_date()
        elif choice == '4':
            show_calendar()
        elif choice == '5':
            install_software()
        elif choice == '6':
            exit()
        elif choice == '7':
            networking_menu()
        else:
            print("Invalid choice. Please try again.")

def create_file():
    file_name = input("Enter your file name: ").strip()
    if file_name:
        subprocess.run(["touch", file_name])
    else:
        print("File name cannot be empty.")

def create_folder():
    folder_name = input("Enter your folder name: ").strip()
    if folder_name:
        subprocess.run(["mkdir", folder_name])
    else:
        print("Folder name cannot be empty.")

def show_date():
    subprocess.run(["date"])

def show_calendar():
    subprocess.run(["cal"])

def install_software():
    software_name = input("Enter your software name: ").strip()
    if software_name:
        subprocess.run(["yum", "install", software_name])
    else:
        print("Software name cannot be empty.")

def networking_menu():
    while True:
        print("""
            Press 1: To show your IP
            Press 2: To go to SSH
            Press 3: To go to SCP
            Press 4: To go to NAS storage
            Press 5: To go back to main menu
        """)
        choice = input("Choose your option: ").strip()
        if choice == '1':
            show_ip()
        elif choice == '2':
            ssh_menu()
        elif choice == '3':
            scp_menu()
        elif choice == '4':
            nas_menu()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def show_ip():
    subprocess.run(["ifconfig"])

def ssh_menu():
    remote_ip = input("Enter the remote IP: ").strip()
    remote_user = input("Enter the remote user: ").strip()
    command = input("Enter the command to execute: ").strip()
    if remote_ip and remote_user and command:
        subprocess.run(["ssh", f"{remote_user}@{remote_ip}", command])
    else:
        print("IP, user, and command cannot be empty.")

def scp_menu():
    source = input("Enter the source file: ").strip()
    destination = input("Enter the destination: ").strip()
    if source and destination:
        subprocess.run(["scp", source, destination])
    else:
        print("Source and destination cannot be empty.")

def nas_menu():
    print("NAS storage options are not implemented yet.")

def remote_menu():
    ip = input("Enter the remote IP: ").strip()
    while True:
        print("""
            Press 1: To create a file
            Press 2: To create a folder
            Press 3: To show the date
            Press 4: To show the calendar
            Press 5: To install software
            Press 6: To exit
        """)
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            remote_create_file(ip)
        elif choice == '2':
            remote_create_folder(ip)
        elif choice == '3':
            remote_show_date(ip)
        elif choice == '4':
            remote_show_calendar(ip)
        elif choice == '5':
            remote_install_software(ip)
        elif choice == '6':
            exit()
        else:
            print("Invalid choice. Please try again.")

def remote_create_file(ip):
    file_name = input("Enter your file name: ").strip()
    if file_name:
        subprocess.run(["ssh", ip, "touch", file_name])
    else:
        print("File name cannot be empty.")

def remote_create_folder(ip):
    folder_name = input("Enter your folder name: ").strip()
    if folder_name:
        subprocess.run(["ssh", ip, "mkdir", folder_name])
    else:
        print("Folder name cannot be empty.")

def remote_show_date(ip):
    subprocess.run(["ssh", ip, "date"])

def remote_show_calendar(ip):
    subprocess.run(["ssh", ip, "cal"])

def remote_install_software(ip):
    software_name = input("Enter your software name: ").strip()
    if software_name:
        subprocess.run(["ssh", ip, "yum", "install", software_name])
    else:
        print("Software name cannot be empty.")

if __name__ == "__main__":
    main_menu()
