"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Create a Python script to filter Emanuelson Reels models by price range and line class, including options like "Trout 2 Wide" and "Sea-Trout."
Generated: DETERMINISTIC_a0012d01cc787e66
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Define a class to represent the Emanuelson Reels filter
class EmanuelsonReelsFilter:
    def __init__(self, data_file):
        """
        Initializes the filter with the reels data from a CSV file.
        
        :param data_file: Path to the CSV file containing the reels data
        """
        self.data_file = data_file
        self.reels_data = self.load_data()

    def load_data(self):
        """
        Loads the reels data from the specified CSV file.
        
        :return: DataFrame containing the reels data
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            print(f"Error: The file '{self.data_file}' was not found.")
            return pd.DataFrame()  # Return an empty DataFrame on error
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")
            return pd.DataFrame()

    def filter_reels(self, price_range, line_class):
        """
        Filters the reels data based on the specified price range and line class.
        
        :param price_range: Tuple containing the minimum and maximum price
        :param line_class: The line class to filter by (e.g., 'Trout 2 Wide', 'Sea-Trout')
        :return: Filtered DataFrame containing reels that match the criteria
        """
        if not isinstance(price_range, tuple) or len(price_range) != 2:
            raise ValueError("Price range must be a tuple of (min_price, max_price)")
        
        min_price, max_price = price_range
        
        # Perform filtering based on price range and line class
        filtered_reels = self.reels_data[
            (self.reels_data['price'] >= min_price) & 
            (self.reels_data['price'] <= max_price) & 
            (self.reels_data['line_class'].str.contains(line_class, case=False, na=False))
        ]
        
        return filtered_reels

# Example usage (this part can be removed or commented out in production):
if __name__ == "__main__":
    # Initialize the filter with the CSV data file
    reels_filter = EmanuelsonReelsFilter('emanuelson_reels.csv')
    
    # Define the price range and line class for filtering
    price_range = (50, 150)  # Example price range
    line_class = 'Trout 2 Wide'  # Example line class

    # Perform filtering
    try:
        filtered_reels = reels_filter.filter_reels(price_range, line_class)
        print(filtered_reels)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Error: {e}")
```

Make sure to have the appropriate CSV file named `emanuelson_reels.csv` in the same directory or provide the correct path to the file when using this script. The CSV file should contain at least the columns 'price' and 'line_class' for the filtering to work correctly.
