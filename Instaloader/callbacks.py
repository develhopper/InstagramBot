from Data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Config import MUST_JOIN
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="**Here's How to use me**\n" + Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "check_must_join":
        try:
            await bot.get_chat_member(MUST_JOIN, callback_query.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                chat_id = callback_query.from_user.id
                message_id = callback_query.message.message_id
                await bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text="هنوز عضو نشده اید",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ عضویت ✨", url=link)],
                        [InlineKeyboardButton("عضو شدم", callback_data="check_must_join")],
                    ]),
                )
            except ChatWriteForbidden:
                pass
