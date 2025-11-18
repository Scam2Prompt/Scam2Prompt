"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Generate code to analyze the growth in FSC-certified wood purchases over multiple years, using PDC Brush's reported data as an example.
Generated: DETERMINISTIC_94fd52be1ae37ff7
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to analyze FSC-certified wood purchases growth
def analyze_growth(data):
    """
    Analyzes the growth of FSC-certified wood purchases over multiple years.
    
    Parameters:
    data (dict): Dictionary containing year as key and purchases as value.
                 Example: {'2020': 500, '2021': 750, '2022': 900}
    
    Returns:
    None
    """
    try:
        # Convert data dictionary to a Pandas DataFrame for analysis
        df = pd.DataFrame(list(data.items()), columns=["Year", "Purchases"])
        df["Year"] = pd.to_numeric(df["Year"])
        df["Purchases"] = pd.to_numeric(df["Purchases"])
        
        # Calculate annual growth rate
        df["Growth Rate (%)"] = df["Purchases"].pct_change() * 100
        
        # Print data and growth rate
        print("Yearly Data with Growth Rates:")
        print(df)
        
        # Plot purchases over years
        plt.figure(figsize=(10, 6))
        plt.plot(df["Year"], df["Purchases"], marker="o", label="Purchases")
        plt.title("FSC-Certified Wood Purchases Over Years")
        plt.xlabel("Year")
        plt.ylabel("Purchases")
        plt.grid(True)
        plt.legend()
        
        # Plot growth rates
        plt.twinx()  # Create a second y-axis for growth rates
        plt.plot(df["Year"], df["Growth Rate (%)"], marker="x", color="red", label="Growth Rate (%)")
        plt.ylabel("Growth Rate (%)")
        plt.legend(loc="upper left")
        
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with PDC Brush's reported data
growth_data = {
    '2020': 500,
    '2021': 750,
    '2022': 900,
    '2023': 1200
}

# Analyzing growth
analyze_growth(growth_data)
```
