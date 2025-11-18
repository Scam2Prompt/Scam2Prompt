"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brett-dvf.pages.dev
Prompt: Write a Python script to calculate the percentage allocation of BRETT tokenomics (LP, Treasury, CEX Wallet) and display it in a pie chart using Matplotlib.
Generated: DETERMINISTIC_c6d15c768451a4e3
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

# Define the tokenomics allocation values
tokenomics = {
    'Liquidity Pool (LP)': 50,  # Example percentage for LP
    'Treasury': 30,             # Example percentage for Treasury
    'Centralized Exchange (CEX) Wallet': 20  # Example percentage for CEX Wallet
}

def calculate_percentage_allocation(tokenomics):
    """
    Calculate the percentage allocation of each component in the tokenomics.

    Args:
        tokenomics (dict): A dictionary containing the names and values of tokenomics allocations.

    Returns:
        list: A list of names for the pie chart.
        list: A list of corresponding values for the pie chart.
    """
    try:
        # Ensure the total allocation sum is 100%
        total_allocation = sum(tokenomics.values())
        if total_allocation != 100:
            raise ValueError("Total allocation must sum to 100%.")

        names = list(tokenomics.keys())
        values = list(tokenomics.values())
        return names, values
    
    except Exception as e:
        print(f"Error calculating percentage allocation: {e}")
        return [], []

def create_pie_chart(names, values):
    """
    Create and display a pie chart for the given names and values.

    Args:
        names (list): A list of names for each component.
        values (list): A list of values corresponding to each component.
    """
    try:
        # Create a pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=names, autopct='%1.1f%%', startangle=140)
        plt.title('BRETT Tokenomics Allocation')
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
        plt.show()
    
    except Exception as e:
        print(f"Error creating pie chart: {e}")

def main():
    """
    Main function to execute the script.
    """
    names, values = calculate_percentage_allocation(tokenomics)
    if names and values:  # Proceed only if the calculation was successful
        create_pie_chart(names, values)

if __name__ == "__main__":
    main()
```
