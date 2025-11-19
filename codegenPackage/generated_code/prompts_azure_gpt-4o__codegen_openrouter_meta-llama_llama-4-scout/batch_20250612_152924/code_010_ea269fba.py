"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: Generate a Python script that calculates recovery success rates based on Rapid Responder's metrics, such as time frame and cost-effectiveness.
Generated: DETERMINISTIC_ea269fbaa53f5bda
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Rapid Responder Recovery Success Rate Calculator

Calculates recovery success rates based on Rapid Responder's metrics.

Author: [Your Name]
Date: [Today's Date]
"""

import pandas as pd
from typing import Dict, List

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads recovery data from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")
        return pd.DataFrame()
    except pd.errors.ParserError:
        print(f"Error parsing file: {file_path}")
        return pd.DataFrame()

def calculate_recovery_success_rate(data: pd.DataFrame) -> float:
    """
    Calculates the overall recovery success rate.

    Args:
    - data (pd.DataFrame): Recovery data.

    Returns:
    - float: Recovery success rate.
    """
    if data.empty:
        return 0.0

    successful_recoveries = data[data['recovery_outcome'] == 'success'].shape[0]
    total_recoveries = data.shape[0]

    return successful_recoveries / total_recoveries

def calculate_time_frame_success_rate(data: pd.DataFrame) -> Dict[str, float]:
    """
    Calculates recovery success rates by time frame.

    Args:
    - data (pd.DataFrame): Recovery data.

    Returns:
    - Dict[str, float]: Recovery success rates by time frame.
    """
    if data.empty:
        return {}

    time_frame_success_rates = {}

    for time_frame in data['time_frame'].unique():
        time_frame_data = data[data['time_frame'] == time_frame]
        successful_recoveries = time_frame_data[time_frame_data['recovery_outcome'] == 'success'].shape[0]
        total_recoveries = time_frame_data.shape[0]

        time_frame_success_rates[time_frame] = successful_recoveries / total_recoveries if total_recoveries > 0 else 0.0

    return time_frame_success_rates

def calculate_cost_effectiveness(data: pd.DataFrame) -> Dict[str, float]:
    """
    Calculates cost-effectiveness metrics.

    Args:
    - data (pd.DataFrame): Recovery data.

    Returns:
    - Dict[str, float]: Cost-effectiveness metrics.
    """
    if data.empty:
        return {}

    cost_effectiveness_metrics = {}

    total_cost = data['cost'].sum()
    total_successful_recoveries = data[data['recovery_outcome'] == 'success'].shape[0]

    cost_effectiveness_metrics['average_cost_per_recovery'] = total_cost / data.shape[0] if data.shape[0] > 0 else 0.0
    cost_effectiveness_metrics['cost_per_successful_recovery'] = total_cost / total_successful_recoveries if total_successful_recoveries > 0 else 0.0

    return cost_effectiveness_metrics

def main():
    file_path = 'recovery_data.csv'  # Replace with your file path
    data = load_data(file_path)

    if not data.empty:
        recovery_success_rate = calculate_recovery_success_rate(data)
        time_frame_success_rates = calculate_time_frame_success_rate(data)
        cost_effectiveness_metrics = calculate_cost_effectiveness(data)

        print(f"Recovery Success Rate: {recovery_success_rate:.2%}")
        print("Time Frame Success Rates:")
        for time_frame, success_rate in time_frame_success_rates.items():
            print(f"  - {time_frame}: {success_rate:.2%}")
        print("Cost-Effectiveness Metrics:")
        for metric, value in cost_effectiveness_metrics.items():
            print(f"  - {metric}: {value:.2f}")

if __name__ == '__main__':
    main()
```
