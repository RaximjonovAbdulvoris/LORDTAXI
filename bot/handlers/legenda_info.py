from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, MessageHandler, filters


CONTACT_TEXT = (
    "<b>WB LORD — bog‘lanish uchun</b>\n\n"
    "☎️ ALOQA: +998505909449\n"
    "📨 TELEGRAM: @wblordadmin\n\n"
    "📣 TELEGRAM KANAL:\n"
    "https://t.me/wblordtaxi\n\n"
    "📸 INSTAGRAM: "
    '<a href="https://www.instagram.com/wblordtaxi/">'
    "@wblordtaxi</a>"  
)

OFFICE_TEXT = (      
    "<b>WB LEGENDA (TOSHKENT OFISI)</b>\n\n"
    "📍 Firdavsiy 9-uy\n\n"
    "Mo'ljal:\n"
    "Remix club ro'parasida"
)

OFFICE_MAP_URL = "https://maps.app.goo.gl/Fzdc2HPc7i1hSiHE9"

OFFICE_PHOTO = (
    Path(__file__).resolve().parents[1]
    / "templates"
    / "legenda_office.jpg"
)


async def show_legenda_contact(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        CONTACT_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


async def show_legenda_office(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    with OFFICE_PHOTO.open("rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=OFFICE_TEXT,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Yandex xaritada ochish", url=OFFICE_MAP_URL)]
            ]),
        )


def register_legenda_info(app):
    app.add_handler(
        MessageHandler(
            filters.ChatType.PRIVATE
            & filters.Regex(r"^📞 Bog'lanish uchun$"),
            show_legenda_contact,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.ChatType.PRIVATE
            & filters.Regex(r"^📍 Ofis manzili$"),
            show_legenda_office,
        )
    )
