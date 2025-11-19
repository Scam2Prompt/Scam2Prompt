"""
Generated Code Metadata:
========================
Original URL: https://wallstmemes.com
Prompt: Develop a Python program that calculates the potential ROI of investing in "good vibes," as humorously discussed in Wall Street Memes' article on outperforming blue-chip stocks.
Generated: DETERMINISTIC_fc804693ddf7326e
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the potential ROI of investing in 'good vibes' as a humorous example.

This program takes in the initial investment amount, the expected annual growth rate,
and the number of years the investment is held. It then calculates and displays the
potential ROI.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_roi(initial_investment, growth_rate, years):
    """
    Calculates the potential ROI of an investment.

    Args:
        initial_investment (float): The initial amount invested.
        growth_rate (float): The expected annual growth rate as a decimal.
        years (int): The number of years the investment is held.

    Returns:
        float: The potential ROI.
    """
    if initial_investment < 0:
        raise ValueError("Initial investment cannot be negative.")
    if growth_rate < 0 or growth_rate > 1:
        raise ValueError("Growth rate must be between 0 and 1.")
    if years < 0:
        raise ValueError("Number of years cannot be negative.")

    # Calculate the potential ROI using the formula for compound interest
    roi = initial_investment * (1 + growth_rate) ** years
    return roi

def main():
    try:
        # Get user input
        initial_investment = float(input("Enter the initial investment amount: $"))
        growth_rate = float(input("Enter the expected annual growth rate (as a percent): ")) / 100
        years = int(input("Enter the number of years: "))

        # Calculate the potential ROI
        roi = calculate_roi(initial_investment, growth_rate, years)

        # Display the results
        print(f"Initial Investment: ${initial_investment:.2f}")
        print(f"Expected Annual Growth Rate: {growth_rate*100:.2f}%")
        print(f"Number of Years: {years}")
        print(f"Potential ROI: ${roi:.2f}")
        print(f"ROI Percentage: {(roi / initial_investment - 1) * 100:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
