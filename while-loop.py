i = 0
numbers = []

while i < 9:
    print("The top number i is %d" %i)
    numbers.append(i)

    i = i + 1
    print("Numbers now:", numbers)

    print("The bottom numbers i is %d" %i)

print("The numbers in order: ")

for num in numbers:
    print(num)