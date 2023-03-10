# (c) @MayurSakule

import urllib.parse
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram.enums.parse_mode import ParseMode

db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
<i>๐ Hแดส,</i>{}\n
<i>๐๐๐๐๐๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐, ๐๐ ๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐.</i>\n
<i>Cสษชแดแด แดษด Hแดสแด แดแด ษขแดแด แดแดสแด ษชษดาแดสแดแดแดษชแดษด</i>\n
<i><u>๐ช๐๐ฅ๐ก๐๐ก๐ ๐ธ</u></i>
<b>๐ แดแดสษด แดแดษดแดแดษดแด๊ฑ สแดแดแด๊ฑ แดแด แดแดสแดแดษดแดษดแด สแดษด สแดแด.</b>\n\n
<i><b>๐ Bแดแด Mแดษชษดแดแดษชษดแดแด Bส :</b>@MAYUR_SAKULE</i>"""

HELP_TEXT = """
<i>- ๐๐๐๐๐๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐</i>
<i>- ๐๐ ๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐.</i>
<i>- Aแดแด Mแด ษชษด สแดแดส Cสแดษดษดแดส Fแดส Dษชสแดแดแด Dแดแดกษดสแดแดแด Lษชษดแดs Bแดแดแดแดษด</i>
<i>- แดสษช๊ฑ ษช๊ฑ แดแดสแดแดษดแดษดแด สษชษดแด แดกษชแดส ๊ฐแด๊ฑแดแด๊ฑแด ๊ฑแดแดแดแด.</i>\n
<u>๐ธ ๐ช๐๐ฅ๐ก๐๐ก๐ ๐ธ</u>\n
<b>๐ แดแดสษด แดแดษดแดแดษดแด๊ฑ สแดแดแด๊ฑ แดแด แดแดสแดแดษดแดษดแด สแดษด สแดแด.</b>\n
<i>Cแดษดแดแดแดแด แดแดแด แดสแดแดแดส (แดส) สแดแดแดสแด สแดษข๊ฑ</i> <b>: <a href='https://github.com/MayurSakule'>[ แดสษชแดแด สแดสแด ]</a></b>"""

ABOUT_TEXT = """
<b>โ Mส ษดแดแดแด : ๐๐๐๐๐ ๐๐๐๐ ๐๐๐</b>\n
<b>๐ธVแดส๊ฑษชแดษด : <a href='https://t.me/MAYUR_SAKULE'>3.0.1</a></b>\n
<b>๐นSแดแดสแดแด : <a href='https://github.com/MayurSakule/MAYUR-DLGT-BOT'>Cสษชแดแด Hแดสแด</a></b>\n
<b>๐ธGitHub : <a href='https://github.com/MayurSakule'>Fแดสสแดแดก</a></b>\n
<b>๐นDแดแด แดสแดแดแดส : <a href='https://t.me/MAYUR_SAKULE'>๐๐๐ช๐ฆ๐ฃ ๐๐๐๐ฆ๐๐</a></b>\n
<b>๐ธLแด๊ฑแด แดแดแดแดแดแดแด : <a href='https://t.me/MAYUR_SAKULE'>[ 21-JULY-2022 ] 02:00 PM</a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hแดสแด', callback_data='help'),
        InlineKeyboardButton('Aสแดแดแด', callback_data='about'),
        InlineKeyboardButton('Cสแดsแด', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hแดแดแด', callback_data='home'),
        InlineKeyboardButton('Aสแดแดแด', callback_data='about'),
        InlineKeyboardButton('Cสแดsแด', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hแดแดแด', callback_data='home'),
        InlineKeyboardButton('Hแดสแด', callback_data='help'),
        InlineKeyboardButton('Cสแดsแด', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()

def get_media_file_size(m):
    media = m.video or m.audio or m.document
    if media and media.file_size:
        return media.file_size
    else:
        return None


def get_media_file_name(m):
    media = m.video or m.document or m.audio
    if media and media.file_name:
        return urllib.parse.quote_plus(media.file_name)
    else:
        return None


@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nแดแดก Usแดส Jแดษชษดแดแด:** \n\n__Mส Nแดแดก Fสษชแดษดแด__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sแดแดสแดแดแด Yแดแดส Bแดแด !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__Sแดสสส Sษชส, Yแดแด แดสแด Bแดษดษดแดแด แดแด แดsแด แดแด. Cแดษดแดแดแดแด แดสแด Dแดแด แดสแดแดแดส__\n\n @MAYUR_SAKULE **Tสแดส Wษชสส Hแดสแด Yแดแด**",
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Jแดษชษด แดส แดแดแดแดแดแด แดสแดษดษดแดส แดแด แดsแด แดแด ๐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Jแดษชษด ษดแดแดก ๐", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode=ParseMode.HTML
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Sแดแดแดแดสษชษดษข แดกสแดษดษข แดแดษดแดแดแดแด แดส แดแดแด แดสแดแดแดส</i> <b><a href='https://t.me/MAYUR_SAKULE'>[ แดสษชแดแด สแดสแด ]</a></b>",
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sแดสสส Sษชส, Yแดแด แดสแด Bแดษดษดแดแด แดแด แดsแด แดแด. Qแดษชแดแดสส แดแดษดแดแดแดแด** @MAYUR_SAKULE",
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Pสแดแดsแด Jแดษชษด Mส Uแดแดแดแดแดs Cสแดษดษดแดส แดแด แดsแด แดสษชs Bแดแด**!\n\n**Dแดแด แดแด Oแด แดสสแดแดแด, Oษดสส Cสแดษดษดแดส Sแดสsแดสษชสแดสs แดแดษด แดsแด แดสแด Bแดแด**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("๐ค Jแดษชษด Uแดแดแดแดแดs Cสแดษดษดแดส", url=f"https://t.me/{Var.UPDATES_CHANNEL}")],
                         [InlineKeyboardButton("๐ Refresh / Try Again", url=f"https://t.me/{(await b.get_me()).username}?start=MAYUR_SAKULE_{usr_cmd}")
                        
                        ]]
                    ),
                    parse_mode=ParseMode.MARKDOWN
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sแดแดแดแดสษชษดษข แดกแดษดแด Wสแดษดษข. Cแดษดแดแดแดแด แดแด** [๐๐๐ช๐ฆ๐ฃ ๐๐๐๐ฆ๐๐](https://t.me/MAYUR_SAKULE).",
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))
        file_name = get_media_file_name(get_msg)
        file_size = humanbytes(get_media_file_size(get_msg))

        stream_link = "https://{}/{}/{}".format(Var.FQDN, get_msg.id, file_name) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id,
                                     file_name)

        msg_text ="""
<i><u>๐ฌ๐ผ๐๐ฟ ๐๐ถ๐ป๐ธ ๐๐ฒ๐ป๐ฒ๐ฟ๐ฎ๐๐ฒ๐ฑ !</u></i>\n
<b>๐ Fษชสแด ษดแดแดแด :</b> <i>{}</i>\n
<b>๐ฆ Fษชสแด ๊ฑษชแดขแด :</b> <i>{}</i>\n
<b>๐ฅ Dแดแดกษดสแดแดแด :</b> <i>{}</i>\n
<b>๐ธ Nแดแดแด : ๐๐ก๐ข๐ฌ ๐ฅ๐ข๐ง๐ค ๐ฐ๐ข๐ฅ๐ฅ ๐๐ ๐ฐ๐จ๐ซ๐ค๐ข๐ง๐  ๐จ๐ง๐ฅ๐ฒ ๐ข๐ง ๐๐๐ญ๐ฐ๐๐๐ง ๐๐:๐๐ ๐๐ ๐ญ๐จ ๐๐:๐๐ ๐๐ ๐๐ฏ๐๐ซ๐ฒ ๐๐๐ฒ.</b>\n
<i>๐ Bแดแด Mแดษชษดแดแดษชษดแดแด Bส :</i> <b>@MAYUR_SAKULE</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dแดแดกษดสแดแดแด ษดแดแดก ๐ฅ", url=stream_link)]])
        )



@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nแดแดก Usแดส Jแดษชษดแดแด **\n\n__Mส Nแดแดก Fสษชแดษดแด__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sแดสสส Sษชส, Yแดแด แดสแด Bแดษดษดแดแด แดแด แดsแด แดแด. Cแดษดแดแดแดแด แดสแด Dแดแด แดสแดแดแดส</i>",
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Pสแดแดsแด Jแดษชษด Mส Uแดแดแดแดแดs Cสแดษดษดแดส แดแด แดsแด แดสษชs Bแดแด!**\n\n__Dแดแด แดแด Oแด แดสสแดแดแด, Oษดสส Cสแดษดษดแดส Sแดสsแดสษชสแดสs แดแดษด แดsแด แดสแด Bแดแด!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("๐ค Jแดษชษด Uแดแดแดแดแดs Cสแดษดษดแดส", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode=ParseMode.MARKDOWN
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sแดแดแดแดสษชษดษข แดกแดษดแด Wสแดษดษข. Cแดษดแดแดแดแด แดแด__ [๐๐๐ช๐ฆ๐ฃ ๐๐๐๐ฆ๐๐](https://t.me/MAYUR_SAKULE).",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )

