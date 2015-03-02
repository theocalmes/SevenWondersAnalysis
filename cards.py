
def contains(a, b):
	b_copy = list(b)
	for x in a:
		if x in b:
			b_copy.remove(x)
		else:
			return False
	return True
	
class CardAbstract(object):
	def __init__(self, name):
		self.name = name
		self.gold_cost = 0
		self.resource_cost = []
		self.is_free_with = []
		
	def can_buy(resources, gold):
		return contains(self.resource_cost, resources) and self.gold_cost <= gold
	
	def is_free_with_cards(cards):
		return False
	
	def reward(self):
		return None
		
	def __repr__(self):
		return self.name
	
class Resource(object):
	def __init__(self, type):
		self.type = type
	def __repr__(self):
		return self.type

class VictoryPoint(object):
	def __init__(self, amount):
		self.amount = amount
	def __repr__(self):
		return "Points: %s" % (self.amount,)

class ResourceCard(CardAbstract):
	def __init__(self, name, resources, gold_cost):
		self.name = name
		self.gold_cost = gold_cost
		self.resources = resources
		super(ResourceCard, self).__init__(name)
		
	def reward(self):
		return self.resources
		
		
class BlueCard(CardAbstract):
	def __init__(self, name, resources_cost, points, is_free_with=None):
		if is_free_with is None:
			self.is_free_with = []
		else:
			self.is_free_with = is_free_with
					
		self.name = name
		self.resource_cost = resources_cost
		self.victory_points = VictoryPoint(points)
	
	def is_free_with_cards(self, cards):
		for card in cards:
			if card.name in self.is_free_with:
				return True
		return False


	def reward(self):
		return self.victory_points

timber_yard = ResourceCard("Timber Yard", [Resource("wood"), Resource("stone")], 1)
pawn_shop = BlueCard("Baths", [], 3)
cards = [timber_yard, pawn_shop]
aquaduct = BlueCard("Aquaduct", [], 5, is_free_with=["Baths"])


print 'is it free? %s' % (aquaduct.is_free_with_cards(cards), )

for card in cards:
	print card.reward()