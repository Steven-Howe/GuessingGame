from random import randint
from time import sleep


class GuessingGame:

    def __init__(self):
        """Initialises game records and values."""
        self.wins = 0
        self.losses = 0
        self.rounds = 0
        self.score_bank = 0
        self.high_score = 0
        self.easy = False
        self.medium = False
        self.hard = False
        self.guess_count = 0

    def __str__(self):
        """Returns creator information for string representation of objects"""
        return "This game was created by Steven Howe."

    @staticmethod
    def __game_title():
        """Prints the game title and information."""

        print("""
           ______ __  __ ______ _____ _____  ____ _   __ ______   ______ ___     __  ___ ______
          / ____// / / // ____// ___// ___/ /  _// | / // ____/  / ____//   |   /  |/  // ____/
         / / __ / / / // __/   \__ \ \__ \  / / /  |/ // / __   / / __ / /| |  / /|_/ // __/   
        / /_/ // /_/ // /___  ___/ /___/ /_/ / / /|  // /_/ /  / /_/ // ___ | / /  / // /___   
        \____/ \____//_____/ /____//____//___//_/ |_/ \____/   \____//_/  |_|/_/  /_//_____/   

        ========================================================
                --- Welcome to the Guessing Game! v1.0 ---
                  This game was created by Steven Howe.""")

    @staticmethod
    def __game_instructions():
        """Prints detailed game instructions."""
        print("""
        ========================================================
                        ---Game Instructions---

        The Guessing Game has three levels; Easy, Medium, and Hard.""")
        sleep(3)
        print("""
        The goal of the game is to guess the correct number before
        your lives run out. Each successive level grants more points
        for correct answers than the previous. Your points are stored
        in the score bank and can be accessed via the options menu.""")
        sleep(9)
        print("""
        If you guess the correct number without running out of lives
        then you win the game! And if you happen to guess the correct 
        number within the first two tries you will gain extra points. 
        However, if you run out of lives you will loose the game with 
        the option to try again.""")
        sleep(9)
        print("""
        =========================================================
                        ---Easy Level---
        You will have to guess a number between 1 - 10.
        You will have 5 lives to use.

                        ---Medium Level---
        You will have to guess a number between 1 - 12.
        You will have 5 lives to use.

                        ---Hard Level---
        You will have to guess a number between 1 - 15.
        You will have 5 lives to use.

        Type !options during the game to get to the options menu.
        =========================================================
        """)
        sleep(3)

    def __options_menu(self):
        """Prints options menu and gets command from player."""
        print("""\n
        ==================O=P=T=I=O=N=S==M=E=N=U=================
        To resume playing type '!resume'
        To start a new game type '!start'
        To quit game type '!quit'
        To see game instructions type '!instructions'
        To see your overall game records type '!records'
        To reset your game records type '!reset'
        =========================================================""")
        # sleep(2)
        option = input("Enter the chosen option. >>> ").lower()
        # Will exit options menu back to function that called it
        if option == "!resume":
            return
        elif option == "!start":
            self.__choose_level()
        elif option == "!quit":
            # Will write records to file before exiting the game
            self.__write_records()
            print("\nThanks for playing!")
            quit()
        elif option == "!instructions":
            self.__game_instructions()
            return
        elif option == "!records":
            # Makes records up to date before printing records
            self.__write_records()
            self.__get_records()
            self.__show_records()
            return
            # Resets each record to a zero
        elif option == "!reset":
            self.__reset_records()

        else:
            # If input is incorrect the options will appear till correct input
            self.__options_menu()

    def __get_records(self):
        """Gets existing game records from game record file."""
        # If file doesn't exist yet the file will be created
        try:
            record_file = open("game_records.txt", "r")
        except FileNotFoundError:
            record_file = open("game_records.txt", "w+")

        records = record_file.readlines()
        # If there's nothing within the file then function will exit
        if not records:
            record_file.close()
            return
        # Assigns file game record values to current game records
        else:
            self.wins = int(records[0].strip())
            self.losses = int(records[1].strip())
            self.rounds = int(records[2].strip())
            self.score_bank = int(records[3].strip())
            self.high_score = int(records[4].strip())

        record_file.close()

    def __show_records(self):
        """Will print the current player's game records."""
        print(f"""
        You're total amount of wins are: {self.wins}.
        You're total amount of losses are: {self.losses}.
        You've played {self.rounds} rounds in total.
        You currently have {self.score_bank} in you're score bank.
        Your highest score achieved is: {self.high_score}.
        """)

    def __write_records(self):
        """Writes to game record file the current game records."""
        # Erases all current records and writes new values
        record_file = open("game_records.txt", "w+")
        # Writes and saves current game records to the record file
        record_file.write(str(self.wins) + '\n')
        record_file.write(str(self.losses) + '\n')
        record_file.write(str(self.rounds) + '\n')
        record_file.write(str(self.score_bank) + '\n')
        # Will write a new high score if it's broken
        if self.score_bank > self.high_score:
            record_file.write(str(self.score_bank))
            # Needed if there was no value written before
        elif self.high_score == 0:
            record_file.write("0")
        else:
            # Leaves high score value in file if unbroken
            record_file.write(str(self.high_score))

        record_file.close()

    def __reset_records(self):
        """Resets player's records back to zero."""
        # All in-game records become zero and values are written to file
        self.wins = 0
        self.losses = 0
        self.rounds = 0
        self.score_bank = 0
        self.high_score = 0
        self.__write_records()

    def __guess(self):
        """Gets the guessed number from the player."""
        guessed_number = input("\n>>> ").lower()
        # Presents options menu if requested
        if guessed_number == "!options":
            self.__options_menu()
            return
        # Returns guess only if it's an int
        elif guessed_number.isdigit():
            self.guess_count += 1
            return int(guessed_number)
        else:
            self.guess_count += 1
            print("\nYou didn't enter a digit, try again!")
            return

    def __number_over(self, player_guess):
        """Determines if player's guess is outside the range of numbers for level."""
        if self.easy:
            if player_guess < 1 or player_guess > 10:
                print("You have guessed a number outside the range of 1 - 10.")
        elif self.medium:
            if player_guess < 1 or player_guess > 12:
                print("You have guessed a number outside the range of 1 - 12.")
        elif self.hard:
            if player_guess < 1 or player_guess > 15:
                print("You have guessed a number outside the range of 1 - 15.")
        else:
            print("Something has gone wrong!")

    def __score_generator(self):
        """Determines the amount of points the player receives."""
        # Score is greater for each level if number guessed correctly on guess 1 or 2
        if self.easy:
            if self.guess_count == 1:
                self.score_bank += 500
            elif self.guess_count == 2:
                self.score_bank += 400
            else:
                # Standard points given for easy
                self.score_bank += 300

        elif self.medium:
            if self.guess_count == 1:
                self.score_bank += 700
            elif self.guess_count == 2:
                self.score_bank += 600
            else:
                # Standard points given for medium
                self.score_bank += 500
        else:
            if self.guess_count == 1:
                self.score_bank += 1000
            elif self.guess_count == 2:
                self.score_bank += 900
            else:
                # Standard points given for hard
                self.score_bank += 800
        # Will assign a new high score if bank grows higher
        if self.score_bank > self.high_score:
            self.high_score = self.score_bank

    def __you_won(self):
        """Prints message if player guesses correct number."""
        print("\nYOU WON! You guessed the right number!")
        self.rounds += 1
        self.wins += 1
        # Computes scores and asks player if they want to play again
        self.__score_generator()
        self.__play_again()

    def __game_over(self, correct_number):
        """Prints message if player looses game."""
        print("\nGAME OVER: you ran out of lives!")
        print(f"The number you were looking for was >> {correct_number} <<.\n")
        self.losses += 1
        self.rounds += 1
        # Each game lost results in minus 100 points from score bank
        self.score_bank -= 100
        self.__play_again()

    @staticmethod
    def __try_again():
        """Prints message if player's guessed number is incorrect."""
        print("Sorry that number was incorrect, try again!")

    def __play_again(self):
        """Determines if player wants to play another game or to quit the game."""
        answer = input("Would you like to play again? Enter 'yes' or 'no'. >>> ").lower()

        if answer == "!options":
            self.__options_menu()
        elif answer == "yes":
            # Resets level and amount of guesses
            self.easy, self.medium, self.hard = False, False, False
            self.guess_count = 0
            self.__choose_level()
        elif answer == "no":
            quit_game = input("\nWould you like to quit? Enter 'yes' or 'no'. >>> ").lower()

            if quit_game == "yes":
                # Writes current game records to record file before quiting
                self.__write_records()
                print("\nThanks for playing!")
                quit()
            else:
                self.__play_again()
        else:
            print("You have entered an incorrect command, type '!options' to get the options menu.")
            self.__options_menu()

    def __choose_level(self):
        """Allows player to choose what difficult level they would like to play."""
        print("\nChoose what level difficulty you want to play")
        level_difficulty = input("(Enter Easy, Medium, or Hard) >>> ").lower()
        # Runs level difficulty chosen by player
        if level_difficulty == "easy":
            self.easy = True
            self.__easy_game()
        elif level_difficulty == "medium":
            self.medium = True
            self.__medium_game()
        elif level_difficulty == "hard":
            self.hard = True
            self.__hard_game()
        else:
            # Will show options menu as default if incorrect input from player
            self.__options_menu()
            self.__choose_level()

    def __run_game(self, lives_number, correct_number):
        """Core game mechanics for each level."""
        # Gives player amount of guesses according to lives they are given
        # Built function this way so lives numbers can be adjusted
        for lives in range(lives_number):
            sleep(1)
            player_guess = self.__guess()
            # If guess isn't an int will run function amount of times lives - guesses are left
            while not str(player_guess).isdigit():
                for num in range(lives_number - self.guess_count):
                    self.__run_game(lives_number, correct_number)
                # If lives are all gone then game over
                if self.guess_count == 5:
                    self.__game_over(correct_number)
                # If number is over the limit then exits function
            if self.__number_over(player_guess):
                return

            if player_guess == correct_number:
                self.__you_won()
                self.__play_again()
            # Once lives are all used game is over
            elif lives == lives_number - 1:
                self.__game_over(correct_number)
                self.__play_again()

            else:
                # Another try if not correct number and lives aren't all used up
                self.__try_again()

    def __easy_game(self):
        """Runs an instance of an easy difficulty game."""
        # Runs game with easy parameters
        correct_number = randint(1, 10)
        lives_number = 5
        print("\nNumber has been picked.. Guess away!")
        self.__run_game(lives_number, correct_number)

    def __medium_game(self):
        """Runs an instance of a medium difficulty game."""
        # Runs game with medium parameters
        correct_number = randint(1, 12)
        lives_number = 5
        print("\nNumber has been picked.. Guess away!")
        self.__run_game(lives_number, correct_number)

    def __hard_game(self):
        """Runs an instance of a hard difficulty game."""
        # Runs game with hard parameters
        correct_number = randint(1, 15)
        lives_number = 5
        print("\nNumber has been picked.. Guess away!")
        self.__run_game(lives_number, correct_number)

    def game_instance(self):
        """Starts an instance of the game from the beginning."""
        self.__game_title()
        sleep(4)
        self.__game_instructions()
        self.__get_records()
        self.__write_records()
        sleep(5)
        self.__choose_level()


def main():
    """Runs the main game program."""
    game = GuessingGame()
    game.game_instance()


if __name__ == '__main__':
    main()
