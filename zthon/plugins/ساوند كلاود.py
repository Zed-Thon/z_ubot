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
    pattern="ุณุงููุฏ(?:\s|$)([\s\S]*)",
    command=("ุณุงููุฏ", plugin_category),
    info={
        "header": "ูุชุญููู ุงูุงุบุงูู ูู ุณุงููุฏ ูููุฏ ุนุจุฑ ุงูุฑุงุจูุท",
        "ุงูุงุณุชูุฎูุฏุงู": "{tr}ุณุงููุฏ ุจุงููุฑุฏ ุน ุฑุงุจูุท",
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
    chat = "@DeezerMusicBot"
    catevent = await edit_or_reply(
        event, "**โฎ โ ุฌูุงุฑู ุงูุชุญูููู ูู ุณูุงููุฏ ูููุงูุฏ ุงูุชุธูุฑ ููููุงู  โฌโญ... ๐ซโฐ**"
    )
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=595898211)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**โโุชุญููู ูู ุงููู ูู ุชููู ุจุญุธูุฑ ุงูุจูุช @downloader_tiktok_bot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**๐คจ๐...ุ**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(
    pattern="ูููุฏ ([\s\S]*)",
    command=("ูููุฏ", plugin_category),
    info={
        "header": "ูุชุญููู ุงูุงุบุงูู ูู ุณุงููุฏ ูููุฏ ุนุจุฑ ุงูุฑุงุจูุท",
        "ุงูุงุณุชูุฎูุฏุงู": "{tr}ูููุฏ + ุฑุงุจุท",
    },
)
async def zed(event):
    if event.fwd_from:
        return
    zedr = event.pattern_match.group(1)
    zelzal = "@DeezerMusicBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(zelzal, zedr)
    await tap[0].click(event.chat_id)
    await event.delete()
