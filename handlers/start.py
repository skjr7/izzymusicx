import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**🌈 𝐇ɪ 𝐂ʜʟᴍ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu}), 𝐍ᴇᴡ 𝐅ᴜᴛᴄʜᴇʀ 𝐌ᴜsɪᴄ 𝐁ᴏᴛ😍



𖤓 𝐂ʀᴇᴀᴛ ʙʏ : [@king_of_izzy](t.me/{me})

𖤓 🦸‍♂️6ᴛʜ-𝐆ᴇɴ 𝐈ᴍʙᴜʟᴇᴅ 𝐒ʏsᴛᴇᴍ🦸

𖤓 😈𝐇ɪᴛᴇᴄʜ 𝐄ɴɢɪɴᴇ😈

𖤓 🥳𝐍ᴏ 𝐋ᴀɢ ✵ 𝐔ʟᴛʀᴀ 𝐐ᴜᴀʟɪᴛʏ🥳

𖤓 ⚜️𝐀ɴɴᴀ ♡︎ 𝐊ɪɴɢ 𝐎ғ 𝐈ᴢᴢʏʏɪʀ⚜️

𖤓 🔱𝐓ʜᴀᴍʙɪ ♡︎ 𝐒ᴜʀʏᴀ

𖤓 😈𝐏ʀᴏᴘᴏss 𝐌ᴇ   
- @Tamil_chat_junctions

𖤓 🌈𝐓ʜᴀɴᴋs 𝐅ᴏʀ 𝐔sᴇɪɴɢ !!!


🌈 𝐏ʀᴏʙʟᴇᴍ 𝐕ᴀɴᴛʜᴀ  𝐃ᴍ @king_of_izzy 🥵**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥺 𝐆ʀᴏᴜᴘ 𝐀ᴅᴅ 𝐏ᴀɴɴᴀᴛʜᴀᴠᴀɴ 𝐑ᴀᴛʜᴀᴍ 𝐊ᴀᴋᴋɪ 𝐒ᴀᴠᴀɴ  🥺", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "👑 𝐊ɪɴɢ 👑", url="https://t.me/king_of_izzy"
                    ),
                    InlineKeyboardButton(
                        "😻 𝐒ᴜᴘᴘᴏʀᴛ 😻", url=f"https://t.me/Suryaakumar"
                    )
                ],[
                    InlineKeyboardButton(
                        "🔱 𝐓ᴀᴍɪʟ 𝐉ᴜɴᴄᴛɪᴏɴ 🔱", url= "https://t.me/Tamil_chat_junctions"
                    ),
                    InlineKeyboardButton(
                        "🤧 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🤧", url="https://github.com/TeamYukki/YukkiMusicBot"
                    )]
            ]
       ),
    )

