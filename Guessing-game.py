import random as rd

welcome_msg = '''
 --------------------------------------------
|                                           |
|  🎲🎲 WELCOME TO THE GUESSING GAME 🎲🎲   |
|                                           |
 --------------------------------------------
'''2

instruction_msg = '''
1. Try and guess the number I picked.
2. You have 5 lives. 
3. The game ends when you guess correctly or lose all 5 lives.
'''
no
high_msg = "That number is high 👆. Try again: "
low_msg = "That number is low 👇. Try again: "

congrats_msg = '''
*********************************************
🎉🎉 CONGRATULATIONS, YOU GUESSED RIGHT 🎉🎉
*********************************************
'''

game_over = '''
💔💔💔💔💔💔💔 
OOH NO, YOU LOST
💔💔💔💔💔💔💔
'''

print(welcome_msg)
print(instruction_msg)


def play_game():
    game_num = rd.randint(1, 100)
    game_lives = 5

    # print(game_num)

    print("Let's start. Guess the number: ")

    while game_lives > 0:
        game_guess = int(input())

        if game_guess == game_num:
            print(congrats_msg)
            break
        elif game_guess > game_num:
            print(high_msg)
        else:
            print(low_msg)

        game_lives = game_lives - 1

    if game_lives == 0:
        print(game_over)
        print("The correct number is: " + str(game_num))

    play_again = input("Do you want to play again? Type yes/no: ")

    if play_again == 'yes':
        play_game()
    else:
        print("Thank you for playing the game 👊")


play_game()
