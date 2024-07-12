# pip install python-telegram-bot
# pip install TelegramBotAPI
# pip uninstall -y


#Assignment_11
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters


def start(update, context):
    update.message.reply_text("Hello! I'm a Math Calculator Bot. How can I help you today?")

def perimeter(update, context):
    try:
        sides = [float(x) for x in context.args]
        if len(sides) == 1:
            result = 4 * sides[0]
            update.message.reply_text(f"The perimeter of the square is {result}")
        elif len(sides) == 2:
            result = 2 * (sides[0] + sides[1])
            update.message.reply_text(f"The perimeter of the rectangle is {result}")
        else:
            update.message.reply_text("Please provide the correct number of sides.")
    except ValueError:
        update.message.reply_text("Please provide valid numbers.")

def area(update, context):
    try:
        sides = [float(x) for x in context.args]
        if len(sides) == 1:
            result = sides[0] ** 2
            update.message.reply_text(f"The area of the square is {result}")
        elif len(sides) == 2:
            result = sides[0] * sides[1]
            update.message.reply_text(f"The area of the rectangle is {result}")
        else:
            update.message.reply_text("Please provide the correct number of sides.")
    except ValueError:
        update.message.reply_text("Please provide valid numbers.")

def discriminant(update, context):
    try:
        a, b, c = [float(x) for x in context.args]
        result = b**2 - 4*a*c
        update.message.reply_text(f"The discriminant is {result}")
    except ValueError:
        update.message.reply_text("Please provide valid numbers.")

def root(update, context):
    try:
        a, b, c = [float(x) for x in context.args]
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            update.message.reply_text("The roots are imaginary.")
        else:
            root1 = (-b + discriminant**0.5) / (2*a)
            root2 = (-b - discriminant**0.5) / (2*a)
            update.message.reply_text(f"The roots are {root1} and {root2}")
    except ValueError:
        update.message.reply_text("Please provide valid numbers.")

def power(update, context):
    try:
        base, exponent = [float(x) for x in context.args]
        result = base ** exponent
        update.message.reply_text(f"{base} raised to the power of {exponent} is {result}")
    except ValueError:
        update.message.reply_text("Please provide valid numbers.")

def main():
    # replace YOUR_TOKEN with your bot token
    updater = Updater(token='6225138374:AAGmLdqlS1-xroU5HtRW5XiNFKZbfHcYNck', use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for different commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("perimeter", perimeter))
    dispatcher.add_handler(CommandHandler("area", area))
    dispatcher.add_handler(CommandHandler("discriminant", discriminant))
    dispatcher.add_handler(CommandHandler("root", root))
    dispatcher.add_handler(CommandHandler("power", power))

    # start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

