import random

def roll():
    max_value = 6
    min_value = 1

    roll_result = random.randint(min_value, max_value)

    return roll_result

while True:
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid input. Please try again.")

max_score = 50
player_scores = [0] * players

while max(player_scores) < max_score:

    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn")
        print(f"Your score is: {player_scores[player_index]}")

        current_score = 0
        while True:
            should_roll = input("Would you like to roll? (y/n): ").lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}!")
                print(f"Your score is: {current_score}")

        player_scores[player_index] += current_score
        print(f"Your total score is: {player_scores[player_index]}")

print("Game over!")
