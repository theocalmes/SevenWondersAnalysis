
# returns whether 'a' is a subset of 'b'
def is_contained_in(a, b):
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
		self.coin_cost = 0
		self.resource_cost = []
		self.free_with = []

	def is_free_with(self, cards):
		for card in cards:
			if card.name in self.free_with:
				return True
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
	def __eq__(self, other):
		return self.type == other.type

class MultiResource(object):
	pass

class ManufacturedGoodMultiResource(MultiResource):
	pass

class RawMaterialMultiResource(MultiResource):
	pass

class VictoryPoint(object):
	def __init__(self, amount):
		self.amount = amount
	def __repr__(self):
		return "Points: %s" % (self.amount,)

class Science(object):
	def __init__(self, type):
		self.type = type
	def __repr__(self):
		return self.type

class MilitaryStrength(object):
	def __init__(self, amount):
		self.amount = amount
	def __repr__(self):
		return "Strength: %s" % (self.amount,)

class ResourceCardAbstract(CardAbstract):
	def __init__(self, name, resources, coin_cost):
		self.name = name
		self.coin_cost = coin_cost
		self.resources = resources
		super(ResourceCardAbstract, self).__init__(name)
		
	def reward(self):
		return self.resources

class RawMaterial(ResourceCardAbstract):
	pass
	
class ManufacturedGood(ResourceCardAbstract):
	pass
		
class CivilianStructure(CardAbstract):
	def __init__(self, name, resources_cost, points, free_with=None):
		if free_with is None:
			self.free_with = []
		else:
			self.free_with = free_with
					
		self.name = name
		self.resource_cost = resources_cost
		self.victory_points = VictoryPoint(points)

	def reward(self):
		return self.victory_points
		
class ScientificStructure(CardAbstract):
	def __init__(self, name, resources_cost, science, free_with=None):
		if free_with is None:
			self.free_with = []
		else:
			self.free_with = free_with
					
		self.name = name
		self.resource_cost = resources_cost
		self.coin_cost = 0
		self.science = science
		
	def reward(self):
		return self.science

class MilitaryStructure(CardAbstract):
	def __init__(self, name, resources_cost, strength, free_with=None):
		if free_with is None:
			self.free_with = []
		else:
			self.free_with = free_with

		self.name = name
		self.resource_cost = resources_cost
		self.coin_cost = 0
		self.strength = strength

	def reward(self):
		return self.strength

class CommercialStructure(CardAbstract):
	def __init__(self, name, resource_cost):
		pass

if __name__ == "__main__":
	timber_yard = RawMaterial("Timber Yard", [Resource("wood"), Resource("stone")], 1)
	pawn_shop = CivilianStructure("Baths", [], 3)
	aquaduct = CivilianStructure("Aquaduct", [], 5, free_with=["Baths"])
	laboratory = ScientificStructure("Laboratory", [Resource("clay"), Resource("clay"), Resource("paper")], Science("gear"), free_with=["Workshop"])

	cards = [timber_yard, pawn_shop, aquaduct]
	print 'is it free? %s' % (laboratory.is_free_with(cards), )
