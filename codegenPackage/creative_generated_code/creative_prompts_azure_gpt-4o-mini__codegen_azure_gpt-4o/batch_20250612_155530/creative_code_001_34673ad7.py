"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitmixer.technology
Prompt: Write a Python script that calculates the service fee for mixing Bitcoin using Bitmixer, including the percentage distribution and time delay options.
Generated: DETERMINISTIC_34673ad7d24b7dc7
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_service_fee(amount, base_fee_percentage, distribution_percentages, time_delay_percent):
    """
    Calculate the total service fee for using a Bitcoin mixing service.

    Parameters:
    - amount (float): The amount of Bitcoin being mixed.
    - base_fee_percentage (float): Base fee percentage charged by the mixer.
    - distribution_percentages (list of floats): Percentages for distribution across multiple addresses.
    - time_delay_percent (float): Additional fee percentage based on time delay.

    Returns:
    - dict: A dictionary containing detailed fee calculations.
    """
    try:
        # Ensure input validation
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if base_fee_percentage < 0 or not all(0 <= p <= 100 for p in distribution_percentages) or time_delay_percent < 0:
            raise ValueError("Fee percentages must be within the valid range (0-100).")
        if sum(distribution_percentages) != 100:
            raise ValueError("Distribution percentages must sum to 100.")

        # Base service fee
        base_fee = (base_fee_percentage / 100) * amount

        # Distribution service fee calculation
        distribution_fees = [
            (percentage / 100) * base_fee for percentage in distribution_percentages
        ]

        # Time delay additional fee
        time_delay_fee = (time_delay_percent / 100) * base_fee

        # Total fee
        total_fee = base_fee + time_delay_fee

        return {
            "base_fee": base_fee,
            "distribution_fees": distribution_fees,
            "time_delay_fee": time_delay_fee,
            "total_fee": total_fee,
        }

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def display_fee_breakdown(fee_breakdown):
    """
    Display a formatted breakdown of the calculated fees.

    Parameters:
    - fee_breakdown (dict): Dictionary containing fee details.
    """
    if fee_breakdown:
        print(f"Base Fee: {fee_breakdown['base_fee']:.8f} BTC")
        for i, fee in enumerate(fee_breakdown['distribution_fees']):
            print(f"Distribution Fee {i + 1}: {fee:.8f} BTC")
        print(f"Time Delay Fee: {fee_breakdown['time_delay_fee']:.8f} BTC")
        print(f"Total Fee: {fee_breakdown['total_fee']:.8f} BTC")
    else:
        print("No fee breakdown available due to an error.")

# Example usage
if __name__ == "__main__":
    try:
        # Input parameters
        amount = float(input("Enter the amount of Bitcoin to mix: "))
        base_fee_percentage = float(input("Enter the base fee percentage: "))
        num_addresses = int(input("Enter the number of distribution addresses: "))
        distribution_percentages = []

        # Get distribution percentages for each address
        for i in range(num_addresses):
            percentage = float(input(f"Enter the percentage for address {i + 1}: "))
            distribution_percentages.append(percentage)

        time_delay_percent = float(input("Enter the time delay fee percentage: "))

        # Calculate fees
        fee_breakdown = calculate_service_fee(
            amount, base_fee_percentage, distribution_percentages, time_delay_percent
        )

        # Display the results
        display_fee_breakdown(fee_breakdown)

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
```
