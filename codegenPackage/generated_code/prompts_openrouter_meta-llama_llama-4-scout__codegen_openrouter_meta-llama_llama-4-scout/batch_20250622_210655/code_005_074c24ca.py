"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Develop a use case for a Geographic Information System (GIS) to manage and analyze geological and geotechnical data for construction projects, similar to those undertaken by URANPRES, s.r.o."
Generated: DETERMINISTIC_074c24ca2361e0ab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon
from typing import Dict, List

class GeologicalData:
    """Class to manage and analyze geological and geotechnical data."""

    def __init__(self, data: Dict):
        """
        Initialize the GeologicalData class.

        Args:
        - data (Dict): A dictionary containing geological and geotechnical data.
        """
        self.data = data

    def validate_data(self) -> bool:
        """
        Validate the input data.

        Returns:
        - bool: True if the data is valid, False otherwise.
        """
        required_keys = ['location', 'geology', 'geotechnics']
        return all(key in self.data for key in required_keys)

    def create_geopandas_df(self) -> gpd.GeoDataFrame:
        """
        Create a GeoPandas DataFrame from the input data.

        Returns:
        - gpd.GeoDataFrame: A GeoPandas DataFrame containing the geological and geotechnical data.
        """
        try:
            # Create a dictionary to store the data
            data_dict = {
                'location': [],
                'geology': [],
                'geotechnics': [],
                'geometry': []
            }

            # Iterate over the input data
            for item in self.data['location']:
                # Create a Point geometry object
                point = Point(item['x'], item['y'])

                # Append the data to the dictionary
                data_dict['location'].append(item)
                data_dict['geology'].append(self.data['geology'])
                data_dict['geotechnics'].append(self.data['geotechnics'])
                data_dict['geometry'].append(point)

            # Create a Pandas DataFrame
            df = pd.DataFrame(data_dict)

            # Convert the DataFrame to a GeoPandas DataFrame
            gdf = gpd.GeoDataFrame(df, geometry='geometry')

            return gdf

        except Exception as e:
            print(f"An error occurred: {e}")
            return None


class GIS:
    """Class to manage and analyze geological and geotechnical data for construction projects."""

    def __init__(self):
        """
        Initialize the GIS class.
        """
        self.geological_data = []

    def add_geological_data(self, data: Dict):
        """
        Add geological and geotechnical data to the GIS.

        Args:
        - data (Dict): A dictionary containing geological and geotechnical data.
        """
        geological_data = GeologicalData(data)
        if geological_data.validate_data():
            self.geological_data.append(geological_data)
        else:
            print("Invalid data")

    def analyze_data(self) -> List[gpd.GeoDataFrame]:
        """
        Analyze the geological and geotechnical data.

        Returns:
        - List[gpd.GeoDataFrame]: A list of GeoPandas DataFrames containing the analyzed data.
        """
        analyzed_data = []
        for data in self.geological_data:
            gdf = data.create_geopandas_df()
            if gdf is not None:
                analyzed_data.append(gdf)

        return analyzed_data


def main():
    # Example usage
    gis = GIS()

    data1 = {
        'location': [{'x': 10, 'y': 20}],
        'geology': 'rock',
        'geotechnics': 'stable'
    }

    data2 = {
        'location': [{'x': 30, 'y': 40}],
        'geology': 'soil',
        'geotechnics': 'unstable'
    }

    gis.add_geological_data(data1)
    gis.add_geological_data(data2)

    analyzed_data = gis.analyze_data()

    for i, gdf in enumerate(analyzed_data):
        print(f"Analyzed Data {i+1}:")
        print(gdf)


if __name__ == "__main__":
    main()
```
