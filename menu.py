import subprocess
import re
import getpass

# ---------------- Utility Functions ----------------

def execute_command(command, shell=False):
    """Run a system command and handle exceptions."""
    try:
        result = subprocess.run(command, shell=shell, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr if e.stderr else 'No error message available'}")

def validate_ip(ip):
    """Validate an IP address."""
    ip_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(ip_regex, ip) is not None

# ---------------- Menus ----------------

def display_menu(title, options):
    """Display a menu and return the user's choice."""
    print(f"\n{title}")
    print("-" * len(title))
    for key, value in options.items():
        print(f"{key}: {value['desc']}")
    return input("Enter your choice: ").strip()

def main_menu():
    """Main menu for user authentication and entry point."""
    print("\nWelcome to the Linux Menu Project")
    passwd = getpass.getpass("Enter your Password: ")
    if passwd != "ayush":
        print("Authentication failed.")
        return
    
    while True:
        user_type = input("Choose user type (local/remote): ").strip().lower()
        if user_type == "local":
            local_menu()
            break
        elif user_type == "remote":
            remote_menu()
            break
        else:
            print("Invalid option. Please enter 'local' or 'remote'.")

def local_menu():
    """Local operations menu."""
    options = {
        '1': {'desc': 'Create a file', 'func': create_file},
        '2': {'desc': 'Create a folder', 'func': create_folder},
        '3': {'desc': 'Show the date', 'func': show_date},
        '4': {'desc': 'Show the calendar', 'func': show_calendar},
        '5': {'desc': 'Install software', 'func': install_software},
    }
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        choice = display_menu("Local Operations Menu", options)
        if choice in options:
            options[choice]['func']()
            attempts = 0  # reset attempts after a valid choice
        else:
            print("Invalid choice. Please try again.")
            attempts += 1
    print("Too many invalid attempts. Exiting menu.")
    
def networking_menu():
    """Networking operations menu."""
    options = {
        '1': {'desc': 'Show IP address', 'func': show_ip},
        '2': {'desc': 'SSH to a server', 'func': ssh_menu},
        '3': {'desc': 'SCP file transfer', 'func': scp_menu},
        '4': {'desc': 'NAS storage options', 'func': nas_menu},
        '5': {'desc': 'Back to main menu', 'func': main_menu},
    }
    while True:
        choice = display_menu("Networking Operations Menu", options)
        if choice in options:
            options[choice]['func']()
        else:
            print("Invalid choice. Please try again.")

def remote_menu():
    """Remote operations menu."""
    ip = input("Enter the remote IP: ").strip()
    if not validate_ip(ip):
        print("Invalid IP address.")
        return
    # Similar to `local_menu` but with remote operations.

# ---------------- Operations ----------------

def create_file():
    """Create a new file."""
    file_name = input("Enter file name: ").strip()
    if file_name:
        execute_command(["touch", file_name])
    else:
        print("File name cannot be empty.")

def create_folder():
    """Create a new folder."""
    folder_name = input("Enter folder name: ").strip()
    if folder_name:
        execute_command(["mkdir", folder_name])
    else:
        print("Folder name cannot be empty.")

def show_date():
    """Display the current date."""
    execute_command(["date"])

def show_calendar():
    """Display the calendar."""
    execute_command(["cal"])

def install_software():
    """Install software based on the system."""
    software_name = input("Enter software name: ").strip()
    if software_name:
        execute_command(["sudo", "apt", "install", software_name, "-y"])
    else:
        print("Software name cannot be empty.")

def show_ip():
    """Show the current IP address."""
    execute_command("ifconfig | grep inet | awk 'NR==1 { print $2 }'", shell=True)

def ssh_menu():
    """SSH into a remote machine."""
    remote_ip = input("Enter remote IP: ").strip()
    remote_user = input("Enter remote user: ").strip()
    command = input("Enter command to execute: ").strip()
    if remote_ip and remote_user and command:
        execute_command(["ssh", f"{remote_user}@{remote_ip}", command])
    else:
        print("IP, user, and command cannot be empty.")

def scp_menu():
    """Transfer files using SCP."""
    source = input("Enter source file: ").strip()
    destination = input("Enter destination: ").strip()
    if source and destination:
        # Sanitize inputs to prevent command injection
        source = re.escape(source)
        destination = re.escape(destination)
        execute_command(["scp", source, destination])
    else:
        print("Source and destination cannot be empty.")

def nas_menu():
    """Placeholder for NAS storage options."""
    print("NAS storage options are not implemented yet.")

# ---------------- Main Program ----------------

if __name__ == "__main__":
    main_menu()
