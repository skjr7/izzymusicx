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
SESSION_NAME = getenv("SESSION_NAME", "BQBTrupBMhA5ZcFTXnBfH0hSLiVVogmUDpV4GzCjV-0Z-hWvUxVddpqk_yqFzS4UJoLRoDTIovyV4_32ekaKhC0ego1gwVtuBHQ_r2KQGTYz25NAD7vSRop0SMliVwHNwvE5EL540_39wNGzsTFVgUC5cOfM-fJGRmFRaBNVbzRNXeWk3obOJsuEdsD46DNx0VwbR_veNMt8JAVpT7qQmk6cLfqc5bHbQv0ES5ESJZi7J0AkmSNUowniHJ5ufseWQaKZfGw6vJu2GguaIDsD4iulUboXSYW-0P0Ko2lwlNNon0L6fxl2G-6CTUG6aCGQqznImdJQeoy3W4KIxYuyzpu5AAAAAUVK74EA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5457506177").split()))
