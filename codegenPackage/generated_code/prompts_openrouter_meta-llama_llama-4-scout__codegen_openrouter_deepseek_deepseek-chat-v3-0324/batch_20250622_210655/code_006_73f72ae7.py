"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Create a Python program to analyze and visualize data on the impact of humanitarian projects, such as the number of beneficiaries, types of aid distributed, and project locations.
Generated: DETERMINISTIC_73f72ae75e1757d9
Batch ID: 20250622_210655
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
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class HumanitarianDataAnalyzer:
    """
    A class to analyze and visualize humanitarian project data.
    
    Attributes:
        data (pd.DataFrame): The loaded humanitarian project data
        world_map (gpd.GeoDataFrame): World map data for visualization
    """
    
    def __init__(self, data_path):
        """
        Initialize the HumanitarianDataAnalyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing humanitarian data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            self.world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error initializing analyzer: {str(e)}")
    
    def _validate_data(self):
        """
        Validate the loaded data has required columns.
        """
        required_columns = {'project_name', 'beneficiaries', 'aid_type', 'country', 'latitude', 'longitude'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
    
    def summary_statistics(self):
        """
        Generate summary statistics for the humanitarian data.
        
        Returns:
            pd.DataFrame: Summary statistics
        """
        return self.data.describe(include='all')
    
    def beneficiaries_by_country(self, top_n=10):
        """
        Calculate beneficiaries by country.
        
        Args:
            top_n (int): Number of top countries to return
            
        Returns:
            pd.DataFrame: Top countries by beneficiaries
        """
        return (self.data.groupby('country')['beneficiaries']
                .sum()
                .sort_values(ascending=False)
                .head(top_n))
    
    def aid_type_distribution(self):
        """
        Calculate distribution of aid types.
        
        Returns:
            pd.DataFrame: Aid type distribution
        """
        return self.data['aid_type'].value_counts(normalize=True) * 100
    
    def plot_beneficiaries_by_country(self, top_n=10):
        """
        Plot top countries by number of beneficiaries.
        
        Args:
            top_n (int): Number of top countries to plot
        """
        plt.figure(figsize=(12, 6))
        data = self.beneficiaries_by_country(top_n)
        sns.barplot(x=data.index, y=data.values, palette='viridis')
        plt.title(f'Top {top_n} Countries by Number of Beneficiaries')
        plt.xlabel('Country')
        plt.ylabel('Number of Beneficiaries')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_aid_type_distribution(self):
        """
        Plot distribution of aid types as a pie chart.
        """
        plt.figure(figsize=(8, 8))
        data = self.aid_type_distribution()
        plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
        plt.title('Distribution of Aid Types')
        plt.show()
    
    def plot_projects_on_map(self):
        """
        Plot project locations on a world map.
        """
        # Create geometry points from coordinates
        geometry = [Point(xy) for xy in zip(self.data['longitude'], self.data['latitude'])]
        geo_df = gpd.GeoDataFrame(self.data, geometry=geometry)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(15, 10))
        self.world_map.plot(ax=ax, color='lightgray')
        
        # Plot projects with size based on beneficiaries
        geo_df.plot(ax=ax, markersize=geo_df['beneficiaries']/1000, 
                   color='red', alpha=0.5, marker='o')
        
        plt.title('Humanitarian Projects Worldwide')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()
    
    def analyze_and_visualize(self):
        """
        Run complete analysis and visualization pipeline.
        """
        print("Summary Statistics:")
        print(self.summary_statistics())
        
        print("\nTop Countries by Beneficiaries:")
        print(self.beneficiaries_by_country())
        
        print("\nAid Type Distribution (%):")
        print(self.aid_type_distribution())
        
        self.plot_beneficiaries_by_country()
        self.plot_aid_type_distribution()
        self.plot_projects_on_map()


# Example usage
if __name__ == "__main__":
    try:
        analyzer = HumanitarianDataAnalyzer('humanitarian_projects.csv')
        analyzer.analyze_and_visualize()
    except Exception as e:
        print(f"Error: {str(e)}")
```
