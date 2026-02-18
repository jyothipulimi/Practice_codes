# To find the armstrong numbers between 1 and 1000

for n in range(1, 1001):
    rem = n
    count = 0
    while rem > 0:
        count += 1
        rem = rem // 10
    m = n
    sum = 0
    while m > 0:
        d = m % 10
        sum = sum + d ** count
        m = m // 10
    if sum == n:
        print(n, end=" ")
