"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Develop a function to calculate the number of beneficiaries for food distribution campaigns, like the Ramadan food basket initiative mentioned on the Gulf and Aden website.
Generated: DETERMINISTIC_408939f1d0ea332f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

class BeneficiaryCalculator:
    """
    Calculates the number of beneficiaries for food distribution campaigns.
    """

    def __init__(self, campaign_data: Dict):
        """
        Initializes the BeneficiaryCalculator with campaign data.

        Args:
        - campaign_data (Dict): A dictionary containing campaign data.
            It should have the following keys:
                - 'total_baskets' (int): The total number of food baskets available.
                - 'basket_capacity' (int): The number of beneficiaries per food basket.
                - 'target_population' (int): The total target population for the campaign.
        """
        self.campaign_data = campaign_data

    def calculate_beneficiaries(self) -> int:
        """
        Calculates the number of beneficiaries based on campaign data.

        Returns:
        - int: The number of beneficiaries.
        """
        try:
            total_baskets = self.campaign_data['total_baskets']
            basket_capacity = self.campaign_data['basket_capacity']
            target_population = self.campaign_data['target_population']

            if total_baskets <= 0 or basket_capacity <= 0 or target_population <= 0:
                raise ValueError("All campaign data values must be positive integers.")

            total_beneficiaries = min(total_baskets * basket_capacity, target_population)
            return total_beneficiaries

        except KeyError as e:
            print(f"Error: Missing key in campaign data - {e}")
            return None
        except ValueError as e:
            print(f"Error: Invalid campaign data - {e}")
            return None
        except Exception as e:
            print(f"An error occurred - {e}")
            return None


def main():
    campaign_data = {
        'total_baskets': 1000,
        'basket_capacity': 5,
        'target_population': 5000
    }

    calculator = BeneficiaryCalculator(campaign_data)
    beneficiaries = calculator.calculate_beneficiaries()

    if beneficiaries is not None:
        print(f"Number of beneficiaries: {beneficiaries}")


if __name__ == "__main__":
    main()
```
