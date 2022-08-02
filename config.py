from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "19197570"))
API_HASH = getenv("API_HASH", "0401e837796d193ec9ae6e17cb8cfbf8")
BOT_TOKEN = getenv("BOT_TOKEN", "5533302610:AAFuXxCFlgs7bTUSEm_N2zmKXevwNcyPsSc")
BOT_NAME = getenv("BOT_NAME","one love")
BOT_USERNAME = getenv("BOT_USERNAME", "Tj_Onelove_Music_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "king_of_izzy")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Tamil_chat_junctions")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/988bb4cc5867257ea8fca.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQB1_DB980I9HFInumkfmmStmAhg72mLbzURusZIo9AUbur1pMW3vshsJrbW2CDSyP7_hvpel8f6XJFaLu7I6T-Dbeg9I3fcJdBygB3G6VKfl7dxOHs4d2yFg800sVtT_03slrNL1MfGgaMpF8RvdQziYtkEzxGTvBaMevG7RPB0tfeAcT1QLGf9GfhoDbbkkz83UuNbN38d7qzjw_NSmezJJaTqYQP4lSWZgE9dux9J25Wm4ubU1MD-wKGEP_bkhVeLqDoFZVARntxZos2n6L5MeWw48MN7TDCwGcb1nPqV00RPg0CbUAGdYmeMCeuI0m9FDCwEnedraXZrCWh5w2V6AAAAAUcdewgA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5429873872").split()))
