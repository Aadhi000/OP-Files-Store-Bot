#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "<b>𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙴 𝙵𝙸𝚁𝚂𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙳𝙱 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 (𝚆𝙸𝚃𝙷 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚀𝙾𝚄𝚃𝙴)....\n\n𝙾𝚁\n\n𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙿𝙾𝚂𝚃 𝙻𝙸𝙽𝙺</b>", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("<b>🚫 𝙴𝚁𝚁𝙾𝚁\n\n𝚃𝙷𝙸𝚂 𝙵𝙾𝚁𝚆𝙰𝚁𝙳𝙴𝙳 𝙿𝙾𝚂𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙾𝙼 𝙼𝚈 𝙳𝙱 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙾𝚁 𝙻𝙸𝙽𝙺 𝙸𝚂 𝙽𝙾𝚃 𝚃𝙰𝙺𝙴𝙽 𝙵𝚁𝙾𝙼 𝙳𝙱 𝙲𝙷𝙰𝙽𝙽𝙴𝙻...</b>", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "<b>𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙴 𝙻𝙰𝚂𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙳𝙱 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 (𝚆𝙸𝚃𝙷 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚀𝙾𝚄𝚃𝙴)....\n\n𝙾𝚁\n\n𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙿𝙾𝚂𝚃 𝙻𝙸𝙽𝙺</b>", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("<b>🚫 𝙴𝚛𝚛𝚘𝚛\n\n𝚃𝙷𝙸𝚂 𝙵𝙾𝚁𝚆𝙰𝚁𝙳𝙴𝙳 𝙿𝙾𝚂𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙾𝙼 𝙼𝚈 𝙳𝙱 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙾𝚁 𝙻𝙸𝙽𝙺 𝙸𝚂 𝙽𝙾𝚃 𝚃𝙰𝙺𝙴𝙽 𝙵𝚁𝙾𝙼 𝙳𝙱 𝙲𝙷𝙰𝙽𝙽𝙴𝙻...</b>", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("𝚂𝙷𝙰𝚁𝙴 𝚄𝚁𝙻", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>𝙷𝙴𝚁𝙴 𝙸𝚂 𝚈𝙾𝚄𝚁 𝙻𝙸𝙽𝙺</b>\n\n{link}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("<b>🚫 𝙴𝚛𝚛𝚘𝚛\n\n𝚃𝙷𝙸𝚂 𝙵𝙾𝚁𝚆𝙰𝚁𝙳𝙴𝙳 𝙿𝙾𝚂𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝚁𝙾𝙼 𝙼𝚈 𝙳𝙱 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙾𝚁 𝙻𝙸𝙽𝙺 𝙸𝚂 𝙽𝙾𝚃 𝚃𝙰𝙺𝙴𝙽 𝙵𝚁𝙾𝙼 𝙳𝙱 𝙲𝙷𝙰𝙽𝙽𝙴𝙻...</b>", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("𝚂𝙷𝙰𝚁𝙴 𝚄𝚁𝙻", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>𝙷𝙴𝚁𝙴 𝙸𝚂 𝚈𝙾𝚄𝚁 𝙻𝙸𝙽𝙺</b>\n\n{link}", quote=True, reply_markup=reply_markup)
