"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.pages.dev
Prompt: Write a script to analyze the capital efficiency of liquidity provision on Magpie XYZ across different platforms, using the provided TVL data.
Generated: DETERMINISTIC_9714ba67ea97ef51
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to analyze capital efficiency of liquidity provision across different platforms on Magpie XYZ
import json
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_tvl_data(file_path: str) -> Dict[str, float]:
    """
    Load Total Value Locked (TVL) data from a JSON file.

    :param file_path: Path to the JSON file containing TVL data
    :return: Dictionary with platform names as keys and TVL values as floats
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return {key: float(value) for key, value in data.items()}
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Failed to decode JSON from file: {file_path}")
        raise
    except ValueError:
        logging.error(f"Invalid TVL data format in file: {file_path}")
        raise

def calculate_capital_efficiency(tvl_data: Dict[str, float]) -> List[Dict[str, float]]:
    """
    Calculate capital efficiency for each platform.

    Capital Efficiency = TVL / Sum(TVL for all platforms)

    :param tvl_data: Dictionary with platform names as keys and TVL values as floats
    :return: List of dictionaries with platform name and capital efficiency percentage
    """
    if not tvl_data:
        logging.error("TVL data is empty.")
        raise ValueError("TVL data cannot be empty.")

    total_tvl = sum(tvl_data.values())
    if total_tvl == 0:
        logging.error("Total TVL across all platforms is zero.")
        raise ValueError("Total TVL cannot be zero.")

    efficiency_results = []
    for platform, tvl in tvl_data.items():
        efficiency_percentage = (tvl / total_tvl) * 100
        efficiency_results.append({
            "platform": platform,
            "capital_efficiency_percentage": round(efficiency_percentage, 2)
        })
    
    return efficiency_results

def main():
    """
    Main function to execute the script.
    """
    # Specify the path to the TVL JSON data file
    tvl_file_path = 'tvl_data.json'

    try:
        # Step 1: Load TVL data
        logging.info("Loading TVL data...")
        tvl_data = load_tvl_data(tvl_file_path)

        # Step 2: Calculate capital efficiency
        logging.info("Calculating capital efficiency...")
        efficiency_results = calculate_capital_efficiency(tvl_data)

        # Step 3: Display results
        logging.info("Capital Efficiency Analysis Results:")
        for result in efficiency_results:
            logging.info(f"Platform: {result['platform']} - Efficiency: {result['capital_efficiency_percentage']}%")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
