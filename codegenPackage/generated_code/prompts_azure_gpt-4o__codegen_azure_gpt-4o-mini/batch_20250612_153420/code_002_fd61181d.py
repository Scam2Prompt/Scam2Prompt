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

    Parameters:
    sediment_fragments (int): The number of sediment fragments used.

    Returns:
    dict: A dictionary containing the probabilities of Nascent Aura and Overload Aura.
    """
    
    # Validate input
    if not isinstance(sediment_fragments, int) or sediment_fragments < 0:
        raise ValueError("The number of sediment fragments must be a non-negative integer.")

    # Constants for probabilities (these values are hypothetical and should be adjusted as needed)
    nascent_aura_base_probability = 0.05  # Base probability for Nascent Aura
    overload_aura_base_probability = 0.03  # Base probability for Overload Aura

    # Calculate probabilities based on the number of fragments
    nascent_aura_probability = min(1.0, nascent_aura_base_probability * sediment_fragments)
    overload_aura_probability = min(1.0, overload_aura_base_probability * sediment_fragments)

    # Ensure total probability does not exceed 1
    total_probability = nascent_aura_probability + overload_aura_probability
    if total_probability > 1.0:
        nascent_aura_probability /= total_probability
        overload_aura_probability /= total_probability

    return {
        "Nascent Aura Probability": round(nascent_aura_probability, 4),
        "Overload Aura Probability": round(overload_aura_probability, 4)
    }

# Example usage
if __name__ == "__main__":
    try:
        fragments = 10  # Example number of sediment fragments
        probabilities = calculate_aura_probability(fragments)
        print(probabilities)
    except ValueError as e:
        print(f"Error: {e}")
```
