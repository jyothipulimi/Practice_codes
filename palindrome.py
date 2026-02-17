# To print Palindrome Numbers in between 0 to 100

for i in range(1,101):
    temp = i
    rev = 0
    while temp > 0:
        j = temp%10
        rev = rev *10+j
        temp = temp//10
    if i == rev:
        print(i,end=' ')
