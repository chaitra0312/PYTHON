n = int(input("Enter rows: "))
for i in range(1, n+1):         # row number goes from 1 to n
    for j in range(i):          # print i stars in each row
        print("*", end="")
    print()                     # move to next line
