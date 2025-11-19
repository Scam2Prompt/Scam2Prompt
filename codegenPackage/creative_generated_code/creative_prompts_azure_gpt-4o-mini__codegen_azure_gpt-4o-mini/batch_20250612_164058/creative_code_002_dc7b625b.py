"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magplexyz.xyz
Prompt: Create a function that calculates the total cashback earned from trading on Bybit, using the data provided in the April and March 2025 reports from Ace Crypto.
Generated: DETERMINISTIC_dc7b625bce82597a
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def calculate_total_cashback(report_march, report_april):
    """
    Calculates the total cashback earned from trading on Bybit 
    using the provided trading reports from March and April 2025.

    Args:
        report_march (str): Path to the March 2025 report CSV file.
        report_april (str): Path to the April 2025 report CSV file.

    Returns:
        float: Total cashback earned from both reports.
    """
    
    try:
        # Load the trading reports into DataFrames
        df_march = pd.read_csv(report_march)
        df_april = pd.read_csv(report_april)

        # Check if the necessary columns exist in the reports
        if 'cashback' not in df_march.columns or 'cashback' not in df_april.columns:
            raise ValueError("The reports must contain a 'cashback' column.")

        # Calculate total cashback from both reports
        total_cashback_march = df_march['cashback'].sum()
        total_cashback_april = df_april['cashback'].sum()

        total_cashback = total_cashback_march + total_cashback_april

        return total_cashback

    except FileNotFoundError as e:
        print(f"Error: The file was not found. {e}")
        return 0.0
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return 0.0
    except ValueError as e:
        print(f"Error: {e}")
        return 0.0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0.0

# Example usage (commented out for production):
# total_cashback = calculate_total_cashback('march_report.csv', 'april_report.csv')
# print(f"Total Cashback Earned: ${total_cashback:.2f}")
```
