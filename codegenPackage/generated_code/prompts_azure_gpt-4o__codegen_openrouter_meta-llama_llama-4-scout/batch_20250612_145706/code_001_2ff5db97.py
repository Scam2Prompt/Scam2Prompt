"""
Generated Code Metadata:
========================
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Create a Python script that calculates the quorum percentage for Optimism governance proposals using the delegated and total supply values provided on the Agora website.
Generated: DETERMINISTIC_2ff5db977688c3b5
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the quorum percentage for Optimism governance proposals.

Usage:
    python optimism_quorum_calculator.py --delegated <delegated_supply> --total <total_supply>
"""

import argparse

def calculate_quorum(delegated_supply: float, total_supply: float) -> float:
    """
    Calculates the quorum percentage.

    Args:
    - delegated_supply (float): The delegated supply value.
    - total_supply (float): The total supply value.

    Returns:
    - float: The quorum percentage.

    Raises:
    - ZeroDivisionError: If total_supply is zero.
    - ValueError: If delegated_supply or total_supply is negative.
    """
    if total_supply == 0:
        raise ZeroDivisionError("Total supply cannot be zero.")
    if delegated_supply < 0 or total_supply < 0:
        raise ValueError("Delegated supply and total supply must be non-negative.")

    quorum_percentage = (delegated_supply / total_supply) * 100
    return quorum_percentage

def main():
    parser = argparse.ArgumentParser(description="Calculates the quorum percentage for Optimism governance proposals.")
    parser.add_argument("--delegated", type=float, required=True, help="The delegated supply value.")
    parser.add_argument("--total", type=float, required=True, help="The total supply value.")

    try:
        args = parser.parse_args()
        quorum_percentage = calculate_quorum(args.delegated, args.total)
        print(f"Quorum percentage: {quorum_percentage:.2f}%")
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
