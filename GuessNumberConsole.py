from random import randint
from colorama import *
from ctypes import windll
from time import sleep
# Игра "Угадай число"
windll.kernel32.SetConsoleTitleW("GuessNumber")
init()

number = None
guess = None

print(Fore.GREEN)
print('Game "GuessNumber" by Oleg4260 ')
sleep(0.5)
print(Fore.CYAN)
print("I make a number from 1 to 10 and you need to guess it.")

while True:
    number = randint(1, 10)
    try:
        print(Fore.BLUE)
        guess = int(input("I made a number. Do you know, what is this?\n> "))
    except ValueError:
        sleep(0.5)
        print(Fore.RED)
        print("Enter the number!")
        sleep(0.5)
    if (guess >= 1 and guess <= 10):
        if (guess == number):
            sleep(0.5)
            print(Fore.GREEN)
            print("Congratulations! You guessed the number  " + str(number) + "!")
            sleep(0.5)
        else: 
            sleep(0.5)
            print(Fore.YELLOW)
            print("Sorry, but it was " + str(number) + ".")
            sleep(0.5)
    else:
        sleep(0.5)
        print(Fore.RED)
        print("Enter the number from 1 to 10.")
        sleep(0.5)