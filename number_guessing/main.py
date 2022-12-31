import random
import sys


class NumApp:
    def __init__(self, lowest, highest, attempts):
        self.lowest = lowest
        self.highest = highest
        self.attempts = attempts

    def print_log(self, msg):
        sys.stdout.buffer.write(msg.encode())
        sys.stdout.flush()

    def setUp(self, lowest, highest, n):
        target = random.randint(lowest, highest)
        self.print_log('guessing game of number between {lowest} and {highest}. You have {n} attempts'.format(lowest=lowest, highest=highest, n=n))
        return target

    def not_valid(self, lowest, highest, user_num_input):
        return user_num_input < lowest or highest < user_num_input
        
    def num_check(self, lowest, highest, user_num_input, target):
        if self.not_valid(self.lowest, self.highest, user_num_input):
            sys.exit('Please input the number in the range\n')
        if user_num_input < highest and target < user_num_input:
            self.print_log('Your guess is above the answer\n')
        elif lowest < user_num_input and user_num_input < target:
            self.print_log('Your guess is below the answer\n')
        elif user_num_input == target:
            self.print_log("You've successfully guessed the number within your attempts!\n")
            sys.exit('Finishing the game. Have a great day')

    def run(self):
        n = 0
        target = self.setUp(self.lowest, self.highest, self.attempts)
        while n < self.attempts:
            try:
                self.print_log('please enter your nunber: ')
            except ValueError:
                self.print_log("Not an integer! Try again.")
            min_num = int(sys.stdin.buffer.readline().decode("utf-8"))
            self.num_check(self.lowest, self.highest, min_num, target)
            n += 1

        print('Over the maxium attempts. Game Over')
            

if __name__ == '__main__':
    num_guess = NumApp(lowest=0, highest=50, attempts=10)
    num_guess.run()