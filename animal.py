import csv
import random
from pprint import pprint

# 1 Intro
def intro():
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("<>           MIGHTY           <>")
    print("<>          CREATURES         <>")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("")
    print("           Let's Play!          ")
    print("")
    print("--------------------------------")


# Reads .CSV File
def read_file():
    data = []
    with open('animals.csv', 'r') as animal_data:
        spreadsheet = csv.DictReader(animal_data)
        for row in spreadsheet:
            data.append(row)
    return data


# Allows player to pick an option
def options():
    animal_options = random.sample(list(read_file()), 3)
    animal_dict = {
        1: animal_options[0],
        2: animal_options[1],
        3: animal_options[2],
    }
    # Prints out the options
    numbers = 1
    for i in animal_dict:
        print('Option {}: {:20} -> Speed: {:5}, Weight: {:6}, Size {:5}'.format(numbers, animal_dict[i]['name'],
                                                                                animal_dict[i]['speed'],
                                                                                animal_dict[i]['weight'],
                                                                                animal_dict[i]['size']))
        numbers += 1
    # Player chooses
    # This catches errors
    error = True
    while error:
        try:
            player_choice = int(input('\nWhich animal do you want? (pick between 1-3 from above options): '))
            if player_choice > 3:
                raise ValueError
            error = False
        except ValueError:
            print("\nPlease the numbers 1, 2 or 3")
        except Exception:
            print("Something went wrong")
    chosen_animal = animal_dict[player_choice]
    print('\nYou chose {} '.format(chosen_animal['name'].upper()))
    return chosen_animal
# Allows player to pick a stat and calculate outcome


def game():
    chosen_option = options()
    # Assigns computer their animal and let's player choose stat
    random_computer = random.choice(list(read_file()))
    print('Computer chose {} \n'.format(random_computer['name'].upper()))
    error = True
    while error:
        try:
            stat_choice = input("What Stat do you want to use? (weight,speed,size) \n")
            if stat_choice in chosen_option:
                your_animal = int(chosen_option[stat_choice])
                computer_animal = int(random_computer[stat_choice])
            else:
                raise KeyError
            error = False
        except KeyError:
            print("\nPlease pick one of the following stats: weight, size or speed")
        except Exception:
            print("Something went wrong")
    win_lose = 0

    # Determines who wins each round
    if your_animal > computer_animal:
        print(f"\nYour stat is {your_animal} \nThe computer's stat is {computer_animal} \n \nYou win this round!")
        win_lose = 1
    elif computer_animal > your_animal:
        print(f"\nYour stat is {your_animal} \nThe computer's stat is {computer_animal} \n \nYou lose this round :(")
        win_lose = 2
    else:
        print(f"\nYour stat is {your_animal} \nThe computer's stat is {computer_animal} \nThis round is a draw")
        win_lose = 3
    return win_lose


def count_rounds():
    no_rounds = 0
    how_many_rounds = int(input("How many rounds do you want to play? "))
    your_score = 0
    comp_score = 0
    # Keeps the game going within the amount of rounds specified
    while no_rounds < how_many_rounds:
        for i in range(how_many_rounds):
            no_rounds += 1
            rounds_left = how_many_rounds - no_rounds
            print(f"\n**** ROUND {no_rounds} **** You have {rounds_left} rounds left ****")
            # Counts score
            result = game()
            if result == 1:
                your_score += 1
            elif result == 2:
                comp_score += 1
        # Calculates who wins the game
        if your_score > comp_score:
            print("\nCONGRATULATIONS! YOU WIN THE GAME!")
        elif comp_score > your_score:
            print("\nSorry, you lose the game :(")
        else:
            print("\nIt's a draw!")
    print("\n========================")
    print("G A M E  O V E R")
    print("========================")
    print(f"Your total  score is {your_score} and the computer's total  score is {comp_score}")

intro()
count_rounds()
