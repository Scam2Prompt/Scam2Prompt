"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skinny-park-scarce.on-fleek.app
Prompt: Create a script to calculate the total rewards earned over a specified time period based on swap volume data.
Generated: DETERMINISTIC_7effd6fbf8bf6dcc
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

# Function to parse input swap volume data
def parse_swap_data(file_path):
    """
    Parses swap volume data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing swap volume data.

    Returns:
        list: A list of dictionaries containing swap data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in the file.")
    except Exception as e:
        raise RuntimeError(f"Error loading swap data: {e}")


# Function to calculate total rewards
def calculate_rewards(swap_data, start_date, end_date, reward_rate):
    """
    Calculates total rewards earned over the specified time period.

    Args:
        swap_data (list): List of swap volume data dictionaries.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
        reward_rate (float): Reward rate (e.g., 0.01 for 1%).

    Returns:
        float: Total rewards earned within the specified date range.
    """
    try:
        # Convert input dates to datetime objects
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        # Validate date range
        if start_date > end_date:
            raise ValueError("Start date must be earlier than or equal to end date.")

        total_rewards = 0

        # Calculate rewards for each swap entry
        for entry in swap_data:
            swap_date = datetime.datetime.strptime(entry["date"], "%Y-%m-%d")
            if start_date <= swap_date <= end_date:
                volume = entry.get("volume", 0)
                if volume < 0:
                    raise ValueError("Swap volume cannot be negative.")
                total_rewards += volume * reward_rate

        return total_rewards
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")
    except KeyError:
        raise KeyError("Missing required fields in swap data.")
    except Exception as e:
        raise RuntimeError(f"Error calculating rewards: {e}")


# Main entry point
if __name__ == "__main__":
    # Path to the JSON file containing swap volume data
    file_path = "swap_data.json"

    # Example inputs
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    reward_rate = 0.01  # 1% reward rate

    try:
        # Parse swap data
        swap_data = parse_swap_data(file_path)

        # Calculate total rewards
        total_rewards = calculate_rewards(swap_data, start_date, end_date, reward_rate)

        # Display the result
        print(f"Total rewards earned from {start_date} to {end_date}: {total_rewards:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
