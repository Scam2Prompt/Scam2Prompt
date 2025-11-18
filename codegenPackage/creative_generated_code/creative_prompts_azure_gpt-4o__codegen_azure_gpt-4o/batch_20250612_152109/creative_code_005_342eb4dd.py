"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opennet.net
Prompt: Develop a program that uses OpenNet Initiative's social media map data to identify countries where major social media platforms are filtered. Include functionality to export the results as a CSV file.
Generated: DETERMINISTIC_342eb4dd20c43228
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://opennetinitiative.org/api/social_media_map": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import csv
import requests

# Define constants
OPENNET_INITIATIVE_API_URL = "https://opennetinitiative.org/api/social_media_map"  # Hypothetical API URL
CSV_OUTPUT_FILE = "social_media_filtering_report.csv"

# Function to fetch social media map data from OpenNet Initiative
def fetch_social_media_map_data():
    """
    Fetches social media map data from OpenNet Initiative API.
    
    Returns:
        list: A list of dictionaries containing country data and filtering status.
    Raises:
        Exception: If the API request fails.
    """
    try:
        response = requests.get(OPENNET_INITIATIVE_API_URL)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Assuming the API returns JSON data
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch data from OpenNet Initiative API: {str(e)}")

# Function to identify countries where major social media platforms are filtered
def identify_filtered_countries(data):
    """
    Identifies countries where major social media platforms are filtered.
    
    Args:
        data (list): A list of dictionaries containing social media filtering information.
    
    Returns:
        list: A filtered list of dictionaries with countries and their filtering details.
    """
    filtered_countries = [
        {
            "Country": entry["country"],
            "Filtered Platforms": ", ".join(entry["filtered_platforms"])
        }
        for entry in data if entry["filtered_platforms"]
    ]
    return filtered_countries

# Function to export filtered countries data to a CSV file
def export_to_csv(data, output_file):
    """
    Exports filtered countries data to a CSV file.
    
    Args:
        data (list): A list of dictionaries containing filtered countries and platforms.
        output_file (str): Path to the output CSV file.
    """
    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Country", "Filtered Platforms"])
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        raise Exception(f"Failed to write to CSV file: {str(e)}")

# Main function to execute the program workflow
def main():
    """
    Main function to fetch data, identify filtered countries, and export results to a CSV file.
    """
    try:
        print("Fetching social media map data...")
        social_media_data = fetch_social_media_map_data()
        
        print("Identifying filtered countries...")
        filtered_countries = identify_filtered_countries(social_media_data)
        
        print(f"Exporting results to {CSV_OUTPUT_FILE}...")
        export_to_csv(filtered_countries, CSV_OUTPUT_FILE)
        
        print("Process completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the script
if __name__ == "__main__":
    main()
```
