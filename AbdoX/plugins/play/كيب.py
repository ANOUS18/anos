import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = "اهلا بك بك عزيزي العضو اليك كيب الاعضاء⚡"
        kep = ReplyKeyboardMarkup([
[" المطور", "مطور السورس"],
["السورس","يـوتيوب "],
["اقتباس","استوري"],
["انمي","متحركه"],
["تويت", "صراحه"],
["نكته","احكام"],
[" لو خيروك","انصحني"],
["قران","نقشبندي"],
["اذكار","كتابات"],
["حروف","بوت"],
["غنيلي","سوال"],
["تلاوات","عبدالباسط"],
["افاتار بنات","افاتار شباب"],
["❎ ¦ حذف الكيبورد"]], resize_keyboard=True)
        await message.reply(
              text=text,
               reply_markup=kep,quote=True)

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
)
