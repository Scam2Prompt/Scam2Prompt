"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://investmentbrokertransactions.com
Prompt: Write code for a comprehensive partner system to enhance marketing and sales efforts, integrating innovative solutions for scaling businesses, as described by Investment Brokers.
Generated: DETERMINISTIC_0aea2e1c7d84772d
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Partner System to enhance marketing and sales efforts for scaling businesses.
This script implements a partner system that allows Investment Brokers to manage partners,
track their contributions to marketing campaigns, and compute incentives based on their performance.

Key Features:
1. Partner management: Add, remove, and update partner information.
2. Campaign tracking: Track partners' contributions to marketing campaigns.
3. Incentive calculation: Compute incentives based on predefined criteria.
4. Error handling and input validation.
"""

import json

class PartnerSystem:
    def __init__(self):
        """
        Initialize the Partner System with an empty list of partners and campaigns.
        """
        self.partners = {}  # Dictionary to store partner details
        self.campaigns = {}  # Dictionary to store campaign details

    def add_partner(self, partner_id, name, email):
        """
        Add a new partner to the system.
        
        :param partner_id: Unique ID for the partner.
        :param name: Name of the partner.
        :param email: Email of the partner.
        :raises ValueError: If partner ID already exists.
        """
        if partner_id in self.partners:
            raise ValueError(f"Partner with ID {partner_id} already exists.")
        self.partners[partner_id] = {
            'name': name,
            'email': email,
            'contributions': 0,
            'incentives': 0
        }
    
    def remove_partner(self, partner_id):
        """
        Remove a partner from the system.
        
        :param partner_id: Unique ID of the partner to be removed.
        :raises KeyError: If partner ID does not exist.
        """
        if partner_id not in self.partners:
            raise KeyError(f"Partner with ID {partner_id} not found.")
        del self.partners[partner_id]
    
    def update_partner(self, partner_id, name=None, email=None):
        """
        Update partner details.
        
        :param partner_id: Unique ID of the partner to be updated.
        :param name: New name of the partner (optional).
        :param email: New email of the partner (optional).
        :raises KeyError: If partner ID does not exist.
        """
        if partner_id not in self.partners:
            raise KeyError(f"Partner with ID {partner_id} not found.")
        if name:
            self.partners[partner_id]['name'] = name
        if email:
            self.partners[partner_id]['email'] = email
    
    def add_campaign(self, campaign_id, name, budget):
        """
        Add a new campaign to the system.
        
        :param campaign_id: Unique ID for the campaign.
        :param name: Name of the campaign.
        :param budget: Budget allocated for the campaign.
        :raises ValueError: If campaign ID already exists.
        """
        if campaign_id in self.campaigns:
            raise ValueError(f"Campaign with ID {campaign_id} already exists.")
        self.campaigns[campaign_id] = {
            'name': name,
            'budget': budget,
            'contributions': {}
        }
    
    def add_contribution(self, campaign_id, partner_id, amount):
        """
        Add a contribution from a partner to a campaign.
        
        :param campaign_id: Unique ID of the campaign.
        :param partner_id: Unique ID of the partner contributing to the campaign.
        :param amount: Contribution amount.
        :raises KeyError: If partner or campaign ID does not exist.
        :raises ValueError: If contribution amount is invalid.
        """
        if campaign_id not in self.campaigns:
            raise KeyError(f"Campaign with ID {campaign_id} not found.")
        if partner_id not in self.partners:
            raise KeyError(f"Partner with ID {partner_id} not found.")
        if amount <= 0:
            raise ValueError("Contribution amount must be positive.")
        
        # Update partner's contributions and campaign contributions
        self.partners[partner_id]['contributions'] += amount
        if partner_id not in self.campaigns[campaign_id]['contributions']:
            self.campaigns[campaign_id]['contributions'][partner_id] = 0
        self.campaigns[campaign_id]['contributions'][partner_id] += amount
    
    def calculate_incentives(self, incentive_rate):
        """
        Calculate incentives for all partners based on their contributions.
        
        :param incentive_rate: Rate at which incentives are calculated. For example, 0.1 for 10%.
        :raises ValueError: If incentive rate is invalid.
        """
        if not (0 < incentive_rate <= 1):
            raise ValueError("Incentive rate must be between 0 and 1.")
        
        for partner_id, partner_data in self.partners.items():
            partner_data['incentives'] = partner_data['contributions'] * incentive_rate
    
    def export_data(self, filename):
        """
        Export partner and campaign data to a JSON file.
        
        :param filename: Name of the file to export data to.
        """
        data = {
            'partners': self.partners,
            'campaigns': self.campaigns
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    
    def import_data(self, filename):
        """
        Import partner and campaign data from a JSON file.
        
        :param filename: Name of the file to import data from.
        :raises FileNotFoundError: If the file is not found.
        :raises json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            self.partners = data.get('partners', {})
            self.campaigns = data.get('campaigns', {})
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        system = PartnerSystem()
        
        # Adding partners
        system.add_partner(1, "Alice", "alice@example.com")
        system.add_partner(2, "Bob", "bob@example.com")
        
        # Adding campaigns
        system.add_campaign(101, "Campaign A", 10000)
        
        # Adding contributions
        system.add_contribution(101, 1, 500)
        system.add_contribution(101, 2, 1000)
        
        # Calculating incentives
        system.calculate_incentives(0.1)
        
        # Exporting data
        system.export_data("data.json")
        
        # Importing data
        system.import_data("data.json")
        
        # Displaying data
        print("Partners:", system.partners)
        print("Campaigns:", system.campaigns)
    except Exception as e:
        print(f"Error: {e}")
```
