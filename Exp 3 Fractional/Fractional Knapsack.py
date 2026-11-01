# Fractional Knapsack using Greedy Method

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractionalKnapsack(W, arr):

    # Sort items according to value/weight ratio
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)

    total = 0.0

    for item in arr:

        if item.weight <= W:
            W -= item.weight
            total += item.value

        else:
            total += item.value * W / item.weight
            break

    return total


# Main Program

W = 50

arr = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]



max_val = fractionalKnapsack(W, arr)

print("Maximum profit:", max_val)
