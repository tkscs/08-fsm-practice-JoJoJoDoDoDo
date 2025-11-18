state = "locked"

while state != "finished":
    while state == "locked":
        answer = input("State is currently locked, what would you like to do?")
        if answer == "push":
            print("You pushed, but it's locked, so nothing happened. Please put in a coin.")
        elif answer == "coin":
            print("You put in a coin. You have unlocked the device.")
            state = "unlocked"
    while state == "unlocked":
        answer = input("State is currently unlocked, what would you like to do?")
        if answer == "push":
            print("You have pushed and spun the machine. You may go through!")
            state = "finished"
        elif answer == "nothing":
            print("You did nothing.")
        elif answer == "coin":
            print("You already put in a coin stupid")
            state = "locked"
            

