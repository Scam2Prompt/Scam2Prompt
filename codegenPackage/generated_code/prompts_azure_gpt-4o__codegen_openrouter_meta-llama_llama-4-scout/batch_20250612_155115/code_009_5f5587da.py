"""
Generated Code Metadata:
========================
Original URL: https://cryptomixer.at
Prompt: Create a script to calculate the percentage distribution of Bitcoin outputs for a mixing operation, ensuring privacy as described on CryptoMixer.at.
Generated: DETERMINISTIC_5f5587da006631d3
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
from typing import List, Dict

def calculate_distribution(outputs: List[int], total_output: int) -> Dict[int, float]:
    """
    Calculate the percentage distribution of Bitcoin outputs.

    Args:
    - outputs (List[int]): A list of output values in satoshis.
    - total_output (int): The total output value in satoshis.

    Returns:
    - Dict[int, float]: A dictionary where keys are output values and values are their corresponding percentages.
    """
    distribution = {}
    for output in outputs:
        percentage = (output / total_output) * 100
        distribution[output] = round(percentage, 2)
    return distribution

def validate_inputs(outputs: List[int], total_output: int) -> None:
    """
    Validate the inputs to ensure they are valid for calculation.

    Args:
    - outputs (List[int]): A list of output values in satoshis.
    - total_output (int): The total output value in satoshis.

    Raises:
    - ValueError: If the total output is zero or negative, or if any output is negative.
    - TypeError: If the inputs are not of the correct type.
    """
    if not isinstance(outputs, list) or not all(isinstance(output, int) for output in outputs):
        raise TypeError("Outputs must be a list of integers.")
    if not isinstance(total_output, int):
        raise TypeError("Total output must be an integer.")
    if total_output <= 0:
        raise ValueError("Total output must be greater than zero.")
    if any(output < 0 for output in outputs):
        raise ValueError("Output values cannot be negative.")

def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate Bitcoin output distribution for a mixing operation.")
    parser.add_argument("-o", "--outputs", nargs="+", type=int, help="A list of output values in satoshis.")
    parser.add_argument("-t", "--total_output", type=int, help="The total output value in satoshis.")
    args = parser.parse_args()

    try:
        validate_inputs(args.outputs, args.total_output)
        distribution = calculate_distribution(args.outputs, args.total_output)
        print("Output Distribution:")
        for output, percentage in distribution.items():
            print(f"{output} satoshis: {percentage}%")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
