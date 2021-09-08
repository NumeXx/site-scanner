#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NXScan v1.0
# Coded By : NumeX....

import requests, sys, re, os
from colorama import *

def commonPorts(site):
    os.system('cls || clear')
    if site.startswith("http://") or site.startswith("https://"):
        sys.exit("Dont Use : http:// | https://")

    else:
        requ = requests.post("https://www.portcheckers.com/portscan-result", data={'server': site, "quick": "false"})
        resp = requ.text
        output = re.sub('<pre>|\t|</pre>|<div style="margin:10px 0 20px 0;"><h3>Port Scan Result</h3>|'
                    '<span style="display: inline-block;width:200px;">|</span><span class="label label-danger">|</span>'
                    '|<span class="label label-success">|', '', resp).strip().lstrip()

        output = output.replace("Not Available", " Not Available")
        print(f"├── Host : {Fore.RED}{site}{Fore.RESET}")
        for lines in str(output).splitlines():
            print(f"-> {Fore.LIGHTYELLOW_EX}{lines}{Fore.RESET}")

def reverseIP(site):
    os.system('cls || clear')
    if site.startswith("http://") or site.startswith("https://"):
        sys.exit("Dont Use : http:// | https://")

    else:
        requ = requests.get("https://api.hackertarget.com/reverseiplookup/?q="+site)
        resp = requ.text

        output = resp
        print(f"├── Host : {Fore.RED}{site}{Fore.RESET}")
        for lines in str(output).splitlines():
            print(f"-> {Fore.LIGHTYELLOW_EX}{lines}{Fore.RESET}")

## ./START http Header ##
def httpHeader(site):
    os.system('cls || clear')
    if site.startswith("http://") or site.startswith("https://"):
        sys.exit("Dont Use : http:// | https://")
    
    else:
        requ = requests.get("https://api.hackertarget.com/httpheaders/?q="+site)
        resp = requ.text
        output = resp.strip().lstrip()
        print(f"├── Host : {Fore.RED}{site}{Fore.RESET}")
        for lines in str(output).splitlines():
            print(f"-> {Fore.LIGHTYELLOW_EX}{lines}{Fore.RESET}")
## ./END http Header ##

## ./START TCP Port Scan ##
def TCPport(site):
    os.system('cls || clear')
    if site.startswith("http://") or site.startswith("https://"):
        sys.exit("Dont Use : http:// | https://")
    
    else:
        requ = requests.get("https://api.hackertarget.com/nmap/?q="+site)
        resp = requ.text
        output = resp.strip().lstrip()
        print(f"├── Host : {Fore.RED}{site}{Fore.RESET}")
        for lines in str(output).splitlines():
            print(f"-> {Fore.LIGHTYELLOW_EX}{lines}{Fore.RESET}")
## ./END TCP Port Scan ##

## ./START Extract Links from Page ##
def ELFP(site):
    os.system('cls || clear')
    if site.startswith("http://") or site.startswith("https://"):
        sys.exit("Dont Use : http:// | https://")

    else:
        requ = requests.get("https://api.hackertarget.com/pagelinks/?q="+site)
        resp = requ.text
        output = resp.strip().lstrip()
        print(f"├── Host : {Fore.RED}{site}{Fore.RESET}")
        for lines in str(output).splitlines():
            print(f"-> {Fore.LIGHTYELLOW_EX}{lines}{Fore.RESET}")
## ./END Extract Links from Page ##

## ./START Extract Links from Page ##
def IPlocation(site):
    os.system('cls || clear')
    if site.startswith("http://") or site.startswith("https://"):
        sys.exit("Dont Use : http:// | https://")
    
    else:
        requ = requests.get("https://api.hackertarget.com/geoip/?q="+site)
        resp = requ.text
        output = resp.strip().lstrip()
        print(f"├── Host : {Fore.RED}{site}{Fore.RESET}")
        for lines in str(output).splitlines():
            print(f"-> {Fore.LIGHTYELLOW_EX}{lines}{Fore.RESET}")

## ./END Extract Links from Page ##

## ./START DNS lookup ##
def DNSlookup(site):
    os.system('cls || clear')
    if site.startswith("http://") or site.startswith("https://"):
        sys.exit("Dont Use : http:// | https://")
    
    else:
        requ = requests.get("https://api.hackertarget.com/dnslookup/?q="+site)
        resp = requ.text
        output = re.sub(';; Truncated, retrying in TCP mode.', '', resp).strip().lstrip()
        print(f"├── Host : {Fore.RED}{site}{Fore.RESET}")
        for lines in str(output).splitlines():
            print(f"-> {Fore.LIGHTYELLOW_EX}{lines}{Fore.RESET}")
## ./END DNS lookup ##

def main():
    print(f"""
[ ! ] {Fore.LIGHTCYAN_EX}Site-Scanner By NumeX{Fore.RESET}
[ ! ] {Fore.LIGHTCYAN_EX}Coded in Python 3+{Fore.RESET}
    \n""")
    web = str(input(f"[ ? ] {Fore.LIGHTGREEN_EX}Enter Target : {Fore.RESET}"))
    print(f''' 
-> [1] {Fore.RED}Nmap | TCP Port Scan{Fore.RESET}
-> [2] {Fore.YELLOW}Scan common ports{Fore.RESET}
-> [3] {Fore.GREEN}Reverse IP{Fore.RESET}
-> [4] {Fore.BLUE}HTTP Header{Fore.RESET}
-> [5] {Fore.LIGHTBLUE_EX}DNS lookup{Fore.RESET}
-> [6] {Fore.LIGHTGREEN_EX}IP Location{Fore.RESET}
-> [7] {Fore.LIGHTYELLOW_EX}Extract Links from Page{Fore.RESET}
-> [0] {Fore.LIGHTRED_EX}EXIT{Fore.RESET}''')

    chose = int(input(f'\n{Fore.LIGHTGREEN_EX}[ ? ] Enter Your Choice : {Fore.RESET}'))

    if chose == 1:
        TCPport(web)
    elif chose == 2:
        commonPorts(web)
    elif chose == 3:
        reverseIP(web)
    elif chose == 4:
        httpHeader(web)
    elif chose == 5:
        DNSlookup(web)
    elif chose == 6:
        IPlocation(web)
    elif chose == 7:
        ELFP(web)
    elif chose == 0:
        sys.exit(0)
    else:
        print(f"{Fore.RED}[-] Incorect{Fore.RESET}")
        main()

    returnChose = str(input(f"\n{Fore.LIGHTGREEN_EX}[ ? ] Do You Want To Continue? [Y/T] : {Fore.RESET}"))
    if returnChose == 'Y' or returnChose == 'y':
        main()
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()