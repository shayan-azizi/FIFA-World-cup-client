from database_loader import *

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
                break
    
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
                break
            
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
                break
    
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
    