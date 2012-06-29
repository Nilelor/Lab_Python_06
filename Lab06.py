class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name=firstname
        self.last_name=lastname
        self.score=[]
        self.team=team
        
    def add_score(self,date,score):
        self.score.append(score)

    def __str__(self):
    
        return self.first_name+' '+self.last_name
    def total_score(self):
        
        """total=0
        for i in self.score:
            total=total+i"""
        return sum(self.score)
    
    def average_score(self):
        average_score=float(sum(self.score))/len(self.score)
        return average_score
    
        

torres=Player('Fernando','Torres')
scores=[0,0,1,0,1]
for i in scores:
    torres.add_score('',i)
print torres.score
print torres.total_score()
print torres.average_score()

class Team:
    def __init__(self,name,league,manager_name,points):
        self.name=name
        self.league=league
        self.manager_name=manager_name
        self.points=points
        self.player=[]

    def add_player(self,player):
        self.player.append(player)

    def __str__(self):
        return self.name+' '+self.league+' '+self.manager_name+' '+self.points
        
portugal=Team('Prado','Laliga','Sam','9')

spain=Team('Barca','Europa','Messi','11')

#print portugal

torres=Player('Fernando','Torres',spain)
print torres.team

ronaldo=Player('Christiano','Ronaldo',portugal)
print ronaldo.team

spain.add_player('Torres')
print spain.player

portugal.add_player('Ronaldo')
print portugal.player



