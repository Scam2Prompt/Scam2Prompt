"""
Generated Code Metadata:
========================
Original URL: https://standrewsibanda.org
Prompt: Create a fundraising campaign plan for a charity project aiming to help 400 children access quality education in Ibanda, Uganda, with a target of 8687 donors contributing 25+ Euros.
Generated: DETERMINISTIC_0c39816771f1a799
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class FundraisingCampaign:
    def __init__(self, target_donors: int, target_amount_per_donor: float, total_children: int):
        """
        Initialize the fundraising campaign with target donors, amount per donor, and total children to help.

        :param target_donors: The number of donors to reach.
        :param target_amount_per_donor: The amount each donor is expected to contribute.
        :param total_children: The total number of children to help.
        """
        self.target_donors = target_donors
        self.target_amount_per_donor = target_amount_per_donor
        self.total_children = total_children
        self.total_funds_needed = self.calculate_total_funds_needed()
        self.donors: List[Dict[str, float]] = []

    def calculate_total_funds_needed(self) -> float:
        """
        Calculate the total funds needed for the campaign.

        :return: Total funds needed.
        """
        return self.target_donors * self.target_amount_per_donor

    def add_donor(self, donor_name: str, amount: float) -> None:
        """
        Add a donor to the campaign.

        :param donor_name: The name of the donor.
        :param amount: The amount contributed by the donor.
        :raises ValueError: If the amount is less than the minimum required.
        """
        if amount < self.target_amount_per_donor:
            raise ValueError(f"Minimum contribution is {self.target_amount_per_donor} Euros.")
        
        self.donors.append({"name": donor_name, "amount": amount})

    def get_campaign_summary(self) -> Dict[str, float]:
        """
        Get a summary of the campaign including total funds raised and remaining funds needed.

        :return: A dictionary containing the summary of the campaign.
        """
        total_raised = sum(donor['amount'] for donor in self.donors)
        remaining_funds = self.total_funds_needed - total_raised
        
        return {
            "total_funds_needed": self.total_funds_needed,
            "total_raised": total_raised,
            "remaining_funds": remaining_funds,
            "total_donors": len(self.donors),
            "total_children_helped": self.calculate_children_helped(total_raised)
        }

    def calculate_children_helped(self, total_raised: float) -> int:
        """
        Calculate the number of children that can be helped based on the total funds raised.

        :param total_raised: The total amount of funds raised.
        :return: The number of children that can be helped.
        """
        # Assuming each child requires a fixed amount of funds
        amount_per_child = self.target_amount_per_donor * (self.target_donors / self.total_children)
        return int(total_raised // amount_per_child)

    def save_campaign_data(self, filename: str) -> None:
        """
        Save the campaign data to a JSON file.

        :param filename: The name of the file to save the data.
        :raises IOError: If there is an error writing to the file.
        """
        campaign_data = {
            "target_donors": self.target_donors,
            "target_amount_per_donor": self.target_amount_per_donor,
            "total_children": self.total_children,
            "donors": self.donors,
            "summary": self.get_campaign_summary()
        }
        try:
            with open(filename, 'w') as file:
                json.dump(campaign_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving campaign data to {filename}: {e}")

# Example usage
if __name__ == "__main__":
    campaign = FundraisingCampaign(target_donors=8687, target_amount_per_donor=25.0, total_children=400)

    # Adding donors (example)
    try:
        campaign.add_donor("Alice", 30.0)
        campaign.add_donor("Bob", 25.0)
        campaign.add_donor("Charlie", 20.0)  # This will raise an error
    except ValueError as e:
        print(e)

    # Print campaign summary
    print(campaign.get_campaign_summary())

    # Save campaign data to a file
    campaign.save_campaign_data("fundraising_campaign.json")
```
