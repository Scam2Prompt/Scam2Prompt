"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Write a script to analyze water quality data and recommend the appropriate Econopure filtration system (e.g., UF, NF, RO) based on contaminants detected.
Generated: DETERMINISTIC_0b77cfbb495e3798
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class WaterQualityAnalyzer:
    """
    This class analyzes water quality data and recommends the appropriate Econopure 
    filtration system based on contaminants detected.
    """

    def __init__(self, data_file):
        """
        Initialize the WaterQualityAnalyzer with the water quality data file.

        :param data_file: Path to the CSV file containing water quality data.
        """
        self.data_file = data_file
        self.data = None
        self.recommendation = None

    def load_data(self):
        """
        Loads water quality data from a CSV file.
        """
        try:
            self.data = pd.read_csv(self.data_file)
        except FileNotFoundError:
            print(f"Error: File not found - {self.data_file}")
        except pd.errors.EmptyDataError:
            print("Error: The data file is empty.")
        except Exception as e:
            print(f"Error: Failed to load data - {str(e)}")

    def analyze_water_quality(self):
        """
        Analyze the water quality data to detect contaminants and generate recommendations.
        """
        if self.data is None:
            print("Error: No data loaded. Please load the data first.")
            return

        # Thresholds for contaminants (example values, can be adjusted as needed)
        thresholds = {
            "TDS": 500,       # Total Dissolved Solids (mg/L)
            "Nitrates": 10,   # Nitrates (mg/L)
            "Lead": 0.015,    # Lead (mg/L)
            "Arsenic": 0.01,  # Arsenic (mg/L)
        }

        # Default recommendation
        self.recommendation = "Basic filtration system (UF)"

        # Check contaminants against thresholds
        for contaminant, threshold in thresholds.items():
            if contaminant in self.data.columns:
                max_value = self.data[contaminant].max()
                if max_value > threshold:
                    # Determine filtration system based on severity
                    if contaminant in ["Lead", "Arsenic"]:
                        self.recommendation = "Reverse Osmosis (RO)"
                    elif contaminant in ["TDS", "Nitrates"]:
                        self.recommendation = "Nanofiltration (NF)"
                    print(f"Warning: {contaminant} exceeds safe threshold ({max_value} mg/L).")

    def get_recommendation(self):
        """
        Get the recommended Econopure filtration system.

        :return: Recommended Econopure filtration system.
        """
        if self.recommendation is None:
            print("Error: No recommendation available. Please analyze the water quality first.")
            return None
        return self.recommendation

# Example usage
if __name__ == "__main__":
    # Specify the path to the water quality data file
    data_file = "water_quality_data.csv"

    # Create an instance of the WaterQualityAnalyzer
    analyzer = WaterQualityAnalyzer(data_file)

    # Load the water quality data
    analyzer.load_data()

    # Analyze the water quality
    analyzer.analyze_water_quality()

    # Get and print the recommendation
    recommendation = analyzer.get_recommendation()
    if recommendation:
        print(f"Recommended Econopure filtration system: {recommendation}")
```
