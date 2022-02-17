#optimised approach with time complexity (n*capacity), which is more efficient then basic approcah assuming that n*c < 2^n
def knapsack(capacity, weight, value, n):
    #where n = number of items
    K = [[0 for x in range(capacity +1)] for x in range(n+1)]

    #build table K[[]] in bottom up manner
    for i in range(n+1):
        for c in range(capacity +1):
            if i ==0 or c == 0:
                K[i][c]=0
            elif weight[i-1]<= c:
                K[i][c] = max(value[i-1]+K[i-1][c-weight[i-1]], K[i-1][c])
            else:
                K[i][c]= K[i-1][c]

    return K[n][capacity]

#eg:
v = [60, 100, 120]
w = [10, 20, 60]
c = 50
n = len(v)
print(knapsack(c, w, v, n))   

