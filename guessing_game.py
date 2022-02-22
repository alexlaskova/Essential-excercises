import random

def guessing_game():
    answer = random.randint(0,100)

    while True:
        guess = int(input('Guess a number between 0 to 100: '))

        if guess > answer:
            print('Too high')
            
        elif guess < answer:
            print('Too low')

        else:
                print('Just right')
                break
guessing_game()


