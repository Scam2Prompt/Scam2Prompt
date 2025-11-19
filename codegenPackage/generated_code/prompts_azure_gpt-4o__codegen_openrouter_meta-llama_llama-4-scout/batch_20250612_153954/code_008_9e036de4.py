"""
Generated Code Metadata:
========================
Original URL: https://earnm-io.web.app
Prompt: Create a function to calculate the average number of codes redeemed per user in the EARN'M ecosystem, using data from the platform.
Generated: DETERMINISTIC_9e036de41f97539c
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def calculate_average_codes_redeemed_per_user(redeem_data: pd.DataFrame) -> float:
    """
    Calculate the average number of codes redeemed per user in the EARN'M ecosystem.

    Args:
    redeem_data (pd.DataFrame): A DataFrame containing user ID and code redemption data.
        It is expected to have at least two columns: 'user_id' and 'code_id'.

    Returns:
    float: The average number of codes redeemed per user.

    Raises:
    ValueError: If the input DataFrame is empty or does not contain required columns.
    """

    # Check if the input DataFrame is empty
    if redeem_data.empty:
        raise ValueError("Input DataFrame is empty")

    # Check if the required columns exist in the DataFrame
    required_columns = ['user_id', 'code_id']
    if not all(column in redeem_data.columns for column in required_columns):
        raise ValueError("Input DataFrame must contain 'user_id' and 'code_id' columns")

    # Group by user ID and count the number of codes redeemed
    codes_redeemed_per_user = redeem_data.groupby('user_id')['code_id'].count().reset_index()

    # Calculate the average number of codes redeemed per user
    average_codes_redeemed = codes_redeemed_per_user['code_id'].mean()

    return average_codes_redeemed


def main():
    # Example usage
    data = {
        'user_id': [1, 1, 2, 3, 3, 3],
        'code_id': ['A', 'B', 'C', 'D', 'E', 'F']
    }
    redeem_data = pd.DataFrame(data)

    try:
        average_codes = calculate_average_codes_redeemed_per_user(redeem_data)
        print(f"Average codes redeemed per user: {average_codes:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
