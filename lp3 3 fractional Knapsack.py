
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractionalKnapsack(W, arr):
    # Sort items by value-to-weight ratio
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

    # Total value in the knapsack
    finalvalue = 0.0

    # Iterate through all items
    for item in arr:
        # If the item fits completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value

        # Take the fractional part
        else:
            finalvalue += item.value * W / item.weight
            break

    return finalvalue


# Driver Code
if __name__ == "__main__":
    W = 50
    arr = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print("Maximum value in Knapsack:", max_val)
