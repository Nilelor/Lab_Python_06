"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
import datetime
player_stats={datetime.date(2012,06,23):['rooney',2],
              datetime.date(2012,06,25):['rooney',2],
              datetime.date(2012,06,19):['ronaldo',0],
              datetime.date(2012,06,20):['ronaldo',3],
              datetime.date(2012,06,21):['toress',1]}
#print player_stats[datetime.date(2012,06,19)]
## implement highest_score
score=0
for i in player_stats.keys():
    player_score=player_stats[i]
    if player_score[1]>score:
        score=player_score[1]
        date=i
        name=player_score[0]
print name,date,score
        


## implement highest_score_for_player
def highest_score_for_player(player_stats,player):
    score=0
    
    for i in player_stats.keys():
        player_high=player_stats[i]
        if player_high[0]==player:
            if player_high[1]>score:
                score=player_high[1]
    return score


footballer=raw_input("Enter player")
print highest_score_for_player(player_stats,footballer)


        



## implement highest_scorer
def highest_scorer(player_stats,player):
    
    for i in player_stats.keys():
        player_high=player_stats[i]
        score=player_high[1]
        if player_high[0]==player:
            if player_high[1]>score:
                score=score+player_high[1]
    return score


footballer=raw_input("Enter player")
print highest_scorer(player_stats,footballer)

