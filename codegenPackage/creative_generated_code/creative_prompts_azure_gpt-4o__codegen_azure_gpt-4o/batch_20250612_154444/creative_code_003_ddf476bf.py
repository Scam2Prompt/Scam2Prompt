"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Write a script to analyze terrestrial and airborne LiDAR data for geospatial mapping, referencing Wira Survey Consultants' expertise in laser scanning technologies.
Generated: DETERMINISTIC_ddf476bf55c93f02
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import laspy
import numpy as np
import pandas as pd

# Constants
INPUT_DIR = 'lidar_data/input'  # Directory for input LiDAR files
OUTPUT_DIR = 'lidar_data/output'  # Directory for processed output
GROUND_THRESHOLD = 1.0  # Threshold to separate ground points (z-coordinate)
AIRBORNE_THRESHOLD = 10.0  # Threshold to classify airborne points
OUTPUT_CSV = 'processed_points.csv'  # Output file for processed points

def read_lidar_file(file_path):
    """
    Reads a LiDAR file (.las or .laz) using laspy.

    Args:
        file_path (str): Path to the LiDAR file.

    Returns:
        laspy.LasData: Loaded LiDAR data object.
    """
    try:
        return laspy.read(file_path)
    except Exception as e:
        raise RuntimeError(f"Error reading LiDAR file {file_path}: {e}")

def classify_points(lidar_data):
    """
    Classifies LiDAR data into ground and airborne points based on z-coordinates.

    Args:
        lidar_data (laspy.LasData): LiDAR data object.

    Returns:
        dict: Dictionary containing ground points and airborne points.
    """
    try:
        z_coords = lidar_data.z
        ground_points = lidar_data.points[z_coords <= GROUND_THRESHOLD]
        airborne_points = lidar_data.points[z_coords > AIRBORNE_THRESHOLD]

        return {
            "ground_points": ground_points,
            "airborne_points": airborne_points
        }
    except Exception as e:
        raise ValueError(f"Error classifying points: {e}")

def save_points_to_csv(points_dict, output_file):
    """
    Saves classified points to a CSV file.

    Args:
        points_dict (dict): Dictionary containing classified ground and airborne points.
        output_file (str): Path to the output CSV file.
    """
    try:
        ground_points_df = pd.DataFrame({
            "x": points_dict["ground_points"].x,
            "y": points_dict["ground_points"].y,
            "z": points_dict["ground_points"].z
        })

        airborne_points_df = pd.DataFrame({
            "x": points_dict["airborne_points"].x,
            "y": points_dict["airborne_points"].y,
            "z": points_dict["airborne_points"].z
        })

        ground_points_df["classification"] = "ground"
        airborne_points_df["classification"] = "airborne"

        # Combine into a single DataFrame
        combined_df = pd.concat([ground_points_df, airborne_points_df])
        combined_df.to_csv(output_file, index=False)

        print(f"Processed points saved to: {output_file}")
    except Exception as e:
        raise RuntimeError(f"Error saving points to CSV: {e}")

def process_lidar_data(input_dir, output_dir):
    """
    Processes all LiDAR files in the input directory, classifies points,
    and saves the results to the output directory.

    Args:
        input_dir (str): Directory containing input LiDAR files.
        output_dir (str): Directory to save processed files.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        input_files = [f for f in os.listdir(input_dir) if f.endswith('.las') or f.endswith('.laz')]

        if not input_files:
            print("No LiDAR files found in the input directory.")
            return

        for file in input_files:
            file_path = os.path.join(input_dir, file)
            lidar_data = read_lidar_file(file_path)

            classified_points = classify_points(lidar_data)
            output_file = os.path.join(output_dir, OUTPUT_CSV)

            save_points_to_csv(classified_points, output_file)
    except Exception as e:
        print(f"Error processing LiDAR data: {e}")

if __name__ == "__main__":
    # Entry point for the script
    process_lidar_data(INPUT_DIR, OUTPUT_DIR)
```
