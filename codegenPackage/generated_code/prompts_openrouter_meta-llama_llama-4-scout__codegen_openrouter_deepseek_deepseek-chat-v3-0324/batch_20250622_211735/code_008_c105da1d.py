"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: "Write a script to analyze tenant data and generate insights on preferences for amenities like attached washrooms, parking, and kitchen facilities."
Generated: DETERMINISTIC_c105da1ded8b234d
Batch ID: 20250622_211735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

class TenantAnalyzer:
    """
    A class to analyze tenant data and generate insights on amenity preferences.
    
    Attributes:
        data (pd.DataFrame): DataFrame containing tenant data.
        amenities (list): List of amenities to analyze.
    """
    
    def __init__(self, data_path):
        """
        Initialize the TenantAnalyzer with data from the given path.
        
        Args:
            data_path (str): Path to the CSV file containing tenant data.
        """
        try:
            self.data = pd.read_csv(data_path)
            self.amenities = ['attached_washroom', 'parking', 'kitchen_facilities']
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError("The specified data file was not found.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {e}")
    
    def _validate_data(self):
        """
        Validate the data to ensure required columns are present.
        
        Raises:
            ValueError: If required columns are missing.
        """
        required_columns = ['tenant_id'] + self.amenities
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
    
    def calculate_amenity_preferences(self):
        """
        Calculate the percentage of tenants preferring each amenity.
        
        Returns:
            dict: A dictionary with amenities as keys and preference percentages as values.
        """
        preferences = {}
        total_tenants = len(self.data)
        
        for amenity in self.amenities:
            count = self.data[amenity].sum()
            percentage = (count / total_tenants) * 100
            preferences[amenity] = round(percentage, 2)
        
        return preferences
    
    def generate_insights(self):
        """
        Generate insights based on amenity preferences.
        
        Returns:
            dict: A dictionary containing insights and visualizations.
        """
        preferences = self.calculate_amenity_preferences()
        insights = {
            'preferences': preferences,
            'most_preferred': max(preferences, key=preferences.get),
            'least_preferred': min(preferences, key=preferences.get)
        }
        
        return insights
    
    def plot_preferences(self):
        """
        Generate a bar plot showing amenity preferences.
        """
        preferences = self.calculate_amenity_preferences()
        plt.figure(figsize=(10, 6))
        plt.bar(preferences.keys(), preferences.values(), color='skyblue')
        plt.title('Tenant Amenity Preferences')
        plt.xlabel('Amenities')
        plt.ylabel('Percentage Preference')
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    
    def save_insights(self, output_path):
        """
        Save the insights to a CSV file.
        
        Args:
            output_path (str): Path to save the insights CSV file.
        """
        insights = self.generate_insights()
        df = pd.DataFrame.from_dict(insights['preferences'], orient='index', columns=['percentage'])
        df.to_csv(output_path, index_label='amenity')

# Example usage
if __name__ == "__main__":
    try:
        analyzer = TenantAnalyzer('tenant_data.csv')
        insights = analyzer.generate_insights()
        print("Amenity Preferences:", insights['preferences'])
        print("Most Preferred Amenity:", insights['most_preferred'])
        print("Least Preferred Amenity:", insights['least_preferred'])
        analyzer.plot_preferences()
        analyzer.save_insights('amenity_preferences.csv')
    except Exception as e:
        print(f"Error: {e}")
```
