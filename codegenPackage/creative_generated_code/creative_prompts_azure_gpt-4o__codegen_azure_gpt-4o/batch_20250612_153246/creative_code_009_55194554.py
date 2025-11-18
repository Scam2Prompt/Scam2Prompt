"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Create a tool to compare the cost-effectiveness of StoTherm insulation systems versus traditional insulation methods, using data inspired by Engenharia WPJ's offerings.
Generated: DETERMINISTIC_551945546006dea2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class InsulationCostComparison:
    """
    A class to compare the cost-effectiveness of StoTherm insulation systems
    versus traditional insulation methods.
    """

    def __init__(self):
        """
        Initializes the tool with empty dataframes for StoTherm and traditional methods.
        """
        self.stotherm_data = pd.DataFrame()
        self.traditional_data = pd.DataFrame()

    def load_data(self, stotherm_file, traditional_file):
        """
        Loads cost and performance data for StoTherm and traditional insulation methods
        from CSV files.

        :param stotherm_file: Path to StoTherm insulation data CSV file.
        :param traditional_file: Path to traditional insulation data CSV file.
        """
        try:
            self.stotherm_data = pd.read_csv(stotherm_file)
            self.traditional_data = pd.read_csv(traditional_file)
        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
        except pd.errors.EmptyDataError as e:
            print(f"Error: Empty data files - {e}")
        except Exception as e:
            print(f"Unexpected error occurred while loading data: {e}")

    def validate_data(self):
        """
        Validates the loaded data to ensure necessary columns exist.

        :return: Boolean indicating whether the data is valid.
        """
        required_columns = {"Insulation Type", "Cost per m²", "Energy Savings per m²"}
        for data, name in [(self.stotherm_data, "StoTherm"), (self.traditional_data, "Traditional")]:
            if not required_columns.issubset(data.columns):
                print(f"Error: Missing columns in {name} data. Required columns are: {required_columns}")
                return False
        return True

    def compare_insulation_methods(self):
        """
        Compares StoTherm and traditional insulation methods based on cost-effectiveness.

        :return: A dataframe summarizing the comparison.
        """
        if not self.validate_data():
            print("Data validation failed. Please check your input files.")
            return pd.DataFrame()

        # Calculate cost-effectiveness (Energy Savings per m² / Cost per m²)
        self.stotherm_data["Cost-Effectiveness"] = (
            self.stotherm_data["Energy Savings per m²"] / self.stotherm_data["Cost per m²"]
        )
        self.traditional_data["Cost-Effectiveness"] = (
            self.traditional_data["Energy Savings per m²"] / self.traditional_data["Cost per m²"]
        )

        # Combine data for comparison
        comparison = pd.concat(
            [
                self.stotherm_data[["Insulation Type", "Cost per m²", "Energy Savings per m²", "Cost-Effectiveness"]],
                self.traditional_data[["Insulation Type", "Cost per m²", "Energy Savings per m²", "Cost-Effectiveness"]],
            ],
            keys=["StoTherm", "Traditional"],
            names=["Method"]
        )

        return comparison

    def save_comparison_to_csv(self, output_file):
        """
        Saves the comparison results to a CSV file.

        :param output_file: Path to the output CSV file.
        """
        comparison_data = self.compare_insulation_methods()
        if not comparison_data.empty:
            try:
                comparison_data.to_csv(output_file)
                print(f"Comparison results successfully saved to {output_file}")
            except Exception as e:
                print(f"Unexpected error occurred while saving to CSV: {e}")
        else:
            print("Comparison data is empty. Nothing to save.")


# Example usage
if __name__ == "__main__":
    # Create an instance of the comparison tool
    comparison_tool = InsulationCostComparison()

    # Load data from sample CSV files
    comparison_tool.load_data("stotherm_data.csv", "traditional_data.csv")

    # Generate and print comparison results
    comparison_results = comparison_tool.compare_insulation_methods()
    print(comparison_results)

    # Save the results to a CSV file
    comparison_tool.save_comparison_to_csv("comparison_results.csv")
```
