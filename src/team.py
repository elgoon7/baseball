class Team:
	def __init__(self,name,city,players=None):
		self.name = name
		self.city = city
		self.players = []

	def __append__(self,player):
		return Team(self.players.append(player))