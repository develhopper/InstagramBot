from pyrogram import Client, filters


@Client.on_message(filters.private & ~filters.regex(r'^/'))
async def main(_, msg):
    if 'instagram.com' not in msg.text:
        return msg.reply(error)

    status = await msg.reply('Please Wait...', quote=True)
    reply = msg.text.replace('instagram.com','ddinstagram.com');
    msg.reply(reply)
    


error = """
Please send me a valid instagram post link.
It must be like one of the given below
"""
