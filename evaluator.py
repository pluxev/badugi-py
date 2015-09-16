#!/usr/bin/env python3

from printer import unicard

class Badugi:

	def __init__(self, hand):
		self.hand = hand
		if len(hand) != 4:
			print("not a valid badugi input")
					
	def handRank(self, hand):
		ordered = sorted(hand, key=lambda card: card.rank)
		temphand = sorted(hand, key=lambda card: card.rank)
		discard = []
		
		for x in range(0, len(ordered)):
			for y in range(x+1, len(ordered)):
				if ordered[x].suit == ordered[y].suit:
					if ordered[x].rank > ordered[y].rank:
						try:
							temphand.remove(ordered[x])
							discard.append(ordered[x])
						except ValueError:
							pass
					else:	
						try:	
							temphand.remove(ordered[y])
							discard.append(ordered[y])
						except ValueError:
							pass
		
		
		ordered = temphand 	
		xswitcher = 100
		x1switcher = 100
		x = 0
		while x < len(ordered)-1:
			if ordered[x].rank == ordered[x+1].rank:
				for y in range(0, len(discard)):
					if ordered[x].suit == discard[y].suit:	
						replacepaired = False
						for z in range(0, len(ordered)):
							if discard[y].rank == ordered[z].rank and z != x:
								replacepaired = True
						if not replacepaired:
							if xswitcher == 100:
								xswitcher = y
							else:
								if discard[xswitcher].rank > discard[y].rank:
									xswitcher = y
					elif ordered[x+1].suit == discard[y].suit:
						replacepaired = False
						for z in range(0, len(ordered)):
							if discard[y].rank == ordered[z].rank and z != x:
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
						discard.append(ordered.pop(x))
					except ValueError:
						pass
				if xswitcher == 100 and x1switcher != 100:		
					try:
						temphand.append(discard.pop(x1switcher))
						discard.append(ordered.pop(x+1))
					except ValueError:
						pass
				if xswitcher != 100 and x1switcher != 100:
					if discard[xswitcher].rank < discard[x1switcher].rank:
						try:
							temphand.append(discard.pop(xswitcher))
							discard.append(ordered.pop(x))
						except ValueError:
							pass
					else:
						try:
							temphand.append(discard.pop(x1switcher))
							discard.append(ordered.pop(x+1))
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
			
