from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import quote_html
from bot.common import report_msg_cb
from bot.config_reader import Config
from bot.localization import get_string


def get_message_url(chat_id, message_id):
    return "t.me/c/{chat_id}/{message_id}".format(
        chat_id=-1_000_000_000_000-chat_id,
        message_id=message_id
    )


async def error_no_reply(message: types.Message):
    lang = message.bot.get("config").lang
    await message.reply(get_string(lang, "error_no_reply"))


async def cmd_report(message: types.Message):
    config = message.bot.get("config")
    reported = await message.chat.get_member(message.reply_to_message.from_user.id)
    if reported.is_chat_admin():
        await message.reply(get_string(config.lang, "error_report_admin"))
        return

    available_options = {
        get_string(config.lang, "action_del_msg"): "del",
        get_string(config.lang, "action_del_and_ban"): "ban"
    }
    parts = message.text.split(maxsplit=1)
    report_msg_template = get_string(config.lang, "report_message")
    if len(parts) == 2:
        report_msg_template += get_string(config.lang, "report_note").format(note=quote_html(parts[1]))

    msg = await message.reply(get_string(config.lang, "report_sent"))

    kb = types.InlineKeyboardMarkup()
    for button_text, option in available_options.items():
        kb.add(types.InlineKeyboardButton(
            text=button_text,
            callback_data=report_msg_cb.new(
                option=option,
                user_id=message.reply_to_message.from_user.id,
                # Collect all IDs (initial message, report message, report confirmation) to delete afterwards
                message_ids=f"{message.reply_to_message.message_id},{message.message_id},{msg.message_id}"
            )))
    await message.reply_to_message.forward(config.group.reports)
    await message.bot.send_message(
        config.group.reports,
        report_msg_template.format(
            time=message.reply_to_message.date.strftime(get_string(config.lang, "report_date_format")),
            msg_url=get_message_url(message.chat.id, message.reply_to_message.message_id),
        ),
        reply_markup=kb
    )


async def calling_all_units(message: types.Message):
    config = message.bot.get("config")
    msg_url = get_message_url(message.chat.id, message.message_id)
    text = get_string(config.lang, "need_admins_attention").format(msg_url=msg_url)
    await message.bot.send_message(config.group.reports, text)


def register_main_group_user(dp: Dispatcher, main_group_id: int):
    dp.register_message_handler(error_no_reply, chat_id=main_group_id, is_reply=False, commands=["report"])
    dp.register_message_handler(cmd_report, chat_id=main_group_id, is_reply=True, commands="report")
    dp.register_message_handler(calling_all_units, Text(startswith="@admin", ignore_case=True), chat_id=main_group_id)
