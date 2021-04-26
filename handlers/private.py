from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**مرحبا انا **{bn}** 🎵

بامكاني تشغيل الاغاني في المكالمات الجماعيه 
قم برفعي  مشرف في قناتك مع البوت المساعد [𝗠𝗨𝗦𝗜𝗖 𝗦𝗧𝗢𝗥𝗠](https://t.me/MUSIC_VOICEY).

قم باضافتي الى مجموعتك لتبدأ الحفله 🎶**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 لطلب المساعده 🛠", url="https://t.me/hhmhhh")
                  ],[
                    InlineKeyboardButton(
                        "💬 قناة للشروحات", url="https://t.me/in_arrray"
                    ),
                    InlineKeyboardButton(
                        "🔊 قناتي", url="https://t.me/CQCQQ"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕  اضفني الى مجموعتك ➕", url="https://t.me/zK_GvCBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** تم تفعيل البوت بنجاح ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 قناتي الخاصه", url="https://t.me/z44z4")
                ]
            ]
        )
   )


