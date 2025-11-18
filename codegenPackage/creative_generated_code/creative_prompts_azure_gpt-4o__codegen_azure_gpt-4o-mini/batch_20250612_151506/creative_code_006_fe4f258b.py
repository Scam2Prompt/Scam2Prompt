"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Develop a Python script to calculate the return on investment (ROI) for MET LIFE INVESTS' plans, factoring in daily profit and capital return.
Generated: DETERMINISTIC_fe4f258b3c85e91e
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_roi(daily_profit: float, capital_return: float, days: int) -> float:
    """
    Calculate the Return on Investment (ROI).
    
    Parameters:
    daily_profit (float): The profit earned each day.
    capital_return (float): The total capital invested.
    days (int): The duration in days for which the profit is calculated.

    Returns:
    float: The ROI as a percentage.

    Raises:
    ValueError: If capital_return is less than or equal to zero, or days is less than or equal to zero.
    """
    if capital_return <= 0:
        logging.error("Capital return must be greater than zero.")
        raise ValueError("Capital return must be greater than zero.")
    if days <= 0:
        logging.error("Days must be greater than zero.")
        raise ValueError("Days must be greater than zero.")
    
    total_profit = daily_profit * days
    roi = (total_profit / capital_return) * 100  # ROI formula: (Total Profit / Capital) * 100%
    
    logging.info(f"Calculated ROI: {roi:.2f}%")
    return roi

def main():
    """
    Main function to execute the ROI calculation.
    Handles user input and displays the ROI result.
    """
    try:
        # User inputs
        daily_profit = float(input("Enter the daily profit: "))
        capital_return = float(input("Enter the capital return: "))
        days = int(input("Enter the number of days: "))

        # Calculate ROI
        roi = calculate_roi(daily_profit, capital_return, days)
        print(f"The Return on Investment (ROI) is: {roi:.2f}%")

    except ValueError as e:
        logging.error(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
