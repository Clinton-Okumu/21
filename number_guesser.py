import random

top_range = input("Pick a number? ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Pick a number above 0 next time")
        quit()

else:
    print("pick a number next time please")
    quit()

random_num = random.randint(1, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess? ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number!")
        continue

    if user_guess == random_num:
        print("You got it right!")
        break
    elif user_guess > random_num:
        print("You were above the number!")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses")
