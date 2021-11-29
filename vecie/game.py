import random

hangman = [
    """  
       +---+
       |   |
           |
           |
           |
           |
    =========
    """, # 0 zimējam ja fails ir 0
    """
      +---+
      |   |
      o   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  | 
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
     / \  |
          |
    =========
    """ # 6, zīmējam ja ir 6 kļūdas
]

words = [
    'saraksts',
    'zobs',
    'nezinu',
    'datoriumbot',
    'python', 
]



random_word = random.choice(words)


fails = 0
guessed_letters = []

while fails < 6:

    print(hangman[fails])


    word_with_dashes = ''
    
    for letter in random_word:

        if letter in guessed_letters:
            word_with_dashes += letter

        else:
            word_with_dashes += '-'

        if word_with_dashes == random_word:
            print ('YOU WIN')
            break
            

    print(word_with_dashes)
    print(f'Guessed letters: {guessed_letters}')
    letter = input('Enter letter: ')
    guessed_letters.append(letter)

    if letter not in random_word:
        fails += 1



if fails == 6:
    print(hangman[6])
    print('YOU LOST')
    print('WORD : ', random_word)