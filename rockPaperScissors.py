import random

#import random

def rockPaperScissors(user_input, computer_input):
    if(user_input == "rock") & (computer_input == "rock"):
        print("The computer threw rock. Rock and rock end in a draw")
    elif(user_input == "scissors") & (computer_input == "scissors"):
        print("The computer threw scissors. Scissors and scissors end in a draw") 
    elif(user_input == "paper") & (computer_input == "paper"):
        print("THe computer threw paper. Paper and Paper end in a draw")


    elif(user_input == "rock") & (computer_input == "paper"):
        print("The computer threw scissors. Rock versus scissors, computer wins!")
    elif(user_input == "paper") & (computer_input == "scissors"):
        print("The computer threw scissors. Paper versus scissors, computer wins!")
    elif(user_input == "scissors") & (computer_input == "rock"):
        print("The computer threw rock. Rock versus scissors, computer wins!")
      
    
    elif (user_input == "rock") & (computer_input == "scissors"):
        print("The computer threw sissors. Rock versus scissors, I win!")
    elif (user_input == "paper") & (computer_input == "rock"):
        print("The computer threw rock. paper versus scissors, I win!")
    elif (user_input == "scissors") & (computer_input == "paper"):
        print("The computer threw paper. scissors versus paper, I win!")

rock = "rock"
paper = "paper"
scissors = "scissors"
list = [rock, paper, scissors]

computer = random.choice(list)
response = input ("do you want to play rock, paper, scissors? 'Y' for yes, anything else for no ").upper()
#user = input("Rock. Paper. Scissors. Shoot!: ")

#rockPaperScissors(user, computer)


while response =="Y": 
    user = input("Rock. Paper. Scissors. Shoot!: ")
    rockPaperScissors(user, computer)
    computer = random.choice(list)
    response = input ("Do you want to play again? 'Y' for yes, anything else for no")
