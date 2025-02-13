import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
value = roll()
print(value)


while True:
    player = input("enter the number of players(2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("must be between 2 and 4 players")
    else:
        print("Invalid input.")

max_score = 50
player_score = [0 for _ in range(player)]
while max(player_score) < max_score:
    should_roll = input("would you like to roll? (y/n): ")
    if should_roll.lower() == "y":
        value = roll()




