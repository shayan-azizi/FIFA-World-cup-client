from database_loader import *

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
    