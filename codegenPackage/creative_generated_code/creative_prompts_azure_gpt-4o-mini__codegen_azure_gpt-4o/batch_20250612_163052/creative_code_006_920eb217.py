"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.nl
Prompt: How does Immediate Peak help users understand the risks and opportunities associated with different types of investments?
Generated: DETERMINISTIC_920eb217264b8950
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import csv
import logging
from typing import List, Dict, Tuple

# Configure logging for error handling and tracking
logging.basicConfig(
    filename="investment_analysis.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_investment_data(file_path: str) -> List[Dict[str, str]]:
    """
    Loads investment data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing investment data.
        
    Returns:
        List[Dict[str, str]]: List of investment records as dictionaries.
    """
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            logging.info("Investment data loaded successfully.")
            return list(csv_reader)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error occurred while loading data: {str(e)}")
        raise

def analyze_risks_and_opportunities(data: List[Dict[str, str]]) -> Tuple[Dict[str, float], Dict[str, float]]:
    """
    Analyzes risks and opportunities based on investment data.
    
    Args:
        data (List[Dict[str, str]]): List of investment records.
        
    Returns:
        Tuple[Dict[str, float], Dict[str, float]]: 
            A dictionary containing risk scores and a dictionary containing opportunity scores.
    """
    risk_scores = {}
    opportunity_scores = {}

    try:
        for item in data:
            investment_type = item.get("investment_type", "Unknown")
            risk_factor = float(item.get("risk_factor", 0))
            opportunity_factor = float(item.get("opportunity_factor", 0))

            # Accumulate scores for each investment type
            risk_scores[investment_type] = risk_scores.get(investment_type, 0) + risk_factor
            opportunity_scores[investment_type] = opportunity_scores.get(investment_type, 0) + opportunity_factor

        logging.info("Risk and opportunity analysis completed successfully.")
        return risk_scores, opportunity_scores
    except ValueError as e:
        logging.error(f"Error parsing numerical values in data: {str(e)}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error during analysis: {str(e)}")
        raise

def display_analysis(risks: Dict[str, float], opportunities: Dict[str, float]) -> None:
    """
    Displays the analysis of risks and opportunities.
    
    Args:
        risks (Dict[str, float]): Dictionary containing risk scores.
        opportunities (Dict[str, float]): Dictionary containing opportunity scores.
    """
    print("Investment Risk and Opportunity Analysis:")
    print("------------------------------------------")
    print(f"{'Investment Type':<20}{'Risk Score':<15}{'Opportunity Score':<15}")
    print("------------------------------------------")
    for investment_type in risks.keys():
        print(f"{investment_type:<20}{risks[investment_type]:<15.2f}{opportunities.get(investment_type, 0):<15.2f}")
    print("------------------------------------------")

def main():
    """
    Main function to execute the investment analysis workflow.
    """
    # Path to the CSV file containing investment data
    file_path = "investment_data.csv"

    try:
        # Load investment data
        investment_data = load_investment_data(file_path)
        
        # Analyze risks and opportunities
        risks, opportunities = analyze_risks_and_opportunities(investment_data)
        
        # Display the analysis results
        display_analysis(risks, opportunities)
    except Exception as e:
        logging.error(f"Error in main workflow: {str(e)}")
        print("An error occurred during the investment analysis. Check the logs for details.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
