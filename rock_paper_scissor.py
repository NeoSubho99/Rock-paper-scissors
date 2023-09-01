import random

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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

# User's turn
print("You chose")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Invalid input")

# Computer's turn
print("\nComputer chose")
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

# Match Result
if computer_choice == choice:
    print("It's a Draw")
elif computer_choice == 0 and choice == 1:
    print("You Win!")
elif computer_choice == 0 and choice == 2:
    print("You Lose!")
elif computer_choice == 1 and choice == 0:
    print("You Lose!")
elif computer_choice == 1 and choice == 2:
    print("You Win!")
elif computer_choice == 2 and choice == 0:
    print("You Win!")
elif computer_choice == 2 and choice == 1:
    print("You Lose!")

