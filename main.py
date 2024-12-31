import requests
import threading
import random
from colorama import Fore

response = requests.get("https://raw.githubusercontent.com/nullspechattacks/bot/refs/heads/main/bot.txt")
bot = response.text.split()

send = 0

def main():
    while True:
        id, token, password, device_id, sign = random.choice(bot).split(":")

        headers = {
            "userId": id,
            "access-token": token,
            "user-agent": "okhttp/3.12.0"
        }

        response0 = requests.get("https://solarsys.resquared.fr/friend/api/v1/friends/recommendation", headers=headers).json()

        if response0["message"] == "SUCCESS":
            request = -1
            while True:
                request += 1

                if request == 10:
                    break

                id, token, password, device_id, sign = random.choice(bot).split(":")

                headers = {
                    "userId": id,
                    "access-token": token,
                    "user-agent": "okhttp/3.12.0"
                }

                data = {
                    "friendId": response0["data"][request]["userId"],
                    "msg": "telegram @nullowns"
                }

                response = requests.post("https://solarsys.resquared.fr/friend/api/v1/friends", headers=headers, json=data).json()

                if response["message"] == "SUCCESS":
                    print(Fore.LIGHTGREEN_EX + response["message"] + Fore.RESET)
                else:
                    print(Fore.LIGHTRED_EX + "limit on sending friend requests" + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX + "limit on getting friends" + Fore.RESET)

for _ in range(5):
    threading.Thread(target=main).start()
