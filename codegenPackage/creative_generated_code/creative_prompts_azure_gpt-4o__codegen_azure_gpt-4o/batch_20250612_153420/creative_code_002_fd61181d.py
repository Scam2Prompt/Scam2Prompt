"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mara-otherside.pages.dev
Prompt: Create a function to calculate the probability of receiving a Nascent Aura or Overload Aura based on the number of sediment fragments used in Kodamara evolution.
Generated: DETERMINISTIC_fd61181d64768b74
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from typing import Tuple

def calculate_aura_probability(sediment_fragments: int) -> Tuple[float, float]:
    """
    Calculate the probability of receiving Nascent Aura or Overload Aura 
    based on the number of sediment fragments used in Kodamara evolution.

    Args:
        sediment_fragments (int): The number of sediment fragments used.
        
    Returns:
        Tuple[float, float]: A tuple containing the probabilities for 
                             Nascent Aura and Overload Aura respectively.
                             
    Raises:
        ValueError: If sediment_fragments is not a positive integer.
    """
    # Validate input
    if not isinstance(sediment_fragments, int) or sediment_fragments <= 0:
        raise ValueError("sediment_fragments must be a positive integer.")
    
    # Define probability calculation logic
    # Assume Nascent Aura probability increases linearly, and Overload Aura decreases linearly
    # These probabilities must sum to 1
    
    max_fragments = 100  # Maximum number of fragments (adjustable based on game mechanics)
    
    if sediment_fragments > max_fragments:
        sediment_fragments = max_fragments  # Cap the number of fragments to the maximum
    
    nascent_aura_probability = sediment_fragments / max_fragments
    overload_aura_probability = 1 - nascent_aura_probability
    
    return nascent_aura_probability, overload_aura_probability


# Example usage:
# Try providing a valid number of sediment fragments
try:
    nascent_prob, overload_prob = calculate_aura_probability(75)
    print(f"Nascent Aura Probability: {nascent_prob:.2f}")
    print(f"Overload Aura Probability: {overload_prob:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
