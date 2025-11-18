"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-gpu.pages.dev
Prompt: Generate a script to calculate rewards multipliers based on Node Score and Validator health (NH = 1) within the GPUnet ecosystem.
Generated: DETERMINISTIC_64669b9dac42b13e
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate rewards multipliers based on Node Score and Validator Health (NH) in the GPUnet ecosystem.

def calculate_rewards_multiplier(node_score, validator_health):
    """
    Calculate the rewards multiplier based on Node Score and Validator Health.
    
    Parameters:
        node_score (float): The performance score of the node (0.0 to 1.0).
        validator_health (int): The health status of the validator (1 = Healthy, 0 = Unhealthy).
    
    Returns:
        float: Rewards multiplier. If validator is unhealthy, multiplier will be 0.
    """
    try:
        # Ensure node_score is within valid range
        if not (0.0 <= node_score <= 1.0):
            raise ValueError("Node Score must be between 0.0 and 1.0.")

        # Ensure validator_health is a binary value (0 or 1)
        if validator_health not in (0, 1):
            raise ValueError("Validator Health must be 0 (Unhealthy) or 1 (Healthy).")

        # If validator is unhealthy, rewards multiplier is 0
        if validator_health == 0:
            return 0.0

        # Calculate multiplier based on Node Score and Validator Health
        multiplier = 1.0 + (node_score * 0.5)
        return round(multiplier, 4)  # Return rounded multiplier for precision

    except ValueError as e:
        print(f"Input Error: {e}")
        return 0.0  # Return 0 multiplier in case of invalid inputs
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return 0.0


def main():
    """
    Main function to test the rewards multiplier calculation.
    """
    # Example inputs
    example_inputs = [
        {"node_score": 0.9, "validator_health": 1},
        {"node_score": 0.5, "validator_health": 1},
        {"node_score": 1.2, "validator_health": 1},  # Invalid Node Score
        {"node_score": 0.8, "validator_health": 0},  # Unhealthy Validator
        {"node_score": 0.7, "validator_health": 2},  # Invalid Validator Health
    ]

    # Process each input and calculate the rewards multiplier
    for i, inputs in enumerate(example_inputs, 1):
        print(f"Test Case {i}:")
        try:
            node_score = inputs["node_score"]
            validator_health = inputs["validator_health"]
            multiplier = calculate_rewards_multiplier(node_score, validator_health)
            print(f"  Node Score: {node_score}, Validator Health: {validator_health}")
            print(f"  Rewards Multiplier: {multiplier}")
        except KeyError as e:
            print(f"  Missing Key in Input: {e}")
        print()  # Blank line for readability


if __name__ == "__main__":
    # Entry point for the script
    main()
```
