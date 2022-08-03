import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT, SUPPORT_GROUP
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(
    command(["play", "p", "fuck"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer

    await message.delete()

    fallen = await message.reply("» 𝐕ᴀɴᴀɴᴋᴀᴍ 𝐃ᴀ 𝐌ᴀᴘʟᴀ 𝐎ɴᴇ 𝐋ᴏᴠᴇ 𝐌ᴜsɪᴄ 𝐋ᴀ 𝐒ᴏɴɢ 𝐕ᴀʀᴜᴍ ᴋᴇᴀʟʟᴜ 🤫꧁🎧🎧 𝐏ᴏᴅᴅᴜ 𝐏ᴀɴɴɢᴜ꧂")

    chumtiya = message.from_user.mention

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Steffen"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await fallen.edit(
                        "<b>» 𝐘ᴇʟʟᴇᴀ 𝐌ᴀᴋᴋᴀ 𝐏ʀᴏᴍᴏᴛᴇ 𝐏ᴀɴɴᴜ 𝐋ᴇᴀ 🥵</b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "» 𝐀ssɪsᴛᴀɴᴛ 𝐆ʀᴏᴜᴘ 𝐊ᴜ 𝐕ᴀɴᴛᴇᴀɴ 𝐂ʜʟᴍ  𝐈ᴘᴏ 𝐁ᴀᴊᴀɴᴀɪ 𝐀ʀᴀᴍʙɪᴋᴀʟʟᴀᴍ 🕺✨​.")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await fallen.edit(
                        f"<b>» 𝐀ssɪsᴛᴀɴᴛ 𝐔ʟʟᴀ 𝐕ᴀʀᴀ 𝐌ᴜᴅɪʏᴀʟᴀ 𝐓ʜʀᴏɢᴀᴍ 🤦🏻 /join 𝐈ᴘᴏ 𝐓ʜᴀ 𝐔ʟʟᴀ 𝐕ᴀʀᴇᴀɴ  𝐀ᴛʜᴜᴋᴜʟʟᴀ 𝐈ᴘᴀᴅɪ 𝐏ᴀɴɴᴀʀɪɢᴀʟᴇᴀ 𝐍ʟʟᴀ 𝐏ᴀɴɴᴀʀɪɢᴀ 𝐌ᴀɴ.")
    try:
        await USER.get_chat(chid)
    except Exception as e:
        await fallen.edit(
            f"<i>» 𝐀ssɪsᴛᴀɴᴛ 𝐔ʟʟᴀ 𝐕ᴀʀᴀ 𝐌ᴜᴅɪʏᴀʟᴀ 𝐓ʜʀᴏɢᴀᴍ 🤦🏻.</i>\n\n𝐊ᴀʀᴀɴᴀᴍ : {e}")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"» 𝐌ᴀɴɴᴜᴄʜᴜʀᴜ 𝐋ᴇᴀ 😒, 𝐓ʀᴀᴄᴋ 𝐏ᴇᴀʀᴜsᴜ 𝐃ᴀ {DURATION_LIMIT} 𝐌ɪɴᴜᴛᴇs 𝐀ʟʟᴏᴡ 𝐏ᴀɴɴᴀʟʟᴀ 𝐃ᴀ 𝐒ᴀᴍʙᴜ-𝐌ᴀᴠᴀɴᴇᴀ "
            )

        file_name = get_file_name(audio)
        title = file_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            title = "NaN"
            duration = "NaN"
            views = "NaN"

        if (dur / 60) > DURATION_LIMIT:
            await fallen.edit(
                f"» 𝐒ᴏʀʀʏ 𝐂ʜʟᴍ, 𝐓ʀᴀᴄᴋ 𝐏ᴇᴀʀᴜsᴜ 𝐃ᴀ {DURATION_LIMIT} 𝐌ɪɴᴜᴛᴇs 𝐀ʟʟᴏᴡ 𝐏ᴀɴɴᴀʟʟᴀ 𝐃ᴀ 𝐒ᴀᴍʙᴜ-𝐌ᴀᴠᴀɴᴇᴀ"
            )
            return
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await fallen.edit(
                "» 🤯𝐘ᴀʀʀᴀ 𝐍ɪɢᴀʟʟᴀ 𝐄ᴀɴᴅᴀ 𝐄ɴ 𝐔ʏɪʀᴀ 𝐕ᴀɴɢᴀʀɪɢᴀ😤 𝐒ᴏɴɢ 𝐍ᴀᴍᴇ 𝐏ᴏᴅᴜ 𝐃ᴀ 𝐕ᴇɴʀᴜ🤬"
            )
        await fallen.edit("😻")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await fallen.edit(
                "»𝐋ᴇᴀ 𝐎ʟᴜɴɢᴀ 𝐓ʏᴘᴇ 𝐏ᴀɴɴᴜ🥺, 𝐒ᴏɴɢ 𝐍ᴀᴍᴇ 𝐂ʀᴛ 𝐇ᴀ 𝐏ᴏᴅᴜ 𝐂ʜʟᴍ🥰🙈"
            )
            print(str(e))
            return

        if (dur / 60) > DURATION_LIMIT:
            await fallen.edit(
                f"»𝐒ᴏʀʀʏ 𝐂ʜʟᴍ, 𝐓ʀᴀᴄᴋ 𝐏ᴇᴀʀᴜsᴜ 𝐃ᴀ  {DURATION_LIMIT} 𝐌ɪɴᴜᴛᴇs 𝐀ʟʟᴏᴡ 𝐏ᴀɴɴᴀʟʟᴀ 𝐃ᴀ 𝐒ᴀᴍʙᴜ-𝐌ᴀᴠᴀɴᴇᴀ"
            )
            return
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_text(
            text=f"**» 𝐓ʀᴀᴄᴋ 𝐐ᴜᴇᴜᴇᴅ 𝐀ᴛ {position} 𝐂ʜʟᴍ **\n📌 **𝐓ɪᴛʟᴇ​ :**[{title[:65]}]({url})\n\n🕕** 𝐃ᴜʀᴀᴛɪᴏɴ :** `{duration}` ** 𝐌ɪɴᴜᴛᴇs **\n💕** 𝐑ᴇǫᴜᴇsᴛᴇᴅ 𝐁ʏ​ : **{chumtiya}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• 𝐒ᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("» 𝐂ʟᴏsᴇ «", callback_data="close_play")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_text(
            text=f"** » 🎧𝐈ᴘᴏ 𝐏ʟᴀʏɪɴɢ 𝐃ᴀ 𝐂ʜʟᴍ🎧 «**\n📌 **⚜️𝐒ᴏɴɢ 𝐓ɪᴛʟᴇ⚜️​:** [{title[:65]}]({url})\n🕕 **✨𝐃ᴜʀᴀᴛɪᴏɴ✨:** `{duration}` 𝐌ɪɴᴜᴛᴇs s\n💕 **🥵𝐑ᴇǫᴜᴇsᴛᴇᴅ 𝐁ʏ🥵​:** {chumtiya}\n🍺 **𝐏ʟᴀʏɪɴɢ ɪɴ​:** `{message.chat.title}`\n🎥 **𝐒ᴛʀᴇᴀᴍ 𝐓ʏᴘᴇ:** 𝐘ᴏᴜᴛᴜʙᴇ 𝐌ᴜsɪᴄ\n",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😘𝐒ᴜᴩᴩᴏʀᴛ 𝐉ᴏɪɴ😘", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("» 😘𝐌ʟᴏsᴇ😘 «", callback_data="close_play")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

    return await fallen.delete()

@Client.on_callback_query(filters.regex("close_play"))
async def in_close_play(_, query: CallbackQuery):
    await query.message.delete()
