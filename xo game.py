places = {"1": " ", "2": " ", "3": " ",
          "4": " ", "5": " ", "6": " ",
          "7": " ", "8": " ", "9": " "}


def table(place):
    print(place["7"] + "|" + place["8"] + "|" + place["9"])
    print("=+=+=")
    print(place["4"] + "|" + place["5"] + "|" + place["6"])
    print("=+=+=")
    print(place["1"] + "|" + place["2"] + "|" + place["3"])

num_places = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def game():
    player = "X"
    counter = 0

    while counter < 9:
        table(places)
        print(f"it's your turne {player}")
        move = input(f"where do you wanna place your {player} : ")

        find_move = False

        for item in num_places:
            if move == item:
                find_move = True
                
        if find_move == True:
            if places[move] == " ":
                places[move] = player
                counter += 1
                if counter == 9:
                    table(places)
                    print(" /*/ GAME OVER /*/ The game ended in a draw  /*/ ")
            else:
                print("the place is full")
                continue
        else:
            print("there is no place with that value. try again with value between 1 and 9")
            continue

        if counter >= 5:
            if places["1"] == places["2"] == places["3"] != " ":
                table(places)
                print(f"the player |{player}| win the game")
                print("*** GoOd JoB ***")
                break
            elif places["4"] == places["5"] == places["6"] != " ":
                table(places)
                print(f"the player |{player}| win the game")
                print("*** GoOd JoB ***")
                break
            elif places["7"] == places["8"] == places["9"] != " ":
                table(places)
                print(f"the player |{player}| win the game")
                print("*** GoOd JoB ***")
                break
            elif places["1"] == places["4"] == places["7"] != " ":
                table(places)
                print(f"the player |{player}| win the game")
                print("*** GoOd JoB ***")
                break
            elif places["2"] == places["5"] == places["8"] != " ":
                table(places)
                print(f"the player |{player}| win the game")
                print("*** GoOd JoB ***")
                break
            elif places["3"] == places["6"] == places["9"] != " ":
                table(places)
                print(f"the player |{player}| win the game")
                print("*** GoOd JoB ***")
                break
            elif places["1"] == places["5"] == places["9"] != " ":
                table(places)
                print(f"the player |{player}| win the game")
                print("*** GoOd JoB ***")
                break
            elif places["3"] == places["5"] == places["7"] != " ":
                table(places)
                print(f"the player |{player}| win the game")
                print("*** GoOd JoB ***")
                break
        
        

        if player == "X":
            player = "O"
        else:
            player = "X"
        

game()

print("do you want to play again print yes or no ?")
play_again = input()

if play_again.lower() == "yes" :
    game()
else:
    print("**Ok Good Bye**")

