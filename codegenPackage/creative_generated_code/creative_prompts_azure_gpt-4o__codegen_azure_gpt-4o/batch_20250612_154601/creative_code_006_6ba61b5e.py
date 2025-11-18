"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterdigitalasset.com
Prompt: Develop a Python program that calculates the impact of Bitcoin scarcity on its long-term valuation, referencing its deflationary nature and capped supply of 21 million coins.
Generated: DETERMINISTIC_6ba61b5e0c867606
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_bitcoin_valuation(current_supply, annual_growth_rate, years, max_supply=21_000_000):
    """
    Calculate the long-term impact of Bitcoin scarcity on its valuation.

    Parameters:
    - current_supply (float): Current circulating supply of Bitcoin.
    - annual_growth_rate (float): Annual percentage growth in demand (as a decimal, e.g., 0.05 for 5%).
    - years (int): Number of years to project.
    - max_supply (float): Maximum Bitcoin supply (default is 21,000,000).

    Returns:
    - valuation (float): Projected valuation based on the scarcity model.
    """
    try:
        # Validate inputs
        if current_supply <= 0 or annual_growth_rate < 0 or years <= 0:
            raise ValueError("Invalid input values. All inputs must be positive.")

        if current_supply > max_supply:
            raise ValueError("Current supply cannot exceed max supply.")

        # Calculate the rate of scarcity
        scarcity = max_supply - current_supply

        # Apply compounding growth in demand
        projected_demand = current_supply * (1 + annual_growth_rate) ** years

        # Estimate valuation based on scarcity and projected demand
        # Using logarithmic valuation model with scarcity as a multiplier
        valuation = projected_demand * math.log(max_supply / scarcity)

        return valuation

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None
    except ZeroDivisionError:
        print("Scarcity calculation resulted in division by zero.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to execute the Bitcoin valuation model.
    """
    print("Bitcoin Scarcity Valuation Model\n")
    
    try:
        # Gather user inputs
        current_supply = float(input("Enter the current circulating supply of Bitcoin: "))
        annual_growth_rate = float(input("Enter annual demand growth rate (e.g., 0.05 for 5%): "))
        years = int(input("Enter the number of years for projection: "))

        # Calculate valuation
        valuation = calculate_bitcoin_valuation(current_supply, annual_growth_rate, years)

        if valuation is not None:
            print(f"\nProjected Bitcoin valuation after {years} years: ${valuation:,.2f}")
        else:
            print("\nUnable to calculate valuation due to input errors or unexpected issues.")

    except ValueError:
        print("Invalid input. Please use numbers for supply, growth rate, and years.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
