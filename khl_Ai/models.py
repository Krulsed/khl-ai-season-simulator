class Team:
    def __init__(self,name,wins,otl,losses):
        self.name = name
        self.wins = wins
        self.otl = otl
        self.losses = losses

    def points(self):
        return self.wins * 2 + self.otl * 1
class Match:
    def __init__(self,date,home_team,away_teem):
        self.date = date
        self.home_team = home_team
        self.away_teem = away_teem
        self.home_team_score = None
        self.away_team_score = None
        self.status = "scheduled"
