from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
سلام {}
 به اینستادانلودر پارسیس خوش آمدید 🙏🏻
من میتونم عکس پروفایل ، ویدیو ، عکس و ریلز های ایسنتاگرام رو همراه با کپشن براتون دانلود کنم 😎
تو حتی میتونی به من اجازه بدی عکس های اکانت های پرایوت رو هم دانلود کنم .
از دکمه های زیر برای اطلاعات بیشتر استفاده کن 👇🏻
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
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
