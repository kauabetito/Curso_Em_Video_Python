coun = 0
while True:
    coun += 1
    print(coun)
    if coun == 100:
        break

N1 = Sum = 0
while True:
    N1 = int(input("Enter a number: "))

    if N1 == 999:
        break

    Sum += N1
print(f"the sum is worth {Sum}")
