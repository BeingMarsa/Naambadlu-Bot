import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DATABASE_NAME = os.environ.get("DATABASE_NAME","")     
    DATABASE_URL  = os.environ.get("DATABASE_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

    # channels logs
    FORCE_SUBS   = os.environ.get("FORCE_SUBS", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

⌬ Using This Bot You Can Rename And Change Thumbnail Of Your Files.\nYou Can Also Convert Video To File And File To Video.

⌬ This Bot Also Supports Custom Thumbnail, Custom Caption and even let you edit Metadata.

<b>Bot Is Owned By :</b> @MarsaNetwork"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Owned By</b> : <a href=https://t.me/MarsaNetwork>MarsaNetwork</a> 
├<b>⚔️ Anime Channel</b> : <a href=https://t.me/Anime_Marsa>Marsa Anime</a>
├<b>🎥 Movies Channel</b> : <a href=https://t.me/Movie_Marsa>Marsa Movies</a>
├<b>🗃️ Series Channel</b> : <a href=https://t.me/Series_Marsa>Series Marsa</a> 
├<b>📢 𝗙𝗼𝗿 𝗣𝗮𝗶𝗱 𝗣𝗿𝗼𝗺𝗼</b> : <a href=https://t.me/MarsaAdminContactBot>𝗗𝗠 𝗛𝗘𝗥𝗘</a>
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ Send any photo and it'll automatically use it as a thumbnail.
        

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/MarsaAdminContactBot>Support</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like our Bots & channels, You Can 🎁 Donate so that services can run smoothly.

<b>🛍 UPI ID:</b> `Updating This Soon...`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET METADATA</u></b>

For Example :-

<code>By :- @MarsaNetwork</code>

💬 For Any Help Contact @MarsaAdminContactBot
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
