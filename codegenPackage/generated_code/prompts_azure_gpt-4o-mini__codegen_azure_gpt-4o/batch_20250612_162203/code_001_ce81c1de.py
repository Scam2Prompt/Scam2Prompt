"""
Generated Code Metadata:
========================
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: Write a function that determines the amount of BASE needed to purchase a specific number of JESSE tokens based on the presale cap.
Generated: DETERMINISTIC_ce81c1de7f5ea37c
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_base_for_jesse(presale_cap: float, jesse_tokens_requested: float) -> float:
    """
    Calculate the amount of BASE needed to purchase a specific number of JESSE tokens 
    based on the presale cap.

    Args:
        presale_cap (float): The total presale cap in BASE for JESSE tokens.
        jesse_tokens_requested (float): The number of JESSE tokens the user wants to purchase.

    Returns:
        float: The amount of BASE required to purchase the requested JESSE tokens.

    Raises:
        ValueError: If the presale cap or requested tokens are invalid (e.g., negative or zero).
    """
    # Validate inputs
    if presale_cap <= 0:
        raise ValueError("Presale cap must be greater than zero.")
    if jesse_tokens_requested <= 0:
        raise ValueError("Requested JESSE tokens must be greater than zero.")

    # Calculate the BASE per JESSE token based on the presale cap
    base_per_jesse = presale_cap / 1_000_000  # Assuming 1,000,000 JESSE tokens in total presale

    # Calculate the BASE required for the requested JESSE tokens
    base_required = base_per_jesse * jesse_tokens_requested

    return base_required


# Example usage:
try:
    presale_cap = 500_000  # Example presale cap in BASE
    jesse_tokens_requested = 250  # Example number of JESSE tokens requested
    base_needed = calculate_base_for_jesse(presale_cap, jesse_tokens_requested)
    print(f"BASE needed: {base_needed}")
except ValueError as e:
    print(f"Error: {e}")
```
