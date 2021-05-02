# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [CREATOR("ButtonUrl", url="https://t.me/ReSpXcT")],
                        [😜 Just A Test 😜("Inline Button",data="example")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("Nice 🤓! Now, Join @GangstersGroupp")
