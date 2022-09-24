from pyrogram import Client, filters 

API_ID = "12075871"
API_HASH = "e3c805f87c13a7a800dc1ceee2fbab8a"
BOT_TOKEN = "5506852836:AAHFwpwBM0ek8KfgfoXM9atLnmzaemrJPXE"

bot = Client(
  "Bot",
  bot_token=BOT_TOKEN,
  api_id=API_ID,
  api_hash=API_HASH
)

@bot.on_message(filters.command("start"))
async def start(bot, update):
    await update.reply_text("Hi")

bot.run()
