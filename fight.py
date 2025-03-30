import random

while True:
    user_action = input("Enter a choice (grab, parry, punch): ")
    possible_actions = ["grab", "parry", "punch"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "grab":
        if computer_action == "parry":
            print("Command grab! You win!")
        else:
            print("easy hit ! You lose.")
    elif user_action == "parry":
        if computer_action == "punch":
            print("counter attack! You win!")
        else:
            print("Command grab! You lose.")
    elif user_action == "punch":
        if computer_action == "grab":
            print("easy hit! You win!")
        else:
            print("counter attack! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
