import asyncio
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message
from Ayush import Ayush
from Ayush.database.chats import add_served_chat
from Ayush.database.users import add_served_user
from Ayush.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://graph.org/file/210751796ff48991b86a3.jpg",
    "https://graph.org/file/7b4924be4179f70abcf33.jpg",
    "https://graph.org/file/f6d8e64246bddc26b4f66.jpg",
    "https://graph.org/file/63d3ec1ca2c965d6ef210.jpg",
    "https://graph.org/file/9f12dc2a668d40875deb5.jpg",
    "https://graph.org/file/0f89cd8d55fd9bb5130e1.jpg",
    "https://graph.org/file/e5eb7673737ada9679b47.jpg",
    "https://graph.org/file/2e4dfe1fa5185c7ff1bfd.jpg",
    "https://graph.org/file/36af423228372b8899f20.jpg",
    "https://graph.org/file/c698fa9b221772c2a4f3a.jpg",
    "https://graph.org/file/61b08f41855afd9bed0ab.jpg",
    "https://graph.org/file/744b1a83aac76cb3779eb.jpg",
    "https://graph.org/file/814cd9a25dd78480d0ce1.jpg",
    "https://graph.org/file/e8b472bcfa6680f6c6a5d.jpg",
]


#----------------IMG-------------#


#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CdRUi1wABAvYDZ3rCvBECIKK2UkVvdSBygYilxhgAAvQOAAI225hUwbMO2haasLQeBA",
    "CAACAgUAAx0CdRUi1wABAvX7Z3rCe3H0VNdQghTwFwPBtE6E0SsAAn4GAAJ3PnBV-cAFTdolJGEeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#


#---------------EMOJIOS---------------#

EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "☠️"
    "👀"
    "✨"
    "👻",
    "🎃",
    "🎩",
    "🕊",
]


#---------------EMOJIOS---------------#

@Ayush.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("Ꭻᴀʏ")
        await asyncio.sleep(0.2)
        await accha.edit("ᎫᴀʏㅤᏚʜʀᴇᴇ")
        await asyncio.sleep(0.2)
        await accha.edit("🙏|| ᎫᴀʏㅤᏚʜʀᴇᴇㅤᏦʀɪsʜɴᴀ ||🙏")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**🌟 ɪɴɴᴏᴠᴀᴛɪᴠᴇ ᴀɪ ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌟**
            
**ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴛʜᴇ ғᴜᴛᴜʀᴇ ᴏғ ᴄʜᴀᴛʙᴏᴛs ᴡɪᴛʜ

[{Ayush.name}](t.me/{Ayush.username})!**

**ᴇɴɧᴀɴᴄɪɴɢ ᴄᴏᴍᴍᴜɴɪᴄᴀᴛɪᴏɴs, ᴏɴʟɪɴᴇ, ᴡɪᴛʜ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ!**
**ᴡᴏʀᴋɪɴɢ ᴄᴏɴsᴛᴀɴᴛʟʏ ᴛᴏ ᴇɴʜᴀɴᴄᴇ ʏᴏᴜʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ.**
━━━━━━━━━━━━━━
<b>||💬 ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ!||</b>

<b>🧑‍💻 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/moh_maya_official'>ᴀʏᴜsʜ🥀</a></b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)



@Ayush.on_cmd("help")
async def help(client: Ayush, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@Ayush.on_cmd("repo")
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@Ayush.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
