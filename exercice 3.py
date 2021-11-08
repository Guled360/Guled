password ="fruit"

trys = 3
while trys >0:
    playerguess= input("guess my password")
    if playerguess== password:
        print("well done")
        break
    elif playerguess != password and trys > 1:
        print("try again")
        trys -= 1
    else:
        print("you lose")
        break

