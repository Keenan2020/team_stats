import constants
import random

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

    # print(constants.TEAMS)
    # print(constants.PLAYERS)
    # Adding list and dictionary to new variables in the program
    team_list = constants.TEAMS
    player_dic = constants.PLAYERS
    #print(team_list)
    #print(len(player_dic))
    # Unpacking team list into individual variables to hold players. 
    players = [name['name'] for name in player_dic]
    

    warriors = []
    bandits = []
    panthers = []

    warriors, bandits, panthers = assigning_players(panthers, bandits, warriors)

    #print(panthers)
    #print(bandits)
    #print(warriors)
    
    start_console()
    
    display_menu()

    menu_opt = input("What would you like to do? 1 or 2: ")

    while menu_opt == "1":
        
        print("\n 1) Panthers ")
        print("\n 2) Warriors ")
        print("\n 3) Bandits ")
    
        team_choice = input(" Which team stats do you want to see? (1-3) : ")

        if team_choice == "1":
            team_name1 = "Panthers"
            print("\nTeam: {} Stats".format(team_name1))
            print("-------------------------")
            print("Total players: {}\n".format(len(panthers)))
            print(', '.join(panthers))
            break

        elif team_choice == "2":
            team_name2 = "Warriors"
            print("\nTeam: {} Stats".format(team_name2))
            print("-------------------------")
            print("Total players: {}\n".format(len(warriors)))
            print(', '.join(warriors))
            break

        elif team_choice == "3":
            team_name1 = "Bandits"
            print("\nTeam: {} Stats".format(team_name3))
            print("-------------------------")
            print("Total players: {}\n".format(len(bandits)))
            print(', '.join(bandits))
            break
