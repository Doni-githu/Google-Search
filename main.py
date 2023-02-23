import json
import pprint
from deep_translator import GoogleTranslator
import requests

from aiogram import Dispatcher, Bot, executor, types

bot = Bot(token='5707871428:AAHwJQKFCQMi-kHvaRtskaJmxPdS-_7XMQs')

dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_polling(message: types.Message):
    await message.answer("Hi\nI'm Google Search Bot\nYou can find anything on me")


@dp.message_handler()
async def post(message: types.Message):
    url = "https://google-web-search1.p.rapidapi.com/"

    querystring = {"query": {message.text}, "limit": 20, "related_keywords": True}

    headers = {
        "X-RapidAPI-Key": "309762a3f1mshb8816378be4c2bcp1e702fjsn568bcbe3baf1",
        "X-RapidAPI-Host": "google-web-search1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).text
    data = json.loads(response)
    pprint.pprint(data['knowledge_panel']['description']['text'])
    knowledge = data['knowledge_panel']
    pprint.pprint(knowledge)
    description = knowledge['description']
    text = description['text']
    await message.answer(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
