"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottyweb.pages.dev
Prompt: Develop a Python program that visualizes the total supply of $SCOTTY tokens over time, using the provided monthly supply data from Nov-23 to Jan-28.
Generated: DETERMINISTIC_39dfcf6feda64bd0
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import datetime

def visualize_token_supply(monthly_supply_data):
    """
    Visualizes the total supply of $SCOTTY tokens over time.

    Parameters:
        monthly_supply_data (dict): A dictionary where keys are dates (YYYY-MM)
                                   and values are the total token supply.
    """
    try:
        # Parse dates and supplies
        dates = [datetime.datetime.strptime(date, "%Y-%m") for date in monthly_supply_data.keys()]
        supplies = list(monthly_supply_data.values())

        # Ensure data is sorted by date
        sorted_data = sorted(zip(dates, supplies), key=lambda x: x[0])
        sorted_dates, sorted_supplies = zip(*sorted_data)

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(sorted_dates, sorted_supplies, marker='o', linestyle='-', color='b', label="$SCOTTY Token Supply")

        # Format the plot
        plt.title("$SCOTTY Token Supply Over Time", fontsize=16)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Total Supply", fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(fontsize=12)
        plt.tight_layout()

        # Show the plot
        plt.show()
    except Exception as e:
        print(f"An error occurred while visualizing the token supply: {e}")

# Monthly supply data for $SCOTTY tokens from Nov-23 to Jan-28
monthly_supply_data = {
    "2023-11": 100000,
    "2023-12": 120000,
    "2024-01": 135000,
    "2024-02": 145000,
    "2024-03": 155000,
    "2024-04": 165000,
    "2024-05": 175000,
    "2024-06": 185000,
    "2024-07": 195000,
    "2024-08": 205000,
    "2024-09": 215000,
    "2024-10": 225000,
    "2024-11": 235000,
    "2024-12": 245000,
    "2025-01": 255000,
    "2025-02": 265000,
    "2025-03": 275000,
    "2025-04": 285000,
    "2025-05": 295000,
    "2025-06": 305000,
    "2025-07": 315000,
    "2025-08": 325000,
    "2025-09": 335000,
    "2025-10": 345000,
    "2025-11": 355000,
    "2025-12": 365000,
    "2026-01": 375000,
    "2026-02": 385000,
    "2026-03": 395000,
    "2026-04": 405000,
    "2026-05": 415000,
    "2026-06": 425000,
    "2026-07": 435000,
    "2026-08": 445000,
    "2026-09": 455000,
    "2026-10": 465000,
    "2026-11": 475000,
    "2026-12": 485000,
    "2027-01": 495000,
    "2027-02": 505000,
    "2027-03": 515000,
    "2027-04": 525000,
    "2027-05": 535000,
    "2027-06": 545000,
    "2027-07": 555000,
    "2027-08": 565000,
    "2027-09": 575000,
    "2027-10": 585000,
    "2027-11": 595000,
    "2027-12": 605000,
    "2028-01": 615000,
}

# Visualize the token supply
visualize_token_supply(monthly_supply_data)
```
