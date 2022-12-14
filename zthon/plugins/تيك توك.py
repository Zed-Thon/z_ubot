# ๐๐๐๐๐๐ค๐ฃ ยฎ
# Port to ZThon
# modified by @ZedThon
# Copyright (C) 2022.


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from zthon import zedub

from ..core.managers import edit_or_reply

plugin_category = "ุงูุจุญุซ"


@zedub.zed_cmd(
    pattern="ุชููุชูู(?:\s|$)([\s\S]*)",
    command=("ุชููุชูู", plugin_category),
    info={
        "header": "ูู ุชุญููู ุงููููุฏููู ูู ุชููู ุชููู ุนุจูุฑ ุงูุฑุงุจูุท",
        "ุงูุงุณุชูุฎูุฏุงู": "{tr}ุชููุชูู ุจุงููุฑุฏ ุน ุฑุงุจูุท",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```ุจุงููุฑุฏ ุนูู ุงูุฑุงุจูุท ุญูุจูู ๐งธ๐```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```ุจุงููุฑุฏ ุนูู ุงูุฑุงุจูุท ุญูุจูู ๐งธ๐```**")
        return
    chat = "@ZZ191BOT"
    zzzzl1l = await edit_or_reply(
        event, "**โฎ โ ุฌูุงุฑู ุงูุชุญูููู ูู ุชููู ุชููู ุงูุชุธูุฑ ููููุงู  โฌโญ... ๐ซโฐ**"
    )
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2035595446)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit(
                "**โโุชุญููู ูู ุงููู ูู ุชููู ุจุญุธูุฑ ุงูุจูุช @ZZ191BOT .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith(""):
            await zzzzl1l.edit("**๐คจ๐...ุ**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "ุชูู ุชูู": "**ุงุณู ุงูุงุถุงููู : **`ุชูู ุชูู`\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ุชููุชูู` ุจุงูุฑุฏ ุนูู ุงูุฑุงุจุท\
    \n**ุงูุดูุฑุญ โขโข **ุชุญููู ููุงุทูุน ุงูููุฏููู ูู ุชููู ุชููู"
    }
)
