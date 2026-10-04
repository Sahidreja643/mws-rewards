import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
MINI_APP_URL = "https://sahidreja643.github.io/mws-rewards/"

WELCOME_TEXT = """
🌟 <b>WELCOME TO MWS REWARDS</b> 🌟

🎉 <b>Welcome to MWS Rewards!</b>

Complete eligible activities, collect Coins, and build your Rewards Balance.

🚀 <b>START YOUR REWARDS JOURNEY</b>

🪙 Collect Coins
🎁 Claim Daily Rewards
🎡 Enjoy Your Free Spin
✅ Complete Available Tasks
👥 Invite Friends & Earn Referral Rewards
🏆 Check the Leaderboard
👛 Manage Your Wallet

💰 <b>REWARD RATE</b>
<b>10,000 Coins = $1.00</b>

🔐 <b>Secure • Simple • Transparent</b>

📌 Rewards are available only for eligible activities.
📌 Please review the applicable reward and withdrawal rules before requesting a withdrawal.

✨ <b>Ready to get started?</b>

Tap the button below to open MWS Rewards and begin your journey.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 OPEN MWS REWARDS",
                url=MINI_APP_URL
            )
        ]
    ]

    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💎 <b>MWS Rewards Help</b>\n\n"
        "Use /start to open MWS Rewards.",
        parse_mode="HTML"
    )

async def main()
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    await app.run_polling()

if __name__ == "__main__":
    main()
