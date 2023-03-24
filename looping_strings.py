brand = 'mitsubishi'
index = 0

print('while loop output:')
while index < len(brand):
    letter = brand[index]
    print(index, letter)
    index += 1


# more elegant using FOR loop
print('for loop output:')
for x in brand:
    print(x)

# example counting number of 'i's in mitsubishi
count = 0
print(brand)
for x in brand:
    if x == 'i':
        count += 1
print(f'number of i found is {count}')

