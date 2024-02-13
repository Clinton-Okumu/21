import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]
while True:
    user_input = input("type Rock/paper/scissors or  Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in choices:
        continue

    random_choice = random.randint(0, 2)

    computer_pick = choices[random_choice]
    print(f"Computer picked: {computer_pick}")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins = user_wins + 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins = user_wins + 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins = user_wins + 1
    
    else:
        print("computer won and you lost")
        computer_wins = computer_wins + 1


print(f"user wins {user_wins} times")
print(f"Computer wins {computer_wins} times")
print("Goodbye!")
