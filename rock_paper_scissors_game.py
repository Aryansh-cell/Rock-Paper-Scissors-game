import random
print("==============================================================")
print("               🪨  ROCK PAPER SCISSORS 📄")
print("==============================================================")

choices = ["rock", "paper", "scissors"]

play = True
player_score = 0
bot_score = 0 
draw = 0
while play:

    bot_choice = random.choice(choices)
    user_choice = input("Choose one:\nrock\npaper\nscissors\nEnter here: ").lower().strip()

    print(f"Bot chose: {bot_choice}")
    print(f"You chose: {user_choice}")

    if user_choice not in choices:
        print("❌Invalid choice!\nPlease choose between rock, paper, scissors")

    elif bot_choice == "rock" and user_choice == "scissors":
        print("bot won")
        bot_score += 1
    elif bot_choice == "scissors" and  user_choice == "paper":
        print("bot won")
        bot_score += 1
    elif bot_choice == "paper" and user_choice == "rock":
        print("bot won")
        bot_score += 1
    elif bot_choice == "scissors" and user_choice == "rock":
        print("You won 🎉")
        player_score += 1
    elif bot_choice == "paper" and  user_choice == "scissors":
        print("You won 🎉")
        player_score += 1
    elif bot_choice == "rock" and user_choice == "paper":
        print("You won 🎉")
        player_score += 1

    else:
        print("draw")
        draw += 1

    print(f"  |=======================SCOREBOARD================================|")
    print(f"  |  BOT SCORE  = {bot_score}                                       |")
    print(f"  |  Your SCORE = {player_score}                                    |")
    print(f"  |  DRAWS      = {draw}                                            |")
    print(f"  |=================================================================|")
    

    play_again = input("Play again Yes/No : ").lower().strip()
    if play_again == "yes":
        play = True
    elif play_again == "no":
        play = False
        if player_score > bot_score:
            print("🏆 YOU ARE THE CHAMPION!")
        elif bot_score > player_score:
            print("🤖 COMPUTER WINS THE GAME!")
        else:
            print("🤝 IT'S A DRAW!")
            

