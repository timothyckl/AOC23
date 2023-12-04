import re
import numpy as np

with open('./input.txt', 'r') as txt:
  collection = np.array([line.strip() for line in txt])

# part 1
def parse_card(card):
  _, winning_nums, my_nums = re.split(r'\s*\|\s*|\s*:\s*', card)
  winning_nums = re.split(r'\s+', winning_nums)
  my_nums = re.split(r'\s+', my_nums)
  return winning_nums, my_nums

def part_one():
  points = 0

  for card in collection:
    winning_nums, my_nums = parse_card(card)
    game_points = 0
    history = []

    for i, num in enumerate(my_nums):
      if num in winning_nums and len(history) == 0:
        game_points+=1
        history.append(i)
      elif num in winning_nums and len(history) > 0:
        game_points*=2
        history.append(i)
      else:
        continue
    points+=game_points
  return points

# part 2, jj
card_counts = {}
total = 0

def calculate_cards(start_card: int, end_card: int, total: int = 0):
  for card_id in range(start_card, end_card):
    total += 1
    matches = 0
    winning_nums, card_nums = parse_card(collection[card_id])

    # iterate through winning nums
    for num in winning_nums:
      if num in card_nums:
        matches += 1

    # call calculate in itself to calculate card copies
    if card_id not in card_counts:
      start = card_id + 1
      end = card_id + 1 + matches
      card_counts[card_id] = calculate_cards(start, end)

    total += card_counts[card_id]
    matches = 0
  
  return total

def part_two():
  return calculate_cards(0, len(collection))
  
p1 = part_one()
p2 = part_two()

print(p1, p2)
