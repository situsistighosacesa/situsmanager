import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from BagaskaraRobot.events import register
from BagaskaraRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/d5ec232215c11aa3e5013.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hallo !! [{event.sender.first_name}](tg://user?id={event.sender.id}), Saya Alter Base Music Robot.** \n\n"
  TEXT += "ð° **Via aktif : sekarang** \n\n"
  TEXT += f"ð° **My Owner : [Master](https://t.me/hllofubtch)** \n\n"
  TEXT += f"ð° **Library Version :** `{telever}` \n\n"
  TEXT += f"ð° **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"ð° **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Makasih Yaa !! Sudah Mau Pake Saya Disini ð**"
  BUTTON = [
        [
            Button.url("Êá´Êá´â", "https://t.me/video_tante"),
            Button.url("sá´á´á´á´Êá´â", "https://t.me/+fpF_1pbU3FNkMDhl"),
        ]
    ]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
