sum = 0

with open('./input.txt', 'r') as file:
    for line in file:
        front = 0
        back = len(line) - 1

        # Find the first digit
        while front <= back and not line[front].isdigit():
            front += 1

        # Find the last digit
        while back >= front and not line[back].isdigit():
            back -= 1

        if line[front].isdigit() and line[back].isdigit():
            digit = line[front] + line[back]
            sum += int(digit)

print(f"final sum: {sum}")