from pyrogram import Client, filters, enums
from helper.database import jishubotz


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Prefix__\n\nExample:- `/set_prefix @MarsaNetwork`**", quote=True)
    prefix = message.text.split(" ", 1)[1]
    JishuDeveloper = await message.reply_text("Please Wait ...", quote=True)
    await jishubotz.set_prefix(message.from_user.id, prefix)
    await JishuDeveloper.edit("**Prefix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    JishuDeveloper = await message.reply_text("Please Wait ...", quote=True)
    prefix = await jishubotz.get_prefix(message.from_user.id)
    if not prefix:
        return await JishuDeveloper.edit("**Just like you don't have a Girlfriend, you don't have a prefix too. ❌**")
    await jishubotz.set_prefix(message.from_user.id, None)
    await JishuDeveloper.edit("**Prefix Deleted Successfully 🗑️**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    JishuDeveloper = await message.reply_text("Please Wait ...", quote=True)
    prefix = await jishubotz.get_prefix(message.from_user.id)
    if prefix:
        await JishuDeveloper.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await JishuDeveloper.edit("**Just like you don't have a Girlfriend, you don't have a prefix too. ❌**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Suffix__\n\nExample:- `/set_suffix @MadflixBotz`**", quote=True)
    suffix = message.text.split(" ", 1)[1]
    JishuDeveloper = await message.reply_text("Please Wait ...", quote=True)
    await jishubotz.set_suffix(message.from_user.id, suffix)
    await JishuDeveloper.edit("**Suffix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    JishuDeveloper = await message.reply_text("Please Wait ...", quote=True)
    suffix = await jishubotz.get_suffix(message.from_user.id)
    if not suffix:
        return await JishuDeveloper.edit("**Just like you don't have a real job, you don't have a Suffix too. ❌**")
    await jishubotz.set_suffix(message.from_user.id, None)
    await JishuDeveloper.edit("**Suffix Deleted Successfully ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    JishuDeveloper = await message.reply_text("Please Wait ...", quote=True)
    suffix = await jishubotz.get_suffix(message.from_user.id)
    if suffix:
        await JishuDeveloper.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await JishuDeveloper.edit("**Just like you don't have a real job, you don't have a prefix too. ❌**")










# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
