"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write a Python program to compare Engel hard coolers' ice retention capabilities with other brands, using Engel's 7-day ice preservation data as a benchmark.
Generated: DETERMINISTIC_b1e87308d90ef985
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

# Define a class to handle cooler data and comparisons
class CoolerComparison:
    def __init__(self):
        # Initialize a DataFrame to hold cooler data
        self.coolers_data = pd.DataFrame(columns=['Brand', 'Ice Retention Days'])

    def add_cooler(self, brand: str, ice_retention_days: int):
        """Add a cooler's data to the DataFrame.
        
        Args:
            brand (str): The brand of the cooler.
            ice_retention_days (int): The number of days the cooler retains ice.
        """
        # Validate inputs
        if not isinstance(brand, str) or not isinstance(ice_retention_days, int):
            raise ValueError("Brand must be a string and ice retention days must be an integer.")
        
        # Append the cooler data
        self.coolers_data = self.coolers_data.append({'Brand': brand, 'Ice Retention Days': ice_retention_days}, ignore_index=True)

    def compare_with_engel(self):
        """Compare other brands' ice retention capabilities with Engel's benchmark."""
        # Check if Engel's data exists
        if 'Engel' not in self.coolers_data['Brand'].values:
            raise ValueError("Engel cooler data not found in the dataset.")
        
        engel_retention = self.coolers_data.loc[self.coolers_data['Brand'] == 'Engel', 'Ice Retention Days'].values[0]
        
        # Create a new column for comparison
        self.coolers_data['Compared to Engel'] = self.coolers_data['Ice Retention Days'] - engel_retention

    def plot_comparison(self):
        """Plot the ice retention comparison of coolers."""
        try:
            # Plotting the data
            plt.figure(figsize=(10, 6))
            plt.bar(self.coolers_data['Brand'], self.coolers_data['Ice Retention Days'], color='skyblue')
            plt.axhline(y=self.coolers_data.loc[self.coolers_data['Brand'] == 'Engel', 'Ice Retention Days'].values[0],
                        color='orange', linestyle='--', label='Engel Benchmark (7 days)')
            plt.title('Cooler Ice Retention Comparison')
            plt.xlabel('Cooler Brand')
            plt.ylabel('Ice Retention Days')
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

def main():
    """Main function to execute cooler comparison."""
    try:
        comparison = CoolerComparison()
        
        # Adding Engel cooler data
        comparison.add_cooler('Engel', 7)

        # Adding other brands
        comparison.add_cooler('Brand A', 5)
        comparison.add_cooler('Brand B', 6)
        comparison.add_cooler('Brand C', 4)

        # Compare with Engel's data
        comparison.compare_with_engel()

        # Plotting the comparison results
        comparison.plot_comparison()

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
