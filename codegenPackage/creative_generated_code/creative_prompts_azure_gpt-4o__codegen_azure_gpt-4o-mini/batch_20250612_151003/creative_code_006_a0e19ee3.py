"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clearpool.pages.dev
Prompt: Write a function to calculate the relative percentage of voting power for each Clearpool oracle based on their staking size.
Generated: DETERMINISTIC_a0e19ee36ee35a11
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_voting_power(oracles):
    """
    Calculates the relative percentage of voting power for each Clearpool oracle based on their staking size.

    Args:
        oracles (dict): A dictionary where keys are oracle names and values are their respective staking sizes.

    Returns:
        dict: A dictionary containing the relative voting power percentage for each oracle.
        
    Raises:
        ValueError: If the total staking size is zero to avoid division by zero.
    """
    if not isinstance(oracles, dict):
        raise TypeError("The input must be a dictionary.")

    total_staking_size = sum(oracles.values())

    if total_staking_size == 0:
        raise ValueError("Total staking size cannot be zero.")

    voting_power = {}
    
    for oracle, staking_size in oracles.items():
        # Calculate the voting power percentage for each oracle
        voting_power[oracle] = (staking_size / total_staking_size) * 100

    return voting_power

# Example usage
if __name__ == "__main__":
    try:
        oracles_data = {
            'Oracle A': 1500,
            'Oracle B': 3000,
            'Oracle C': 2500
        }

        voting_power_results = calculate_voting_power(oracles_data)
        print("Voting Power Percentages:")
        for oracle, percentage in voting_power_results.items():
            print(f"{oracle}: {percentage:.2f}%")
    except Exception as e:
        print(f"An error occurred: {e}")
```
