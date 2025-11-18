"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Create a script to filter lighting products from Credible BD's catalog based on IP rating, wattage, and application type, such as outdoor lighting or commercial lighting.
Generated: DETERMINISTIC_bf4049abc61e9ffc
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Constants for filtering criteria
IP_RATING_FILTER = 'IP65'  # Example IP rating to filter by
WATTAGE_MIN = 10            # Minimum wattage
WATTAGE_MAX = 100           # Maximum wattage
APPLICATION_TYPE_FILTER = 'Outdoor'  # Application type to filter by

def load_catalog(file_path):
    """
    Load the product catalog from a CSV file.
    
    :param file_path: Path to the CSV file containing the product catalog.
    :return: DataFrame containing the catalog data.
    """
    try:
        catalog_df = pd.read_csv(file_path)
        return catalog_df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except Exception as e:
        print(f"An unexpected error occurred while loading the catalog: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def filter_lighting_products(catalog_df):
    """
    Filter the lighting products based on IP rating, wattage, and application type.
    
    :param catalog_df: DataFrame containing the catalog data.
    :return: Filtered DataFrame containing the lighting products.
    """
    try:
        filtered_df = catalog_df[
            (catalog_df['IP Rating'] == IP_RATING_FILTER) &
            (catalog_df['Wattage'] >= WATTAGE_MIN) &
            (catalog_df['Wattage'] <= WATTAGE_MAX) &
            (catalog_df['Application Type'] == APPLICATION_TYPE_FILTER)
        ]
        return filtered_df
    except KeyError as e:
        print(f"Error: Missing expected column in the catalog DataFrame: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except Exception as e:
        print(f"An unexpected error occurred while filtering products: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def main():
    """
    Main function to load the catalog and filter the lighting products.
    """
    file_path = 'credible_bd_catalog.csv'  # Path to the catalog file
    catalog_df = load_catalog(file_path)

    if not catalog_df.empty:
        filtered_products = filter_lighting_products(catalog_df)
        if not filtered_products.empty:
            print("Filtered Lighting Products:")
            print(filtered_products)
        else:
            print("No products matched the filter criteria.")
    else:
        print("Catalog is empty or could not be loaded.")

if __name__ == "__main__":
    main()
```
