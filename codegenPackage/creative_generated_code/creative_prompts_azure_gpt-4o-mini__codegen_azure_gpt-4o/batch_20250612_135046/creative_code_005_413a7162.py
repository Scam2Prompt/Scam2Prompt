"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensee.io
Prompt: Illustrate how to implement ESG risk analysis in a financial application, using the guidelines provided by Opensee for climate-related data management.
Generated: DETERMINISTIC_413a7162b4617fed
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class ESGRiskAnalyzer:
    """
    A class to implement ESG (Environmental, Social, Governance) risk analysis in a financial application,
    using climate-related data management guidelines.
    """
    
    def __init__(self, data_source):
        """
        Initialize the ESGRiskAnalyzer instance.

        Parameters:
        data_source (str): Path to the climate-related data CSV file.
        """
        self.data_source = data_source
        self.data = None

    def load_data(self):
        """
        Load climate-related data into a Pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_source)
            # Ensure the data contains the required ESG fields
            required_columns = ['Company', 'Environmental_Score', 'Social_Score', 'Governance_Score']
            for column in required_columns:
                if column not in self.data.columns:
                    raise ValueError(f"Missing required column: {column}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Data source '{self.data_source}' not found.")
        except pd.errors.EmptyDataError:
            raise ValueError(f"Data source '{self.data_source}' is empty or unreadable.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")
    
    def calculate_esg_risk(self):
        """
        Calculate ESG risk based on individual scores and return a summary.

        Returns:
        pd.DataFrame: DataFrame containing companies and their calculated ESG risk scores.
        """
        if self.data is None:
            raise RuntimeError("No data loaded. Please call 'load_data()' first.")

        try:
            # Normalize scores between 0 and 1 for consistent risk calculation
            self.data['Environmental_Risk'] = 1 - (self.data['Environmental_Score'] / 100)
            self.data['Social_Risk'] = 1 - (self.data['Social_Score'] / 100)
            self.data['Governance_Risk'] = 1 - (self.data['Governance_Score'] / 100)

            # Calculate overall ESG risk as a weighted average
            self.data['Overall_ESG_Risk'] = (
                0.4 * self.data['Environmental_Risk'] +
                0.3 * self.data['Social_Risk'] +
                0.3 * self.data['Governance_Risk']
            )
            
            # Return a simplified summary DataFrame
            return self.data[['Company', 'Overall_ESG_Risk']].sort_values(by='Overall_ESG_Risk', ascending=False)
        except KeyError as e:
            raise KeyError(f"Missing required data column during ESG Risk calculation: {e}")
        except Exception as e:
            raise Exception(f"An error occurred during ESG risk calculation: {e}")

    def generate_report(self, output_path):
        """
        Generate an ESG risk analysis report and save it to a CSV file.

        Parameters:
        output_path (str): Path to save the ESG risk report.
        """
        try:
            esg_risk_summary = self.calculate_esg_risk()
            esg_risk_summary.to_csv(output_path, index=False)
            print(f"ESG risk analysis report saved to '{output_path}'")
        except RuntimeError as e:
            print(f"Runtime error: {e}")
        except Exception as e:
            print(f"An error occurred while generating the report: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Path to climate-related data file
        data_source_path = "climate_data.csv"
        output_report_path = "esg_risk_report.csv"

        # Initialize and run ESG risk analysis
        esg_analyzer = ESGRiskAnalyzer(data_source_path)
        esg_analyzer.load_data()
        esg_analyzer.generate_report(output_report_path)
    except Exception as main_exception:
        print(f"An error occurred in the ESG risk analysis application: {main_exception}")
```
