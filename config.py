import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐋ᴀʟʟᴜ")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6379796115").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Ganthswea/Lallu")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Team_Remo")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/tamilchats_makkal")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "999"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "999"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "9c6a4f8798904d709938bd23e41bbc02")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "0bd5c948ed0b4add9b985a27c3a7bfe0")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "50"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "5000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "5000"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ",
)

PLAYLIST_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

GLOBAL_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

STATS_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

TELEGRAM_AUDIO_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

TELEGRAM_VIDEO_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

STREAM_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

SOUNCLOUD_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

YOUTUBE_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

SPOTIFY_ARTIST_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

SPOTIFY_ALBUM_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

SPOTIFY_PLAYLIST_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "CgACAgUAAxkBAAIBTGSXjO0pgUwq9NUyrdwmjXZMDERJAAKjCgACsKe4VD3tNmW5gSc1LwQ"
