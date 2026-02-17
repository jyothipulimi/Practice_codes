# To print the Perfect numbers in between the range of 1 to 100

for i in range(1, 101):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)