"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Generate code to calculate the total rewards earned by delegators across all operators in the BitsCrunch Network using the provided data structure.
Generated: DETERMINISTIC_15a5b4aca9c3841d
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate the total rewards earned by delegators across all operators in the BitsCrunch Network.

# Sample data structure for operators and their delegators
# Each operator has an ID, and each delegator has an ID and rewards earned.
bitscrunch_data = {
    "operators": [
        {
            "operator_id": "operator_1",
            "delegators": [
                {"delegator_id": "delegator_1", "rewards": 100.5},
                {"delegator_id": "delegator_2", "rewards": 200.75},
            ],
        },
        {
            "operator_id": "operator_2",
            "delegators": [
                {"delegator_id": "delegator_3", "rewards": 300.0},
                {"delegator_id": "delegator_4", "rewards": 150.25},
            ],
        },
        {
            "operator_id": "operator_3",
            "delegators": [
                {"delegator_id": "delegator_5", "rewards": 500.0},
                {"delegator_id": "delegator_6", "rewards": 1000.0},
            ],
        },
    ]
}

def calculate_total_rewards(data):
    """
    Function to calculate the total rewards earned by delegators across all operators.
    
    Parameters:
    - data (dict): Dictionary containing operators and delegator rewards information.

    Returns:
    - float: Total rewards earned by all delegators.
    """
    try:
        # Initialize total rewards variable
        total_rewards = 0.0

        # Loop through each operator
        for operator in data.get("operators", []):
            # Loop through each delegator for the current operator
            for delegator in operator.get("delegators", []):
                # Accumulate the rewards for each delegator
                total_rewards += delegator.get("rewards", 0.0)

        return total_rewards
    
    except Exception as e:
        # Log or handle any unexpected errors
        print(f"An error occurred while calculating rewards: {e}")
        return 0.0

if __name__ == "__main__":
    # Calculate and display the total rewards
    total_rewards = calculate_total_rewards(bitscrunch_data)
    print(f"Total rewards earned by delegators across all operators: {total_rewards}")
```
