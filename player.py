
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
		return [card for card in hand if self.can_buy(card)]

	def can_buy(self, card):
		return is_contained_in(card.resource_cost, self.resources()) and card.coin_cost <= self.coins

	def resources(self):
		current_resources = []
		for card in self.cards:
			if isinstance(card, ResourceCardAbstract):
				current_resources += card.reward()
		return current_resources

if __name__ == "__main__":
	timber_yard = RawMaterial("Timber Yard", [Resource("wood"), Resource("stone")], 1)
	foo_box = MilitaryStructure("foo", [Resource("wood")], 9)

	player = Player(1, None)

	print '-- %s' % (player.can_buy(foo_box),)
	player.cards.append(timber_yard)
	print '-- %s' % (player.can_buy(foo_box),)
