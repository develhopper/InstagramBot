from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
    سلام {}
به اینستادانلودر پارسیس خوش آمدید 🙏🏻
من میتونم ویدیو ، عکس و ریلز های اینستاگرام رو همراه با کپشن براتون دانلود کنم 😎
✅ هروقت آماده بودی لینک رو برام بفرست
راهنمایی بیشتر ، دکمه های زیر  👇🏻
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 بازگشت 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("راهنمای استفاده ❔", callback_data="help"),
            InlineKeyboardButton("🎪 درباره 🎪", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
ℹ️ چجوری استفاده کنیم ؟

✅ کافیه لینک پست / ریلز/ پروفایل رو برام بفرستی تا با کپشن برات دانلودش کنم .
⚠️ متاسفانه استوری و IGTV  رو نمیتونم دانلود کنم.

"""

    # About Message
    ABOUT = """درباره این بات 

این بات مختص به تیم پارسیس میباشد .
اینستاگرام ما : https://bit.ly/Parsisinsta
کانال ما : @soheylschannel
    """
