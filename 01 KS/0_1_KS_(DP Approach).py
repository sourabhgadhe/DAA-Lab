# This is the memoization approach of  0 / 1 Knapsack in Python 
# we can say recursion + memoization = DP 

def knapsack(weights,profits,c,n):
    
    # base conditions
    if(n==0 or c==0):
        return 0
    if(t[n][c] != -1):
        return t[n][c]
    
    if(weights[n-1] <= c):
        t[n][c] = max( knapsack(weights,profits,c-weights[n-1],n-1)+profits[n-1] , knapsack(weights,profits,c,n-1))  # remember this for getting all remembered
        return t[n][c]
    
    elif(weights[n-1] > c):
        t[n][c] = knapsack(weights,profits,c,n-1)
        return t[n][c]


if __name__ == "__main__":

    # weights=[10,20,30]
    # profits=[60,100,120]
    # c=50
    # n=len(profits)

    c=int(input("Enter the KS capacity: "))
    n=int(input("Enter total no. of items: "))
    weights= []
    profits= []

    t=[[-1 for j in range(c+1)] for i in range (n+1)]     # ******* IMP *******

    print("Enter the weights of the Items: ")
    for i in range(n):
        weights.append(int(input()))
    
    print("Enter the profits of the Items: ")
    for i in range(n):
        profits.append(int(input()))
    
    print("\nThe maximum profit that can be obtained is: ",knapsack(weights,profits,c,n))


