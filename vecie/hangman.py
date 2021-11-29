import random



words = [
    'nezinu',
    'negribu',
    'programma',
    'datoriumbot',
    'else',
    'google',
    'if',
    'phyton',
    'harijs',
    'zobens',
    'akmens',
    'koks',
    'nazis',
    'galva',
    'kaķis',
    'gurķis',
    'apelsīns',
    'divi',
    'kaktus',
    'diskord',
    'loks',
    'profesionālis',
    'opera'
]
hangman = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
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
    """
]

random_word = random.choice(words)
fails = 0
guessed_letters  = []


while fails < 6: 

    print(hangman[fails])

    word_with_dashes = ''

    for letter in random_word:
        if letter in guessed_letters:
            word_with_dashes += letter
        else:
            word_with_dashes += '-'

    if '-' not in word_with_dashes:
        print('Vārds ir uzminēts')
        break

    print(word_with_dashes)
    print(f'Guessed letters: {guessed_letters}')
    letter = input('Enter letter: ')
    guessed_letters.append(letter)


    if letter in random_word:
        print('BURTS IR VĀRDĀ')

    else:
        print('BURTS NAV VĀRDĀ')
        fails += 1

if fails == 6 :
    print('Tu zaudēji !') 
    print('Vārds bija : ', random_word )
