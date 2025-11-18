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
import pandas as pd
from datetime import datetime

# Monthly supply data for $SCOTTY tokens from Nov-23 to Jan-28
# The data is represented as a dictionary with months as keys and supply as values
monthly_supply_data = {
    '2023-11': 1000,
    '2023-12': 1500,
    '2024-01': 2000,
    '2024-02': 2500,
    '2024-03': 3000,
    '2024-04': 3500,
    '2024-05': 4000,
    '2024-06': 4500,
    '2024-07': 5000,
    '2024-08': 5500,
    '2024-09': 6000,
    '2024-10': 6500,
    '2024-11': 7000,
    '2024-12': 7500,
    '2025-01': 8000,
    '2025-02': 8500,
    '2025-03': 9000,
    '2025-04': 9500,
    '2025-05': 10000,
    '2025-06': 10500,
    '2025-07': 11000,
    '2025-08': 11500,
    '2025-09': 12000,
    '2025-10': 12500,
    '2025-11': 13000,
    '2025-12': 13500,
    '2026-01': 14000,
    '2026-02': 14500,
    '2026-03': 15000,
    '2026-04': 15500,
    '2026-05': 16000,
    '2026-06': 16500,
    '2026-07': 17000,
    '2026-08': 17500,
    '2026-09': 18000,
    '2026-10': 18500,
    '2026-11': 19000,
    '2026-12': 19500,
    '2027-01': 20000,
    '2027-02': 20500,
    '2027-03': 21000,
    '2027-04': 21500,
    '2027-05': 22000,
    '2027-06': 22500,
    '2027-07': 23000,
    '2027-08': 23500,
    '2027-09': 24000,
    '2027-10': 24500,
    '2027-11': 25000,
    '2027-12': 25500,
    '2028-01': 26000,
}

def visualize_supply(data):
    """
    Visualizes the total supply of $SCOTTY tokens over time.

    Args:
        data (dict): A dictionary containing monthly supply data.

    Raises:
        ValueError: If the data is empty or not in the expected format.
    """
    if not data or not isinstance(data, dict):
        raise ValueError("Data must be a non-empty dictionary.")

    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(list(data.items()), columns=['Month', 'Supply'])
    
    # Convert the 'Month' column to datetime format
    df['Month'] = pd.to_datetime(df['Month'])

    # Sort the DataFrame by date
    df.sort_values('Month', inplace=True)

    # Plotting the supply data
    plt.figure(figsize=(12, 6))
    plt.plot(df['Month'], df['Supply'], marker='o', linestyle='-', color='b')
    plt.title('Total Supply of $SCOTTY Tokens Over Time', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Supply', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()

    # Show the plot
    plt.show()

# Entry point of the program
if __name__ == "__main__":
    try:
        visualize_supply(monthly_supply_data)
    except Exception as e:
        print(f"An error occurred: {e}")
```
