import random
from collections import Counter


num_simulations = 100000

suits = ['trefla', 'inimaR', 'inimaN', 'romb']
deck = [(value, suit) for value in range(1, 14) for suit in suits]


def has_pair(hand):
    values = [card[0] for card in hand]
    value_counts = Counter(values)
    return any(count == 2 for count in value_counts.values())

def has_two_pairs(hand):
    values = [card[0] for card in hand]
    value_counts = Counter(values)
    return list(value_counts.values()).count(2) == 2


def has_three_of_a_kind(hand):
    values = [card[0] for card in hand]
    value_counts = Counter(values)
    return any(count == 3 for count in value_counts.values())

def has_four_of_a_kind(hand):
    values = [card[0] for card in hand]
    value_counts = Counter(values)
    return any(count == 4 for count in value_counts.values())


def has_straight(hand):
    values = sorted(card[0] for card in hand)
    return values == list(range(values[0], values[0] + 5))

def has_flush(hand):
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1




num_hands_with_pair = 0
num_hands_with_two_pairs = 0
num_hands_with_three_of_a_kind = 0
num_hands_with_straight = 0
num_hands_with_flush = 0
num_hands_with_four_of_a_kind = 0

for _ in range(num_simulations):
    random.shuffle(deck)
    hand = deck[:5]

    if has_pair(hand):
        num_hands_with_pair += 1
    if has_two_pairs(hand):
        num_hands_with_two_pairs += 1
    if has_three_of_a_kind(hand):
        num_hands_with_three_of_a_kind += 1
    if has_straight(hand):
        num_hands_with_straight += 1
    if has_flush(hand):
        num_hands_with_flush += 1
    if has_four_of_a_kind(hand):
        num_hands_with_four_of_a_kind += 1


probability_of_pair = num_hands_with_pair / num_simulations
probability_of_two_pairs = num_hands_with_two_pairs / num_simulations
probability_of_three_of_a_kind = num_hands_with_three_of_a_kind / num_simulations
probability_of_straight = num_hands_with_straight / num_simulations
probability_of_flush = num_hands_with_flush / num_simulations
probability_of_four_of_a_kind = num_hands_with_four_of_a_kind / num_simulations


print("Probabilitatea estimata de a obtine o pereche: ",probability_of_pair)
print("Probabilitatea estimata de a obtine doua perechi: ",probability_of_two_pairs)
print("Probabilitatea estimata de a obtine trei de acelasi fel: ",probability_of_three_of_a_kind)
print("Probabilitatea estimata de a obtine chinta (straight): ",probability_of_straight)
print("Probabilitatea estimata de a obtine culoare (flush): ",probability_of_flush)
print("Probabilitatea estimata de a obtine patru de acelasi fel: ",probability_of_four_of_a_kind)
