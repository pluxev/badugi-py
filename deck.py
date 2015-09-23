#!/usr/bin/env python3

from printer import unicard
from evaluator import Badugi
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
	

	def deckpop(self):
		return self.cards.pop()

class Hand:
	
	def __init__(self):
		self.cards = []

	
	def deal(self, deck, num):
		if num > 0:
			for i in range (0,num):
				self.cards.append(deck.deckpop())

		
'''d = Deck()
d.shuffle()
h = Hand()
h.deal(d,4)
#h.cards.append(card(10,'h'))
#h.cards.append(card(11,'h'))
#h.cards.append(card(12,'h'))
#h.cards.append(card(1,'s'))
for card in h.cards:
	print(unicard[card.realRank+card.suit])
b = Badugi(h.cards)
for rank in b.handRank(h.cards):
	print(rank, end='')
print(' ')'''


