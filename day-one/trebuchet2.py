sum = 0
map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open('./input.txt', 'r') as file:
    for line in file:
        numbers = []
        i = 0

        while i < len(line):
            found = False

            # find word match
            for word in map:
                if line.startswith(word, i):
                    numbers.append(map[word])
                    i += len(word)
                    found = True
                    break

            # if no matches, check if there is digit
            if not found:
                if line[i].isdigit():
                    numbers.append(line[i])
                i += 1

        sum += int(numbers[0] + numbers[-1])

print(f"final sum: {sum}")
