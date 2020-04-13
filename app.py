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

    print("the remaining players are ", players)
    for last in players:
        panthers.append(last)
       # print("panthers = {}".format(panthers))
            
    return (warriors, bandits, panthers)


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

    print(panthers)
    print(bandits)
    print(warriors)