"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indologicalindia.com
Prompt: Generate code to calculate the carbon offset achieved by "Indological India’s" tree-planting campaigns using environmental impact data.
Generated: DETERMINISTIC_927374cfd682aacf
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CarbonOffsetCalculator:
    """
    A class to calculate the carbon offset achieved by tree planting campaigns.

    Attributes:
    ----------
    tree_data : pd.DataFrame
        A DataFrame containing data about the trees planted, including species,
        age, and location, which impact the carbon offset calculation.
    """

    def __init__(self, tree_data: pd.DataFrame):
        """
        Initializes the CarbonOffsetCalculator with tree planting data.

        Parameters:
        ----------
        tree_data : pd.DataFrame
            DataFrame containing columns ['species', 'age', 'location', 'count'].
        """
        self.tree_data = tree_data

    def calculate_carbon_offset(self) -> float:
        """
        Calculates the total carbon offset in tons achieved by the tree planting campaigns.

        Returns:
        -------
        float
            The total carbon offset in tons.
        """
        try:
            # Validate that required columns are present
            required_columns = ['species', 'age', 'location', 'count']
            for column in required_columns:
                if column not in self.tree_data.columns:
                    raise ValueError(f"Missing required column: {column}")

            # Carbon sequestration rates per species (in tons per tree)
            sequestration_rates = {
                'Teak': 0.4,
                'Mango': 0.3,
                'Bamboo': 0.2,
                'Pine': 0.5,
                'Oak': 0.6
            }

            # Initialize total carbon offset
            total_offset = 0.0

            # Calculate total carbon offset based on species and count
            for index, row in self.tree_data.iterrows():
                species = row['species']
                count = row['count']

                # Get the sequestration rate for the species, defaulting to 0 if unknown
                sequestration_rate = sequestration_rates.get(species, 0)
                total_offset += sequestration_rate * count

            return total_offset

        except Exception as e:
            print(f"Error calculating carbon offset: {e}")
            return 0.0  # Return 0.0 in case of an error

# Example usage
if __name__ == "__main__":
    # Sample data for the tree planting campaigns
    data = {
        'species': ['Teak', 'Mango', 'Bamboo', 'Pine', 'Oak', 'Teak'],
        'age': [5, 3, 2, 8, 10, 6],
        'location': ['North', 'South', 'East', 'West', 'Central', 'North'],
        'count': [100, 150, 200, 250, 300, 100]
    }
    
    # Create DataFrame
    tree_df = pd.DataFrame(data)

    # Initialize the calculator
    calculator = CarbonOffsetCalculator(tree_df)

    # Calculate the carbon offset
    total_offset = calculator.calculate_carbon_offset()
    print(f"Total Carbon Offset: {total_offset:.2f} tons")
```
