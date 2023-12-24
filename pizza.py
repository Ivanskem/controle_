import time
def addpizza():
    walletlist.append(pick)
    wallet += pickprice
    return walletlist, wallet
def selectlaunguage():
    launguage = str(input())
    return launguage
def menu():
    print("Выберите, что хотите сделать. Заказать, Посмотреть чек, Выйти.")
    pickif = str(input())
    if pickif == "Заказать" or "заказать" or "ЗАКАЗАТЬ":
        print("В наличие есть такие блюда как:", avaiableru)
        time.sleep(0.3)
        print("Введите название блюда которое хотите заказать: ")
        if str(input()) == "Пеперони":
            pick = "Пеперони"
            pickprice = peperoni
            addpizza()
            wallet += peperoni
            print("Пицца, Пеперони добавлена")
        elif str(input()) == "Маргарита":
            pick = "Маргарита"
            pickprice = margarita
            addpizza()
            wallet += margarita
            print("Пицца, Маргарита добавленна")
    if pickif == "выйти" or "Выйти" or "ВЫЙТИ":
        walletlist.clear()
        wallet = 0
        pick = ""
        pickprice = 0
        pickif = 0
        launguage = ""

    else:
        print("Команда введена неверно!")
    return wallet
def exitclear():
    walletlist.clear()
    wallet = 0
    pick = ""
    pickprice = 0
    pickif = 0
    launguage = ""
#pizza price
peperoni = 500
margarita = 450
launguage = ""
version = "BETA"
wallet = 0
walletlist = []
pick = ""
pickprice = 0
pickif = ""
peperonicount = 500
avaiableru = ["Пеперони", "Маргарита"]
print("Select launguage", "Выберите язык")
time.sleep(0.2)
print("En or Ru")
selectlaunguage()
if launguage == "ru" or "RU":
    print("version: ",version, "launguage: RU")
    print("вы попали на бета тест Пиццерии")
    time.sleep(0.5)
    menu()