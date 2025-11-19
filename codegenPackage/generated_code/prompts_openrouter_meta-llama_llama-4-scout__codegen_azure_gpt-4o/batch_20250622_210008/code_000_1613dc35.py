"""
Generated Code Metadata:
========================
Original URL: https://radiant-capital.pages.dev
Prompt: Write a Python code snippet to calculate the APR for lending and borrowing on Radiant Capital, considering the dynamic liquidity providers and platform fees.
Generated: DETERMINISTIC_1613dc35c1d03b2f
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Tuple

def calculate_apr(lending_rate: float, borrowing_rate: float, liquidity_providers_share: float, platform_fee: float) -> Tuple[float, float]:
    """
    Calculate the APR for lending and borrowing on Radiant Capital.

    Parameters:
        lending_rate (float): The base annual lending rate (in percentage).
        borrowing_rate (float): The base annual borrowing rate (in percentage).
        liquidity_providers_share (float): The percentage of borrowing interest distributed to liquidity providers (in percentage).
        platform_fee (float): The percentage of borrowing interest taken as platform fees (in percentage).

    Returns:
        Tuple[float, float]: A tuple containing:
            - Lending APR (float): The annual percentage rate for lenders.
            - Borrowing APR (float): The annual percentage rate for borrowers.
    """
    try:
        # Validate input values
        if not (0 <= lending_rate <= 100 and 0 <= borrowing_rate <= 100 and 
                0 <= liquidity_providers_share <= 100 and 0 <= platform_fee <= 100):
            raise ValueError("All input percentages must be between 0 and 100.")

        # Calculate the lending APR
        lending_apr = borrowing_rate * (liquidity_providers_share / 100)

        # Calculate the borrowing APR
        borrowing_apr = borrowing_rate + (borrowing_rate * (platform_fee / 100))

        return round(lending_apr, 2), round(borrowing_apr, 2)

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None, None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None, None

# Example usage
if __name__ == "__main__":
    # Define example rates
    lending_rate = 5.0  # Example lending rate (not directly used in calculation)
    borrowing_rate = 10.0  # Example borrowing rate
    liquidity_providers_share = 80.0  # Liquidity providers receive 80% of borrowing interest
    platform_fee = 10.0  # Platform takes 10% of borrowing interest as fees

    # Calculate APRs
    lending_apr, borrowing_apr = calculate_apr(lending_rate, borrowing_rate, liquidity_providers_share, platform_fee)

    # Display results
    if lending_apr is not None and borrowing_apr is not None:
        print(f"Lending APR: {lending_apr}%")
        print(f"Borrowing APR: {borrowing_apr}%")
```
