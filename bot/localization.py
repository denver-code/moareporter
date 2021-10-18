strings = {
    "ru": {
        "error_no_reply": "Командой нужно ответить на сообщение.",
        "error_report_admin": "Не выйдет, он админ, ему можно :)",
        "error_restrict_admin": "Невозможно ограничить администратора.",

        "report_date_format": "%d.%m.%Y в %H:%M",
        "report_message": '👆 Отправлено {time} (время серверное)\n'
                          '<a href="{msg_url}">Перейти к сообщению</a>',
        "report_note": "\n\nПримечание: {note}",
        "report_sent": "<i>Жалоба отправлена администраторам</i>",

        "action_del_msg": "Удалить сообщение",
        "action_del_and_ban": "Удалить и забанить",

        "action_deleted": "\n\n🗑 <b>Удалено</b>",
        "action_deleted_banned": "\n\n🗑❌ <b>Удалено, юзер забанен</b>",
        "action_deleted_partially": "Не удалось найти или удалить некоторые сообщения",

        "readonly_forever": "🙊 <i>Пользователь переведён в режим «только чтение» навсегда</i>",
        "readonly_temporary": "🙊 <i>Пользователь переведён в режим «только чтение» до {time} (время серверное)</i>",
        "nomedia_forever": "🖼 <i>Пользователю запрещено отправлять медиафайлы навсегда</i>",
        "nomedia_temporary": "🖼 <i>Пользователю запрещено отправлять медиафайлы до {time} (время серверное)</i>",

        "need_admins_attention": 'Админы, в чате нужно ваше присутствие!\n\n'
                                 '<a href="{msg_url}">Перейти к чату</a>',
    },
}


def get_string(lang: str, key: str):
    lang = strings.get(lang)
    if not lang:
        if not strings.get("en"):
            raise KeyError(f'Neither "{lang}" nor "en" locales found')
        else:
            lang = strings.get("en")
    try:
        return lang[key]
    except KeyError:
        return strings.get("en").get(key, "ERR_NO_STRING")
