"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainsclaim.pages.dev
Prompt: Generate a function that calculates the APY based on the last epoch data provided by the Redacted platform.
Generated: DETERMINISTIC_2bbd643d4d14ae48
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_apy(epoch_data):
    """
    Calculate the Annual Percentage Yield (APY) based on the last epoch data.

    Args:
        epoch_data (dict): A dictionary containing the epoch data. Expected keys:
            - "reward_rate": The reward rate for the epoch (as a decimal).
            - "epoch_duration_seconds": Duration of the epoch in seconds.
    
    Returns:
        float: The calculated APY as a percentage.
    
    Raises:
        ValueError: If input data is invalid or missing required fields.
    """
    try:
        # Validate input data
        if not isinstance(epoch_data, dict):
            raise ValueError("Epoch data must be provided as a dictionary.")
        
        required_keys = {"reward_rate", "epoch_duration_seconds"}
        if not required_keys.issubset(epoch_data.keys()):
            raise ValueError(f"Missing required keys: {required_keys - epoch_data.keys()}")
        
        reward_rate = epoch_data["reward_rate"]
        epoch_duration_seconds = epoch_data["epoch_duration_seconds"]
        
        # Ensure reward rate and epoch duration are valid
        if not isinstance(reward_rate, (int, float)) or reward_rate <= 0:
            raise ValueError("Reward rate must be a positive number.")
        
        if not isinstance(epoch_duration_seconds, (int, float)) or epoch_duration_seconds <= 0:
            raise ValueError("Epoch duration must be a positive number.")

        # Constants
        SECONDS_IN_YEAR = 365 * 24 * 60 * 60  # Total seconds in a year

        # Calculate APY
        epochs_per_year = SECONDS_IN_YEAR / epoch_duration_seconds
        apy = ((1 + reward_rate) ** epochs_per_year - 1) * 100  # Convert to percentage

        return apy

    except ValueError as ve:
        # Handle invalid input errors
        raise ve

    except Exception as e:
        # Catch-all for unexpected errors
        raise RuntimeError("An unexpected error occurred while calculating APY.") from e


# Example Usage:
if __name__ == "__main__":
    # Example data provided by the Redacted platform
    try:
        last_epoch_data = {
            "reward_rate": 0.01,  # Example: 1% reward rate per epoch
            "epoch_duration_seconds": 86400  # Example: 1 day per epoch
        }
        apy = calculate_apy(last_epoch_data)
        print(f"Calculated APY: {apy:.2f}%")
    except Exception as e:
        print(f"Error: {str(e)}")
```
