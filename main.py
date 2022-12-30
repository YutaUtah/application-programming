import random
import sys

def setUp(lowest, highest, n):
    target = random.randint(lowest, highest)
    print('guessing game of number between {lowest} and {highest}. You have {n} attempts'.format(lowest=lowest, highest=highest, n=n))
    return target

def main(lowest, highest, n):
    attempt = 0
    target = setUp(lowest, highest, n)
    while attempt <= n:
        user_num_input = int(input('Please enter your number: ')) 
        if lowest < user_num_input and user_num_input < target:
            print('Your guess is below the answer.')
        elif user_num_input < highest and target < user_num_input:
            print('Your guess is above the answer')
        elif user_num_input == target:
            print("You've successfully guessed the number within your attempts!")
            sys.exit('Finishing the game. Have a great day')

    print('Over the maxium attemps. Game Over')

if __name__ == '__main__':
    lowest = 0
    highest = 50
    n = 10
    main(lowest, highest, n)