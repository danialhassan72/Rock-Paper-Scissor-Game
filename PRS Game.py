# Rock,Scissor,game

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

game_pic = [rock,paper,scissors]
# 0 rock , 1 paper , 2 scissors

import random

user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors . \n"))

if user_choice >=3 or user_choice < 0 :
    print("you typed an invlaid number,you loose")

else:
    print(game_pic[user_choice])
    computer_choice = random.randint(0,2)
    print("computer choice : ")
    print(game_pic[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("you win!")
    elif user_choice == 2 and computer_choice == 0:
        print("you lose!")
    elif computer_choice > user_choice:
        print("you lose!")
    elif user_choice > computer_choice:
        print("you win!")
    elif computer_choice > user_choice:
        print("its a draw")
