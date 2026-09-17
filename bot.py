"""
3X Rent Car — Telegram bot that launches the Mini App.

Nima qilish kerak:
1. pip install aiogram==3.*
2. BotFather'dan bot yarating, BOT_TOKEN oling.
3. webapp.html faylini biror joyga (GitHub Pages, Vercel, Netlify va h.k.)
   HTTPS orqali joylashtiring va uning havolasini WEBAPP_URL ga yozing.
   (Telegram Web App faqat HTTPS havolalar bilan ishlaydi.)
4. python bot.py

Bot /start buyrug'iga "3X Rent Car'ni ochish" tugmasi bilan javob beradi —
bosilganda Mini App (webapp.html) Telegram ichida ochiladi.
"""

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "PUT_YOUR_BOT_TOKEN_HERE")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://example.com/webapp.html")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚗 3X Rent Car'ni ochish",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )
    await message.answer(
        "Assalomu alaykum! 3X Rent Car — O'zbekiston bo'ylab avtomobil "
        "ijarasi platformasi.\n\nBoshlash uchun quyidagi tugmani bosing:",
        reply_markup=kb,
    )


@dp.message(F.web_app_data)
async def on_webapp_data(message: Message):
    # Mini App ichida tg.sendData(...) chaqirilganda shu yerga keladi
    # (masalan, buyurtma tasdiqlanganda). Hozircha shunchaki qaytarib beramiz —
    # bu yerga buyurtmani bazaga yozish, adminga xabar yuborish va h.k. qo'shiladi.
    await message.answer(f"Buyurtma qabul qilindi:\n{message.web_app_data.data}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
