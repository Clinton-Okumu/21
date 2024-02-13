name = input("Type your name: ").lower

print("Welcome", name ,"to your adventure!")

answer = input("""You are in a pathway in a forest
 and there are two ways your left and your right,
pick one route please? """)

if answer == "left":
    answer = input("""You have come across a river and you 
    only have three options
    (run/walk/swim) pick one? """).lower()
    if answer == "swim":
        print("You swam and were eaten by a crocodile! you you died")
    elif answer == "run":
        print("You ran alot of kilometres and were finally eaten in the wild")
    elif answer == "walk":
        print("You walked an you got eaten by wild animals. Tough luck G!")
    else:
        print("You picked invalid optiion. You lost!")

elif answer == "right":
    answer = input("""You went the right path
    you met a bridge and you have three options
    go through bridge/go back/ look for another path? """).lower()
    if answer == "through bridge":
        print("Courageous enough you won")
    elif answer == "go back":
        print("There is no going back you lost")
    elif answer == "look for another path":
        print("There is no other path! You lost!")
    else:
        print("Invalid option! you lose!")


else:
    print("Not a valid path. You lose!")