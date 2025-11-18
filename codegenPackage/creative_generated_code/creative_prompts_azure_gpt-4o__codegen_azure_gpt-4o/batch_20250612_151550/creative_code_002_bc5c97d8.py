"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Recommend a library or API for visualizing the leaderboard rankings in HV-MTL Forge and write a script to display the top 10 HVs.
Generated: DETERMINISTIC_bc5c97d8141166f6
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to display the top 10 HVs from leaderboard rankings in HV-MTL Forge.
This script uses the `matplotlib` library to visualize the rankings as a horizontal bar chart.

Requirements:
1. Install matplotlib: `pip install matplotlib`
2. Ensure you have access to the leaderboard data (API or local file).

Replace the `fetch_leaderboard_data` function with the appropriate API call or file reading logic.
"""

import matplotlib.pyplot as plt
import random


def fetch_leaderboard_data():
    """
    Mock function to fetch leaderboard data.
    Replace this with the actual API call or file reading logic.
    Returns a list of dictionaries containing HV names and their scores.
    """
    # Example data structure for leaderboard rankings
    # In real use, this would come from an API or database
    leaderboard = [
        {"name": f"HV-{i+1}", "score": random.randint(100, 1000)} for i in range(50)
    ]
    return sorted(leaderboard, key=lambda x: x["score"], reverse=True)


def visualize_top_10_hvs(leaderboard_data):
    """
    Visualize the top 10 HVs using a horizontal bar chart.

    Args:
        leaderboard_data (list): List of dictionaries containing HV names and scores.
    """
    # Extract the top 10 HVs
    top_10 = leaderboard_data[:10]

    # Prepare data for plotting
    hv_names = [hv["name"] for hv in top_10]
    hv_scores = [hv["score"] for hv in top_10]

    # Create a horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(hv_names, hv_scores, color='skyblue')
    plt.xlabel("Score")
    plt.ylabel("HV Name")
    plt.title("Top 10 HVs Leaderboard")
    plt.gca().invert_yaxis()  # Reverse the order for better visuals
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Display the chart
    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to orchestrate leaderboard data fetching and visualization.
    """
    try:
        # Fetch leaderboard data
        leaderboard_data = fetch_leaderboard_data()

        if not leaderboard_data:
            raise ValueError("Leaderboard data is empty or unavailable.")

        # Visualize the top 10 HVs
        visualize_top_10_hvs(leaderboard_data)

    except Exception as e:
        # Handle potential errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
