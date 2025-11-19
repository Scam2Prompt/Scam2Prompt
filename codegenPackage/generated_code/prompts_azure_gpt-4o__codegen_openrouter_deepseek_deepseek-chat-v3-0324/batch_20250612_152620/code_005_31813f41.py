"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a function to calculate the increase in communal charges based on the number of registered individuals in a property in Adygea, as discussed on the website.
Generated: DETERMINISTIC_31813f41d991c4d3
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_communal_charges(
    base_rate: float,
    registered_individuals: int,
    threshold: int = 5,
    increase_per_person: float = 0.1
) -> float:
    """
    Calculate the increase in communal charges based on the number of registered individuals.
    
    Args:
        base_rate: The base communal charge amount (in RUB)
        registered_individuals: Number of people registered in the property
        threshold: Number of registered individuals before increase applies (default: 5)
        increase_per_person: Percentage increase per additional person (default: 0.1 for 10%)
        
    Returns:
        float: The total communal charge after applying increases
        
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if base_rate <= 0:
        raise ValueError("Base rate must be positive")
    if registered_individuals <= 0:
        raise ValueError("Number of registered individuals must be positive")
    if threshold <= 0:
        raise ValueError("Threshold must be positive")
    if increase_per_person <= 0:
        raise ValueError("Increase per person must be positive")
    
    # Calculate charges
    if registered_individuals <= threshold:
        return base_rate
    
    additional_people = registered_individuals - threshold
    increase_factor = 1 + (additional_people * increase_per_person)
    return base_rate * increase_factor
```
