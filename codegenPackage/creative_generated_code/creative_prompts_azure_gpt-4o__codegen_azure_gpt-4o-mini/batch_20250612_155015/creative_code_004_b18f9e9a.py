"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket-soto.pages.dev
Prompt: Write code to perform a comparative analysis of Polymarket's predicted probabilities and the actual trade outcome for Juan Soto, highlighting discrepancies in predictions versus reality.
Generated: DETERMINISTIC_b18f9e9a50b3e89c
Batch ID: 20250612_155015
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.polymarket.com/v1/predictions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.polymarket.com/v1/outcomes": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class PolymarketAnalysis:
    """
    A class to perform comparative analysis of Polymarket's predicted probabilities and actual trade outcomes.
    """

    def __init__(self, prediction_url, outcome_url):
        """
        Initializes the PolymarketAnalysis with URLs for prediction and outcome data.
        
        Args:
            prediction_url (str): URL to fetch Polymarket's predicted probabilities.
            outcome_url (str): URL to fetch the actual trade outcome.
        """
        self.prediction_url = prediction_url
        self.outcome_url = outcome_url
        self.predictions = None
        self.outcomes = None

    def fetch_data(self):
        """Fetches prediction and outcome data from the specified URLs."""
        try:
            self.predictions = pd.read_json(self.prediction_url)
            self.outcomes = pd.read_json(self.outcome_url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
        except ValueError as e:
            print(f"Error processing JSON: {e}")

    def clean_data(self):
        """Cleans and prepares the data for analysis."""
        # Ensure both datasets have the necessary columns
        required_columns = ['market_name', 'probability']
        if not all(col in self.predictions.columns for col in required_columns):
            raise ValueError("Predictions data is missing required columns.")
        if 'outcome' not in self.outcomes.columns:
            raise ValueError("Outcomes data is missing required columns.")

        # Filter for Juan Soto market
        self.predictions = self.predictions[self.predictions['market_name'].str.contains('Juan Soto', case=False)]
        self.outcomes = self.outcomes[self.outcomes['market_name'].str.contains('Juan Soto', case=False)]

    def analyze_discrepancies(self):
        """Analyzes discrepancies between predicted probabilities and actual outcomes."""
        # Merge predictions with outcomes on market name
        analysis_df = pd.merge(self.predictions, self.outcomes, on='market_name', how='inner', suffixes=('_pred', '_actual'))

        # Calculate discrepancy
        analysis_df['discrepancy'] = analysis_df['probability'] - analysis_df['outcome']
        
        return analysis_df

    def plot_discrepancies(self, analysis_df):
        """Plots the discrepancies for visualization."""
        plt.figure(figsize=(10, 6))
        plt.bar(analysis_df['market_name'], analysis_df['discrepancy'], color='blue')
        plt.axhline(0, color='red', linestyle='--')
        plt.title("Discrepancy Analysis: Predicted vs Actual Outcomes for Juan Soto")
        plt.xlabel("Market Name")
        plt.ylabel("Discrepancy in Prediction")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    # Define URLs for prediction and outcome data
    prediction_url = 'https://api.polymarket.com/v1/predictions'  # Placeholder URL
    outcome_url = 'https://api.polymarket.com/v1/outcomes'  # Placeholder URL
    
    analysis = PolymarketAnalysis(prediction_url, outcome_url)
    analysis.fetch_data()
    
    if analysis.predictions is not None and analysis.outcomes is not None:
        analysis.clean_data()
        discrepancies_df = analysis.analyze_discrepancies()
        print(discrepancies_df)

        # Plotting discrepancies
        analysis.plot_discrepancies(discrepancies_df)

if __name__ == "__main__":
    main()
```
