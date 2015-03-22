
from cards import *

STARTING_COIN_AMOUNT = 3

class Player(object):
	def __init__(self, position, wonder):
		self.position = position
		self.wonder = wonder
		self.coins = STARTING_COIN_AMOUNT
		self.cards = []
		self.military_tokens = []

	def get_valid_moves(self, hand):
		# wonders, discards, etc, etc
		affordable_cards = [card for card in hand if self.can_buy(card)]


	def can_buy(self, card):
		# TODO: account for multi-resource cards
		#return is_contained_in(card.resource_cost, self.resources()) and card.coin_cost <= self.coins

		if card.coin_cost <= self.coins:
			return False

		needed_resources = list(card.resource_cost)
		for resource in self.resources():
			needed_resources.remove(resource)

		if needed_resources.length == 0:
			return True
		else:
			raw_materials_needed = len(resource in needed_resources if isinstance(resource, RawMaterial))
			manufactured_goods_needed = len(resource in needed_resources if isinstance(resource, ManufacturedGood))
			for multi_resource in self.multi_resources():
				if isinstance(multi_resource, ManufacturedGoodMultiResource):
					raw_materials_needed -= 1
				elif isinstance(multi_resource, RawMaterialMultiResource):
					raw_materials_needed -= 1

			if raw_materials_needed <= 0 and manufactured_goods_needed <= 0:
				return true

	def resources(self):
		current_resources = []
		for card in self.cards:
			if isinstance(card, ResourceCardAbstract):
				current_resources += card.reward()
		return current_resources

	def mutli_resources(self):
		mutli_resources = []

		for item in (self.commercial_structures() + self.wonder.stages):
			if isinstance(item.reward(), MultiResource):
				mutli_resources.append(item.reward())

		return multi_resources

	def commercial_structures(self):
		return [card for card in self.card if isinstance(card, CommerciaLStructure)]
	
	# how to implement?
	# def trading_discounts(self):
	# 	return [card.reward() for card in self.commercial_structures() if card.reward().isTradingDiscount()]

if __name__ == "__main__":
	timber_yard = RawMaterial("Timber Yard", [Resource("wood"), Resource("stone")], 1)
	foo_card = MilitaryStructure("foo", [Resource("wood")], 2)
	baz_card = MilitaryStructure("baz", [Resource("wood"), Resource("clay")], 3)

	player = Player(1, None)

	print '-- %s' % (player.can_buy(foo_card),)
	player.cards.append(timber_yard)
	print '-- %s' % (player.can_buy(foo_card),)

	print '-- ' + str(player.get_valid_moves([foo_card, baz_card]))
