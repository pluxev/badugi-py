#!/usr/bin/env python3

from printer import unicard

class Badugi:

	def __init__(self, hand):
		self.hand = hand
		if len(hand) != 4:
			print("not a valid badugi input")
					
	def handRank(self, hand):
		temphand = sorted(hand, key=lambda card: card.rank)
		temphand2 = sorted(hand, key=lambda card: card.rank)
		discard = []
		
		for x in range(0, len(temphand2)):
			for y in range(x+1, len(temphand2)):
				if temphand2[x].suit == temphand2[y].suit:
					if temphand2[x].rank > temphand2[y].rank:
						try:
							temphand.remove(temphand2[x])
							discard.append(temphand2[x])
						except ValueError:
							pass
					else:	
						try:	
							temphand.remove(temphand2[y])
							discard.append(temphand2[y])
						except ValueError:
							pass
		
		 	
		xswitcher = 100
		x1switcher = 100
		x = 0
		while x < len(temphand)-1:
			if temphand[x].rank == temphand[x+1].rank:
				for y in range(0, len(discard)):
					if temphand[x].suit == discard[y].suit:	
						replacepaired = False
						for z in range(0, len(temphand)):
							if discard[y].rank == temphand[z].rank and z != x:
								replacepaired = True
						if not replacepaired:
							if xswitcher == 100:
								xswitcher = y
							else:
								if discard[xswitcher].rank > discard[y].rank:
									xswitcher = y
					elif temphand[x+1].suit == discard[y].suit:
						replacepaired = False
						for z in range(0, len(temphand)):
							if discard[y].rank == temphand[z].rank and z != x:
								replaced = True
						if not replacepaired:
							if x1switcher == 100:
								x1switcher = y
							else:
								if discard[x1switcher].rank > discard[y].rank:
									x1switcher = y	
				if xswitcher != 100 and x1switcher == 100:
					try:
						temphand.append(discard.pop(xswitcher))
						discard.append(temphand.pop(x))
					except ValueError:
						pass
				if xswitcher == 100 and x1switcher != 100:		
					try:
						temphand.append(discard.pop(x1switcher))
						discard.append(temphand.pop(x+1))
					except ValueError:
						pass
				if xswitcher != 100 and x1switcher != 100:
					if discard[xswitcher].rank < discard[x1switcher].rank:
						try:
							temphand.append(discard.pop(xswitcher))
							discard.append(temphand.pop(x))
						except ValueError:
							pass
					else:
						try:
							temphand.append(discard.pop(x1switcher))
							discard.append(temphand.pop(x+1))
						except ValueError:
							pass
				if xswitcher == 100 and x1switcher == 100:
					discard.append(temphand.pop(x))	
			else:
				x += 1
	
		badugitype = []
		for card in sorted(temphand, key=lambda card: card.rank, reverse = True):
			badugitype.append(card.realRank)	
		return badugitype
			
