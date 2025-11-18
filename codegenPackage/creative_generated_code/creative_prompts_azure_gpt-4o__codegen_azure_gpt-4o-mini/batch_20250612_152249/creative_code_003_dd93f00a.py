"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Develop a program that calculates property division according to Swedish "Sambolagen" (cohabitation law), as described on juridiskklinik.se.
Generated: DETERMINISTIC_dd93f00a41f91664
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PropertyDivision:
    def __init__(self, assets: dict):
        """
        Initializes the PropertyDivision class with a dictionary of assets.

        Parameters:
        assets (dict): A dictionary where keys are asset names (str) and values are their respective values (float).
        """
        if not isinstance(assets, dict):
            raise ValueError("Assets must be provided as a dictionary.")
        self.assets = assets

    def total_assets_value(self) -> float:
        """
        Calculates the total value of all assets.

        Returns:
        float: The total value of the assets.
        """
        total_value = sum(self.assets.values())
        return total_value

    def divide_assets(self) -> dict:
        """
        Divides the assets between two parties according to Swedish Sambolagen.

        Returns:
        dict: A dictionary containing the division of assets for both parties.
        """
        total_value = self.total_assets_value()

        if total_value == 0:
            raise ValueError("Total asset value cannot be zero.")

        # Each party receives half of the total assets
        party_share = total_value / 2

        # Prepare the division result
        division_result = {
            "Party1": {},
            "Party2": {}
        }

        # Distribute assets between the two parties
        current_party = "Party1"
        remaining_value = party_share

        for asset, value in sorted(self.assets.items(), key=lambda item: item[1], reverse=True):
            if remaining_value <= 0:
                current_party = "Party2"
                remaining_value = party_share
            
            division_result[current_party][asset] = value
            remaining_value -= value

            if remaining_value < 0:
                # If remaining_value goes negative, we need to adjust the last asset taken
                division_result[current_party][asset] = value + remaining_value
                division_result[current_party] = {k: v for k, v in division_result[current_party].items() if v > 0}
                break

        return division_result

    def get_summary(self) -> str:
        """
        Generates a summary of the asset division.

        Returns:
        str: A formatted string summarizing the division.
        """
        division = self.divide_assets()
        summary = "Asset Division Summary:\n"

        for party, assets in division.items():
            summary += f"{party}:\n"
            for asset, value in assets.items():
                summary += f"  - {asset}: {value:.2f}\n"

        return summary


# Example usage
if __name__ == "__main__":
    try:
        # Example assets
        assets_example = {
            "House": 3000000,
            "Car": 250000,
            "Savings": 500000
        }

        property_division = PropertyDivision(assets_example)
        print(property_division.get_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
