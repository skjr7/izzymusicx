from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "10069388"))
API_HASH = getenv("API_HASH", "87c1643359aed164979679e4c3475c1d")
BOT_TOKEN = getenv("BOT_TOKEN", "5396553905:AAGTjeHg3KX77lt0-WZ-m5deoiK0k06K08w")
BOT_NAME = getenv("BOT_NAME","one love")
BOT_USERNAME = getenv("BOT_USERNAME", "One_love_music_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "king_of_izzy")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "mafia_kings_tg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/988bb4cc5867257ea8fca.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQCN4X4pQest0KqFvL7sthu2qJVb1AnK0DQusSQ28dPnSGXYVIH9zH5MdECiwPnIGH0Lf2CtNp4I0Tf5Qh8Tj53K7TzGKbaodS8ViAbhTV8WOC3mGO0itZIlAfAM5BrcwHEZVLYJfpiLjiFGCTpGW1r3aeSL9FTNMPIxX0J5jI6fV7LvycM0-TjTeeK9Wtj3vBzOd-dBAv1eHd9SiPoSiUshGoeUcwIbOBobcpw2VV8DGDdsb5XLbFjO1zN5JKNp_HYUBygSHVQ79Nirk7b_iKzTG48cleJYeMM6IcckgC0Ig52Gmvefwu1HW3HHy5AIqHEvCF1ItUm0JAhKr0MiFujuAAAAAUr0aIEAL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1782402849").split()))
