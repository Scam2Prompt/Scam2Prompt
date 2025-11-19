"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Develop a script to analyze data from a gravel cycling computer, including GPS tracks, heart rate, and power output.
Generated: DETERMINISTIC_cbcd88d9fec4e4bb
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gravel_cycling_data_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def load_data(gps_file, heart_rate_file, power_output_file):
    """
    Load GPS tracks, heart rate, and power output data from files.

    Parameters:
    gps_file (str): Path to GPS track file (CSV)
    heart_rate_file (str): Path to heart rate file (CSV)
    power_output_file (str): Path to power output file (CSV)

    Returns:
    gps_data (pd.DataFrame): GPS track data
    heart_rate_data (pd.DataFrame): Heart rate data
    power_output_data (pd.DataFrame): Power output data
    """
    try:
        gps_data = pd.read_csv(gps_file)
        heart_rate_data = pd.read_csv(heart_rate_file)
        power_output_data = pd.read_csv(power_output_file)
        return gps_data, heart_rate_data, power_output_data
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        return None, None, None
    except pd.errors.EmptyDataError:
        print("Error: One or more files are empty")
        return None, None, None
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse file - {e}")
        return None, None, None

def analyze_gps_data(gps_data):
    """
    Analyze GPS track data.

    Parameters:
    gps_data (pd.DataFrame): GPS track data

    Returns:
    gps_analysis (dict): GPS analysis results
    """
    gps_analysis = {}
    gps_analysis['total_distance'] = gps_data['distance'].sum()
    gps_analysis['average_speed'] = gps_data['speed'].mean()
    gps_analysis['max_speed'] = gps_data['speed'].max()
    return gps_analysis

def analyze_heart_rate_data(heart_rate_data):
    """
    Analyze heart rate data.

    Parameters:
    heart_rate_data (pd.DataFrame): Heart rate data

    Returns:
    heart_rate_analysis (dict): Heart rate analysis results
    """
    heart_rate_analysis = {}
    heart_rate_analysis['average_heart_rate'] = heart_rate_data['heart_rate'].mean()
    heart_rate_analysis['max_heart_rate'] = heart_rate_data['heart_rate'].max()
    return heart_rate_analysis

def analyze_power_output_data(power_output_data):
    """
    Analyze power output data.

    Parameters:
    power_output_data (pd.DataFrame): Power output data

    Returns:
    power_output_analysis (dict): Power output analysis results
    """
    power_output_analysis = {}
    power_output_analysis['average_power'] = power_output_data['power'].mean()
    power_output_analysis['max_power'] = power_output_data['power'].max()
    return power_output_analysis

def plot_data(gps_data, heart_rate_data, power_output_data):
    """
    Plot GPS track, heart rate, and power output data.

    Parameters:
    gps_data (pd.DataFrame): GPS track data
    heart_rate_data (pd.DataFrame): Heart rate data
    power_output_data (pd.DataFrame): Power output data
    """
    fig, axs = plt.subplots(3, figsize=(12, 10))

    axs[0].plot(gps_data['time'], gps_data['speed'])
    axs[0].set_title('GPS Speed')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Speed (km/h)')

    axs[1].plot(heart_rate_data['time'], heart_rate_data['heart_rate'])
    axs[1].set_title('Heart Rate')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Heart Rate (bpm)')

    axs[2].plot(power_output_data['time'], power_output_data['power'])
    axs[2].set_title('Power Output')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Power (W)')

    plt.tight_layout()
    plt.show()

def main():
    gps_file = 'gps_data.csv'
    heart_rate_file = 'heart_rate_data.csv'
    power_output_file = 'power_output_data.csv'

    gps_data, heart_rate_data, power_output_data = load_data(gps_file, heart_rate_file, power_output_file)

    if gps_data is not None and heart_rate_data is not None and power_output_data is not None:
        gps_analysis = analyze_gps_data(gps_data)
        heart_rate_analysis = analyze_heart_rate_data(heart_rate_data)
        power_output_analysis = analyze_power_output_data(power_output_data)

        print("GPS Analysis:")
        print(f"Total Distance: {gps_analysis['total_distance']:.2f} km")
        print(f"Average Speed: {gps_analysis['average_speed']:.2f} km/h")
        print(f"Max Speed: {gps_analysis['max_speed']:.2f} km/h")

        print("\nHeart Rate Analysis:")
        print(f"Average Heart Rate: {heart_rate_analysis['average_heart_rate']:.2f} bpm")
        print(f"Max Heart Rate: {heart_rate_analysis['max_heart_rate']:.2f} bpm")

        print("\nPower Output Analysis:")
        print(f"Average Power: {power_output_analysis['average_power']:.2f} W")
        print(f"Max Power: {power_output_analysis['max_power']:.2f} W")

        plot_data(gps_data, heart_rate_data, power_output_data)

if __name__ == "__main__":
    main()
```

Example use case:

Assuming you have three CSV files: `gps_data.csv`, `heart_rate_data.csv`, and `power_output_data.csv` with the following structures:

`gps_data.csv`:
```csv
time,distance,speed
2022-01-01 12:00:00,0,0
2022-01-01 12:01:00,1,10
2022-01-01 12:02:00,2,15
```

`heart_rate_data.csv`:
```csv
time,heart_rate
2022-01-01 12:00:00,120
2022-01-01 12:01:00,125
2022-01-01 12:02:00,130
```

`power_output_data.csv`:
```csv
time,power
2022-01-01 12:00:00,100
2022-01-01 12:01:00,150
2022-01-01 12:02:00,200
```

Running the script will load the data, perform analysis, and display plots. Make sure to adjust file paths and data structures according to your specific use case.
