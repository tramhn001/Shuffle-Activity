import random

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards without using random.shuffle()
# Using randint() is ok
def shuffle_deck(deck_of_cards):

    shuffled_deck = []
    indices_used = set()

    while len(shuffled_deck) < len(deck_of_cards):
        index = random.randint(0, len(deck_of_cards) - 1)
        if index not in indices_used:
            shuffled_deck.append(deck_of_cards[index])
            indices_used.add(index)
    return shuffled_deck


shuffled = shuffle_deck(deck_of_cards)
print("Shuffled deck:", shuffled)

