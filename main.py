# pip install python-telegram-bot
# pip install TelegramBotAPI
# pip uninstall -y


# import telegram
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, filters, updater
#
# # Replace YOUR_TOKEN_HERE with your actual bot token
# bot = telegram.Bot(token='6193818235:AAFFmF1blK-FomScoFSbyfqohnUeSaWKy9I')
#
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your delivery bot. What would you like to order?")
#
# def order(update, context):
#     # TODO: Implement the menu and order list functionality
#     context.bot.send_message(chat_id=update.effective_chat.id, text="You ordered: ...")
#
# def buy(update, context):
#     # TODO: Implement the buy functionality and calculate the total price
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Your order has been placed. Total price: $...")
#
# def help(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Here are the available commands:\n/menu - to order food\n/order - to add meals to order list\n/buy - to place your order\n/help - to show this help message")
#
# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#
# def main():
#     updater = Updater(token='6193818235:AAFFmF1blK-FomScoFSbyfqohnUeSaWKy9I', use_context=True)
#     dispatcher = updater.dispatcher
#
#     # Add command handlers
#     dispatcher.add_handler(CommandHandler('start', start))
#     dispatcher.add_handler(CommandHandler('menu', order))
#     dispatcher.add_handler(CommandHandler('order', order))
#     dispatcher.add_handler(CommandHandler('buy', buy))
#     dispatcher.add_handler(CommandHandler('help', help))
#
#     # Add message handler to echo any other messages
#     dispatcher.add_handler(MessageHandler(filters.text & (~filters.command), echo))
#
#     updater.start_polling()
#     updater.idle()
#
# # if __name__ == '__main__':
# #     main()
#
# updater.start_polling()
# updater.idle()


# This code creates a Telegram bot that responds to the `/start`, `/menu`, `/order`, `/buy`, and `/help` commands.
# When the user sends any other message, the bot echoes it back. You need to implement the functionality for the
# `/menu`, `/order`, and `/buy` commands.


#Assignment_10
#
# import telegram
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
#
# # Replace YOUR_TOKEN_HERE with your actual bot token
# bot = telegram.Bot(token='6193818235:AAFFmF1blK-FomScoFSbyfqohnUeSaWKy9I')
#
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your delivery bot. What would you like to order?")
#
# def order(update, context):
#     # TODO: Implement the menu and order list functionality
#     context.bot.send_message(chat_id=update.effective_chat.id, text="You ordered: ...")
#
# def buy(update, context):
#     # TODO: Implement the buy functionality and calculate the total price
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Your order has been placed. Total price: $...")
#
# def help(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Here are the available commands:\n/menu - to order food\n/order - to add meals to order list\n/buy - to place your order\n/help - to show this help message")
#
# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#
# def main():
#     updater = Updater(token='6193818235:AAFFmF1blK-FomScoFSbyfqohnUeSaWKy9I', use_context=True)
#     dispatcher = updater.dispatcher
#
#     # Add command handlers
#     dispatcher.add_handler(CommandHandler('start', start))
#     dispatcher.add_handler(CommandHandler('menu', order))
#     dispatcher.add_handler(CommandHandler('order', order))
#     dispatcher.add_handler(CommandHandler('buy', buy))
#     dispatcher.add_handler(CommandHandler('help', help))
#
#     # Add message handler to echo any other messages
#     dispatcher.add_handler(MessageHandler(filters.text & (~filters.command), echo))
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()

import telebot

# Create a new Telegram Bot object
bot = telebot.TeleBot('6193818235:AAFFmF1blK-FomScoFSbyfqohnUeSaWKy9I')
print("Start")

# This dictionary contains the list of foods and their prices
menu = {
    'Pizza': 20,
    'Burger': 10,
    'Hot dog': 8,
    'French fries': 5,
    'Chicken wings': 12
}

# This dictionary contains the current order
order = {}

# This function displays the menu and orders food
@bot.message_handler(commands=['menu'])
def show_menu(message):
    # Create a new inline keyboard
    keyboard = telebot.types.InlineKeyboardMarkup()

    # Add a button for each food item in the menu
    for item in menu:
        button = telebot.types.InlineKeyboardButton(text=item + " - $" + str(menu[item]), callback_data=item)
        keyboard.add(button)

    # Send the menu to the user
    bot.send_message(message.chat.id, "What would you like to order?", reply_markup=keyboard)

# This function adds an item to the current order
@bot.callback_query_handler(func=lambda call: True)
def add_to_order(call):
    # Get the item name and price from the menu
    item = call.data
    price = menu[item]

    # Add the item to the current order
    if item in order:
        order[item]['quantity'] += 1
        order[item]['price'] += price
    else:
        order[item] = {'quantity': 1, 'price': price}

    # Confirm that the item was added to the order
    bot.answer_callback_query(call.id, "Added " + item + " to your order")

# This function displays the current order and the total price
@bot.message_handler(commands=['order'])
def show_order(message):
    # Create a new message for the order details
    text = "*Your Order*\n"

    # Add each item in the order to the message
    for item in order:
        quantity = order[item]['quantity']
        price = order[item]['price']
        text += "{} x {} - ${}\n".format(quantity, item, price)

    # Calculate the total price
    total = sum([order[item]['price'] for item in order])
    delivery_charge = int(total * 0.15)
    total += delivery_charge

    # Add the total price to the message
    text += "\n*Total: ${}*\n".format(total)
    text += "\n*Delivery: ${}*\n".format(total/100*15)

    # Send the order details to the user
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# The buy button confirms the order
@bot.message_handler(commands=['buy'])
def confirm_order(message):
    # If there are no items in the order, ask the user to order something
    if len(order) == 0:
        bot.send_message(message.chat.id, "Please order something first")
        return

    # Confirm the order with the user
    bot.send_message(message.chat.id, "Your order has been confirmed. Thank you!")

    # Reset the order
    order.clear()

# Start the bot
bot.polling()