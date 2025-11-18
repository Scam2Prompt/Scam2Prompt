"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain-app.pages.dev
Prompt: Develop a script to calculate the environmental impact reduction of PulseChain's proof-of-stake validators compared to Ethereum's proof-of-work miners.
Generated: DETERMINISTIC_560091ab9b27beaf
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_impact_reduction(pulsechain_emission, ethereum_emission):
    """
    Calculate the environmental impact reduction based on emissions.

    Parameters:
        pulsechain_emission (float): CO2 emission in metric tons for PulseChain (Proof-of-Stake).
        ethereum_emission (float): CO2 emission in metric tons for Ethereum (Proof-of-Work).

    Returns:
        dict: A dictionary containing absolute reduction and percentage reduction.
    """
    # Ensure valid input values
    if pulsechain_emission < 0 or ethereum_emission < 0:
        raise ValueError("Emissions must be non-negative values.")

    if pulsechain_emission > ethereum_emission:
        raise ValueError("PulseChain emission should be lower than Ethereum for meaningful reduction.")

    # Calculate absolute reduction
    absolute_reduction = ethereum_emission - pulsechain_emission

    # Calculate percentage reduction
    percentage_reduction = (absolute_reduction / ethereum_emission) * 100

    return {
        "absolute_reduction": absolute_reduction,
        "percentage_reduction": percentage_reduction
    }


def main():
    """
    Main function to calculate the environmental impact reduction.
    """
    try:
        # Mock values for demonstration purposes; replace with actual data for production.
        ethereum_emission = float(input("Enter Ethereum's annual CO2 emission (metric tons): "))
        pulsechain_emission = float(input("Enter PulseChain's annual CO2 emission (metric tons): "))

        result = calculate_impact_reduction(pulsechain_emission, ethereum_emission)

        print(f"\nEnvironmental Impact Reduction:")
        print(f"Absolute Reduction: {result['absolute_reduction']:.2f} metric tons of CO2")
        print(f"Percentage Reduction: {result['percentage_reduction']:.2f}%")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
