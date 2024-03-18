import sys
import random


def guess_number(name="Human"):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, guess the number I am thinking of... 1,2, or 3\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2 or 3\n")
            return play_guess_number()

        computerchoice = random.choice("123")

        print(f"\n{name}, you chose {playerchoice}\n")
        print(f"\nI was thinking about the number {computerchoice}\n")

        player = int(playerchoice)
        computer = int(computerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"\nCongrats! {name}, you win!\n"
            else:
                return f"\nSorry, {name}. Better luck next time\n"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s win: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")

        print(f"\nPlay Again, {name}?\n")

        while True:
            playagain = input("\nY for Yes or Q to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\nThank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"\nBye {name}!")
            else:
                return

    return play_guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a Personalized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the player"
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()
