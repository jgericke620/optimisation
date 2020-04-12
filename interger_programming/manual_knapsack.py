#!/Users/jacogericke/anaconda3/bin/python3

max_weight = 10

values = [10, 40, 30, 50]
weights = [5, 4, 6, 3]

comb = [[0 for _ in range(max_weight+1)] for _ in range(len(values)+1)]

for i, tup in enumerate(zip(values, weights)):
    row = i+1
    value, weight = tup
    #print(i+1, value, weight)
    for j in range(max_weight+1):
        col = j

        maxValWithoutCurr = comb[row-1][col]
        maxValWithCurr = 0

        if col >= weight:
            maxValWithCurr = value

            remainingCapacity = col - weight
            maxValWithCurr += comb[row-1][remainingCapacity]
        
        comb[row][col] = max(maxValWithoutCurr, maxValWithCurr)
        print("\nAt item {} (w:{} v:{}) with bag capcity of {}".format(row, weight, value, col))
        print("max without curr = {}, max with cur = {}".format(maxValWithoutCurr, maxValWithCurr))
        input()
        for line in comb:
            print(line)
