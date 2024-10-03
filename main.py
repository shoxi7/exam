# Savollar:
#  1. Aiogram kutubxonasi nima va u Telegram botlarini yaratishda nima uchun ishlatiladi?
#  2. Aiogram yordamida botni qanday yaratish mumkin?
#  3. Botni aiogram’ga ulash uchun BotFather’dan qanday turdagi token olish kerak?
#  4. Aiogram yordamida foydalanuvchilardan kiruvchi xabarlarni qanday qayta ishlash mumkin?
#  5. Bot orqali foydalanuvchiga matnli xabar qanday yuboriladi?
#  6. Aiogram yordamida yana qanday turdagi xabarlarni (foto, audio, video va h.k.) yuborish mumkin?
#  7. Bot orqali foydalanuvchi bilan muloqot qilish uchun tugmachali klaviatura qanday amalga oshiriladi?
#  8. Chat va xabar yuborgan foydalanuvchi haqida qanday ma'lumot olsam bo'ladi?
#  9. SQLite3 ma'lumotlar bazasi nima va unda qanday asosiy operatsiyalarni bajarish mumkin?
#  10. Pythonda SQLite3 ma'lumotlar bazasini qanday ulash va yaratish mumkin?
#  11. Bot foydalanuvchilari haqidagi ma'lumotlarni saqlash uchun jadval yaratish uchun qanday SQL so'rovlarini bajarish kerak?
#  12. Bot orqali ro'yxatdan o'tishda SQLite3 ma'lumotlar bazasiga yangi foydalanuvchi qanday qo'shiladi?
#  13. SQLite3 ma'lumotlar bazasida foydalanuvchi ma'lumotlarini qanday yangilash mumkin, masalan, profil o'zgarganda?
#  14. SQLite3 ma'lumotlar bazasi bilan ishlashda ma'lumotlar xavfsizligini qanday ta'minlash mumkin?
#  15. GPT-3 dan aiogram kutubxonasi bilan birgalikda ijodiy bot yaratish uchun qanday foydalanish mumkin?
# Mini-amaliy vazifa:
# Foydalanuvchidan matnli xabar oladigan va ijodiy javob bilan javob beradigan mini-bot yarating.  Aiogramda suhbatlar tarixini saqlash uchun “SQLite3” dan foydalaning. Bot bir necha turdagi xabarlarga javob bera olishi kerak, masalan, “salom”, “qalaysan?”, “menga hazil ayt”. Har bir savolning ma'lumotlar bazasidan o'ziga xos javobi bo'lishi kerak.


#Javoblar:
#1: Aiogram bu Python da telegram botlarini yaratish uchun juda samarali kutubxona.Aiogram ko'plab vositalar va xususiyatlarni taqdim etadi, bu uni rivojlangan funksionalika ega botlarni yaratish uchun ideal tanlov qiladi.
#KOD: from aiogram import Bot, Dispatcher, filters, types, F


#2: Aiogram yordamida Telegram botini yaratish uchun quyidagi bosqichlarni bajarishingiz mumkin. Aiogram - bu Pythonda yozilgan asinxron kutubxona bo'lib, Telegram botlarini qulay imkonini beradi.
#KOD: from aiogram import Bot, Dispatcher, filters, types, F


#3: APL Token
#KOD: '7341737794:AAGSXlRW6q-AU8rFTEzyFWQaH1ZePlp7IlI'


#4: Aiogram yordamida foydalanuvchilardan kiruvchi xabarlarni qayta ishlash uchun quyidagi kodni yozasiz:
#KOD: misol uchun: @dp.message(filters.Command('start'))


#5: KOD: await message.answer('Привет')


#6: Matnli xabarlar (javob berish, yuborish, javob berish, fotosuratlar, videolar, giflar, geolokatsiyalar, stikerlar)
#KOD: @dp.message(F.animation)
# async def echo_gif(message: Message):
#     await message.reply_animation(message.animation.file_id)


#7: ReplyKeyboardMarkup orqali:
#KOD: from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#
# keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# button = KeyboardButton('Birinchi tugma')
# keyboard.add(button)
#
# await message.answer("Tanlang", reply_markup=keyboard)


#8: Xabar yuborilgan suhbatning identifikatorini olish imkonini beruvchi usul. Botdan xabar yuborish uchun bizga ushbu identifikator kerak:
#KOD: from_chat_id()


#9: Funktsionallik nuqtai nazaridan, SQLite3 mijoz-server ilovalari uchun mijoz dasturidir. Uning yordami bilan siz ma'lumotlar bazasiga so'rovlarni kiritishingiz va uzatishingiz mumkin: jadval yaratish, o'zgartirish, olish yoki o'chirish.


#10: sqlite3 kutubxonasi orqali
#KOD: import sqlite3


#11: Bot foydalanuvchilari uchun jadval yaratish:
#KOD: CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER,
#     phone TEXT
# );


#12: KOD: conn = sqlite3.connect('db/database.db', check_same_thread=False)
#         cursor = conn.cursor()
#         def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
#         cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
#         conn.commit()
#         @dp.message(content_types=['text'])
#         def get_text_messages(message):
#         if message.text.lower() == 'привет':
#       bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')
#
#       us_id = message.from_user.id
#         us_name = message.from_user.first_name
#       us_sname = message.from_user.last_name
#       username = message.from_user.username
#
#       db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


#13: UPDATE orqali


#14: hamma userga limit berish


#15: pip install aiogram openai orqali
#KOD: import openai


import sqlite3
from aiogram import Bot, Dispatcher, types
import asyncio

TOKEN = "7251790744:AAHYES0QWgSwE17HiNAMDb6kvW_s_sW_U50"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


conn = sqlite3.connect('bot.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                )''')
conn.commit()


@dp.message()
async def message(message: types.Message):
    user_id = message.from_user.id
    user_text = message.text.lower()

    cursor.execute("SELECT answer FROM users WHERE question = ?", (user_text,))
    result = cursor.fetchone()

    if result:
        await message.answer(result[0])
    else:
        if user_text == "Salom":
            response = "Salom! Qalaysiz?"
        elif user_text == "qalaysan?":
            response = "Yaxshi, sizchi?"
        elif user_text == "menga hazil ayt":
            response = "Ikkita pomidor ko'chada yuribdi, biri ikkinchisiga: 'Tomatol!'"
        else:
            response = "Bunday savolga hali javobim yo'q."

        cursor.execute("INSERT INTO users (question, answer) VALUES (?, ?)", (user_text, response))
        conn.commit()

        await message.answer(response)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())