from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8284940751:AAGe3tJGRRljvTzWweEw9u4IGHxVPy8deMY"

# --- КНОПКИ ---
main_menu = ReplyKeyboardMarkup(
    [
        ["📘 О курсе"],
        ["🎓 Формат обучения"],
        ["👥 Кому подойдёт"],
        ["🚀 Чему вы научитесь"],
    ],
    resize_keyboard=True
)

back_menu = ReplyKeyboardMarkup(
    [["🔙 Назад"]],
    resize_keyboard=True
)

# --- ТЕКСТЫ ---
texts = {
    "📘 О курсе": (
        "📘 *Нейросети для успешной карьеры*\n\n"
        "Практический курс о том, как использовать ИИ для работы, "
        "карьерного роста и увеличения дохода."
    ),
    "🎓 Формат обучения": (
        "🎓 *Формат обучения*\n\n"
        "• Онлайн\n"
        "• Короткие уроки\n"
        "• Практика\n"
        "• Доступ 24/7"
    ),
    "👥 Кому подойдёт": (
        "👥 *Кому подойдёт курс*\n\n"
        "• Новичкам\n"
        "• Специалистам\n"
        "• Фрилансерам\n"
        "• Предпринимателям"
    ),
    "🚀 Чему вы научитесь": (
        "🚀 *Чему вы научитесь*\n\n"
        "• Работать с нейросетями\n"
        "• Автоматизировать задачи\n"
        "• Создавать контент\n"
        "• Использовать ИИ для дохода"
    ),
}

# --- КОМАНДЫ ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Добро пожаловать!\nВыберите пункт меню 👇",
        reply_markup=main_menu
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 Главное меню:", reply_markup=main_menu)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts["📘 О курсе"], reply_markup=back_menu, parse_mode="Markdown")

async def format_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts["🎓 Формат обучения"], reply_markup=back_menu, parse_mode="Markdown")

async def who(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts["👥 Кому подойдёт"], reply_markup=back_menu, parse_mode="Markdown")

async def skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts["🚀 Чему вы научитесь"], reply_markup=back_menu, parse_mode="Markdown")

# --- ОБРАБОТКА КНОПОК ---
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔙 Назад":
        await update.message.reply_text("📋 Главное меню:", reply_markup=main_menu)
    elif text in texts:
        await update.message.reply_text(texts[text], reply_markup=back_menu, parse_mode="Markdown")

# --- ЗАПУСК ---
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("format", format_cmd))
app.add_handler(CommandHandler("who", who))
app.add_handler(CommandHandler("skills", skills))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

print("✅ Бот запущен")
app.run_polling()
