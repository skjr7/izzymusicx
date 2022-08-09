from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "13399054"))
API_HASH = getenv("API_HASH", "585801d590dac4c79aeaa7bcda495e62")
BOT_TOKEN = getenv("BOT_TOKEN", "5498862653:AAGjcn8ynlmnwa639gV0i3pLRnAH9pQB0YE")
BOT_NAME = getenv("BOT_NAME","one love")
BOT_USERNAME = getenv("BOT_USERNAME", "Tj_Onelove_Music_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "king_of_izzy")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Tamil_chat_junctions")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/988bb4cc5867257ea8fca.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQB_aMgcPgk7moBijoErjMZPOQvcDvB6xxdX4w6au4yGmkoGGhrgrpxOymbeuezkLRC6wr-wYVkmU-HXntg2_25HKZ_oXGhky5Tv2Qtg1I6cOJX8W3NG4RQJaQZBMhj9MwWCblZMkWzLEocmeeKsgX1dZ6sgh5aj-lCG5MZMvUE0bbYEHHvzFYYP0jx5d7Pxh8DE342n7i0UJOHQor7T8z6RbgDlzCWuSiTshi_xuzjyR_HptcJWdupOmR6Ael5mj-iHHA4ojQ1UmU65O8sRp-zOFbrd2L-YSKzf3S0ZxUBXh0xPhIFKCZZtUw87v41ZVna4ds6xGe-GUaCGf6z_dlNkAAAAAUcdewgA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5457506177").split()))
