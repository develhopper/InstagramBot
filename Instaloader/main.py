from pyrogram import Client, filters


@Client.on_message(filters.private & ~filters.regex(r'^/'))
async def main(_, msg):
    if 'instagram.com' not in msg.text:
        return msg.reply(error)

    status = await msg.reply('Please Wait...', quote=True)
    reply = msg.text.replace('instagram.com','ddinstagram.com');
    await msg.reply("[.]("+reply+")",qoute=True)
    


error = """
لینک اشتباه ⚠️ لطفا لینک درست از اینستاگرام ارسال کنید
"""
