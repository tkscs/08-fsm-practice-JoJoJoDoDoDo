state = "locked"
balance = 0

def purchase():
    global state
    global balance
    choice = input(f"You have inserted {balance} coins. Please insert more Coins or please choose an item: \n For 1 Coins: Soda Pop, Cheetos \n For 2 Coins: Keo's Wallet, Keo's Laptop\n")
    if choice == "Soda Pop" or choice == "Cheetos":
        if balance >= 1:
            balance = balance - 1
            print(f"You have purchased your {choice}! Your balance is now {balance}\n")
            locked()
        else:
            print("Insufficient funds.")
            locked()
    elif choice == "Keo's Wallet":
        if balance >= 2:
                balance = balance -2
                input(f"You have purchased Keo's Wallet!")
                coin()
        else:
            print("You have insufficient funds.")
            locked()
    elif choice == "Coin":
        coin()


def locked():
    global state
    global balance
    state = input("Would you like to purhcase an item, insert a Coin, or Leave?\n")
    if state == "Coin":
        coin()   
    if state == "Purchase":
        purchase()

def coin():
    global balance
    balance = balance + 1
    purchase()
     




locked()