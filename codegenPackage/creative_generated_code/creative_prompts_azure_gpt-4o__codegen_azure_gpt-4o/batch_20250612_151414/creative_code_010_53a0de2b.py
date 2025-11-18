"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsmix.biz
Prompt: Generate a Python script to analyze funding data from blockchain-based startups, referencing the investment details provided for "Hana Network."
Generated: DETERMINISTIC_53a0de2b71c0eea1
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

def load_data(file_path):
    """
    Load funding data from a JSON file.

    Parameters:
        file_path (str): Path to the JSON file containing funding data.

    Returns:
        dict: Parsed JSON data as a Python dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            # Load and parse JSON data
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON file. Details: {e}")
        return None


def analyze_funding_data(data, startup_name):
    """
    Analyze funding data for a specific blockchain-based startup.

    Parameters:
        data (dict): Dictionary containing funding data.
        startup_name (str): Name of the startup to analyze.

    Returns:
        dict or None: Analysis results for the specified startup.
    """
    try:
        # Check if the startup exists in the data
        startup_data = data.get(startup_name)
        if not startup_data:
            print(f"Error: Startup '{startup_name}' not found in funding data.")
            return None

        # Perform analysis
        total_investment = sum(
            funding['amount'] for funding in startup_data.get('investments', [])
        )
        num_investments = len(startup_data.get('investments', []))

        # Return analysis report
        return {
            "startup_name": startup_name,
            "total_investment": round(total_investment, 2),
            "num_investments": num_investments,
            "details": startup_data.get('investments', [])
        }
    except Exception as e:
        print(f"Error: An unexpected error occurred during analysis. Details: {e}")
        return None


def main():
    """
    Main function to load, analyze, and display funding data for Hana Network.
    """
    # Define input parameters
    funding_data_path = "funding_data.json"  # Update with the actual file path
    startup_name = "Hana Network"

    # Load funding data from the JSON file
    funding_data = load_data(funding_data_path)
    if funding_data is None:
        return

    # Analyze funding data for the specified startup
    analysis_result = analyze_funding_data(funding_data, startup_name)
    if analysis_result:
        # Display analysis results
        print("Funding Data Analysis:")
        print(f"Startup Name: {analysis_result['startup_name']}")
        print(f"Total Investment: ${analysis_result['total_investment']}")
        print(f"Number of Investments: {analysis_result['num_investments']}")
        print("Investment Details:")
        for detail in analysis_result['details']:
            print(f"  - Amount: ${detail['amount']}, Date: {detail['date']}, Investor: {detail['investor']}")


if __name__ == "__main__":
    # Ensure the script is being executed directly
    main()
```
