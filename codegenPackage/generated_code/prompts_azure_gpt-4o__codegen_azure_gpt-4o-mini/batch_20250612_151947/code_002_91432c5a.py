"""
Generated Code Metadata:
========================
Original URL: https://p30mag.com
Prompt: Generate a script to compare follower drop-off rates between two services, "دیجی فالوور" and "کافه فالوور," using data analysis techniques mentioned on p30mag.com.
Generated: DETERMINISTIC_91432c5ad97ba1fb
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to load data from CSV files
def load_data(file_path):
    """
    Load follower data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the follower data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to calculate drop-off rates
def calculate_drop_off_rate(data):
    """
    Calculate the drop-off rate of followers.

    Parameters:
    data (pd.DataFrame): A DataFrame containing follower data.

    Returns:
    float: The drop-off rate as a percentage.
    """
    if data is None or 'followers' not in data.columns:
        print("Error: Invalid data for drop-off rate calculation.")
        return None

    initial_followers = data['followers'].iloc[0]
    final_followers = data['followers'].iloc[-1]
    
    if initial_followers == 0:
        print("Error: Initial followers count is zero, cannot calculate drop-off rate.")
        return None

    drop_off_rate = ((initial_followers - final_followers) / initial_followers) * 100
    return drop_off_rate

# Function to plot drop-off rates
def plot_drop_off_rates(rates):
    """
    Plot the drop-off rates for the two services.

    Parameters:
    rates (dict): A dictionary containing the drop-off rates for each service.
    """
    services = list(rates.keys())
    drop_off_values = list(rates.values())

    plt.figure(figsize=(10, 6))
    plt.bar(services, drop_off_values, color=['blue', 'orange'])
    plt.title('Follower Drop-off Rates Comparison')
    plt.xlabel('Services')
    plt.ylabel('Drop-off Rate (%)')
    plt.ylim(0, max(drop_off_values) + 10)
    plt.grid(axis='y')
    plt.show()

# Main function to execute the analysis
def main():
    # Load data for both services
    digifollower_data = load_data('digifollower.csv')
    kafefollower_data = load_data('kafefollower.csv')

    # Calculate drop-off rates
    digifollower_drop_off = calculate_drop_off_rate(digifollower_data)
    kafefollower_drop_off = calculate_drop_off_rate(kafefollower_data)

    # Prepare results for plotting
    drop_off_rates = {
        "دیجی فالوور": digifollower_drop_off,
        "کافه فالوور": kafefollower_drop_off
    }

    # Plot the drop-off rates
    plot_drop_off_rates(drop_off_rates)

# Entry point of the script
if __name__ == "__main__":
    main()
```
