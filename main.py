from src.player import Player
from src.team import Team

class main:
	satchel_paige = Player(name="Satchel Paige",position="Pitcher")

	grays = Team(name="Grays",city="Homestead")

	grays.players.append(satchel_paige)

	for i in grays.players:
		print i.name + ", " + i.position

if __name__ == "__main__":
	main()
