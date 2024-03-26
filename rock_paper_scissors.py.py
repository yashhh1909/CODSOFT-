import random


def get_user_choice():
    print("Choose rock, paper, or scissors:")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors:")
        user_choice = input().lower()
    return user_choice


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'User'
    else:
        return 'Computer'


def play_game():
    # Instructions in a box
    print("╔════════════════════════════════════════════════════╗")
    print("║           Welcome to Rock, Paper, Scissors!        ║")
    print("║                                                    ║")
    print("║                   Instructions:                    ║")
    print("║   - Choose either rock, paper, or scissors.        ║")
    print("║   - The computer will randomly select its choice.  ║")
    print("║   - Rock beats scissors, scissors beat paper,      ║")
    print("║     and paper beats rock.                          ║")
    print("║   - Let's see who wins!                            ║")
    print("╚════════════════════════════════════════════════════╝")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    print(f"User chose {user_choice}, computer chose {computer_choice}.")
    print(f"{winner} wins!")
    return winner


def play_again():
    print("Do you want to play again? (yes/no)")
    return input().lower() == 'yes'


def show_leaderboard(scoreboard):
    print("\nLeaderboard:")
    for player, score in scoreboard.items():
        print(f"{player}: {score}")
    print()


def main():
    scoreboard = {'User': 0, 'Computer': 0, 'Tie': 0}
    while True:
        winner = play_game()
        scoreboard[winner] += 1
        show_leaderboard(scoreboard)
        if not play_again():
            break



if __name__ == "__main__":
    main()
