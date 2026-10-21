

class Team:
    def __init__(self,name,wins,otl,losses):
        self.name = name
        self.wins = wins
        self.otl = otl
        self.losses = losses

    def points(self):
        return self.wins * 2 + self.otl * 1
avangard = Team("Avangard", 10, 2, 3)
print(avangard.points())