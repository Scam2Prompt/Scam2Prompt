"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedworldlibertyfinancial.xyz
Prompt: Write a function to calculate the impact of a community takeover on the speed of token transactions, using $BLF as a case study.
Generated: DETERMINISTIC_ea255883b60b91e1
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

def calculate_transaction_speed_impact(pre_takeover_speeds, post_takeover_speeds):
    """
    Calculates the impact of a community takeover on the speed of token transactions.

    Parameters:
    - pre_takeover_speeds (list): A list of transaction speeds (in seconds) before the community takeover.
    - post_takeover_speeds (list): A list of transaction speeds (in seconds) after the community takeover.

    Returns:
    - dict: A dictionary containing:
        - average_speed_pre_takeover (float): Average speed before the takeover.
        - average_speed_post_takeover (float): Average speed after the takeover.
        - speed_difference (float): Difference in average speeds (post - pre).
        - percentage_change (float): Percentage change in transaction speed.
    """
    try:
        # Validate input: Ensure both lists are non-empty and contain only numerical values
        if not pre_takeover_speeds or not post_takeover_speeds:
            raise ValueError("Both pre_takeover_speeds and post_takeover_speeds must be non-empty lists.")
        
        if not all(isinstance(speed, (int, float)) for speed in pre_takeover_speeds + post_takeover_speeds):
            raise ValueError("All transaction speeds should be numbers.")

        # Calculate average transaction speeds
        avg_speed_pre = statistics.mean(pre_takeover_speeds)
        avg_speed_post = statistics.mean(post_takeover_speeds)

        # Calculate speed difference and percentage change
        speed_difference = avg_speed_post - avg_speed_pre
        percentage_change = (speed_difference / avg_speed_pre) * 100

        # Return results as a dictionary
        return {
            "average_speed_pre_takeover": round(avg_speed_pre, 2),
            "average_speed_post_takeover": round(avg_speed_post, 2),
            "speed_difference": round(speed_difference, 2),
            "percentage_change": round(percentage_change, 2)
        }

    except ValueError as e:
        # Handle invalid input
        return {"error": str(e)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
# Pre-takeover transaction speeds (in seconds)
pre_takeover_speeds = [1.2, 1.4, 1.3, 1.1]

# Post-takeover transaction speeds (in seconds)
post_takeover_speeds = [0.9, 1.0, 0.8, 0.85]

# Calculate impact
result = calculate_transaction_speed_impact(pre_takeover_speeds, post_takeover_speeds)

# Print results
print(result)
```
