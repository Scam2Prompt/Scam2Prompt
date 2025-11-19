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
import csv
import json
import os
from datetime import datetime
import statistics

# Define constants for file paths
GPS_TRACK_FILE = "gps_tracks.csv"
HEART_RATE_FILE = "heart_rate.csv"
POWER_OUTPUT_FILE = "power_output.csv"
OUTPUT_FILE = "analysis_results.json"

def read_csv(file_path):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    :param file_path: Path to the CSV file.
    :return: List of dictionaries containing the data.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

def analyze_gps_data(gps_data):
    """
    Analyzes GPS data to calculate total distance and average speed.
    :param gps_data: List of dictionaries containing GPS data.
    :return: Dictionary with total distance and average speed.
    """
    try:
        total_distance = sum(float(row['distance_km']) for row in gps_data)
        total_time_hours = sum(float(row['time_hours']) for row in gps_data)
        average_speed = total_distance / total_time_hours if total_time_hours > 0 else 0
        return {
            "total_distance_km": round(total_distance, 2),
            "average_speed_kmh": round(average_speed, 2)
        }
    except KeyError as e:
        print(f"Error: Missing key in GPS data - {e}")
        return {}

def analyze_heart_rate_data(heart_rate_data):
    """
    Analyzes heart rate data to calculate average and max heart rate.
    :param heart_rate_data: List of dictionaries containing heart rate data.
    :return: Dictionary with average and max heart rate.
    """
    try:
        heart_rates = [int(row['heart_rate_bpm']) for row in heart_rate_data]
        return {
            "average_heart_rate_bpm": round(statistics.mean(heart_rates), 2),
            "max_heart_rate_bpm": max(heart_rates)
        }
    except KeyError as e:
        print(f"Error: Missing key in heart rate data - {e}")
        return {}
    except statistics.StatisticsError:
        print("Error: No heart rate data available.")
        return {}

def analyze_power_output_data(power_output_data):
    """
    Analyzes power output data to calculate average and max power output.
    :param power_output_data: List of dictionaries containing power output data.
    :return: Dictionary with average and max power output.
    """
    try:
        power_outputs = [int(row['power_output_watts']) for row in power_output_data]
        return {
            "average_power_output_watts": round(statistics.mean(power_outputs), 2),
            "max_power_output_watts": max(power_outputs)
        }
    except KeyError as e:
        print(f"Error: Missing key in power output data - {e}")
        return {}
    except statistics.StatisticsError:
        print("Error: No power output data available.")
        return {}

def save_analysis_results(results, output_file):
    """
    Saves the analysis results to a JSON file.
    :param results: Dictionary containing the analysis results.
    :param output_file: Path to the output JSON file.
    """
    try:
        with open(output_file, mode='w') as file:
            json.dump(results, file, indent=4)
        print(f"Analysis results saved to {output_file}")
    except Exception as e:
        print(f"Error saving analysis results: {e}")

def main():
    """
    Main function to orchestrate the data analysis.
    """
    # Read data from CSV files
    gps_data = read_csv(GPS_TRACK_FILE)
    heart_rate_data = read_csv(HEART_RATE_FILE)
    power_output_data = read_csv(POWER_OUTPUT_FILE)

    # Perform analysis
    gps_analysis = analyze_gps_data(gps_data)
    heart_rate_analysis = analyze_heart_rate_data(heart_rate_data)
    power_output_analysis = analyze_power_output_data(power_output_data)

    # Combine results
    analysis_results = {
        "gps_analysis": gps_analysis,
        "heart_rate_analysis": heart_rate_analysis,
        "power_output_analysis": power_output_analysis,
        "analysis_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Save results to a JSON file
    save_analysis_results(analysis_results, OUTPUT_FILE)

if __name__ == "__main__":
    main()
```
