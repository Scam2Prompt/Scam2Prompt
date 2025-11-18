"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Write Python code to analyze real estate investment opportunities, focusing on land acquisition and development strategies similar to those described by Carolina Capital.
Generated: DETERMINISTIC_9c72d983b8233270
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class RealEstateAnalyzer:
    """
    A class to analyze real estate investment opportunities focused on land acquisition and development strategies.
    """

    def __init__(self, data_file):
        """
        Initializes the RealEstateAnalyzer with the provided data file.

        Args:
            data_file (str): The path to the CSV file containing real estate data.
        """
        try:
            self.data = pd.read_csv(data_file)
            self.clean_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided file is empty. Please provide a valid data file.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the data file. Please check the file format.")

    def clean_data(self):
        """
        Cleans the dataset by handling missing values and normalizing data types.
        """
        # Drop rows with missing critical data
        self.data.dropna(subset=['Location', 'Price', 'Size', 'PotentialROI'], inplace=True)

        # Convert data types if necessary
        self.data['Price'] = self.data['Price'].astype(float)
        self.data['Size'] = self.data['Size'].astype(float)
        self.data['PotentialROI'] = self.data['PotentialROI'].astype(float)

    def analyze_opportunities(self, min_roi=0.1):
        """
        Analyzes the dataset for investment opportunities with a potential ROI above the specified threshold.

        Args:
            min_roi (float): The minimum potential ROI percentage for an opportunity to be considered viable.

        Returns:
            DataFrame: A DataFrame containing opportunities that meet the ROI criteria.
        """
        opportunities = self.data[self.data['PotentialROI'] >= min_roi]
        return opportunities[['Location', 'Price', 'Size', 'PotentialROI']]

    def summarize_opportunities(self):
        """
        Summarizes the investment opportunities by calculating total cost and average ROI.

        Returns:
            dict: A summary containing total cost and average ROI of viable opportunities.
        """
        viable_opportunities = self.analyze_opportunities()
        total_cost = viable_opportunities['Price'].sum()
        average_roi = viable_opportunities['PotentialROI'].mean()

        return {
            'Total Cost': total_cost,
            'Average ROI': average_roi
        }

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = RealEstateAnalyzer('real_estate_data.csv')
        opportunities = analyzer.analyze_opportunities(min_roi=0.15)
        print("Viable Investment Opportunities:")
        print(opportunities)

        summary = analyzer.summarize_opportunities()
        print("Investment Summary:")
        print(summary)
    except Exception as e:
        print(f"An error occurred: {e}")
```
