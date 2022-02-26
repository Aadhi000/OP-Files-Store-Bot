#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╭━━━━━━━━━━━━━━━➣\n┣⪼ Creator : <a href='tg://user?id={OWNER_ID}'>Me</a>\n┣⪼ Language : Python3\n┣⪼ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n┣⪼ Source Code : <a href='https://github.com/Aadhi000/OP-Files-Store-Bot'>OP-File Store Bot</a>\n┣⪼ Channel : <a href='https://t.me/OpusTechz'>Opus Techz</a>\n┣⪼ YouTube Channel : <a href='https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA'>Opus Techz</a>\n╰━━━━━━━━━━━━━━━➣</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
