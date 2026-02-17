# To print Prime Numbers in between the range of 1 to 100

prime = []
for i in range(2,100):
    flag = True
    for j in range(2,i):
        if i%j == 0:
            flag = False
            break
    if flag == 1:
        prime.append(i)
print(prime)

