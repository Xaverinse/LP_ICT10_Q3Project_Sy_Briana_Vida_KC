from pyscript import document

takenuser = {
    "KC" : "INeedAHobbyAndSleepAndNoStressPls",
    "Bri" : "ShamanKingIsGOATED",
    "10Sapphire" : "WOOO",
    "Max" : "MaxIsTheBestBadmintoner",
    "Alonso" : "FartsAndButts",
    "Enzo" : "FootballIsLife",
    "Vic" : "letsgoooooo",
    "Kayla" : "SnoopyIsBetterThanYOU",
    "Athena" : "YahooVarsity",
    "Cade" : "BrokenChairsNeverForget",
    "Zyan" : "MeetPotentialMan",
    "Rad" : "RadsDiabetesAppointment",
    "Mara" : "KaworuNagisaShinjiIkari",
    "Kleiser" : "MauiWowie",
    "Curt" : "HandFootMouthDiseaseIsTheWorst",
    "Ethan" : "COOKIENIETHAN",
    "Sophie" : "CapybarasAreTheBest",
    "Javi" : "COCCDicator",
    "AC" : "TALLcookguy",
    "Lei" : "LeiIsMyGOAT",
    "Yanna" : "HolyRagebaiter",
    "Zoe" : "IceSkatesYahoo",
    "Luis" : "ICTGOAT",
    "Ara" : "ComeBack",
    "Inigo" : "CoffeeAddict",
    "Kyler" : "PokemonTCG",
    "Jaedin" : "YABookGirl",
    "Charlotte" : "LetsGoToUrHouse",
    "Jared" : "NonChalant"
    }

def signsups(event):

    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value.strip()

    if username == "" or password == "":
        document.getElementById("signed").innerText = "Put in a username and password PLEASE!!!"
    elif username in takenuser:
        document.getElementById("signed").innerText = "Are you that uncreative lil bro that username is already taken!!! (Your name is already in the files list bro js go to another tab)"
    else:
        takenuser[username] = password
        document.getElementById("signed").innerText = f"WOO! Congrats on signing up!!! Welcome {username} to intrams. (Please do NOT forget ur password cz I am not saving it in my non-existent database)"

