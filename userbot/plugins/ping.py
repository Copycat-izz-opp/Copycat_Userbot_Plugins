import asyncio
from datetime import datetime
from userbot import StartTime
from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from ..cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Deadly User"
opsameer = borg.uid

@bot.on(admin_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))

async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "•PONG•")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"""
    ||•𝗖𝗢𝗣𝗬𝗖𝗔𝗧 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧•||
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱
┃╰━╯┃╭━━╮╭━━╮╭━━╮
┃╭━━╯┃╭╮┃┃╭╮┃┃╭╮┃
┃┃╱╱╱┃╰╯┃┃┃┃┃┃╰╯┃
╰╯╱╱╱╰━━╯╰╯╰╯╰━╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯\n\n
   MY MS → `{ms}`\n
    🇲 𝚈  🇲 𝗔Տᴛ𝐸ℝ  → {DEFAULTUSER}
    """)

# By @Alone_loverboy 
# Don't Steal Credit else gay
# Credit lena wale ki maa ki ch*t 🙂
