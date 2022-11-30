# Databases

players_database = open ("database/players.csv", "r", encoding="utf8").readlines()
teams_database = open("database/teams.csv", "r", encoding="utf8").readlines()
managers_database = open("database/managers.csv", "r", encoding="utf8").readlines()
referees_database = open ("database/referees.csv", "r", encoding="utf8").readlines()

goals_database = open ("database/goals.csv", "r", encoding="utf-8").readlines()
matches_database = open ("database/matches.csv", "r", encoding="utf-8").readlines()

# Main Functions

def search_in (database : list, element : str, row : int):
    result = []
    
    for line in database:
        line = line.split (",")
        
        if element in line[row]:
            result.append (line)
    
    return result

def search_ex (database : list, element : str, row : int):
    result = []
    
    for line in database:
        line = line.split (",")
        
        if element == line[row]:
            result.append (line)
    
    return result


def remove_frequents (array : list) -> list:
    result = []
    for i in array:
        if i not in result:
            result.append (i)

def most_frequent (array : list) -> str:
    max_count = 0
    most_frequent = 0

    for i in range (len (array)):
        count = 0
        
        for j in range(len(array)):
            
            if array[i] == array[j]:
                count += 1
                
        if count > max_count:
            max_count = count
            most_frequent = array[i]
            
    return most_frequent
                
        
# Search Functions

def search_player (player_name : str) -> None:
    results = search_in(players_database, player_name, 1)
    results.extend (search_in(players_database, player_name, 2))
    
    remove_frequents(results)
    
    if results != []:
        for i in range(len(results)):
            result = results[i]
            
            if i + 1 <= 30:
                print (f"{i + 1} -> {result[0]}, {result[1]}, {result[2]}")  
                
            else:
                print ("There are too much answer!")
    
    else:
        print ("There is no results!")

def search_team (team_name : str) -> None:
    results = search_in(teams_database, team_name, 2)
    results.extend(search_in(teams_database, team_name, 1))
    
    remove_frequents(results)
    
    if results != []:
        for i in range(len(results)):
            result = results[i]
            
            if i + 1 <= 30:
                print (f"{i + 1} -> {result[0]}, {result[1]}, {result[2]}")
                
            else:
                print ("There are to much answer!")
            
    else:
        print ("There is not results!")
        
def search_manager (manager_name : str) -> None:
    results = search_in(managers_database, manager_name, 1)
    results.extend (search_in(managers_database, manager_name, 2))
    
    remove_frequents(results)
    
    if results != []:
        for i in range(len(results)):
            result = results[i]
            
            if i + 1 <= 30:
                print (f"{i + 1} -> {result[0]}, {result[1]}, {result[2]}")
                
            else:
                print ("There are too much answer!")
    
    else:
        print ("There is no results!")
        
def search_referee (referee_name : str) -> None:
    results = search_in(referees_database, referee_name, 1)
    results.extend (search_in(referees_database, referee_name, 2))
    
    remove_frequents(results)
    
    if results != []:
        for i in range(len(results)):
            result = results[i]
            
            if i + 1 <= 30:
                print (f"{i + 1} -> {result[0]}, {result[1]}, {result[2]}")
            
            else:
                print ("There are too much answer!")
                break
            
    else:
        print ("There is no results!")
    
# Profile Functions

def profile_player (player_id : str) -> None:
    
    result = search_ex(players_database, player_id, 0)
    if result != []:
        result = result[0]
        goals_count = len (search_ex(goals_database, player_id, 8))
        age = 2022 - int(result[3].split("-")[0])
        
        print (f"{result[0]} -> {result[2]} {result[1]} age: {age} times played: {result[8]} tournoments: {result[9]} goals: {goals_count}")
        
    else:
        print ("There is no answer!")

def profile_team (team_id : str) -> None:
    result = search_ex(teams_database, team_id, 0)
    
    if result != []:
        result = result[0]
        print (f"{result[0]} -> {result[1]} team code: {result[2]} region: {result[3]}")

    else:
        print ("There is no answer!")
    
def profile_manager (manager_id : str) -> None:
    result = search_ex(managers_database, manager_id, 0)
    
    if result != []:
        result = result[0]
        print (f"{result[0]} -> {result [2]} {result [1]} country: {result[3]}")
        
    else:
        print ("There is no answer!")

def profile_referee (referee_id : str) -> None:
    result = search_ex(referees_database, referee_id, 0)
    
    if result != []:
        result = result[0]
        print (f"{result[0]} -> {result[2]} {result[1]} country: {result[3]}")
        
def profile_competition (team1 : str, team2 : str) -> None:
    first_results = search_ex(matches_database, team1, 14)
    final_results = []
    for result in first_results:
        
        if result[15] == team2:
            final_results.append(result)
    
    first_results = search_ex(matches_database, team2, 14)
    
    for result in first_results:
        
        if result[15] == team1:
            final_results.append (result)
            
    if final_results == []:
        print ("There is to answer!")
        return
    
    for i in range (len (final_results)):
        result = final_results[i]
        print (f"{i + 1} -> {result[0]} | match name: {result[1]} tournament id: {result[2]} tournament name: {result[3]} stage: {result[4]} group: {result[5]} date: {result[8]} match time: {result[9]} stadium id: {result[10]} stadium name: {result[11]} city: {result[12]} country: {result[13]} result: {result[16]} extra time: {result[19]} \n")
    
# The best Functions

def top_goal_scorer (year : str) -> None:
    scorers = []
    
    if year == "all":
        
        for line in goals_database:
            line = line.split(",")
            
            scorers.append (line[8])
            
            
    else:
        results = search_in (goals_database, year, 4)
    
        
        for result in results:
            scorers.append (result[8])
        
    top_goal_scorer = most_frequent(scorers)
    
    print (f"{search_ex(players_database, top_goal_scorer, 0)[0][2]} {search_ex(players_database, top_goal_scorer, 0)[0][1]}")
    
    

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