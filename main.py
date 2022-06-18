import random as rand
import food as fd
import os 
import sys

# Random Fruits function
def random_food(f_v):
    point_count = 0
    time_play = 0
    missed_guesses = 0
    guessesd_guesses = 0

    while time_play != 6:
        time_play += 1
        rdf_c = rand.choice(f_v)
        print(f'Guess a fruit or a vegetable that starts with {rdf_c[:2]}')

        # fruit value input control
        try:
            guess = str(input('Guess: '))
            if guess == rdf_c:
                print("Correct!")
                point_count += 1
                guessesd_guesses += 1
                print('+1 point')
            elif guess != rdf_c:
                point_count -= 1
                missed_guesses += 1
                print("Wrong guess!")
                print('-1 point')
        except ValueError:
            print('Invalid input!')

    print('\v')
    print('GAME OVER' + '\v')

    if point_count >= -1 and point_count <= 1:
        print(f'You ended up with {point_count} point')
    elif point_count < -1 and point_count > 1:
        print(f'You ended up with {point_count} points')
    print(f'You guessd {guessesd_guesses} right and {missed_guesses} wrong.')

# Random Vegetables function
"""def random_vegie():
    point_count = 0
    time_play = 0
    missed_guesses = 0
    guessesd_guesses = 0

    while time_play != 6:
        time_play += 1
        rdv_c = rand.choice(fd.all_food['vegetables'])
        print(f'Guess a fruit that starts with {rdv_c[:2]}')
    
    # vegie value input control
    try:

    except ValueError:
        print('Invalid input')"""


# main function
def main():
    vegetables = fd.all_food['vegetables']
    fruits = fd.all_food['fruits']
    games = ['Fruits', 'Vegetables']
    print(f'Game choices are {games[0]} and {games[1]} or Exit')
    while True:
        game_choice = input("Choose game: ")
        if game_choice in games:
            if game_choice == games[0]:
                random_food(fruits)
            elif game_choice == games[1]:
                random_food(vegetables)
        else:
            if games == "Exit":
                break
            else:
                print('Invalid choice, try agai!')

main()