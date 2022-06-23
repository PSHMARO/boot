from pyrogram import Client
from time import sleep
import requests

IMG = "📗📕📒📔📓📙📘"
api_id = 15576709
api_hash = "45adba5cd7a831be11a1c97a40a52528"
ChatId = "Twitter4gramBot"

userbot = Client("Maro", api_id, api_hash)


def main():
    userbot.start()
    while True:
        for ranNum in range(15510, 34082):
            try:
                link = "https://t.me/TTTTpT/" + str(ranNum)
                x = requests.get(link).text
                x = x.split('<meta property="og:description" content="')[1]
                twt = x.split('">')[0]
                for EG in list(IMG):
                    if EG in twt:
                        if "https" in twt or "http" in twt or "t.me" in twt or "@" in twt:
                            pass
                        else:
                            userbot.send_message(
                                chat_id=ChatId,
                                text=twt.replace('📗', '').replace(
                                    '📕', '').replace('📒', '').replace(
                                        '📔', '').replace('📓', '').replace(
                                            '📙', '').replace('📘', ''))
                            sleep(120)
                    else:
                        pass
            except:
                pass


main()
