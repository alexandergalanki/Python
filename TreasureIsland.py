print("welcome to treasure Island")
print("Select right or left to move forward")

choice=input("which way?\n")
if choice =="left":
    choice2=input("swim or wait?\n")
    if choice2=="wait":
        door=input("Choose one door, red, blue, yellow?\n")
        if door == "yellow":
            print("you win")
        elif door == "red" or door == "blue":
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")