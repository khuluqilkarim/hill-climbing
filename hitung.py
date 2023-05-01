import sys

input = sys.argv[1]

matrix = [
    [0, 30, 14, 33],
    [30, 0, 21, 41],
    [14, 21, 0, 24],
    [33, 41, 24, 0]
]

def calculate_value(input):
    value = 0
    for i in range(len(input)-1):
        source = int(input[i])
        dest = int(input[i+1])
        value += matrix[source][dest]
    return value

total = calculate_value(input)
print(total)
