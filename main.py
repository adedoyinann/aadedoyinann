# main.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Using your testing bot token directly
BOT_TOKEN = '7843062879:AAFbuACx2acZ9-pS0yrdpEQY7CVEB-xkjsU'

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    welcome_text = f"""
    👋 Welcome {user.first_name} to our Airdrop Bot!

    � To participate:
    1. Join our Telegram Channel
    2. Join our Telegram Group
    3. Follow our Twitter
    4. Submit your Solana wallet address

    Complete all steps to receive 10 SOL! 🚀
    """

    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/yourchannel")],
        [InlineKeyboardButton("👥 Join Group", url="https://t.me/yourgroup")],
        [InlineKeyboardButton("🐦 Follow Twitter", url="https://twitter.com/yourtwitter")],
        [InlineKeyboardButton("✅ Verify Participation", callback_data="verify")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def verify(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Please send your Solana wallet address now:")

async def handle_wallet(update: Update, context: CallbackContext):
    wallet_address = update.message.text
    # Basic length check for Solana address
    if len(wallet_address) >= 32 and len(wallet_address) <= 44:
        congrats_text = f"""
        🎉 Congratulations!

        You've successfully participated in our airdrop!
        10 SOL is on its way to your wallet:
        {wallet_address}

        ⏳ Please allow 24-48 hours for the tokens to arrive.
        Thank you for participating!
        """
        await update.message.reply_text(congrats_text)
    else:
        await update.message.reply_text("⚠️ That doesn't look like a valid Solana wallet address. Please try again.")

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    
    application.run_polling()

if __name__ == "__main__":
    main()
