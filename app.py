from deck import *
from random import choice

beer_card = Card('7', 'diamons')
print "Beer card: %s" % str(beer_card)

deck = FrenchDeck()
print "Lenght %d" % len(deck)

print "First card: %s" % str(deck[0])
print "Last card: %s" % str(deck[-1])

print "Random card %s" % str(choice(deck))
print "Random card %s" % str(choice(deck))
print "Random card %s" % str(choice(deck))

for card in reversed(deck):
	print(card)