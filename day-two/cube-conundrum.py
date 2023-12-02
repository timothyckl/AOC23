sum = 0
power_sum = 0
max = { "red": 12,"green": 13,"blue": 14 }

with open('./input.txt', 'r') as file:
  for game in file:
    game = game.strip()
    possible = True
    game_id, draw = game.split(": ")
    counts = { "red": 0,"green": 0,"blue": 0 }
    for d in draw.split("; "):
      for c in d.split(", "):
        count, color = c.split()
        if int(count) > counts[color]:
          counts[color] = int(count)
        if int(count) > max.get(color, 0):
          possible = False

    # power = 1
    # for v in counts.values():
    #  power*=v
    power_sum += counts["red"] * counts["green"] * counts["blue"]

    if possible:
      sum+=int(game_id.split()[-1])

print(sum) # part 1
print(power_sum)  # part 2
