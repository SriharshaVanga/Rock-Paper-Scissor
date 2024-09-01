import random
from ascii import rock, paper, scissor
def game():
    re = True
    while True:
        list = ['rock', 'paper', 'scissor']
        user_choice = input("Enter rock or paper or scissor:").lower()
        computer_choice = random.choice(list)

        if user_choice == 'rock':
            print(f"Your choice is: \n{rock}")
        elif user_choice =='paper':
            print(f"Your choice is: \n{paper}")
        elif user_choice == 'scissor':
            print(f"Your choice is:\n{scissor}")

        if computer_choice == 'rock':
            print(f"Computer choice is: \n{rock}")
        elif computer_choice =='paper':
            print(f"Computer choice is: \n{paper}")
        elif computer_choice == 'scissor':
            print(f"Computer choice is:\n{scissor}")


        if computer_choice == user_choice:
            print("Its a tie")
        elif computer_choice == 'rock' and user_choice == 'paper':
            print("You win!")
        elif computer_choice == 'rock' and user_choice =='scissor':
            print("Oopsie, you lose")
        elif computer_choice == 'paper' and user_choice == 'rock':
            print("You lose")
        elif computer_choice == 'paper' and user_choice == 'scissor':
            print("You win!")
        elif computer_choice == 'scissor' and user_choice == 'rock':
            print("You win!")
        elif computer_choice == 'scissor' and user_choice == 'paper':
            print("You lose!")

        choice = input("You want to play again? yes or no:").lower()
        if choice == "yes":
            game()
        elif choice == "no":
            break


game()