"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generate-digital.com
Prompt: Develop a script to calculate the valuation of digital assets and inventory for sports and entertainment businesses, incorporating partner-specific breakdowns as detailed by Generate Digital.
Generated: DETERMINISTIC_d11c6686682e64e1
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Any

class DigitalAssetValuation:
    def __init__(self, assets: List[Dict[str, Any]]):
        """
        Initializes the DigitalAssetValuation with a list of digital assets.
        
        :param assets: A list of dictionaries containing digital asset data.
        """
        self.assets = assets

    def calculate_valuation(self) -> Dict[str, float]:
        """
        Calculates the total valuation of digital assets categorically.

        :return: A dictionary containing the total valuation by category.
        """
        valuation = {}
        
        for asset in self.assets:
            category = asset.get("category")
            value = asset.get("value", 0.0)

            if category not in valuation:
                valuation[category] = 0.0
            
            valuation[category] += value
        
        return valuation

    def breakdown_by_partner(self) -> Dict[str, Dict[str, float]]:
        """
        Breaks down the asset valuation by partners.

        :return: A dictionary containing valuations per partner and category.
        """
        partner_valuation = {}

        for asset in self.assets:
            partner = asset.get("partner")
            category = asset.get("category")
            value = asset.get("value", 0.0)

            if partner not in partner_valuation:
                partner_valuation[partner] = {}

            if category not in partner_valuation[partner]:
                partner_valuation[partner][category] = 0.0
            
            partner_valuation[partner][category] += value

        return partner_valuation

def load_assets_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Loads digital assets from a JSON file.
    
    :param file_path: The path to the JSON file containing asset data.
    :return: A list of digital assets.
    :raises FileNotFoundError: If the file cannot be found.
    :raises json.JSONDecodeError: If the JSON is malformed.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: The file {file_path} was not found.") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Error: The file {file_path} contains invalid JSON.") from e

def main():
    """
    Main function to load assets, calculate valuations, and print results.
    """
    try:
        # Load digital assets from a JSON file
        assets = load_assets_from_json('digital_assets.json')

        # Create a DigitalAssetValuation instance
        valuation_calculator = DigitalAssetValuation(assets)

        # Calculate overall valuation
        overall_valuation = valuation_calculator.calculate_valuation()
        print("Overall Valuation by Category:")
        for category, total in overall_valuation.items():
            print(f"{category}: ${total:,.2f}")

        # Calculate breakdown by partner
        partner_breakdown = valuation_calculator.breakdown_by_partner()
        print("\nValuation Breakdown by Partner:")
        for partner, categories in partner_breakdown.items():
            print(f"Partner: {partner}")
            for category, total in categories.items():
                print(f"  {category}: ${total:,.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```
