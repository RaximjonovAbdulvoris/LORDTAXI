from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, MessageHandler, filters


CONTACT_TEXT = (
    "<b>WB LEGENDA — bog‘lanish uchun</b>\n\n"
    "☎️ ALOQA: +998781505050\n"
    "📱 ALOQA: +998931354484\n"
    "📨 TELEGRAM: @WBLEGENDATAXI\n\n"
    "📣 TELEGRAM KANAL:\n"
    "https://t.me/WBLEGENDA_KANAL\n\n"
    "📸 INSTAGRAM: "
    '<a href="https://www.instagram.com/wb_legenda_taxi/">'
    "@WB_LEGENDA_TAXI</a>"  
)

OFFICE_TEXT = (      
    "<b>WB LEGENDA (TOSHKENT OFISI)</b>\n\n"
    "📍 CHILONZOR 8 - kv 1 - dom\n\n"
    "MANZIL:\n"
    "QATORTOL BEKATI"
)

OFFICE_MAP_URL = "https://yandex.uz/maps/-/CXAOiJ6B"

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
