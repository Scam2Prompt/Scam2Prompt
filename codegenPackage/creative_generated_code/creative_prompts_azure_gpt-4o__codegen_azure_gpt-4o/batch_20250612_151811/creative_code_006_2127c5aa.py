"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalhandelssystem.com
Prompt: Generate a script for automating daily profit distribution to investors based on their deposit amounts and selected investment plans, similar to the system used by Capitalhandelssystem.
Generated: DETERMINISTIC_2127c5aa6831ce30
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
DAILY_PROFIT_RATES = {
    "basic": 0.01,  # 1% daily profit
    "premium": 0.015,  # 1.5% daily profit
    "vip": 0.02  # 2% daily profit
}

# Simulated database
# Example structure: List of investors with their deposit amount and selected plan
INVESTORS_DB = [
    {"id": 1, "name": "Alice", "deposit": 1000, "plan": "basic", "last_profit_date": "2023-10-01"},
    {"id": 2, "name": "Bob", "deposit": 5000, "plan": "premium", "last_profit_date": "2023-10-01"},
    {"id": 3, "name": "Charlie", "deposit": 10000, "plan": "vip", "last_profit_date": "2023-10-01"},
]

# Function to calculate daily profit
def calculate_daily_profit(deposit, plan):
    """
    Calculate the daily profit for an investor based on their deposit and selected plan.

    Args:
        deposit (float): The deposit amount.
        plan (str): The selected investment plan.

    Returns:
        float: The calculated daily profit.
    """
    rate = DAILY_PROFIT_RATES.get(plan, 0)
    return deposit * rate

# Function to distribute profits
def distribute_profits():
    """
    Automates the daily profit distribution to all investors.
    Updates the database to reflect the last profit distribution date.
    """
    today = datetime.now().date()
    for investor in INVESTORS_DB:
        try:
            # Parse the last profit distribution date
            last_profit_date = datetime.strptime(investor["last_profit_date"], "%Y-%m-%d").date()
            
            # Ensure profits are distributed only once per day
            if last_profit_date >= today:
                logging.info(f"Investor {investor['name']} already received profit today. Skipping.")
                continue
            
            # Calculate profit
            daily_profit = calculate_daily_profit(investor["deposit"], investor["plan"])
            
            # Simulate profit distribution (e.g., update account balance)
            # For demonstration, we log the profit distribution
            logging.info(f"Distributed ${daily_profit:.2f} profit to {investor['name']} (Plan: {investor['plan']}).")

            # Update the last profit distribution date
            investor["last_profit_date"] = today.strftime("%Y-%m-%d")
        
        except Exception as e:
            logging.error(f"Error distributing profit to {investor['name']}: {e}")

# Simulated main function
if __name__ == "__main__":
    try:
        logging.info("Starting daily profit distribution script...")
        distribute_profits()
        logging.info("Profit distribution completed successfully.")
        
        # Optionally save updated database to a file (e.g., JSON)
        with open("investors_db.json", "w") as file:
            json.dump(INVESTORS_DB, file, indent=4)
            logging.info("Updated investor database saved to 'investors_db.json'.")
    
    except Exception as e:
        logging.error(f"Critical error in script execution: {e}")
```
