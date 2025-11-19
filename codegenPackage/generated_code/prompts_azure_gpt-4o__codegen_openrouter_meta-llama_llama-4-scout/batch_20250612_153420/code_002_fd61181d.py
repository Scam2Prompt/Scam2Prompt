"""
Generated Code Metadata:
========================
Original URL: https://mara-otherside.pages.dev
Prompt: Create a function to calculate the probability of receiving a Nascent Aura or Overload Aura based on the number of sediment fragments used in Kodamara evolution.
Generated: DETERMINISTIC_fd61181d64768b74
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_aura_probability(sediment_fragments: int) -> dict:
    """
    Calculate the probability of receiving a Nascent Aura or Overload Aura 
    based on the number of sediment fragments used in Kodamara evolution.

    Args:
        sediment_fragments (int): The number of sediment fragments used.

    Returns:
        dict: A dictionary containing the probabilities of Nascent Aura and Overload Aura.

    Raises:
        ValueError: If the number of sediment fragments is negative.
    """

    # Check if the number of sediment fragments is non-negative
    if sediment_fragments < 0:
        raise ValueError("The number of sediment fragments cannot be negative.")

    # Define the base probabilities
    # Assuming the base probabilities are 0.05 for Nascent Aura and 0.01 for Overload Aura
    base_nascent_probability = 0.05
    base_overload_probability = 0.01

    # Calculate the probability increase per sediment fragment
    # Assuming the probability increases by 0.001 for Nascent Aura and 0.0005 for Overload Aura per fragment
    nascent_probability_increase = 0.001
    overload_probability_increase = 0.0005

    # Calculate the probabilities
    nascent_probability = min(base_nascent_probability + (sediment_fragments * nascent_probability_increase), 1)
    overload_probability = min(base_overload_probability + (sediment_fragments * overload_probability_increase), 1)

    # Ensure the probabilities do not exceed 1
    if nascent_probability + overload_probability > 1:
        # Normalize the probabilities to ensure they add up to 1
        total_probability = nascent_probability + overload_probability
        nascent_probability = nascent_probability / total_probability
        overload_probability = overload_probability / total_probability

    return {
        "Nascent Aura": nascent_probability,
        "Overload Aura": overload_probability
    }

# Example usage:
def main():
    try:
        sediment_fragments = 10
        probabilities = calculate_aura_probability(sediment_fragments)
        print(f"Probabilities after using {sediment_fragments} sediment fragments:")
        for aura, probability in probabilities.items():
            print(f"{aura}: {probability:.4f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
