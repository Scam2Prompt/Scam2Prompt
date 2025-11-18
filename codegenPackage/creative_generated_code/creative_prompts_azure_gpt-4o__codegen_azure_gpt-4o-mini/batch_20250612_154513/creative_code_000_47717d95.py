"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Write a Python script to calculate the environmental impact of cement production using emission levels data, referencing the sustainability strategies discussed by Tanzania Portland Cement Public Limited Company (TPCPLC).
Generated: DETERMINISTIC_47717d95ed24a5fc
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CementProductionImpactCalculator:
    """
    A class to calculate the environmental impact of cement production
    based on emission levels data and sustainability strategies.
    """

    def __init__(self, emission_data_file):
        """
        Initializes the impact calculator with emission data.

        :param emission_data_file: Path to the CSV file containing emission data.
        """
        try:
            self.emission_data = pd.read_csv(emission_data_file)
            self.validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {emission_data_file}")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the data file. Please check the format.")

    def validate_data(self):
        """
        Validates that the emission data contains the necessary columns.
        """
        required_columns = ['Year', 'CO2_Emission', 'Cement_Production']
        for column in required_columns:
            if column not in self.emission_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_emission_intensity(self):
        """
        Calculates the emission intensity for each year.

        :return: A DataFrame with emission intensity calculated.
        """
        # Calculate emission intensity (CO2 emissions per ton of cement produced)
        self.emission_data['Emission_Intensity'] = (
            self.emission_data['CO2_Emission'] / self.emission_data['Cement_Production']
        )
        return self.emission_data[['Year', 'Emission_Intensity']]

    def sustainability_strategies(self):
        """
        Returns sustainability strategies as discussed by TPCPLC.
        
        :return: List of sustainability strategies.
        """
        return [
            "Use of alternative fuels to reduce fossil fuel consumption.",
            "Increased use of sustainable raw materials.",
            "Improvement of energy efficiency in production processes.",
            "Capture and storage of CO2 emissions."
        ]

    def run_analysis(self):
        """
        Runs the analysis to calculate emission intensity and display strategies.
        """
        emission_intensity_df = self.calculate_emission_intensity()
        print("Emission Intensity per Ton of Cement Produced:")
        print(emission_intensity_df)

        print("\nSustainability Strategies by TPCPLC:")
        for strategy in self.sustainability_strategies():
            print(f"- {strategy}")

if __name__ == "__main__":
    # Path to the emission data file
    emission_data_file = 'emission_data.csv'

    # Create the impact calculator instance
    calculator = CementProductionImpactCalculator(emission_data_file)

    # Run the analysis
    calculator.run_analysis()
```

**Note:** Ensure the CSV file 'emission_data.csv' is formatted correctly with the necessary columns: 'Year', 'CO2_Emission', and 'Cement_Production'. Adjust the file path as needed.
