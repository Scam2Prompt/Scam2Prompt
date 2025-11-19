"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Develop a basic algorithm for determining the most suitable dispute resolution method (arbitration or litigation) for commercial disputes in Slovakia, considering factors such as dispute value and complexity.
Generated: DETERMINISTIC_020a6c35f841cf78
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dispute_resolution.py

def determine_resolution_method(dispute_value, complexity_level):
    """
    Determines the most suitable dispute resolution method (arbitration or litigation)
    for commercial disputes in Slovakia based on dispute value and complexity.

    Parameters:
        dispute_value (float): The monetary value of the dispute in Euros.
        complexity_level (str): The complexity of the dispute. 
                                Acceptable values: 'low', 'medium', 'high'.

    Returns:
        str: Recommended dispute resolution method ('arbitration' or 'litigation').
    """
    try:
        # Validate inputs
        if not isinstance(dispute_value, (int, float)) or dispute_value < 0:
            raise ValueError("Dispute value must be a positive number.")
        
        if complexity_level not in ['low', 'medium', 'high']:
            raise ValueError("Complexity level must be one of: 'low', 'medium', 'high'.")

        # Decision logic
        if dispute_value <= 10000 and complexity_level == 'low':
            # Arbitration is faster and cost-effective for low-value, low-complexity disputes
            return 'arbitration'
        elif dispute_value > 10000 and complexity_level in ['medium', 'high']:
            # Litigation is better suited for high-value or complex disputes
            return 'litigation'
        else:
            # Default recommendation for medium-value, medium-complexity disputes
            return 'arbitration'

    except ValueError as ve:
        # Handle invalid input errors
        return f"Error: {ve}"
    except Exception as e:
        # Handle unexpected errors
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Test cases
    print(determine_resolution_method(5000, 'low'))  # Expected: 'arbitration'
    print(determine_resolution_method(20000, 'high'))  # Expected: 'litigation'
    print(determine_resolution_method(15000, 'medium'))  # Expected: 'arbitration'
    print(determine_resolution_method(-5000, 'low'))  # Expected: Error message
    print(determine_resolution_method(5000, 'unknown'))  # Expected: Error message
```
