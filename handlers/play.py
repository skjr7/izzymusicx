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

    fallen = await message.reply("Â» ðá´É´á´É´á´á´á´ ðá´ ðá´á´Êá´ ðÉ´á´ ðá´á´ á´ ðá´sÉªá´ ðá´ ðá´É´É¢ ðá´Êá´á´ á´á´á´ÊÊá´ ð¤«ê§ð§ð§ ðá´á´á´á´ ðá´É´É´É¢á´ê§")

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
                        "<b>Â» ðá´ÊÊá´á´ ðá´á´á´á´ ðÊá´á´á´á´á´ ðá´É´É´á´ ðá´á´ ð¥µ</b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "Â» ðssÉªsá´á´É´á´ ðÊá´á´á´ ðá´ ðá´É´á´á´á´É´ ðÊÊá´  ðá´á´ ðá´á´á´É´á´Éª ðÊá´á´ÊÉªá´á´ÊÊá´á´ ðºâ¨â.")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await fallen.edit(
                        f"<b>Â» ðssÉªsá´á´É´á´ ðÊÊá´ ðá´Êá´ ðá´á´ÉªÊá´Êá´ ðÊÊá´É¢á´á´ ð¤¦ð» /join ðá´á´ ðÊá´ ðÊÊá´ ðá´Êá´á´É´  ðá´Êá´á´á´ÊÊá´ ðá´á´á´Éª ðá´É´É´á´ÊÉªÉ¢á´Êá´á´ ðÊÊá´ ðá´É´É´á´ÊÉªÉ¢á´ ðá´É´.")
    try:
        await USER.get_chat(chid)
    except Exception as e:
        await fallen.edit(
            f"<i>Â» ðssÉªsá´á´É´á´ ðÊÊá´ ðá´Êá´ ðá´á´ÉªÊá´Êá´ ðÊÊá´É¢á´á´ ð¤¦ð».</i>\n\nðá´Êá´É´á´á´ : {e}")
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
                f"Â» ðá´É´É´á´á´Êá´Êá´ ðá´á´ ð, ðÊá´á´á´ ðá´á´Êá´sá´ ðá´ {DURATION_LIMIT} ðÉªÉ´á´á´á´s ðÊÊá´á´¡ ðá´É´É´á´ÊÊá´ ðá´ ðá´á´Êá´-ðá´á´ á´É´á´á´ "
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
                f"Â» ðá´ÊÊÊ ðÊÊá´, ðÊá´á´á´ ðá´á´Êá´sá´ ðá´ {DURATION_LIMIT} ðÉªÉ´á´á´á´s ðÊÊá´á´¡ ðá´É´É´á´ÊÊá´ ðá´ ðá´á´Êá´-ðá´á´ á´É´á´á´"
            )
            return
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await fallen.edit(
                "Â» ð¤¯ðá´ÊÊá´ ðÉªÉ¢á´ÊÊá´ ðá´É´á´á´ ðÉ´ ðÊÉªÊá´ ðá´É´É¢á´ÊÉªÉ¢á´ð¤ ðá´É´É¢ ðá´á´á´ ðá´á´á´ ðá´ ðá´É´Êá´ð¤¬"
            )
        await fallen.edit("ð»")
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
                "Â»ðá´á´ ðÊá´É´É¢á´ ðÊá´á´ ðá´É´É´á´ð¥º, ðá´É´É¢ ðá´á´á´ ðÊá´ ðá´ ðá´á´á´ ðÊÊá´ð¥°ð"
            )
            print(str(e))
            return

        if (dur / 60) > DURATION_LIMIT:
            await fallen.edit(
                f"Â»ðá´ÊÊÊ ðÊÊá´, ðÊá´á´á´ ðá´á´Êá´sá´ ðá´  {DURATION_LIMIT} ðÉªÉ´á´á´á´s ðÊÊá´á´¡ ðá´É´É´á´ÊÊá´ ðá´ ðá´á´Êá´-ðá´á´ á´É´á´á´"
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
            text=f"**Â» ðÊá´á´á´ ðá´á´á´á´á´ ðá´ {position} ðÊÊá´ **\n **ðÉªá´Êá´â :**[{title[:65]}]({url})\n\nð** ðá´Êá´á´Éªá´É´ :** `{duration}` ** ðÉªÉ´á´á´á´s **\nð** ðá´Ç«á´á´sá´á´á´ ðÊâ : **{chumtiya}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("â¢ ðá´á´á´á´Êá´ â¢", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("Â» ðÊá´sá´ Â«", callback_data="close_play")
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
            text=f"** Â» ð§ðá´á´ ðÊá´ÊÉªÉ´É¢ ðá´ ðÊÊá´ð§ Â«**\n **âï¸ðá´É´É¢ ðÉªá´Êá´âï¸â:** [{title[:65]}]({url})\nð **â¨ðá´Êá´á´Éªá´É´â¨:** `{duration}` ðÉªÉ´á´á´á´s \nð **ð¥µðá´Ç«á´á´sá´á´á´ ðÊð¥µâ:** {chumtiya}\nðº **ðÊá´ÊÉªÉ´É¢ ÉªÉ´â:** `{message.chat.title}`\nð¥ **ðá´Êá´á´á´ ðÊá´á´:** ðá´á´á´á´Êá´ ðá´sÉªá´\n",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ððá´á´©á´©á´Êá´ ðá´ÉªÉ´ð", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("Â» ððÊá´sá´ð Â«", callback_data="close_play")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

    return await fallen.delete()

@Client.on_callback_query(filters.regex("close_play"))
async def in_close_play(_, query: CallbackQuery):
    await query.message.delete()
