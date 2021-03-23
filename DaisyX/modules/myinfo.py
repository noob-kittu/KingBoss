# COPYRIGHT (C) BY KoraTeam
"""
(((((((((((((((((((((((@USEIES)))))))))))))))))))))))))))
(((((((((((((((((((((((@USEIES)))))))))))))))))))))))))))
(((((((((((((((((((((((@USEIES)))))))))))))))))))))))))))
(((((((((((((((((((((((@USEIES)))))))))))))))))))))))))))
               MADE BY USEIES AND KITTU
              COPYRIGHT BY USEIES AND KITTU
                 CREDIT #KORATEAM 
         IF YOU KANG THEN DONT REMOVE THIS LINES 
"""
import re

from telethon import custom, events

from DaisyX import telethn as bot
from DaisyX import telethn as tgbot
from DaisyX.events import register


@register(pattern="/myinfo")
async def proboyx(event):
    button = [[custom.Button.inline("⚡ CLICK ⚡", data="information")]]
    await bot.send_message(event.chat, "👤 CHECK YOUR INFORMATION", buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        SAMMY = "📝 YOUR DETAILS BY INNEXIA\n"
        SAMMY += f"🆔 FIRST NAME : {PRO.first_name} \n"
        SAMMY += f"📋 LAST NAME : {PRO.last_name}\n"
        SAMMY += f"🤖 YOU BOT : {PRO.bot} \n"
        SAMMY += f"🚫 RESTRICTED : {PRO.restricted} \n"
        SAMMY += f"👤 USER ID : {boy}\n"
        SAMMY += f"🛡️ USERNAME : {PRO.username}\n"
        await event.answer(SAMMY, alert=True)
    except Exception as e:
        await event.reply(f"{e}")
