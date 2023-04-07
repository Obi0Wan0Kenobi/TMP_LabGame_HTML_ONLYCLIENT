import time

import requests

domain = "http://localhost:80"

url = domain + "/new"
userinfo = requests.request("GET", url)
userinfo = userinfo.json()
Userid = userinfo["UserUid"]
Usertoken = userinfo["Token"]
print(f"Ваш айди: {Userid}")

while True:
    print("Ожидание...")
    findgame = requests.request("GET", f"{domain}/find/{Userid}?token={Usertoken}").json()
    while not findgame["Finded"]:
        findgame = requests.request("GET", f"{domain}/find/{Userid}?token={Usertoken}").json()
        time.sleep(0.1)
    print(f"Вы играете с {findgame['Playingwith']}")

    choose = input("Выберите 1 - камень, 2 - ножницы, 3 - бумага: ")
    while not (choose == "1" or choose == "2" or choose == "3"):
        choose = input("Выберите 1 - камень, 2 - ножницы, 3 - бумага: ")


    requests.request("GET", f"{domain}/choose/{Userid}?token={Usertoken}&chose={choose}")

    winornot = requests.request("GET", f"{domain}/check/{Userid}?token={Usertoken}").json()
    while winornot["Wait"]:
        winornot = requests.request("GET", f"{domain}/check/{Userid}?token={Usertoken}").json()
        time.sleep(0.1)

    print(winornot["Windata"])

    restart = input("Введите 1 если хотите сыграть еще раз: ")
    if restart != "1":
        exit()
    else:
        requests.request("GET", f"{domain}/restart/{Userid}?token={Usertoken}").json()

