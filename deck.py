#!/usr/bin/env python3

from printer import unicard
import random
class card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		ranks = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
		self.realRank = ranks[int(self.rank)]

	def getRank(self):
		return self.rank
	

	def getSuit(self):
		return self.suit

	def __str__(self):
		card = self.realRank+self.suit
		return card

class Deck:
	
	def __init__(self):
		self.cards = []
		suits = ["d","s","h","c"]
		for suit in range(4):
			for rank in range(13):
				self.cards.append(card(rank, suits[suit]))

	def shuffle(self):
		random.shuffle(self.cards)



d = Deck()
d.shuffle()
for card in d.cards:
	print(unicard[card.realRank+card.suit],end=" ")

