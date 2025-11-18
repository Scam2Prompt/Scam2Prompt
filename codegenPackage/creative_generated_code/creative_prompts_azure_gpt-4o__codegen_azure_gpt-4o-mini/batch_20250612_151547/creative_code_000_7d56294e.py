"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Write Python code to automate the selection of Brother ScanNCut machine models from a product catalog, filtering by price and features such as Disney-themed designs.
Generated: DETERMINISTIC_7d56294ee2b9baa8
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class ScanNCutFilter:
    def __init__(self, catalog_file):
        """
        Initialize the ScanNCutFilter with the product catalog file.
        
        :param catalog_file: Path to the CSV file containing the product catalog.
        """
        self.catalog_file = catalog_file
        self.catalog = self.load_catalog()

    def load_catalog(self):
        """
        Load the product catalog from a CSV file.
        
        :return: DataFrame containing product information.
        """
        try:
            catalog = pd.read_csv(self.catalog_file)
            print("Catalog loaded successfully.")
            return catalog
        except FileNotFoundError:
            raise Exception(f"Catalog file not found: {self.catalog_file}")
        except pd.errors.EmptyDataError:
            raise Exception("Catalog file is empty.")
        except pd.errors.ParserError:
            raise Exception("Error parsing the catalog file.")
    
    def filter_by_price(self, max_price):
        """
        Filter the catalog by maximum price.
        
        :param max_price: Maximum price to filter the products.
        :return: DataFrame containing filtered products.
        """
        filtered_catalog = self.catalog[self.catalog['Price'] <= max_price]
        print(f"Filtered by price: {len(filtered_catalog)} products found.")
        return filtered_catalog

    def filter_by_feature(self, feature):
        """
        Filter the catalog by a specific feature.
        
        :param feature: Feature to filter the products (e.g., 'Disney').
        :return: DataFrame containing filtered products.
        """
        filtered_catalog = self.catalog[self.catalog['Features'].str.contains(feature, case=False, na=False)]
        print(f"Filtered by feature '{feature}': {len(filtered_catalog)} products found.")
        return filtered_catalog

    def automate_selection(self, max_price, feature):
        """
        Automate the selection of machines based on price and features.
        
        :param max_price: Maximum price for filtering.
        :param feature: Feature to filter the products.
        :return: DataFrame of products that meet the criteria.
        """
        try:
            price_filtered = self.filter_by_price(max_price)
            feature_filtered = self.filter_by_feature(feature)
            final_selection = pd.merge(price_filtered, feature_filtered, how='inner')
            print(f"Final selection contains {len(final_selection)} products.")
            return final_selection
        except Exception as e:
            print(f"Error during selection: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

# Example usage:
if __name__ == "__main__":
    catalog_path = 'scan_n_cut_catalog.csv'  # Path to the product catalog CSV
    max_price_limit = 300.00  # Example max price
    search_feature = 'Disney'  # Example feature to search for

    try:
        scanner = ScanNCutFilter(catalog_path)
        result = scanner.automate_selection(max_price_limit, search_feature)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
```
