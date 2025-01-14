#choose your own path
print("Welcome to Tresure island. \n Your mission is to find the treasure")






while True:
    ltoR_user = input("You're at a cross road. Where do you want to go? type Left or Right").lower() #one option is game over
    if ltoR_user == "left":
        print("You fell into a hole")
    elif ltoR_user =="right":
        wait_swim = input("You come to lake. There is an island in the middle of the lake. Type wait to wait for the boat. Type swim to swim across. ").lower() #1 option is game over 
        if wait_swim == "swim":
            print("Game over")
        elif wait_swim == "wait":
            doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()  #1 door is game over
            if doors == "red":
                print("You ran into a room on fire! \nGame Over")
            elif doors == "blue":
                print("You ran into a room with a killer in it. \nGame Over")
            elif doors == "yellow":
                print("You found the treasure! \nYou win!")
                break
            