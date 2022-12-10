# Imports
from database_loader import *
from searchs import *
from profiles import *
from bests import *

# Main function

def main () -> None:

    # Main loop
    
    while True:
        command = input()

        if command == "search player":
            player_name = input("Enter player name or lastname: ")
            search_player (player_name) 
        
        if command == "search team":
            team_name = input("Enter team name or code: ")
            search_team (team_name)
            
        if command == "search manager":
            manager_name = input("Enter manager name or lastname: ")
            search_manager(manager_name)
        
        if command == "search referee":
            referee_name = input("Enter referee name or lastname: ")
            search_referee(referee_name)
            
        
            
        if command == "profile player":
            player_id = input('Enter player ID: ')
            profile_player (player_id)
            
        if command == "profile team":
            team_id = input('Enter team ID: ')
            profile_team(team_id)
            
        if command == "profile manager":
            manager_id = input("Enter manager ID: ")
            profile_manager (manager_id)
            
        if command == "profile referee":
            referee_id = input ("Enter referee ID: ")
            profile_referee (referee_id)
            
        if command == "profile competition":
            team1 = input ("Enter first team ID: ")
            team2 = input ("Enter second team ID: ")
            
            profile_competition (team1, team2)
            
        
        if command == "top goal scorer":
            year = input ("Enter the year: ")
            
            top_goal_scorer (year)
            
            


if __name__ == "__main__":
    main ()