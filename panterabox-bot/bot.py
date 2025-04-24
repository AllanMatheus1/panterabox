import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

#variaveis do ambiente
load_dotenv()

# painel de opções

async def show_panel(update: Update, context: ContextTypes.DEFAULT_TYPE, first_time=False):
    keyboard = [
        [InlineKeyboardButton("Notícias", callback_data="noticias")],
        [InlineKeyboardButton("Jogos", callback_data="jogos")],
        [InlineKeyboardButton("Loja furia", callback_data="loja_furia")],
        [InlineKeyboardButton("Próximos Campeonatos",
                              callback_data="prox_campeonatos")],
        [InlineKeyboardButton("Redes Sociais", callback_data="redes_sociais")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if first_time:

        await update.message.reply_text(f"Olá, {update.effective_user.first_name}! 🐾 Bem-vindo ao Bot da FURIA!", reply_markup=reply_markup)
    else:

        if hasattr(update, "callback_query") and update.callback_query:
            await update.callback_query.message.reply_text("Outras Opções:", reply_markup=reply_markup)
        elif hasattr(update, "message") and update.message:
            await update.message.reply_text("Outras Opções:", reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_reply_markup(reply_markup=None)

    if query.data == "noticias":
        await noticias(update, context)

    elif query.data == "jogos":
        await jogos(update, context)

    elif query.data == "loja_furia":
        await loja_furia(update, context)

    elif query.data == "prox_campeonatos":
        await prox_campeonatos(update, context)

    elif query.data == "redes_sociais":
        await redes_sociais(update, context)

    await show_panel(update, context, first_time=False)

    # comandos


async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.message.reply_text(
        "Aqui estão as últimas notícias da FURIA! 🔥\n\n"
        "[Draft5 Notícias](https://draft5.gg/equipe/330-FURIA)",
        parse_mode="Markdown"
    )
    await query.message.reply_text(
        "[HLTV Notícias](https://www.hltv.org/team/8297/furia)",
        parse_mode="Markdown"
    )


async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.message.reply_text("Aqui estão os próximos jogos da FURIA! 🎮\n\n- A definir!")


async def loja_furia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.message.reply_text("Acesse a FURIA Store aqui: https://www.furia.gg/")


async def prox_campeonatos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.message.reply_text(
        "Aqui estão os próximos campeonatos da FURIA! 🏆\n\n"
        "- [Próximos Campeonatos](https://draft5.gg/campeonato/2064-PGL-Astana-2025)",
        parse_mode="Markdown"
    )


async def redes_sociais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.message.reply_text(
        "Siga a FURIA nas redes sociais! 📱")

    await query.message.reply_text(
        "[Twitter](https://www.x.com/FURIA)", parse_mode="Markdown")
    await query.message.reply_text(
        "[Instagram](https://www.instagram.com/furiagg/)", parse_mode="Markdown")
    await query.message.reply_text(
        "[Facebook](https://www.facebook.com/furiagg)", parse_mode="Markdown")
    await query.message.reply_text(
        "[YouTube](https://www.youtube.com/@FURIAggCS)", parse_mode="Markdown")
    await query.message.reply_text(
        "[Twitch](https://www.twitch.tv/furiatv)", parse_mode="Markdown")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_panel(update, context, first_time=True)


if __name__ == '__main__':
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError(
            "O token do bot não foi configurado. Verifique o arquivo .env.")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Deu certo")
    app.run_polling()
