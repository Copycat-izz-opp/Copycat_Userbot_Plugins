import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, deadlyversion
from deadlybot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Copycat Bot"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

deadly = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = Config.ALIVE_PIC
""" =======================CONSTANTS====================== """

pm_caption = "__                       **😎🔥 #Copycat_Spam_Bot On Fire 😈🔥**  __\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
pm_caption += "✘ ᗩᗷOᑌT ᗰY ՏYՏTᗴᗰ ✘\n\n"
pm_caption += "➠ TᗴᒪᗴTᕼOᑎ   ➣ 1.22.0\n"                 
pm_caption += "➠ Tᗴᗩᗰ ᘜᖇOᑌᑭ ➣ [𝐉𝐎𝐈𝐍](https://t.me/Lovers_Match)\n"
pm_caption += "➠ ՏᑌᑭᑭOᖇT ᑕᕼᑎᑎᒪ ➣ [𝐉𝐎𝐈𝐍](https://t.me/Copycat_Spam)\n"
pm_caption += "➠ ՏᑌᑭᑭOᖇT ᘜᖇᑭ ➣ [𝐉𝐎𝐈𝐍](https://t.me/Copycat_Spam_Bot)\n"
pm_caption += "➠ ᑕᖇᗴᗩTOᖇ ➣ [😈Copycat😈](t.me/My_Love_Coming_Near)\n\n" 
pm_caption += "[😈ᗪᗴᑭᒪOY ᑕOᑭYᑕᗩT Տᑭᗩᗰ ᗷOT😈](https://github.com/Copycat-izz-opp/CopyCat_Spam_Bot/blob/master/README.md)"
                                                     
# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "awake", None, "To check am i alive with your favorite alive pic"
).add()
