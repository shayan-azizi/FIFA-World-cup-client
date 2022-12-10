from database_loader import *

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
    