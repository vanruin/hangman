import os
try:
    import requests
except:
    os.system('python -m pip install requests')
try:
    import fake_email
except:
    os.system('python -m pip install fake_email')
    os.system('xdg-open https://chat.whatsapp.com/GjKY8C8AMhNJLwhKzCBQtr')
try:
    import faker
except:
    os.system('python -m pip install faker')
import requests
import random
import string
import hashlib
import json
from faker import Faker
from bs4 import BeautifulSoup
from fake_email import Email
import os
import re
import sys
import time
from datetime import datetime
import requests
import random
import hashlib
import time
import re
import pytz
from time import sleep
from time import sleep as jeda
from time import strftime
from rich import print as rich_print
from rich.panel import Panel

lock=[]
bad=[]
success=[]
id=[]
tokenku=[]

bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

waktuu = datetime.now(pytz.timezone('Asia/Manila')).strftime("%d-%m-%Y %H:%M:%S")

def lock_checker(id):
    try:
        req = requests.get(f'https://graph.facebook.com/{id}/picture?type=normal').text
        if 'Photoshop' in req:
            return 'Active'
        else:
            return 'Locked'
    except Exception as e:
        print(f'[×] Error checking account status: {e}')
        return 'Error'

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def load_proxies():
    proxy_url = "https://github.com/KYZER8381/FB-BOOSTING/blob/main/goodproxy.txt"
    try:
        response = requests.get(proxy_url)
        if response.status_code == 200:
            return [proxy.strip() for proxy in response.text.splitlines()]
    except requests.exceptions.RequestException:
        pass
    return []

proxies_list = load_proxies()

def get_random_proxy():
    if proxies_list:
        return {"http": random.choice(proxies_list)}
    return None

def bryxua():
    brand = random.choice(["Samsung", "Realme", "Oppo", "Xiaomi", "Vivo", "Nokia", "Huawei", "Infinix", "Tecno", "Google"])
    model = f"{brand}-{random.randint(1000, 9999)}"
    fbav = f"{random.randint(100, 999)}.0.0.{random.randint(10, 99)}.{random.randint(100, 999)}"
    fbbv = random.randint(100000000, 999999999)
    fbdm_width = random.choice([720, 1080, 1440, 1920])
    fbdm_height = int(fbdm_width * (16 / 9))
    fbdm_density = round(random.uniform(2.0, 4.0), 1)
    fbpn = random.choice(["com.facebook.katana", "com.facebook.lite", "com.facebook.orca"])
    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {random.randint(6, 15)}; {brand} {model}) "
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM={{density={fbdm_density},width={fbdm_width},height={fbdm_height}}};"
        f"FBLC/en_US;FBPN/{fbpn}]"
    )
    return ua

def progres(current,num_accounts,delay):
		for sleep in range(int(delay), 0, -1):
			sys.stdout.write(f'\033[1;37m[\033[1;35mBRYX\033[1;37m]-[\033[1;36m{current}\033[1;37m|\033[1;31m{num_accounts}\033[1;37m]-[\033[1;32mSUCCESS:-{len(success)}\033[1;37m]-[\033[1;31mBAD:-{len(bad)}\033[1;37m]-[\033[1;33mLOCK:-{len(lock)}\033[1;37m]\r');sys.stdout.flush()
			time.sleep(1)
			if current == num_accounts:
				break
def GetPhone():
    na = random.choice(['77', '78', '59'])
    ni = str(random.randrange(1000, 10000))
    nu = str(random.randrange(10000, 100000))
    nope = '+639%s%s%s' % (na, ni, nu)
    return nope


def results():
    rich_print(Panel(f"""  [bold white]FINAL RESULTS\n  TOTAL SUCCESS : [bold green]{len(success)}[/]\n  TOTAL BAD     : [bold red]{len(bad)}[/]\n  TOTAL LOCK    : [bold yellow]{len(lock)}[/]\n  RESULTS ARE SAVED TO THE RESULTS FOLDER""",subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold purple"))

def register_facebook_account(password, first_name, last_name, birthday, attempt=1):
    phone = GetPhone()
    if attempt > 3:
        return
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    session = requests.Session()
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    em = Email().Mail()
    email = em['mail']
    req = {
        'api_key': api_key, 
        'attempt_login': True, 
        'birthday': birthday.strftime('%Y-%m-%d'), 
        'client_country_code': 'US', 
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod', 
        'fb_api_req_friendly_name': 'registerAccount', 
        'firstname': first_name, 
        'format': 'json',
        'gender': gender, 
        'lastname': last_name, 
        'email': email, 
        
        'locale': 'en_US', 
        'method': 'user.register', 
        'password': password, 
        'reg_instance': generate_random_string(32), 
        'access_token': accessToken,
        'return_multiple_errors': True
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    headers = {'User-Agent': bryxua()}
    proxy = get_random_proxy()
    try:
        response = requests.post(api_url, data=req, headers=headers, proxies=proxy, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        pass
        return
    reg = response.json()
    id = reg.get('new_user_id')
    token = reg.get('session_info', {}).get('access_token')
    account_name = fetch_account_name(reg.get('session_info', {}).get('access_token'))
    if id:
        check = lock_checker(id)
        if 'Locked' in check:
            lock.append(id)
        else:
            print('\033[1;32mSLEEPING MODE ACTIVE...')
            time.sleep(30)
            try:
                cod = Email(em["session"]).inbox()
                code = re.search(r'(\d+)', str(cod['topic'])).group(1)
            except Exception as e:
                pass
            if code:
                rich_print(Panel(f" [bold green1]STATUS     : ALIVE\n [bold green1]TIMESTAMP  : [bold cyan1]{waktuu}\n[bold green1] NAME       : {account_name.upper()}\n[bold green1] EMAIL      : {email}\n[bold green1] UID        : {id}\n[bold green1] PASSWORD   : {password}\n[bold green1] BIRTHDAY   : [bold green1]{birthday}\n[bold green1] CODE   : [bold green1]{code}",subtitle="[bold yellow] CREATE ",style="bold purple"))
                rich_print(Panel(f" [bold green1]TOKEN : {token}",subtitle="[bold blue] TOKEN ",style="bold purple"))
                success.append(id)
            else:
                print()
    else:
        bad.append(id)
    if id and token:
        try:
            with open("save.txt", "a") as f:
                f.write(f"{id}|{password}|{code}\n")
        except Exception as e:
            print(f"Error saving token: {e}")
    if attempt <= 3:
        register_facebook_account(password, first_name, last_name, birthday, attempt=1)

def fetch_account_name(token):
    url = f"https://graph.facebook.com/v11.0/me?access_token={token}"
    response = requests.get(url).json()
    return response.get(f"name", f"{first_name} {last_name}")

if __name__ == '__main__':
    fake = Faker()
    os.system('clear')
    #print(logo)
    num_accounts = int(input("\033[1;37mHOW MANY ACC: "))
    delay = int(input("\033[1;37mDELAY TIME BETWEEN REQUESTS: "))
    password=input('\033[1;37mENTER CUSTOM PASSWORD : ')
    print()
    for _ in range(num_accounts):
        progres(_+1,num_accounts,delay)
        first_name = fake.first_name()
        last_name = fake.last_name()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        register_facebook_account(password, first_name, last_name, birthday, attempt=1)
    results()
