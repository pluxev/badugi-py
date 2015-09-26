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
c = Hand()
c.deal(d,4)
x=0

while x < 3:
	for card in h.cards:
		print(unicard[card.realRank+card.suit],end=" ")
		temp.cards.append(card)
	choice = input(" which card(s) to discard? ")
	for i in choice:
		try:
			if int(i) > 0 and int(i) < 5:
				try:
					temp.cards.remove(h.cards[int(i)-1])	
				except ValueError:	
					pass
		except ValueError:
			pass
	h.cards.clear()
	for card in temp.cards:
		h.cards.append(card)
	h.deal(d,4-len(h.cards))
	temp.cards.clear()
	
	ctemp = []
	b = Badugi(c.cards)
	for card in b.handRank(c.cards):
		ctemp.append(card)
	print("computer is discarding "+str(4-len(ctemp))+" cards")
	c.cards.clear()
	for card in ctemp:
		c.cards.append(card)
	c.deal(d,4-len(c.cards))
	ctemp.clear()

	if x == 2:
		play = []
		comp = []
	
		for card in h.cards:
			print(unicard[card.realRank+card.suit],end=" ")
		b = Badugi(h.cards)
		for card in b.handRank(h.cards):
			print(card.realRank, end="")
			play.append(card.rank)

		print("\ncomputer's cards: ")
		for card in c.cards:
			print(unicard[card.realRank+card.suit],end=" ")
		b2 = Badugi(c.cards)
		for card in b2.handRank(c.cards):
			print(card.realRank, end="")
			comp.append(card.rank)
		
		won = 100

		if len(play) > len(comp):
			print("\nyou win!")
		elif len(comp) > len(play):
			print("\nyou lost")
		else:
			for x in range(0,len(play)-1):
				if play[x] < comp[x]:
					won = 1
					break
				if comp[x] < play[x]:
					won = 0
					break
			if won == 1:
				print("\nyou win!")
			elif won == 0:
				print("\nyou lost")
			elif won == 100:
				print("tie!!!")		


		again = input("play again? y for yes: ")
		if again == 'y':
			x = 0
			d = Deck()
			d.shuffle()
			h.cards.clear()
			h.deal(d,4)
			c.cards.clear()
			c.deal(d,4)
			os.system('clear')
		else:
			x = x + 1
			break
	else:
		x = x + 1
