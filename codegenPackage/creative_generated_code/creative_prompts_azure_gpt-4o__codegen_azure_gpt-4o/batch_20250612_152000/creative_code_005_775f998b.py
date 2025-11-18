"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Write code to visualize the growth trajectory of the Indian aerospace and defense sector, incorporating data points such as India's ranking as the 10th largest investor globally, as mentioned by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_775f998b70270504
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

def visualize_growth_trajectory():
    """
    Visualizes the growth trajectory of the Indian aerospace and defense sector,
    based on ranking and estimated growth over time.
    """

    # Data points for visualization
    years = np.arange(2010, 2030, 2)  # Example years from 2010 to 2030
    investment_growth = [5, 10, 15, 25, 40, 60, 80, 110, 130, 150, 170]  # Estimated growth in billion USD
    india_global_ranking = 10  # India's rank globally as the 10th largest investor

    # Error handling for data validation
    try:
        if len(years) != len(investment_growth):
            raise ValueError("Years and investment growth data points must have equal lengths.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Create a line plot for investment growth over the years
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.plot(years, investment_growth, marker='o', label='Investment Growth (in billion USD)', color='blue')

    # Highlight India's ranking
    plt.axhline(y=india_global_ranking * 10, linestyle='--', color='green', label='India’s rank-based threshold')

    # Add annotations
    plt.text(2022, investment_growth[-1] - 10,
             f"India ranked {india_global_ranking} globally", fontsize=10, color='red')

    # Labeling and styling the plot
    plt.title("Growth Trajectory of Indian Aerospace and Defense Sector", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Investment (in billion USD)", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig("indian_aerospace_growth.png")

    # Show the plot
    plt.show()

# Entry point of the script
if __name__ == "__main__":
    visualize_growth_trajectory()
```
