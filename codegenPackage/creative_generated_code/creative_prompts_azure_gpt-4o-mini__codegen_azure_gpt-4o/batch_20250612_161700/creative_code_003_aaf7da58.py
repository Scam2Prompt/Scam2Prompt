"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Develop a script to compare different Nepal tour packages offered by SafarGenie, focusing on unique features and pricing.
Generated: DETERMINISTIC_aaf7da587eef6b82
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a function to load tour packages from a JSON file
def load_tour_packages(file_path):
    """
    Load tour packages from a specified JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing tour package data.
        
    Returns:
        list: List of tour packages as dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' contains invalid JSON.")
        return []

# Define a function to compare tour packages based on features and pricing
def compare_tour_packages(tour_packages):
    """
    Compare different tour packages based on their unique features and pricing.
    
    Args:
        tour_packages (list): List of tour packages, each as a dictionary.
        
    Returns:
        None
    """
    if not tour_packages:
        print("No tour packages to compare.")
        return

    print("\n--- Tour Package Comparison ---\n")
    for package in tour_packages:
        try:
            # Extract details for comparison
            name = package.get("name", "Unknown Package")
            price = package.get("price", "N/A")
            features = package.get("features", [])
            
            # Display package details
            print(f"Package Name: {name}")
            print(f"Price: {price}")
            print(f"Features: {', '.join(features) if features else 'No features listed'}")
            print("-" * 40)
        except Exception as e:
            print(f"Error processing package: {e}")

# Define the main function
def main():
    """
    Main function to load and compare tour packages.
    """
    # Path to the JSON file containing tour package data
    file_path = "nepal_tour_packages.json"
    
    # Load tour packages
    tour_packages = load_tour_packages(file_path)
    
    # Compare tour packages
    compare_tour_packages(tour_packages)

# Entry point for the script
if __name__ == "__main__":
    main()
```

**Notes:**
1. Ensure you have a valid `nepal_tour_packages.json` file with properly formatted data before running the script.
2. Example JSON structure for the file:
```json
[
    {
        "name": "Adventure Nepal",
        "price": "$500",
        "features": ["Hiking", "Rafting", "Cultural tour"]
    },
    {
        "name": "Luxury Nepal",
        "price": "$1200",
        "features": ["5-star hotels", "Private transport", "Guided tours"]
    }
]
```
