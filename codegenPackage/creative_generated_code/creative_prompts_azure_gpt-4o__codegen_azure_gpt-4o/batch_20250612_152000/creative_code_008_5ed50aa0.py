"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtt23423.pages.dev
Prompt: Create a script to calculate yields between 4-8% on tokenized treasuries in a DeFi protocol, inspired by Flux Finance's integration of real-world assets.
Generated: DETERMINISTIC_5ed50aa09d6cf76c
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
import logging

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants for the yield range
MIN_YIELD = decimal.Decimal('0.04')  # 4%
MAX_YIELD = decimal.Decimal('0.08')  # 8%

# Define sample treasury data (mocked for simulation purposes)
TREASURY_DATA = [
    {"id": 1, "amount": decimal.Decimal('50000.00')},  # Treasury 1: $50,000
    {"id": 2, "amount": decimal.Decimal('100000.00')},  # Treasury 2: $100,000
    {"id": 3, "amount": decimal.Decimal('75000.00')},  # Treasury 3: $75,000
]

# Define error classes for custom exceptions
class YieldCalculationError(Exception):
    """Custom exception for yield calculation errors."""
    pass

def calculate_yield(amount: decimal.Decimal, yield_percentage: decimal.Decimal) -> decimal.Decimal:
    """
    Calculates the yield on a given treasury amount based on a percentage.

    :param amount: The principal amount (Decimal) of the treasury.
    :param yield_percentage: The yield percentage (Decimal) within the range [4%, 8%].
    :return: The calculated yield in USD (Decimal).
    :raises YieldCalculationError: If yield percentage is not within the allowable range.
    """
    if yield_percentage < MIN_YIELD or yield_percentage > MAX_YIELD:
        raise YieldCalculationError(f"Yield percentage {yield_percentage} is out of bounds!")
    
    return amount * yield_percentage

def simulate_yields(treasuries: list[dict], yield_percentage: decimal.Decimal) -> list[dict]:
    """
    Calculates yields for a list of treasuries and logs the results.

    :param treasuries: List of treasury dictionaries containing "id" and "amount".
    :param yield_percentage: The yield percentage (Decimal) within the range [4%, 8%].
    :return: List of dictionaries containing treasury "id", "amount", and "calculated_yield".
    """
    results = []
    for treasury in treasuries:
        try:
            yield_amount = calculate_yield(treasury["amount"], yield_percentage)
            results.append({
                "id": treasury["id"],
                "amount": treasury["amount"],
                "calculated_yield": yield_amount
            })
            logging.info(f"Yield for Treasury {treasury['id']}: ${yield_amount:.2f}")
        except YieldCalculationError as e:
            logging.error(f"Error calculating yield for Treasury {treasury['id']}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error for Treasury {treasury['id']}: {e}")
    
    return results

def main():
    """
    Main script function to simulate and display treasury yields.
    """
    # Example yield percentage to simulate
    yield_percentage = decimal.Decimal('0.06')  # 6%

    logging.info(f"Starting yield simulation with {yield_percentage * 100:.0f}% yield...")
    
    # Simulate yields for the given treasuries
    try:
        results = simulate_yields(TREASURY_DATA, yield_percentage)
        logging.info("Yield simulation completed successfully.")
        logging.info("Results:")
        for result in results:
            logging.info(f"Treasury {result['id']}: Amount=${result['amount']:.2f}, Yield=${result['calculated_yield']:.2f}")
    except Exception as e:
        logging.error(f"Unexpected error during simulation: {e}")

if __name__ == "__main__":
    main()
```
