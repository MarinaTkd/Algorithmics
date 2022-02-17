#this is a branch and bound approach with time complexity (2^n)

def knapsack(capacity, weight, value, n):
    #where n = number of items

    #base case
    if n == 0 or capacity ==0:
        return 0

    if (weight[n-1] > capacity):
        return knapsack(capacity, weight, value, n-1)
    
    else:
        return max(value[n-1] +knapsack(capacity - weight[n-1], weight, value, n-1), knapsack(capacity, weight, value, n-1))

#Driver Code
v = [60, 100, 120]
w = [60, 60, 60]
c = 50
n = len(v)
print (knapsack(c, w, v, n))
 