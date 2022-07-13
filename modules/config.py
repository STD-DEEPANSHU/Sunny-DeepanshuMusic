# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@Sunny_meena @STD_DEEPANSHU)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @Sunny_meena @STD_DEEPANSHU
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/7e21fadaa6d92c195b481.jpg")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
MONGODB_URL = getenv("MONGODB_URL", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
OWNER_NAME = getenv("OWNER_NAME", "Ɗᴇᴇᴘᴀɴꜱʜᴜ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "BikashHalder")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/STD_DEEPANSHU")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2084361997").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/best_friends_chat_group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/DEEPANSHU_WORLD")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐒𝐓𝐃 𝐃𝐄𝐄𝐏𝐀𝐍𝐒𝐇𝐔) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/girls_and_boys_dp")
