import random
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for paper , 2 for Scissor : \n"))
computer_choice = random.randint(0,2)
print(f"Computer Chose {computer_choice}\n")


if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number, you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you wins")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif user_choice > computer_choice:
    print("you wins")
elif computer_choice > user_choice:
    print("you lose")
elif computer_choice == user_choice:
    print("its Draw")
