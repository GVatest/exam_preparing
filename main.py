f = open('Z:/777.txt')
s = f.readline()
print(s)
counter = 0
x = 0
max = 0
for i in range(len(s) - 1):
    if s[x] == 'L' and s[x + 1] == 'D' and s[x + 2] == 'R':
        counter += 1
        x += 2
        if max < counter:
            max = counter
    else:
        counter = 0

print(counter, end='')

