
# Dynamic Programming solution for 0-1 Knapsack Problem

def knapSack(W, wt, val, n):
    # Initialize the DP array
    dp = [0 for i in range(W + 1)]

    # Consider each item one by one
    for i in range(1, n + 1):
        # Traverse capacities in reverse order
        for w in range(W, 0, -1):
            if wt[i - 1] <= w:
                dp[w] = max(
                    dp[w],
                    dp[w - wt[i - 1]] + val[i - 1]
                )

    return dp[W]


# Driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print("Maximum value in Knapsack:", knapSack(W, wt, val, n))
