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
    event = await edit_or_reply(event, "â¢PONGâ¢")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"""
    ||â¢ðð¢ð£ð¬ððð§ ð¦ð£ðð  ðð¢ð§â¢||
â­ââââ®â±â±â±â±â±â±â±â±â±â±â±â±
ââ­ââ®ââ±â±â±â±â±â±â±â±â±â±â±â±
ââ°ââ¯ââ­âââ®â­âââ®â­âââ®
ââ­âââ¯ââ­â®âââ­â®âââ­â®â
âââ±â±â±ââ°â¯âââââââ°â¯â
â°â¯â±â±â±â°âââ¯â°â¯â°â¯â°ââ®â
â±â±â±â±â±â±â±â±â±â±â±â±â±â­ââ¯â
â±â±â±â±â±â±â±â±â±â±â±â±â±â°âââ¯\n\n
   MY MS â `{ms}`\n
    ð²âð  ð²âðÕá´ð¸â  â {DEFAULTUSER}
    """)

# By @Alone_loverboy 
# Don't Steal Credit else gay
# Credit lena wale ki maa ki ch*t ð
