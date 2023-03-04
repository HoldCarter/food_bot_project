import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6014478028:AAErpHdDve-9rQb-eIQtY5buQjsQ2c9mjQU"
MSG = "Заюш, или {}, если официально (сладость моя, 'ам!'- съел), я пока только разрабатываюсь твоим МЧ :) Знаю одну кнопку (:"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Привет! Скорее всего это ты, Мари, но телеграм знает тебя как {user_full_name}")

    # for i in range(10):
    time.sleep(2)
    await bot.send_message(user_id, MSG.format(user_name))

# @dp.message_handler(commands=['start'])


if __name__ == '__main__':
    executor.start_polling(dp)