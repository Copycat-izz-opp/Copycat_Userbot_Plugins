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

pm_caption = "__                       **ππ₯ #Copycat_Spam_Bot On Fire ππ₯**  __\n\n"

pm_caption += f"               __βΌπΌπ°πππ΄πβ__\n**      γ{DEFAULTUSER}γ**\n\n"
pm_caption += "β α©α·OαT α°Y ΥYΥTα΄α° β\n\n"
pm_caption += "β  Tα΄αͺα΄TαΌOα   β£ 1.22.0\n"                 
pm_caption += "β  Tα΄α©α° ααOαα­ β£ [ππππ](https://t.me/Lovers_Match)\n"
pm_caption += "β  Υαα­α­OαT ααΌαααͺ β£ [ππππ](https://t.me/Copycat_Spam)\n"
pm_caption += "β  Υαα­α­OαT ααα­ β£ [ππππ](https://t.me/Copycat_Spam_Bot)\n"
pm_caption += "β  ααα΄α©TOα β£ [πCopycatπ](t.me/My_Love_Coming_Near)\n\n" 
pm_caption += "[παͺα΄α­αͺOY αOα­Yαα©T Υα­α©α° α·OTπ](https://github.com/Copycat-izz-opp/copycat_spam_userbot)"
                                                     
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
