
import random
from colorama import Fore


red = Fore.RED
black = Fore.BLACK
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE

def tempetureConverter(user_input):
    FAHRENHEIT_TO_CELSIUS = (user_input - 32) * (5/9)
    if(user_input >= 90): 
        print("Fahrenheit:   ", red, user_input, black)
        print("Celsius: ", red, FAHRENHEIT_TO_CELSIUS, black)
    elif(user_input >=75) & (user_input <= 89):
        print ("Faherenhit:   ", yellow, user_input, black)
        print ("Celsius : ", yellow, user_input, black)
    elif(user_input >= 64) & (user_input <= 74): 
        print("Fahrenheit: ", green, user_input, black)
        print("Celsius:", green, user_input, black)


    else:
        print("Fahrenheit: ", blue, user_input, black)
        print("Celsius:", blue, user_input, black)

user=int (input("Enter a temperature in Fahrenheit to convert to Celsius:  ") )

for x in range(5):
    tempetureConverter(user)
    user=int(input("Enter a temperature in Fahreit to convert to Celsius:   ")  )