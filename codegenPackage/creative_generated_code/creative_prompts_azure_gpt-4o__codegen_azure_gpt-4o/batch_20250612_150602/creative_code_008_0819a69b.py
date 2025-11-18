"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Write code to calculate the percentage increase in FSC-certified wood purchases year-over-year, as highlighted by PDC Brush's environmental commitment.
Generated: DETERMINISTIC_0819a69b5daf9e5a
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def calculate_percentage_increase(data):
    """
    Calculate the year-over-year percentage increase for FSC-certified wood purchases.

    Parameters:
    data (pd.DataFrame): A pandas DataFrame with two columns:
                         - 'Year' (int): The year of the data.
                         - 'FSC_Purchases' (float): The FSC-certified wood purchases for that year.

    Returns:
    pd.DataFrame: A DataFrame with the original data plus a new column 'Percentage_Increase',
                  which contains the year-over-year percentage increase.
    """
    # Ensure data is sorted by year
    data = data.sort_values(by='Year')
    
    # Calculate the year-over-year percentage increase
    data['Percentage_Increase'] = data['FSC_Purchases'].pct_change() * 100
    
    return data


# Example usage
if __name__ == '__main__':
    # Example data for FSC-certified wood purchases
    data = {
        'Year': [2020, 2021, 2022],
        'FSC_Purchases': [100.0, 150.0, 200.0]  # Example values in cubic meters or equivalent
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    try:
        # Calculate percentage increase
        result = calculate_percentage_increase(df)

        # Print the result
        print("Year-over-Year Percentage Increase in FSC-certified Wood Purchases:")
        print(result)
    except Exception as e:
        # Handle any errors that occur
        print(f"An error occurred: {e}")
```

Above code assumes the input data is provided as a DataFrame, making it flexible for production use. Replace the `data` dictionary with your real data source for actual usage.
