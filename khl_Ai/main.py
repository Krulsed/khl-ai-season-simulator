from models import Team,Match
avangard = Team("Авангард",10,2,3)
print(avangard.points())
match = Match("2026-09-01", "Авангард", "ЦСКА")
print(match.status)