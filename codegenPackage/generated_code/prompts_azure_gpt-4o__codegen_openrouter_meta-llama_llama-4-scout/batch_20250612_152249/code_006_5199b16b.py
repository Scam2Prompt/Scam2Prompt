"""
Generated Code Metadata:
========================
Original URL: https://2xether.com
Prompt: Write a script to calculate and visualize the slope-of-force and phase metrics for ETHT and ETHD, as described in the momentum-trend analysis on 2xEther.com.
Generated: DETERMINISTIC_5199b16bcaff3d7a
Batch ID: 20250612_152249
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

def calculate_slope_of_force(data, window=14):
    """
    Calculate the slope of force metric.

    Parameters:
    data (pandas.Series): Price data
    window (int): Window size for calculation

    Returns:
    pandas.Series: Slope of force values
    """
    # Calculate differences in price
    delta_price = data.diff()

    # Calculate slope of force
    slope_of_force = delta_price.ewm(span=window, adjust=False).mean()

    return slope_of_force

def calculate_phase(data, window=14):
    """
    Calculate the phase metric.

    Parameters:
    data (pandas.Series): Price data
    window (int): Window size for calculation

    Returns:
    pandas.Series: Phase values
    """
    # Calculate phase
    phase = np.arctan2(data.ewm(span=window, adjust=False).std(), data)

    return phase

def visualize_metrics(ethd_data, etht_data):
    """
    Visualize slope of force and phase metrics for ETHD and ETHT.

    Parameters:
    ethd_data (pandas.DataFrame): ETHD price data
    etht_data (pandas.DataFrame): ETHT price data
    """
    # Calculate slope of force and phase for ETHD
    ethd_slope_of_force = calculate_slope_of_force(etd_data['Close'])
    ethd_phase = calculate_phase(etd_data['Close'])

    # Calculate slope of force and phase for ETHT
    etht_slope_of_force = calculate_slope_of_force(etht_data['Close'])
    etht_phase = calculate_phase(etht_data['Close'])

    # Create a figure and axis
    fig, axs = plt.subplots(4, 1, figsize=(12, 12))

    # Plot slope of force for ETHD
    axs[0].plot(etd_data.index, ethd_slope_of_force)
    axs[0].set_title('ETHD Slope of Force')

    # Plot phase for ETHD
    axs[1].plot(etd_data.index, ethd_phase)
    axs[1].set_title('ETHD Phase')

    # Plot slope of force for ETHT
    axs[2].plot(etht_data.index, etht_slope_of_force)
    axs[2].set_title('ETHT Slope of Force')

    # Plot phase for ETHT
    axs[3].plot(etht_data.index, etht_phase)
    axs[3].set_title('ETHT Phase')

    # Layout so plots do not overlap
    fig.tight_layout()

    plt.show()

def main():
    try:
        # Load data
        ethd_data = pd.read_csv('ethd_data.csv', index_col='Date', parse_dates=['Date'])
        etht_data = pd.read_csv('etht_data.csv', index_col='Date', parse_dates=['Date'])

        # Check if data is not empty
        if ethd_data.empty or etht_data.empty:
            raise ValueError("Data is empty")

        # Visualize metrics
        visualize_metrics(etd_data=etd_data, etht_data=etht_data)

    except FileNotFoundError:
        print("File not found. Please check file paths.")
    except pd.errors.EmptyDataError:
        print("Data is empty. Please check data files.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
