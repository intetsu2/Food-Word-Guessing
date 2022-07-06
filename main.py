import random as rand
import food as fd
import time

# Random Fruits & Vegetables function
def random_food(f_or_v, option_check):
    point_count = 0
    time_play = 0
    missed_guesses = 0
    guessesd_guesses = 0

    while time_play != 6:
        time_play += 1
        rdf_c = rand.choice(f_or_v)
        if option_check == 'Fruits':
            print(f'Guess a fruit that starts with {rdf_c[:2]}')
        elif option_check == 'Vegetables':
            print(f'Guess a vegetable that starts with {rdf_c[:2]}')

        # fruit value input control
        try:
            time.sleep(2)
            guess = str(input('Guess or Quit: ')).capitalize()
            if guess == rdf_c:
                print("Correct!")
                point_count += 1
                guessesd_guesses += 1
                print('+1 point')
            elif guess != rdf_c:
                if guess == 'Quit':
                    break
                else:
                    continue
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

# main function
def main():
    vegetables = fd.all_food['vegetables']
    fruits = fd.all_food['fruits']
    games = ['Fruits', 'Vegetables']
    print(f'Game choices are {games[0]} and {games[1]} or Exit')

    while True:
        game_choice = input("Choose game: ").capitalize()
        if game_choice in games:
            if game_choice == games[0]:
                random_food(fruits, game_choice)
            elif game_choice == games[1]:
                random_food(vegetables, game_choice)
        else:
            if games == "Exit":
                break
            else:
                print('Checking your input....')
                time.sleep(4)
                print('Invalid choice, try agai!')

if __name__ == "__main__":
    main()