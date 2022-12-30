import random
import sys


class NumApp:
    def __init__(self, lowest, highest, attempts):
        self.lowest = lowest
        self.highest = highest
        self.attempts = attempts

    def setUp(self, lowest, highest, n):
        target = random.randint(lowest, highest)
        print('guessing game of number between {lowest} and {highest}. You have {n} attempts'.format(lowest=lowest, highest=highest, n=n))
        return target

    def not_valid(self, lowest, highest, user_num_input):
        return user_num_input < lowest or highest < user_num_input
        
    def num_check(self, lowest, highest, user_num_input, target):
        if self.not_valid(self.lowest, self.highest, user_num_input):
            sys.exit('Please input the number in the range')
        if user_num_input < highest and target < user_num_input:
            print('Your guess is above the answer')
        elif lowest < user_num_input and user_num_input < target:
            print('Your guess is below the answer')
        elif user_num_input == target:
            print("You've successfully guessed the number within your attempts!")
            sys.exit('Finishing the game. Have a great day')

    def run(self):
        n = 0
        target = self.setUp(self.lowest, self.highest, self.attempts)
        while n < self.attempts:
            try:
                user_num_input = int(input('please enter your number: ')) 
            except ValueError:
                print("Not an integer! Try again.")
            # if self.not_valid(self.lowest, self.highest, user_num_input):
            #     sys.exit('Please input the number in the range')
            self.num_check(self.lowest, self.highest, user_num_input, target)
            n += 1

        print('Over the maxium attemps. Game Over')
            

if __name__ == '__main__':
    num_guess = NumApp(lowest=0, highest=50, attempts=10)
    num_guess.run()