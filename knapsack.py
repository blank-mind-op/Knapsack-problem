import matplotlib.pyplot as plt
import numpy as np

def plot_knapsack(weights, values, capacity):
    n = len(weights)

    # Initialize a matrix to store optimal solution values
    z = np.zeros((n + 1, capacity + 1))
    A = np.zeros((n + 1, capacity + 1))

    # Dynamic programming
    for j in range(1, n + 1):
        for d in range(1, capacity + 1):
            if weights[j - 1] <= d:
                if z[j - 1, d] < z[j - 1, d - weights[j - 1]] + values[j - 1]:
                    z[j, d] = z[j - 1, d - weights[j - 1]] + values[j - 1]
                    A[j, d] = 1
                else:
                    z[j, d] = z[j - 1, d]
                    A[j, d] = 0
            else:
                z[j, d] = z[j - 1, d]
                A[j, d] = 0

    # Plotting the dynamic programming table
    fig, ax = plt.subplots()
    cax = ax.matshow(z, cmap='Blues')
    plt.title('0/1 Knapsack Dynamic Programming Table')
    plt.xlabel('Capacity')
    plt.ylabel('Item Index')

    # Highlight the optimal subset
    selected_items = []
    j, d = n, capacity
    while j > 0 and d > 0:
        if A[j, d] == 1:
            selected_items.append(j)
            d -= weights[j - 1]
        j -= 1

    # Mark the optimal subset with a different color
    for i in range(1, n + 1):
        if i in selected_items:
            ax.add_patch(plt.Rectangle((i - 1, 0), 1, capacity + 1, fill=False, edgecolor='red'))

    plt.xticks(np.arange(n + 1), [''] + list(range(1, n + 1)))
    plt.yticks(np.arange(capacity + 1))
    plt.colorbar(cax)
    plt.show()

# Example usage
weights = [4, 2, 6, 4]
values = [12, 10, 20, 15]
capacity = 5

plot_knapsack(weights, values, capacity)
