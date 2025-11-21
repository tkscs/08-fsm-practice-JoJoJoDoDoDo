

state = "locked"

def finished():
    locked()






def locked():
    answer = input("Turnstile is currently locked, what would you like to do?")
    if answer == "push":
        print("You pushed, but it's locked, so nothing happened. Please insert a coin.")
        locked()
    elif answer == "coin":
        print("You put in a coin. You have unlocked the turnstile.")
        unlocked()
       
def unlocked():  
    answer = input("Turnstile is currently unlocked, what would you like to do?")
    if answer == "walk":
        print("You have pushed and spun the turnstile. You may go through!")
        finished()
    elif answer == "nothing":
        print("You did nothing.")
        unlocked()
    elif answer == "coin":
        print("You already put in a coin bruh")
        locked()
        

locked()