import random
import time

def russian_roulette():
    chambers = 6
    players = ["player1","player2"]
    bullet_chamber = random.randint(1,chambers)
    current_chamber = random.randint(1,chambers)

    print("lets enter the game player1 and player2 , lets see who survives")
    turn =0
    
    while True:
        cur_player = players[turn]
        input(f"{cur_player} press enter to fire the gun bro: ")
        print("just pressed enter")
        time.sleep(1)

        if(current_chamber == bullet_chamber):
            print(f"sry {cur_player} bro , u loose :( ")
            break
        else:
            print("ooh u got lucky , lets go to the other player")

        current_chamber = current_chamber%chambers + 1
        turn = 1- turn

russian_roulette()
