#!/usr/bin/env python3

import os
from printer import unicard
from evaluator import Badugi
from deck import card, Deck, Hand

os.system('clear')
d = Deck()
d.shuffle()
h = Hand()
temp = Hand()
h.deal(d,4)
x=0

while x < 3:
	for card in h.cards:
		print(unicard[card.realRank+card.suit],end=" ")
		temp.cards.append(card)
	choice = input(" which card(s) to discard? ")
	for i in choice:
		try:
			if int(i) >= 0 and int(i) < 4:
				try:
					temp.cards.remove(h.cards[int(i)])	
				except ValueError:	
					pass
		except ValueError:
			pass
	h.cards.clear()
	for card in temp.cards:
		h.cards.append(card)
	h.deal(d,4-len(h.cards))
	temp.cards.clear()
	
	if x == 2:
		for card in h.cards:
			print(unicard[card.realRank+card.suit],end=" ")
		b = Badugi(h.cards)
		for rank in b.handRank(h.cards):
        		print(rank, end='')
		again = input(" play again? y for yes: ")
		if again == 'y':
			x = 0
			d = Deck()
			d.shuffle()
			h.cards.clear()
			h.deal(d,4)
			os.system('clear')
		else:
			x = x + 1
	else:
		x = x + 1
