"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shebatek.com
Prompt: Develop a marketing automation script for promoting services and products within budget, as highlighted by ShebaTek's marketing services.
Generated: DETERMINISTIC_8f13c50e99620867
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketingAutomation:
    def __init__(self, budget):
        """
        Initialize MarketingAutomation with a given budget.

        :param budget: float - The total budget allocated for marketing
        """
        self.budget = budget
        self.campaigns = []
    
    def add_campaign(self, name, cost):
        """
        Add a marketing campaign to the list if within budget.

        :param name: str - The name of the campaign
        :param cost: float - The cost of the campaign
        :raises ValueError: If the campaign cost exceeds the remaining budget
        """
        if self.get_remaining_budget() < cost:
            raise ValueError(f"Cannot add campaign '{name}'. Cost exceeds remaining budget.")
        
        self.campaigns.append({"name": name, "cost": cost, "date_added": datetime.now()})
        logging.info(f"Campaign '{name}' added with cost: {cost}")

    def get_remaining_budget(self):
        """
        Calculate remaining budget after adding campaigns.

        :return: float - Remaining budget
        """
        total_spent = sum(campaign['cost'] for campaign in self.campaigns)
        return self.budget - total_spent
    
    def generate_report(self):
        """
        Generate a report of all campaigns and the budget status.

        :return: dict - Report containing campaign details and budget status
        """
        report = {
            "total_budget": self.budget,
            "total_spent": sum(campaign['cost'] for campaign in self.campaigns),
            "remaining_budget": self.get_remaining_budget(),
            "campaigns": self.campaigns
        }
        return report

    def save_report_to_file(self, file_path):
        """
        Save the marketing report to a JSON file.

        :param file_path: str - The path where the report will be saved
        :raises IOError: If there is an error saving the file
        """
        report = self.generate_report()
        try:
            with open(file_path, 'w') as json_file:
                json.dump(report, json_file, indent=4)
            logging.info(f"Report saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to write report to file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the marketing automation with a budget of $5000
        marketing_automation = MarketingAutomation(budget=5000)
        
        # Add campaigns
        marketing_automation.add_campaign("Social Media Ads", 1500)
        marketing_automation.add_campaign("Email Marketing", 1200)
        marketing_automation.add_campaign("PPC Campaign", 2000)
        
        # Attempt to add another campaign exceeding budget
        marketing_automation.add_campaign("Print Ads", 800)  # This will raise an error
        
    except ValueError as ve:
        logging.error(ve)
        
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
    
    finally:
        # Save report regardless of success or failure
        marketing_automation.save_report_to_file('marketing_report.json')
```
