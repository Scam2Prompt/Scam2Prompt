"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presales1.pages.dev
Prompt: Write a function that determines the number of JESSE tokens received for different BASE contributions (e.g., 0.1 BASE, 25 BASE, 100 BASE).
Generated: DETERMINISTIC_0732361808b5cd1a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate the number of JESSE tokens received based on BASE contributions.

def calculate_jesse_tokens(base_contribution):
    """
    Calculate the number of JESSE tokens based on the amount of BASE contributed.
    
    Conversion rules:
    - 1 BASE = 100 JESSE tokens.
    - Minimum contribution is 0.1 BASE (10 JESSE tokens).
    
    Args:
        base_contribution (float): Amount of BASE contributed.
        
    Returns:
        float: Number of JESSE tokens awarded.
        
    Raises:
        ValueError: If the BASE contribution is less than the minimum allowed (0.1 BASE).
    """
    # Conversion rate.
    BASE_TO_JESSE_RATE = 100
    MIN_BASE_CONTRIBUTION = 0.1

    try:
        # Validate that the contribution is above the minimum allowed.
        if base_contribution < MIN_BASE_CONTRIBUTION:
            raise ValueError(f"Minimum contribution is {MIN_BASE_CONTRIBUTION} BASE. Provided: {base_contribution} BASE")

        # Calculate the JESSE tokens.
        jesse_tokens = base_contribution * BASE_TO_JESSE_RATE
        return jesse_tokens
    except ValueError as ve:
        # Handle invalid contribution amounts gracefully.
        print(f"Error: {ve}")
        return 0  # Return 0 tokens in case of error.

# Example usage:
if __name__ == "__main__":
    # Test cases for the function.
    contributions = [0.1, 25, 100, 0.05]  # List of BASE contributions to test.
    for contribution in contributions:
        tokens = calculate_jesse_tokens(contribution)
        print(f"BASE Contribution: {contribution} -> JESSE Tokens: {tokens}")
```
