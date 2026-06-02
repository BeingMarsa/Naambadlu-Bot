from pyrogram import Client, filters 
from helper.database import jishubotz

@Client.on_message(filters.private & filters.command(['set_caption', "sc"]))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Give The Caption**", quote=True)
    caption = message.text.split(" ", 1)[1]
    await jishubotz.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**Your Caption Successfully Added ✅**", quote=True)
   
@Client.on_message(filters.private & filters.command(['del_caption', "dc"]))
async def delete_caption(client, message):
    caption = await jishubotz.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**Just like you don't have a Girlfriend, you don't have a caption set either.**", quote=True)
    await jishubotz.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**Your Caption Successfully Deleted, just like Love from your life. 🗑️**", quote=True)
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption', "vc"]))
async def see_caption(client, message):
    caption = await jishubotz.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Your Caption :**\n\n`{caption}`", quote=True)
    else:
       await message.reply_text("**You Don't set any caption, so how can I show you, jerk!! 🤬**", quote=True)









# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
