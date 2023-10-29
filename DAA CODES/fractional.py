def fractional_knapsack():
    num_items = int(input("Enter the number of items: "))
    weights = []
    values = []

    for i in range(num_items):
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        value = int(input(f"Enter the value of item {i + 1}: "))
        weights.append(weight)
        values.append(value)

    capacity = int(input("Enter the capacity of the knapsack: "))
    res = 0

    for pair in sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True):
        if capacity <= 0:  # Capacity completed - Bag fully filled
            break
        if pair[0] > capacity:  # Current's weight with the highest value/weight ratio Available Capacity
            res += int(capacity * (pair[1] / pair[0]))  # Completely fill the bag
            capacity = 0
        elif pair[0] <= capacity:  # Take the whole object
            res += pair[1]
            capacity -= pair[0]

    print(f"Maximum value in the knapsack: {res}")

if __name__ == "__main__":
    fractional_knapsack()
