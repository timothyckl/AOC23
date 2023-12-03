from collections import defaultdict

res = 0

with open('./input.txt', 'r') as txt:
  matrix = [[char for char in line] for line in txt]

rows = len(matrix)
cols = len(matrix[0])

nums = defaultdict(list)

for row in range(rows):
  gears = set()
  n = 0
  has_part = False
  for col in range(len(matrix[row]) + 1):
    if col<cols and matrix[row][col].isdigit():
      n = n * 10 + int(matrix[row][col])
      for i in [-1,0,1]:
        for j in [-1,0,1]:
          if 0<=row+i<rows and 0<=col+j<cols:
            ch = matrix[row+i][col+j]
            if not ch.isdigit() and ch != '.':
              has_part = True
            if ch=='*':
              gears.add((row+i, col+j))
    elif n>0:
      for gear in gears:
        nums[gear].append(n)
      if has_part:
        res+=n
      n = 0
      has_part = False
      gears = set()    

print(f"final sum: {res}\n")  # part 1

res = sum([v[0] * v[1] for v in nums.values() if len(v) == 2])

print(f"final sum: {res}\n")  # part 2