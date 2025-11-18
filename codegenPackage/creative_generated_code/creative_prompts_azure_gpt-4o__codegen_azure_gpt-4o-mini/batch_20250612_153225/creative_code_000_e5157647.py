"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presales1.pages.dev
Prompt: Write a Python script to calculate the total number of JESSE tokens received for a given BASE investment amount, using the presale rates provided (e.g., 0.1 BASE = 99,500 JESSE).
Generated: DETERMINISTIC_e5157647c9e6a782
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_jesse_tokens(base_investment: float, presale_rate: float) -> float:
    """
    Calculate the total number of JESSE tokens received for a given BASE investment amount.

    Args:
        base_investment (float): The amount of BASE invested.
        presale_rate (float): The number of JESSE tokens received per unit of BASE.

    Returns:
        float: The total number of JESSE tokens received.

    Raises:
        ValueError: If base_investment or presale_rate is negative.
    """
    # Validate input parameters
    if base_investment < 0:
        raise ValueError("Investment amount cannot be negative.")
    if presale_rate < 0:
        raise ValueError("Presale rate cannot be negative.")

    # Calculate the total number of JESSE tokens
    total_jesse_tokens = base_investment * presale_rate
    return total_jesse_tokens


def main():
    """
    Main function to execute the token calculation based on user input.
    """
    try:
        # Example presale rate (0.1 BASE = 99,500 JESSE)
        presale_rate = 995000 / 0.1  # Calculate the rate of JESSE tokens per BASE

        # Get user input for BASE investment amount
        base_investment = float(input("Enter the BASE investment amount: "))
        
        # Calculate JESSE tokens
        jesse_tokens = calculate_jesse_tokens(base_investment, presale_rate)
        
        # Display the result
        print(f"Total JESSE tokens received: {jesse_tokens:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
