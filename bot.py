import os
import time

from pyrogram import Client, filters, idle
from pyrogram.raw.functions.account import UpdateStatus

os.chdir(os.path.dirname(__file__))

app = Client(
    session_name = 'bot',
    api_id = 0,
    api_hash = '',
    app_version = '1.0',
    device_model = 'github:rahmansharifi/pyrogram-interactions',
    system_version = '1.0',
)

@app.on_message(filters.command('ping'))
def _(Client, Message):
    Client.read_history(Message.chat.id)
    Client.send_chat_action(Message.chat.id,'typing')
    time.sleep(1)
    Message.reply('Userbot works fine!')

app.start()
app.send(UpdateStatus(offline=False))
idle()
app.stop()
