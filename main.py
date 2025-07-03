import secrets
import string


possible_chars = [
    string.punctuation,
    string.ascii_uppercase,
    string.ascii_lowercase,
    string.digits,
]
config = [
    input('What length would you like your password(s) to be? (integer)\n'),
    input('How may passwords would you like to generate? (integer)\n'),
    input('Would you like to allow special characters? (1/0)\n'),
    input('Would you like to allow capital letters? (1/0)\n'),
    input('Would you like to allow lowercase letters? (1/0)\n'),
    input('Would you like to allow numbers? (1/0)\n'),
]


try:
    def func(x): return int(config[2:][possible_chars.index(x)])
    possible_chars = list(filter(func, possible_chars))
    for i in range(int(config[1])):
        password = ''
        for i in range(int(config[0])):
            password += secrets.choice(secrets.choice(possible_chars))
        print(f'\n{password}')
except:
    print('\nSomething went wrong. You may want to choose different settings.')

