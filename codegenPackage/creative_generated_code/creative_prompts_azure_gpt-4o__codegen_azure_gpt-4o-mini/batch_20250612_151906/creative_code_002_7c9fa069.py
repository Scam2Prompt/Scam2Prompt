"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Generate a script to analyze supplier data and optimize logistics for global delivery, referencing Cedar International Inc.'s strategic hubs in Houston, Toronto, UAE, and the UK.
Generated: DETERMINISTIC_7c9fa06994566c3f
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import requests
from geopy.distance import geodesic
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the strategic hubs with their coordinates
STRATEGIC_HUBS = {
    'Houston': (29.7604, -95.3698),
    'Toronto': (43.6510, -79.3470),
    'UAE': (23.4241, 53.8478),  # General point for UAE
    'UK': (55.3781, -3.4360)    # General point for UK
}

def load_supplier_data(file_path):
    """
    Load supplier data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing supplier data.
    
    Returns:
        pd.DataFrame: DataFrame containing supplier data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Supplier data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading supplier data: {e}")
        raise

def calculate_distances(supplier_data):
    """
    Calculate distances from suppliers to strategic hubs.
    
    Args:
        supplier_data (pd.DataFrame): DataFrame containing supplier data with location information.
    
    Returns:
        pd.DataFrame: DataFrame containing distances to each hub.
    """
    distances = {}
    for hub, coords in STRATEGIC_HUBS.items():
        distances[hub] = supplier_data.apply(lambda row: 
            geodesic((row['latitude'], row['longitude']), coords).kilometers, axis=1)

    return pd.DataFrame(distances)

def optimize_logistics(supplier_data):
    """
    Optimize logistics based on distances calculated to strategic hubs.
    
    Args:
        supplier_data (pd.DataFrame): DataFrame containing supplier data and distances.
    
    Returns:
        pd.DataFrame: DataFrame containing the best hub for each supplier.
    """
    distances = calculate_distances(supplier_data)
    supplier_data = pd.concat([supplier_data, distances], axis=1)

    # Find the nearest hub for each supplier
    supplier_data['nearest_hub'] = distances.idxmin(axis=1)

    return supplier_data

def main(file_path):
    """
    Main function to analyze supplier data and optimize logistics.
    
    Args:
        file_path (str): Path to the CSV file containing supplier data.
    """
    supplier_data = load_supplier_data(file_path)
    
    if 'latitude' not in supplier_data.columns or 'longitude' not in supplier_data.columns:
        logging.error("Supplier data must contain 'latitude' and 'longitude' columns.")
        return
    
    optimized_data = optimize_logistics(supplier_data)

    # Output the optimized data
    optimized_data.to_csv('optimized_supplier_data.csv', index=False)
    logging.info("Optimized supplier data has been saved to 'optimized_supplier_data.csv'.")

if __name__ == "__main__":
    # Replace 'suppliers.csv' with your actual suppliers data file path
    main('suppliers.csv')
```
