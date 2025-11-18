"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myhealthcarebilling.com
Prompt: Create a script for analyzing unpaid claims and generating detailed account analysis reports, leveraging the A/R recovery strategies mentioned on My Healthcare Billing's site.
Generated: DETERMINISTIC_4887eece2f5d7f84
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
from datetime import datetime
import logging

# Configure logging for debugging and information tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClaimsAnalyzer:
    def __init__(self, claims_data_path, output_report_path):
        """
        Initializes the ClaimsAnalyzer with the path to the claims data and output report.
        
        :param claims_data_path: str, path to the CSV file containing claims data
        :param output_report_path: str, path where the output report will be saved
        """
        self.claims_data_path = claims_data_path
        self.output_report_path = output_report_path
        self.claims_data = self.load_claims_data()

    def load_claims_data(self):
        """
        Load claims data from a CSV file.
        
        :return: DataFrame containing claims data
        :raises FileNotFoundError: if the claims data file does not exist
        :raises ValueError: if the data cannot be converted to a DataFrame
        """
        try:
            claims_data = pd.read_csv(self.claims_data_path)
            logging.info("Claims data loaded successfully.")
            return claims_data
        except FileNotFoundError:
            logging.error(f"Claims data file not found: {self.claims_data_path}")
            raise
        except ValueError as e:
            logging.error(f"Error reading claims data: {e}")
            raise

    def analyze_unpaid_claims(self):
        """
        Analyze unpaid claims and generate a summary report.
        
        :return: DataFrame containing the analysis of unpaid claims
        """
        unpaid_claims = self.claims_data[self.claims_data['Status'] == 'Unpaid']
        logging.info(f"Identified {len(unpaid_claims)} unpaid claims.")

        # Perform aggregation and analysis
        report = unpaid_claims.groupby('AccountID').agg(
            TotalDue=('AmountDue', 'sum'),
            ClaimCount=('ClaimID', 'count'),
            LastClaimDate=('ClaimDate', 'max')
        ).reset_index()

        logging.info("Unpaid claims analysis completed.")
        return report

    def generate_report(self):
        """
        Generate and save the detailed account analysis report.
        """
        report = self.analyze_unpaid_claims()
        report.to_csv(self.output_report_path, index=False)
        logging.info(f"Report generated and saved at: {self.output_report_path}")

if __name__ == "__main__":
    # Set paths for claims data and output report
    claims_data_path = 'unpaid_claims.csv'  # Example path to the CSV file
    output_report_path = 'unpaid_claims_report.csv'  # Path to save the report

    try:
        # Initialize the ClaimsAnalyzer
        analyzer = ClaimsAnalyzer(claims_data_path, output_report_path)
        
        # Generate the report
        analyzer.generate_report()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

**Note**: Ensure the CSV file structure matches the expected format, including the relevant columns (Status, AmountDue, AccountID, ClaimID, ClaimDate) for the analysis to work correctly.
