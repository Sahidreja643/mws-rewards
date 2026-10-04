import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("BOT_TOKEN")
APP_URL = "https://sahidreja643.github.io/mws-rewards/"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = (
        "🌟 <b>WELCOME TO MWS REWARDS</b> 🌟\n\n"
        "🎉 <b>Welcome to MWS Rewards!</b>\n\n"
        "Complete eligible activities, collect Coins, "
        "and build your Rewards Balance.\n\n"
        "🚀 <b>START YOUR REWARDS JOURNEY</b>\n\n"
        "🪙 Collect Coins\n"
        "🎁 Claim Daily Rewards\n"
        "🎡 Enjoy Your Free Spin\n"
        "✅ Complete Available Tasks\n"
        "👥 Invite Friends & Earn Referral Rewards\n"
        "🏆 Check the Leaderboard\n"
        "👛 Manage Your Wallet\n\n"
        "💰 <b>REWARD RATE</b>\n"
        "<b>10,000 Coins = $1.00</b>\n\n"
        "🔐 <b>Secure • Simple • Transparent</b>\n\n"
        "📌 Rewards are available only for eligible activities.\n"
        "📌 Please review the applicable reward and withdrawal "
        "rules before requesting a withdrawal.\n\n"
        "✨ <b>Ready to get started?</b>\n\n"
        "Tap the button below to open MWS Rewards."
    )

    button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🚀 OPEN MWS REWARDS",
                url=APP_URL
            )
        ]
    ])

    await update.message.reply_text(
        message,
        parse_mode="HTML",
        reply_markup=button
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "💎 <b>MWS Rewards Help</b>\n\n"
        "Use /start to open MWS Rewards.",
        parse_mode="HTML"
    )


def main():

    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not configured.")

    bot = Application.builder().token(TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("help", help_command))

    print("MWS Rewards Bot is running...")

    bot.run_polling()


if __name__ == "__main__":
    main()
