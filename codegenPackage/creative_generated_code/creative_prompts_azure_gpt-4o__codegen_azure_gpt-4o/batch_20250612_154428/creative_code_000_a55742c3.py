"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Write a Python script to filter rental properties in Gurugram from a dataset based on criteria like location, price range, and amenities such as "high-speed WiFi" or "attached kitchen," as described on the Moms PG website.
Generated: DETERMINISTIC_a55742c372510073
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def filter_properties(dataset_path, location=None, price_range=None, amenities=None):
    """
    Filters rental properties from the dataset based on criteria.

    Parameters:
        dataset_path (str): Path to the CSV dataset file.
        location (str, optional): Desired location (e.g., 'Sector 45, Gurugram').
        price_range (tuple, optional): Price range as a tuple (min_price, max_price).
        amenities (list, optional): List of desired amenities (e.g., ['high-speed WiFi', 'attached kitchen']).

    Returns:
        pd.DataFrame: Filtered properties as a DataFrame.
    """
    try:
        # Load the dataset
        df = pd.read_csv(dataset_path)

        # Ensure required columns exist in the dataset
        required_columns = ['Location', 'Price', 'Amenities']
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Dataset is missing required column: {column}")

        # Start filtering
        filtered_df = df.copy()

        # Filter by location
        if location:
            filtered_df = filtered_df[filtered_df['Location'].str.contains(location, case=False, na=False)]

        # Filter by price range
        if price_range:
            min_price, max_price = price_range
            filtered_df = filtered_df[
                (filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)
            ]

        # Filter by amenities
        if amenities:
            for amenity in amenities:
                filtered_df = filtered_df[filtered_df['Amenities'].str.contains(amenity, case=False, na=False)]

        return filtered_df

    except FileNotFoundError:
        print("Error: Dataset file not found. Please ensure the file path is correct.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    dataset_path = "rental_properties.csv"  # Path to your dataset
    location = "Sector 45, Gurugram"
    price_range = (5000, 15000)  # Example price range
    amenities = ["high-speed WiFi", "attached kitchen"]

    filtered_properties = filter_properties(dataset_path, location, price_range, amenities)
    
    if filtered_properties is not None and not filtered_properties.empty:
        print("Filtered Properties:")
        print(filtered_properties)
    else:
        print("No properties matched the criteria.")
```
