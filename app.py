import constants
import random

    # Unpacking team list into individual variables to hold players. 
def assigning_players(panthers, bandits, warriors):

    random.shuffle(players)
    for player in range(6):
        warriors.append(players.pop(player))
        #print("warrior = {}".format(warriors))

    random.shuffle(players)    
    for player in range(6):
        bandits.append(players.pop(player))
        #print("bandit = {}".format(bandits))

    for last in players:
        panthers.append(last)
       # print("panthers = {}".format(panthers))
            
    return (warriors, bandits, panthers)

def experience_conversion():    
    for player in player_dic:
        #print(player['experience'])
        if player['experience'] == 'YES':
            player['experience'] = True
        elif player['experience'] == 'NO':
            player['experience'] = False
      
      
def height_conversion():
    for h in player_dic:
        h['height'] = h['height'].strip('inches')
        h['height'] = int(h['height'])


def start_console():
    print("\n****************************")
    print("      WELCOME TO THE \n BASKETBALL TEAM STATS TOOL")
    print("****************************")


def display_menu():
    print("\n  ---- MENU ----")
    print("\nHere are your choices:")
    print("  1) Display Team Stats")
    print("  2) Quit \n")

if __name__ == "__main__":


    # Adding list with dictionaries to new variables in the program
    team_list = constants.TEAMS
    player_dic = constants.PLAYERS
 
    # print(player_dic)

    # change experience yes/no value to boolean 
    experience_conversion()

    # change height string into and int
    height_conversion()

    # Pulling player name data from dictionary to assign to a team
    players = [name['name'] for name in player_dic]
    
    # creating team list to hold players
    warriors = []
    bandits = []
    panthers = []

    # assigning players to team variables
    warriors, bandits, panthers = assigning_players(panthers, bandits, warriors)
    
    start_console()
    

    while True:


        try:

            display_menu()
            menu_opt = input("What would you like to do? 1 or 2: ")
            menu_opt = int(menu_opt)
            if menu_opt > 2 or menu_opt < 1:
                error = menu_opt/(menu_opt - menu_opt)

        except (ValueError, ZeroDivisionError):
            print("\n*****OOOPS! THAT WONT WORK! USE 1 OR 2*****\n")

        else:

            if menu_opt == 1:
            
                print("\n 1) Panthers ")
                print("\n 2) Warriors ")
                print("\n 3) Bandits ")
                
                try:

                    team_choice = input("\n **Which team stats do you want to see? (1-3)** : ")
                    team_choice = int(team_choice)

                    if team_choice > 3 or team_choice < 1:
                        error = team_choice /(team_choice - team_choice)

                except (ValueError, ZeroDivisionError):
                    print("\n ERROR! CHOOSE A TEAM BY USING THE NUMBERS (1 - 3) NEXT TIME")
                    print(" Re-directing you to the __MENU__")
                    

                else:

                    if team_choice == 1:
                        team_name1 = "Panthers"
                        print("\nTeam: {} Stats".format(team_name1))
                        print("-------------------------")
                        print("Total players: {}\n".format(len(panthers)))
                        print(', '.join(panthers))
                        print('--------------------------------------------------------------------------------')
                        print("\n")
                        continue

                    elif team_choice == 2:
                        team_name2 = "Warriors"
                        print("\nTeam: {} Stats".format(team_name2))
                        print("-------------------------")
                        print("Total players: {}\n".format(len(warriors)))
                        print(', '.join(warriors))
                        print('--------------------------------------------------------------------------------')
                        continue

                    elif team_choice == 3:
                        team_name3 = "Bandits"
                        print("\nTeam: {} Stats".format(team_name3))
                        print("-------------------------")
                        print("Total players: {}\n".format(len(bandits)))
                        print(', '.join(bandits))
                        print('--------------------------------------------------------------------------------')
                        continue

            elif menu_opt == 2:
                    print("\nHAVE A GREAT DAY! \nBYE BYE!\n")
                    break

    #to check that the data was cleaned, remove '#' from print statement below
    #print(player_dic)