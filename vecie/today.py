import random


while True:

    random_number = random.randint(0, 150)
    #print(random_number)


    guessing_number = True
    guesses = []

    while guessing_number:

        user_guess = int(input('Guess the number: '))

        #lielāks
        if user_guess > random_number:
            print('Your guess is larger than my number')
            guesses.append(user_guess - random_number)

        #mazāks
        elif user_guess < random_number:
            print('Your guess is lesser than my number')
            guesses.append(random_number - user_guess)

        else: 
            print('You guessed my number!')
            guessing_number = False


    print(f'Average deviation: {sum(guesses) / len(guesses)}') 
    print(f'Total amount of guesses: {len(guesses)}')
