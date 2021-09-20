import os

from speedtest import Speedtest
# discontinued -> import wget

from bot.helper.telegram_helper.filters import CustomFilters
from bot import dispatcher
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage # discontinued -> , sendPhoto
from telegram.ext import CommandHandler


def speedtest(update, context):
    speed = sendMessage("<code>Running speed test...</code>", context.bot, update)
    test = Speedtest()
    test.get_best_server()
    editMessage("<code>Performing download test.</code>", speed)
    editMessage("<code>Performing download test..</code>", speed)
    editMessage("<code>Performing download test...</code>", speed)
    test.download()
    editMessage("<code>Performing upload test.</code>", speed)
    editMessage("<code>Performing upload test..</code>", speed)
    editMessage("<code>Performing upload test...</code>", speed)
    test.upload()
    test.results.share()
    result = test.results.dict()
    # discontinued -> path = (wget.download)(result['share'])
    string_speed = f"""<b>--Started at {result['timestamp']}--

Client:

ISP: <code>{result['client']['isp']}</code>
ISP Rating: <code>{result['client']['isprating']}</code>
Country: <code>{result['client']['country']}</code>

Server:

Name: <code>{result['server']['name']}</code>
Country: <code>{result['server']['country']}, {result['server']['cc']}</code>
Sponsor: <code>{result['server']['sponsor']}</code>
Latency: <code>{result['server']['latency']}</code>

Ping: <code>{result['ping']}</code>
Sent: <code>{speed_convert(result['bytes_sent'])}</code>
Received: <code>{speed_convert(result['bytes_received'])}</code>
Upload: <code>{speed_convert(result['upload'] / 8)}/s</code>
Download: <code>{speed_convert(result['download'] / 8)}/s</code></b>"""
    editMessage(string_speed, speed)
# discontinued ->
    # editMessage(string_speed, speed) # SEMEN GRESIK
    #
    # deleteMessage(context.bot, speed)
    # await message.send_photo(chat_id=message.chat.id,
    #                          photo=path,
    #                          caption=string_speed)
    #
    # deleteMessage(context.bot, speed)
    # sendPhoto(context.bot,
    #           update,
    #         # property of speedtest.py
    #           photo=path,
    #           caption=string_speed)
    #
    # deleteMessage(context.bot, speed)
    # sendSpeedImage(context.bot,
    #                result['share'],
    #                caption=string_speed)
    #
    # deleteMessage(context.bot, speed)
    # await message.send_photo(chat_id=message.chat.id,
    #                          f"{result['share']}",
    #                          caption=string_speed)
    #
    # deleteMessage(context.bot, speed)
    # sendPhoto(context.bot, result['share'],
    #           caption=string_speed)
    #
    # # # os.remove(path) # # #

def speed_convert(size):
    """Hi human, you can't read bytes?"""
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "MB/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


SPEED_HANDLER = CommandHandler(BotCommands.SpeedCommand, speedtest, 
                                                  filters=CustomFilters.owner_filter | CustomFilters.authorized_user, run_async=True)

dispatcher.add_handler(SPEED_HANDLER)
