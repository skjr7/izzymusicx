import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**ð ðÉª ðÊÊá´ {message.from_user.mention()} !

        á´ÊÉªs Éªs [{bn}](t.me/{bu}), ðá´á´¡ ðá´á´á´Êá´Ê ðá´sÉªá´ ðá´á´ð



ð¤ ðÊá´á´á´ ÊÊ : [@king_of_izzy](t.me/{me})

ð¤ ð¦¸ââï¸6á´Ê-ðá´É´ ðá´Êá´Êá´á´ ðÊsá´á´á´ð¦¸

ð¤ ððÉªá´á´á´Ê ðÉ´É¢ÉªÉ´á´ð

ð¤ ð¥³ðá´ ðá´É¢ âµ ðÊá´Êá´ ðá´á´ÊÉªá´Êð¥³

ð¤ âï¸ðÉ´É´á´ â¡ï¸ ðÉªÉ´É¢ ðÒ ðá´¢á´¢ÊÊÉªÊâï¸

ð¤ ð±ðÊá´á´ÊÉª â¡ï¸ ðá´ÊÊá´

ð¤ ððÊá´á´á´ss ðá´   
 @kaathuvaakula4

ð¤ ððÊá´É´á´s ðá´Ê ðsá´ÉªÉ´É¢ !!!


ð ðÊá´ÊÊá´á´ ðá´É´á´Êá´  ðá´ @king_of_izzy ð¥µ**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥º ðÊá´á´á´ ðá´á´ ðá´É´É´á´á´Êá´á´ á´É´ ðá´á´Êá´á´ ðá´á´á´Éª ðá´á´ á´É´  ð¥º", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "ð ðÉªÉ´É¢ ð", url="https://t.me/king_of_izzy"
                    ),
                    InlineKeyboardButton(
                        "ð» ðá´á´á´á´Êá´ ð»", url=f"https://t.me/kaathuvaakula4"
                    )
                ],[
                    InlineKeyboardButton(
                        "ð± ðá´á´ÉªÊ ðá´É´á´á´Éªá´É´ ð±", url= "https://t.me/Tamil_chat_junctions"
                    ),
                    InlineKeyboardButton(
                        "ð¤§ sá´á´Êá´á´ á´á´á´á´ ð¤§", url= "https://t.me/repo_izzy_bot"
                    )]
            ]
       ),
    )

