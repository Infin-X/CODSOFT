import random

def get_player_choice():
    while True:
        p_choice = input("Choose rock, paper, or scissors: ").lower()
        if p_choice in ['rock', 'paper', 'scissors']:
            return p_choice
        else:
            print("\nInvalid choice. Please choose rock, paper, or scissors.")

def get_comp_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(p_choice, computer_choice):
    if p_choice == computer_choice:
        return 'tie'
    elif (p_choice == 'rock' and computer_choice == 'scissors') or \
         (p_choice == 'scissors' and computer_choice == 'paper') or \
         (p_choice == 'paper' and computer_choice == 'rock'):
        return 'player'
    else:
        return 'computer'

def display_result(p_choice, computer_choice, winner):
    print(f"User chose {p_choice}.")
    print(f"Computer chose {computer_choice}.")
    if winner == 'tie':
        print("It's a tie!")
    else:
        print(f"{winner.capitalize()} wins!")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def main():
    p_score = 0
    c_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    a=input("Enter your player name: ")

    while True:
        p_choice = get_player_choice()
        computer_choice = get_comp_choice()
        winner = determine_winner(p_choice, computer_choice)
        display_result(p_choice, computer_choice, winner)

        if winner == 'player':
            p_score += 1
        elif winner == 'computer':
            c_score += 1

        print(f"Score: User {a} {p_score} - {c_score} Computer")

        if not play_again():
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
