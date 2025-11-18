"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geosatelites.com
Prompt: Write code to compare the resolution of satellite images (FORMOSAT-2, Pléiades, KOMPSAT-2) and generate a report, referencing the specifications mentioned on geosatelites.com.
Generated: DETERMINISTIC_40ca8fd40bb8a166
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import csv

def fetch_satellite_data():
    """
    Fetch satellite resolution specifications from geosatelites.com.
    Returns:
        dict: A dictionary with satellite names as keys and their resolutions as values.
    """
    # Mockup data since we can't directly fetch from geosatelites.com
    # Replace this with an actual API call or scraping logic if needed.
    return {
        "FORMOSAT-2": 2.0,  # Resolution in meters
        "Pléiades": 0.5,    # Resolution in meters
        "KOMPSAT-2": 1.0    # Resolution in meters
    }

def compare_resolutions(satellite_data):
    """
    Compares the resolutions of satellites and generates a report.
    
    Args:
        satellite_data (dict): Dictionary with satellite names and their resolutions.
        
    Returns:
        list: A list of tuples sorted by resolution, with each tuple containing satellite name and resolution.
    """
    # Sort satellites by resolution (ascending order since lower is better)
    sorted_data = sorted(satellite_data.items(), key=lambda x: x[1])
    return sorted_data

def generate_report(sorted_data, output_file="satellite_report.csv"):
    """
    Generates a CSV report of satellite resolutions.
    
    Args:
        sorted_data (list): List of tuples containing satellite names and their resolutions.
        output_file (str): Name of the file to save the report.
    """
    try:
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(["Satellite Name", "Resolution (meters)"])
            # Write satellite data
            for satellite, resolution in sorted_data:
                writer.writerow([satellite, resolution])
        print(f"Report successfully generated: {output_file}")
    except Exception as e:
        print(f"Error generating report: {e}")

def main():
    """
    Main function to fetch data, compare resolutions and generate a report.
    """
    try:
        # Step 1: Fetch satellite data
        satellite_data = fetch_satellite_data()
        
        # Step 2: Compare satellite resolutions
        sorted_data = compare_resolutions(satellite_data)
        
        # Step 3: Generate report
        generate_report(sorted_data)
    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
```
