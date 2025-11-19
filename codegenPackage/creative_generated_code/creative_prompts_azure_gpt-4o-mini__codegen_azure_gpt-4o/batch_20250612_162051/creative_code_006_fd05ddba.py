"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahnoorpc.net
Prompt: Suggest a method for GPS data analysis using TopoGrafix ExpertGPS 8.64.0 as described on Mahnoor PC.
Generated: DETERMINISTIC_fd05ddba557ddf0a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

def analyze_gps_data(file_path):
    """
    Analyzes GPS data from a CSV file exported by ExpertGPS.

    Args:
        file_path (str): Path to the CSV file containing GPS data.

    Returns:
        dict: A summary of GPS data analysis including total points,
              average latitude, average longitude, and bounding box.
    """
    try:
        # Validate the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        # Initialize variables for analysis
        latitudes = []
        longitudes = []
        bounding_box = {"min_lat": float("inf"), "max_lat": float("-inf"),
                        "min_lon": float("inf"), "max_lon": float("-inf")}

        # Read the CSV file
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Validate the presence of required columns
            required_columns = ["Latitude", "Longitude"]
            for column in required_columns:
                if column not in csv_reader.fieldnames:
                    raise ValueError(f"Missing required column '{column}' in the CSV file.")

            # Process each row
            for row in csv_reader:
                try:
                    latitude = float(row["Latitude"])
                    longitude = float(row["Longitude"])
                    
                    # Update lists
                    latitudes.append(latitude)
                    longitudes.append(longitude)
                    
                    # Update bounding box
                    bounding_box["min_lat"] = min(bounding_box["min_lat"], latitude)
                    bounding_box["max_lat"] = max(bounding_box["max_lat"], latitude)
                    bounding_box["min_lon"] = min(bounding_box["min_lon"], longitude)
                    bounding_box["max_lon"] = max(bounding_box["max_lon"], longitude)
                except ValueError:
                    # Handle invalid GPS data gracefully
                    print(f"Skipping invalid GPS data row: {row}")

        # Calculate averages
        total_points = len(latitudes)
        if total_points == 0:
            raise ValueError("No valid GPS data points found in the CSV file.")
        
        average_latitude = sum(latitudes) / total_points
        average_longitude = sum(longitudes) / total_points

        # Return analysis results
        return {
            "total_points": total_points,
            "average_latitude": average_latitude,
            "average_longitude": average_longitude,
            "bounding_box": bounding_box
        }
    except Exception as e:
        # Log any exceptions encountered
        print(f"An error occurred during GPS data analysis: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with the actual path to the ExpertGPS CSV file
    gps_file_path = "path_to_expertgps_export.csv"
    
    # Analyze GPS data
    result = analyze_gps_data(gps_file_path)
    
    if result:
        print("GPS Data Analysis Completed:")
        print(f"Total Points: {result['total_points']}")
        print(f"Average Latitude: {result['average_latitude']}")
        print(f"Average Longitude: {result['average_longitude']}")
        print(f"Bounding Box: {result['bounding_box']}")
    else:
        print("GPS Data Analysis failed.")
```
