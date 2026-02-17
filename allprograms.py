s = int(input())
e = int(input())
if s > e:
    print("Invalid Input")
else:
    even_numbers = []
    odd_numbers = []
    fact_numbers = []
    prime_numbers = []
    perfect_numbers = []
    palindrome_numbers = []
    palindrome_sum = []

    for i in range(s, e + 1):
        # Even
        if i % 2 == 0:
            even_numbers.append(i)

        # Odd
        if i % 2 != 0:
            odd_numbers.append(i)

        # Prime
        if i > 1:
            flag = 0
            for j in range(2, i):
                if i % j == 0:
                    flag = 1
                    break
            if flag == 0:
                prime_numbers.append(i)

        # Factorial
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        fact_numbers.append(factorial)

        # Perfect number
        if i > 0:
            c = 0
            for j in range(1, i):
                if i % j == 0:
                    c += j
            if c == i:
                perfect_numbers.append(i)

        # Palindrome
        temp = i
        rev = 0

        while temp > 0:
            d = temp % 10
            rev = rev * 10 + d
            temp = temp // 10

        if i == rev:
            palindrome_numbers.append(i)

            c = 0
            num = i
            while num > 0:
                c += num % 10
                num = num // 10
            palindrome_sum.append(c)
    # Even
    even = list(map(lambda x: x + 10, even_numbers))
    # Odd
    odd = list(map(lambda x: x ** 2, odd_numbers))
    # Prime
    prime = sum(prime_numbers)
    # Factorial

    f = []
    for i in fact_numbers:
        count = 0
        temp = i
        if temp == 0:
            count = 1
        else:
            while temp > 0:
                count += 1
                temp = temp // 10
        f.append(count)

    print("Even numbers: ", even_numbers)
    print("After adding 10: ", even)

    print("Odd numbers: ", odd_numbers)
    print("After squaring: ", odd)

    print("Prime numbers: ", prime_numbers)
    print("Sum of all primes: ", prime)

    print("Factorials: ", fact_numbers)
    print("Digit counts: ", f)

    print("Palindrome numbers: ", palindrome_numbers)
    print("Sum of digits: ", palindrome_sum)
    print("Perfect numbers: ", perfect_numbers)
