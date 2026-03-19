import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV file containing experiment results
df = pd.read_csv("results/quicksort_results.csv")


# Loop through each input type (Random, Sorted, Reverse, Repeated)
for dtype in df["Input Type"].unique():

    # Filter data for the current input type
    subset = df[df["Input Type"] == dtype]

    # Plot results for each algorithm (Deterministic vs Randomized)
    for algo in subset["Algorithm"].unique():

        # Further filter data for the current algorithm
        data = subset[subset["Algorithm"] == algo]

        # Plot input size vs execution time
        plt.plot(data["Size"], data["Time (seconds)"], label=algo)

    # Add title and labels for clarity
    plt.title(f"Quicksort Performance - {dtype} Input")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")

    # Show legend to differentiate algorithms
    plt.legend()

    # Save the graph as an image file in results folder
    plt.savefig(f"results/{dtype}_plot.png")

    # Clear the plot before the next iteration
    plt.clf()


print("Graphs generated successfully in the results folder.")