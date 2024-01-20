import sys
import random
from enum import Enum
def rps():
    game_count = 0
    player_wins = 0
    lyte_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal lyte_wins

        class RPS(Enum):
            ROCK=1
            PAPER=2
            SCISSORS=3

        
        print("")
        player_choice = input("Enter...\n1 for rock\n2for paper and\n3for scissors:\n\n")

        if player_choice not in ["1","2","3"]:
            print("you must enter 1,2, or 3")
            return play_rps()

        player = int(player_choice)

        

        comp_c = random.choice("123")

        computer=int(comp_c)
        print("")
        print("you chose"+str(RPS(player)).replace('RPS.','')+".")
        print("lyte chose"+str(RPS(computer)).replace('RPS.','')+".")
        print("")

        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal lyte_wins
            if player==1 and computer==3:
                player_wins += 1
                return "🥂you win!"
            elif player==2 and computer==1:
                player_wins += 1
                return "🥂you win!"
            elif player==3 and computer==2:
                player_wins += 1
                return "🥂you win!"
            elif player==computer:
                return "👀tie game!"
            else:
                lyte_wins += 1
                return "🐍lyte wins!"
            
        game_result = decide_winner(player,computer)

        print(game_result)

        nonlocal game_count
        game_count +=1

        print(f"\ngame count:"+ str(game_count))
        print(f"\nplayer wins:"+ str(player_wins))
        print(f"\nlyte wins:"+ str(lyte_wins))

        print("\nPlay again?")

        while True:
            playagain=input("\nplay again?\ny for yes or\nq for quit\n\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n💕👌\n")
            print("thank you for playing!")
            sys.exit("byee from lyte!💖")#break works too
    return play_rps

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()

