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

# Load the dataset of rental properties
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the rental properties dataset from a CSV file.
    
    :param file_path: Path to the CSV file containing properties data.
    :return: DataFrame containing the rental properties.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Filter properties based on criteria
def filter_properties(df: pd.DataFrame, location: str, min_price: float, max_price: float, amenities: list) -> pd.DataFrame:
    """
    Filter the properties based on location, price range, and amenities.
    
    :param df: DataFrame containing the rental properties.
    :param location: Desired location for rental properties.
    :param min_price: Minimum price for the rental.
    :param max_price: Maximum price for the rental.
    :param amenities: List of desired amenities.
    :return: Filtered DataFrame containing properties that match the criteria.
    """
    if df.empty:
        print("Error: The properties DataFrame is empty. Cannot filter.")
        return df
    
    # Filter by location
    filtered_df = df[df['Location'].str.contains(location, case=False, na=False)]
    
    # Filter by price range
    filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
    
    # Filter by amenities
    for amenity in amenities:
        filtered_df = filtered_df[filtered_df['Amenities'].str.contains(amenity, case=False, na=False)]
    
    return filtered_df

# Main function to execute the script
def main():
    # Path to the dataset (update as needed)
    file_path = 'rental_properties.csv'

    # Load the data
    properties_df = load_data(file_path)

    # Define filter criteria
    location = "Gurugram"
    min_price = 5000  # Minimum price in the currency unit
    max_price = 20000  # Maximum price in the currency unit
    amenities = ["high-speed WiFi", "attached kitchen"]

    # Filter properties based on criteria
    filtered_properties = filter_properties(properties_df, location, min_price, max_price, amenities)

    # Display filtered properties
    if not filtered_properties.empty:
        print("Filtered Rental Properties:")
        print(filtered_properties)
    else:
        print("No properties found matching the criteria.")

if __name__ == "__main__":
    main()
```
