import itertools, random

deck_cards = list(itertools.product(range(1,14), ["Spades", "Clubs", "Diamonds", "Hearts"]))

random.shuffle(deck_cards)

for i in range(5):
    print(deck_cards [i] [0], "of", deck_cards [1] [1])

