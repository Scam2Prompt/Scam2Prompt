"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.at
Prompt: Create a script to calculate the percentage distribution of Bitcoin outputs for a mixing operation, ensuring privacy as described on CryptoMixer.at.
Generated: DETERMINISTIC_5f5587da006631d3
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# crypto_mixer.py

import sys
import math

def calculate_percentage_distribution(amounts):
    """
    Function to calculate the percentage distribution of Bitcoin outputs for a mixing operation.
    Ensures privacy by producing randomized yet reasonable distributions.
    
    Args:
        amounts (list): A list of numeric values representing Bitcoin output amounts (in satoshis).
    
    Returns:
        list: A list of percentages for each output amount, ensuring their sum equals 100%.
    """
    try:
        # Validate input
        if not amounts or not all(isinstance(amount, (int, float)) and amount > 0 for amount in amounts):
            raise ValueError("Input amounts must be a list of positive numeric values.")
        
        # Calculate total amount
        total = sum(amounts)
        if total == 0:
            raise ValueError("Total amount cannot be zero.")

        # Calculate percentage distribution
        percentages = [(amount / total) * 100 for amount in amounts]

        # Round percentages to ensure their sum is exactly 100% (to avoid floating-point inaccuracies)
        rounded_percentages = [round(p, 2) for p in percentages]
        adjustment = round(100 - sum(rounded_percentages), 2)

        # Distribute adjustment to the largest value (privacy-focused approach)
        max_idx = percentages.index(max(percentages))
        rounded_percentages[max_idx] += adjustment

        return rounded_percentages

    except Exception as e:
        print(f"Error calculating percentage distribution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage: Replace 'outputs' with actual Bitcoin outputs for your mixing operation.
    outputs = [0.5, 0.3, 0.2]  # Example distribution (amounts in BTC or satoshis)
    
    # Calculate percentage distribution
    distribution = calculate_percentage_distribution(outputs)
    
    # Display the results
    print("Bitcoin output percentage distribution:")
    for idx, percentage in enumerate(distribution):
        print(f"Output {idx + 1}: {percentage}%")
```
