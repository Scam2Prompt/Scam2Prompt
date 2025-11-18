"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afranaden.org
Prompt: Develop a function to calculate the number of beneficiaries for food distribution campaigns, like the Ramadan food basket initiative mentioned on the Gulf and Aden website.
Generated: DETERMINISTIC_408939f1d0ea332f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_beneficiaries(total_population: int, percentage_needing_assistance: float) -> int:
    """
    Calculate the number of beneficiaries for food distribution campaigns.

    Parameters:
    total_population (int): The total number of people in the population.
    percentage_needing_assistance (float): The percentage of the population needing assistance (0-100).

    Returns:
    int: The estimated number of beneficiaries needing assistance.

    Raises:
    ValueError: If total_population is negative or if percentage_needing_assistance is not within the range [0, 100].
    """

    # Validate input parameters
    if total_population < 0:
        raise ValueError("Total population cannot be negative.")
    if not (0 <= percentage_needing_assistance <= 100):
        raise ValueError("Percentage needing assistance must be between 0 and 100.")

    # Calculate the number of beneficiaries
    beneficiaries = (total_population * percentage_needing_assistance) / 100

    # Return the number of beneficiaries as an integer
    return int(beneficiaries)

# Example usage
if __name__ == "__main__":
    try:
        # User-defined values for testing
        total_population = 10000  # Example total population
        percentage_needing_assistance = 25.0  # 25% of the population needs assistance

        # Calculate beneficiaries
        beneficiaries = calculate_beneficiaries(total_population, percentage_needing_assistance)
        print(f"Estimated number of beneficiaries: {beneficiaries}")

    except ValueError as e:
        print(f"Error: {e}")
```
