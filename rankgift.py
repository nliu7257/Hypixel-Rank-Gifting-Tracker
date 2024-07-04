import requests
import time
import winsound
from gtts import gTTS
import os


#data = requests.get(
   # url = "https://api.hypixel.net/player",
   # params = {
   #     "key": "0a45f668-8e28-46e5-945d-4b235da9ee76",
   #     "uuid": "9110e508131448648beb3adfe5841b90"
   # }
#).json()
ItzFunday = "e3ca6916278948d08fa403b85145affc"
AnimeCulture = "93992ef078aa48278d063619850197ec"
MrEnderdan = "219d62a92af54f5790d89c54e9941b80"
Whyplay = "e913fd01e84e4c6ead5b7419a12de481"
drakulatand = "abb1d5d9988741b58bc8cda47ce6899b" #Upgrading Ranks This Weekend Possibly
fz4 = "1e75fd33a765437b927810006e882b42" #Upgrading ranks This Friday Possibly
zywr = "4f39e70d34b243a98bbce61b38be80fa" #Upgrading Ranks Today Possibly
seven04k ="65317bc686274c29a87ac02231385916"
cassukee = "d848968ea8d04ec588f074272e80eeb8"
noobslayer700 = "9c6011447c764bcab4f32c5c68bda39c"
Choke = "0124f10b296d40f2b504da62fd66ebc2"
Ficcare = "163fa312b504470e8f1ca32ceafe7772" #Getting Money 12th of July #has api turned off
Lobby = "f9575394703f47ca8c902d7fd32b6818"
Requestable = "606898888ca74b5696310c37f3f1b12f" #has api turned off
uhMatthew = "870ed669750741c89a8947827de63912" #has api turned off
owo67 = "c9223a82964943b6aad14f2a09bdddbf" #has api turned off
ttiop= "e2ce3186598e458ca6da94db421644fc"
RenoldHenold = "0ef78c1317cd450cb3a3a89b5bb578e8" #has api turned off
Flamer777 = "52325c3bede74940addea4b05f45c324"
ZomIsABot = "4b3367a169a44a6d9eaae7a82d82c456"
qAway = "5ae4f86918f24bd2a77391f377830be8"
Kxric = "8b4d398bdfdb4011b9d96b291f28fb5c" #gifts people minding their own business 
hewty = "d347e56c69cd48489983b69e90614846"

list = [ItzFunday, AnimeCulture, MrEnderdan, Whyplay, drakulatand, fz4, zywr, seven04k, cassukee, noobslayer700, Choke, Ficcare, Lobby, Requestable, uhMatthew, owo67, ttiop, RenoldHenold, Flamer777, ZomIsABot, qAway, Kxric, hewty]

list2 = ["ItzFunday", "AnimeCulture", "MrEnderdan", "Whyplay", "drakulatand", "fz4", "zywr", "704k", "cassukee", "noobslayer700", "Choke", "Ficcare", "Lobby", "Requestable", "uhMatthew", "owo67", "ttiop", "RenoldHenold", "Flamer777", "ZomIsABot", "qAway", "Kxric", "hewty"]
list_ranks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

gifting_message = ""



isOnline = False
while True:
    for i in range(len(list)):
        header = {"key": "fa80b0dc-85f4-4fea-8621-244dc7d273dd","uuid": list[i]}
        try:
            isOnline = requests.get("https://api.hypixel.net/status", params=header).json()["session"]["online"]  #error
        except KeyError:
             print("Error: Online status for "+list2[i]+" is unknown. Try retrieving a new api from https://developer.hypixel.net/dashboard")
        
        if isOnline:
                try: 
                    x = requests.get("https://api.hypixel.net/status", params=header).json()["session"]["gameType"] #error
                    y= requests.get("https://api.hypixel.net/status", params=header).json()["session"]["mode"] #error
                    z= requests.get("https://api.hypixel.net/player", params = header).json()
                except:
                    print("Error occured while retrieving "+list2[i]+ "'s data \n")
                    time.sleep(2)
                    continue
                try:
                    gifted_ranks = z["player"]["giftingMeta"]["ranksGiven"] #error #this line of code doesn't work for noobslayer700
                except:
                    print(list2[i]+ " hasn't gifted any ranks yet! \n")
                    time.sleep(2)
                    continue

                print(list2[i] + " Is Currently Online")
                print(x)
                print(y)
                print("They has gifted "+str(gifted_ranks)+" ranks! \n") #it prints here the number of gifted ranks a player has

                if(list_ranks[i]!=gifted_ranks and list_ranks[i]!=0):
                    gifting_message = list2[i] + " just gifted a rank! Join the server now! \n"

                    myobj = gTTS(text = gifting_message, lang="en", slow=False)
                    myobj.save("giftedlol.mp3")
                    os.system("start giftedlol.mp3")
                    os.system("oh-my-god-meme.mp3")

                    print(gifting_message)  
                    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                    #time.sleep(2)
                    #winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                    #time.sleep(2)
                    #winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

                list_ranks[i] = gifted_ranks
        else:
            print(list2[i] + " Is Offline or has their API turned off\n")

        time.sleep(2)

    # Poll every 2min


#skywars_coins = data["player"]["stats"]["Duels"]["wins"]
##server_status = data["player"]["stats"]['session']['online']

#print(skywars_coins)


