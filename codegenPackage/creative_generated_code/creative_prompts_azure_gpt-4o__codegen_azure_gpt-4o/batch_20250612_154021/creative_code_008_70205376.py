"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saterdex.com
Prompt: Write a program to calculate potential earnings from staking BNB, USDT, BTC, and CAKE on Aster, factoring in APY rates and compounding rewards over time.
Generated: DETERMINISTIC_7020537617a677f0
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_staking_earnings(principal, apy, duration_years, compounding_frequency):
    """
    Calculate potential earnings from staking with compound interest.

    Parameters:
        principal (float): Initial amount staked.
        apy (float): Annual Percentage Yield (as a percentage, e.g., 5 for 5%).
        duration_years (float): Duration of staking in years.
        compounding_frequency (int): Number of times rewards are compounded per year.

    Returns:
        float: Total earnings after staking duration (principal + interest).
    """
    try:
        # Convert APY to a fraction
        rate = apy / 100
        
        # Compound interest formula: A = P * (1 + r/n)^(n*t)
        total = principal * math.pow(1 + rate / compounding_frequency, compounding_frequency * duration_years)
        
        return total
    except Exception as e:
        print(f"An error occurred while calculating earnings: {e}")
        return None


def main():
    """
    Main function to calculate staking earnings for various cryptocurrencies.
    """
    try:
        print("Calculate Staking Earnings on Aster\n")

        # Define staking parameters for each cryptocurrency
        staking_data = [
            {"name": "BNB", "principal": 1000, "apy": 10.2, "duration_years": 1, "compounding_frequency": 12},
            {"name": "USDT", "principal": 5000, "apy": 8.5, "duration_years": 1, "compounding_frequency": 12},
            {"name": "BTC", "principal": 0.1, "apy": 5.0, "duration_years": 2, "compounding_frequency": 12},
            {"name": "CAKE", "principal": 200, "apy": 75.0, "duration_years": 2, "compounding_frequency": 52},
        ]

        # Iterate through each staking configuration and calculate earnings
        for data in staking_data:
            total_earnings = calculate_staking_earnings(
                principal=data["principal"],
                apy=data["apy"],
                duration_years=data["duration_years"],
                compounding_frequency=data["compounding_frequency"]
            )

            if total_earnings is not None:
                earned_interest = total_earnings - data["principal"]
                print(
                    f"{data['name']} Staking:\n"
                    f"  Principal: {data['principal']}\n"
                    f"  APY: {data['apy']}%\n"
                    f"  Duration: {data['duration_years']} years\n"
                    f"  Total Earnings: {total_earnings:.2f}\n"
                    f"  Interest Earned: {earned_interest:.2f}\n"
                )
            print("-" * 40)

    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
```
