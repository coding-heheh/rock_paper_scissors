import random

def rock_paper_scissors():
     print("Welcome to Rock-Paper-Scissors!")
     print("Enter your choice:")
     print("1. Rock")
     print("2. Paper")
     print("3. Scissors")
     print("0. Exit")

     while True:
         try:
             user_choice = int(input("Enter your choice (1-3): "))

             if user_choice == 0:
                 print("Exiting game. Goodbye!")
                 break
             elif user_choice not in (1, 2, 3):
                 print("Invalid choice. Please enter a number between 1 and 3.")
                 continue

             # Map user choice to string
             if user_choice == 1:
                 user_choice_str = "Rock"
             elif user_choice == 2:
                 user_choice_str = "Paper"
             elif user_choice == 3:
                 user_choice_str = "Scissors"

             # Generate computer's choice randomly
             computer_choice = random.randint(1, 3)
             if computer_choice == 1:
                 computer_choice_str = "Rock"
             elif computer_choice == 2:
                 computer_choice_str = "Paper"
             elif computer_choice == 3:
                 computer_choice_str = "Scissors"

             print(f"You chose {user_choice_str}.")
             print(f"Computer chose {computer_choice_str}.")

             # Determine the winner
             if user_choice == computer_choice:
                 print("It's a tie!")
             elif (user_choice == 1 and computer_choice == 3) or \
                  (user_choice == 2 and computer_choice == 1) or \
                  (user_choice == 3 and computer_choice == 2):
                 print("Congratulations! You win!")
             else:
                 print("Computer wins!")

         except ValueError:
             print("Invalid input. Please enter a number.")

         print()

