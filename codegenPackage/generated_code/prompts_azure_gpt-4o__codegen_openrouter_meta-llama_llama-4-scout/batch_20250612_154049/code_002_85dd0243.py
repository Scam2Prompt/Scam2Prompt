"""
Generated Code Metadata:
========================
Original URL: https://eigenlayer.com
Prompt: Create a Python script to calculate rewards earned from validating services on EigenLayer, given the $47M rewards data and TVL statistics.
Generated: DETERMINISTIC_85dd0243c8443841
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# eigenlayer_rewards_calculator.py

import pandas as pd

def calculate_rewards(rewards_data: pd.DataFrame, tvl_statistics: pd.DataFrame) -> dict:
    """
    Calculate rewards earned from validating services on EigenLayer.

    Args:
    - rewards_data (pd.DataFrame): DataFrame containing $47M rewards data.
    - tvl_statistics (pd.DataFrame): DataFrame containing TVL statistics.

    Returns:
    - dict: Dictionary containing rewards earned for each validating service.
    """

    # Ensure inputs are DataFrames
    if not isinstance(rewards_data, pd.DataFrame) or not isinstance(tvl_statistics, pd.DataFrame):
        raise ValueError("Both rewards_data and tvl_statistics must be pandas DataFrames")

    # Validate required columns exist in DataFrames
    required_columns = ['service', 'rewards', 'tvl']
    for column in required_columns:
        if column not in rewards_data.columns or column not in tvl_statistics.columns:
            raise ValueError(f"Missing required column: {column}")

    # Merge rewards data and TVL statistics on 'service'
    merged_data = pd.merge(rewards_data, tvl_statistics, on='service')

    # Calculate rewards earned for each service
    merged_data['rewards_earned'] = merged_data['rewards'] * (merged_data['tvl'] / merged_data['tvl'].sum())

    # Group by service and sum rewards earned
    rewards_earned = merged_data.groupby('service')['rewards_earned'].sum().to_dict()

    return rewards_earned


def load_rewards_data(file_path: str) -> pd.DataFrame:
    """
    Load $47M rewards data from CSV file.

    Args:
    - file_path (str): Path to CSV file containing rewards data.

    Returns:
    - pd.DataFrame: DataFrame containing rewards data.
    """

    try:
        rewards_data = pd.read_csv(file_path)
        return rewards_data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: No data in file at {file_path}")
        return pd.DataFrame()
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse file at {file_path} - {e}")
        return pd.DataFrame()


def load_tvl_statistics(file_path: str) -> pd.DataFrame:
    """
    Load TVL statistics from CSV file.

    Args:
    - file_path (str): Path to CSV file containing TVL statistics.

    Returns:
    - pd.DataFrame: DataFrame containing TVL statistics.
    """

    try:
        tvl_statistics = pd.read_csv(file_path)
        return tvl_statistics
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: No data in file at {file_path}")
        return pd.DataFrame()
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse file at {file_path} - {e}")
        return pd.DataFrame()


def main():
    rewards_data_file = 'rewards_data.csv'
    tvl_statistics_file = 'tvl_statistics.csv'

    rewards_data = load_rewards_data(rewards_data_file)
    tvl_statistics = load_tvl_statistics(tvl_statistics_file)

    if not rewards_data.empty and not tvl_statistics.empty:
        rewards_earned = calculate_rewards(rewards_data, tvl_statistics)
        print("Rewards Earned:")
        for service, reward in rewards_earned.items():
            print(f"{service}: ${reward:.2f}")


if __name__ == "__main__":
    main()
```
