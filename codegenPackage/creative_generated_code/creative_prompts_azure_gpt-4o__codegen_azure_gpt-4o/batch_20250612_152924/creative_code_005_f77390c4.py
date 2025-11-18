"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingeostar.com
Prompt: Create a Python program to process geospatial data for topographic leveling, including trigonometrical and geometrical adjustments.
Generated: DETERMINISTIC_f77390c4b45cddce
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import csv
from typing import List, Tuple, Union

# Define a custom exception for invalid data
class InvalidGeospatialDataError(Exception):
    pass

# Function to read geospatial data from a CSV file
def read_geospatial_data(file_path: str) -> List[Tuple[float, float, float]]:
    """
    Reads geospatial data from a CSV file.
    Each row in the file should have three columns: latitude, longitude, elevation.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        List[Tuple[float, float, float]]: A list of tuples containing latitude, longitude, and elevation.

    Raises:
        InvalidGeospatialDataError: If the data is not formatted correctly.
    """
    geospatial_data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    raise InvalidGeospatialDataError("Row does not contain exactly 3 columns.")
                try:
                    latitude = float(row[0])
                    longitude = float(row[1])
                    elevation = float(row[2])
                    geospatial_data.append((latitude, longitude, elevation))
                except ValueError:
                    raise InvalidGeospatialDataError("Row contains non-numeric data.")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    return geospatial_data

# Function to perform trigonometrical leveling
def trigonometrical_leveling(data: List[Tuple[float, float, float]]) -> List[Tuple[float, float, float]]:
    """
    Applies trigonometrical leveling adjustments to the geospatial data.

    Args:
        data (List[Tuple[float, float, float]]): The original geospatial data.

    Returns:
        List[Tuple[float, float, float]]: The adjusted geospatial data.
    """
    adjusted_data = []
    for latitude, longitude, elevation in data:
        # Example adjustment: apply a sinusoidal scaling based on latitude
        adjustment_factor = math.sin(math.radians(latitude))
        adjusted_elevation = elevation * adjustment_factor
        adjusted_data.append((latitude, longitude, adjusted_elevation))
    return adjusted_data

# Function to perform geometrical leveling
def geometrical_leveling(data: List[Tuple[float, float, float]]) -> List[Tuple[float, float, float]]:
    """
    Applies geometrical leveling adjustments to the geospatial data.

    Args:
        data (List[Tuple[float, float, float]]): The original geospatial data.

    Returns:
        List[Tuple[float, float, float]]: The adjusted geospatial data.
    """
    adjusted_data = []
    for latitude, longitude, elevation in data:
        # Example adjustment: normalize elevation based on a fixed reference point
        reference_elevation = 100.0  # A fixed reference elevation
        adjusted_elevation = elevation - reference_elevation
        adjusted_data.append((latitude, longitude, adjusted_elevation))
    return adjusted_data

# Function to save adjusted data to a CSV file
def save_adjusted_data(file_path: str, data: List[Tuple[float, float, float]]) -> None:
    """
    Saves adjusted geospatial data to a CSV file.

    Args:
        file_path (str): The path to the output CSV file.
        data (List[Tuple[float, float, float]]): The adjusted geospatial data.

    Returns:
        None
    """
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Latitude", "Longitude", "Elevation"])
            writer.writerows(data)
    except Exception as e:
        raise IOError(f"Failed to write adjusted data to '{file_path}': {e}")

# Main function to execute the program
def main():
    """
    Main function to process geospatial data for topographic leveling.
    """
    input_file = "input_geospatial_data.csv"
    trig_output_file = "trigonometrical_adjusted_data.csv"
    geom_output_file = "geometrical_adjusted_data.csv"

    try:
        # Read geospatial data from the input file
        geospatial_data = read_geospatial_data(input_file)
        
        # Perform trigonometrical leveling
        trig_adjusted_data = trigonometrical_leveling(geospatial_data)
        
        # Save trigonometrically leveled data to output file
        save_adjusted_data(trig_output_file, trig_adjusted_data)
        
        # Perform geometrical leveling
        geom_adjusted_data = geometrical_leveling(geospatial_data)
        
        # Save geometrically leveled data to output file
        save_adjusted_data(geom_output_file, geom_adjusted_data)

        print(f"Geospatial data processed successfully. Adjusted data saved to '{trig_output_file}' and '{geom_output_file}'.")
    except Exception as e:
        print(f"Error: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```
