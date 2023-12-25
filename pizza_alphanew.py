import time
def checkwallet():
    print(wallet, walletlist)
def exitclear():
    walletlist.clear()
    wallet = 0
    pick = ""
    pickprice = 0
    pickif = 0
    launguage = ""
    return wallet, pick, pickprice, pickif, launguage
def addpizza(wallet=0):
    walletlist.append(pick)
    wallet += pickprice
    return walletlist, wallet
def selectlaunguage():

    return launguage
def menuRu(wallet=0):
    print("Выберите, что хотите сделать. Заказать, Посмотреть чек, Выйти.")
    pickif = str(input())
    if pickif == "Заказать" or "заказать" or "ЗАКАЗАТЬ":
        print("В наличие есть такие блюда как:", avaiableru)
        time.sleep(0.3)
        print("Введите название блюда которое хотите заказать: ")
        pizzachoose = str(input())
        if pizzachoose == "Пеперони" or "пеперони" or "ПЕПЕРОНИ":
            pick = "Пеперони"
            pickprice = peperoni
            addpizza()
            wallet += peperoni
            print("Пицца, Пеперони добавлена")
        elif pizzachoose == "Маргарита" or "маргарита" or "МАРГАРИТА":
            pick = "Маргарита"
            pickprice = margarita
            addpizza()
            wallet += margarita
            print("Пицца, Маргарита добавленна")
        else:
            print("Имя пиццы написана неправильно")
    else:
        print("Команда введена неверно!")
    if pickif == "посмотреть чек" or "Посмотреть Чек" or "ПОСМОТРЕТЬ ЧЕК":
        checkwallet()
    else:
        print("Команда введена неверно!")
    if pickif == "выйти" or "Выйти" or "ВЫЙТИ":
        exitclear()
    else:
        print("Команда введена неверно!")
    return wallet, walletlist, pick, pickprice
def menuEN(wallet=0):
    print("Choose, what you need to do. order, check wallet, Exit.")
    pickif = str(input())
    if pickif == "order" or "Order" or "ORDER":
        print("There are dishes available such as:", avaiableen)
        time.sleep(0.3)
        print("Enter the name of the dish you want to order: ")
        pizzachoose = str(input())
        if pizzachoose == "Peperoni" or "peperoni" or "PEPERONI":
            pick = "peperoni"
            pickprice = peperoni
            addpizza()
            wallet += peperoni
            print("Pizza, Peperoni was added")
        elif pizzachoose == "Margarita" or "margarita" or "MARGARITA":
            pick = "Margarita"
            pickprice = margarita
            addpizza()
            wallet += margarita
            print("Pizza, Margarita was added")
        else:
            print("Name of pizza is incorrect")
    else:
        print("Command is incorrect!")
    if pickif == "check wallet" or "Check Wallet" or "CHECK WALLET":
        checkwallet()
    else:
        print("Command is incorrect!")
    if pickif == "exit" or "Exit" or "EXIT":
        exitclear()
    else:
        print("Command is incorrect!")
    return wallet, walletlist, pick, pickprice
#pizza price
peperoni = 500
pizzachoose = ""
margarita = 450
launguage: str = ""
version = "ALPHA"
wallet = 0
walletlist = []
pick = ""
pickprice = 0
pickif = ""
peperonicount = 500
avaiableru = ["Пеперони", "Маргарита"]
avaiableen = ["Peperoni", "Margarita"]
print("Select launguage",";", "Выберите язык")
time.sleep(0.2)
print("En or Ru")
menuEN()