"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Suggest a library for developing promotional tools specifically for the on-trade market, similar to the services offered by Lords Marketing.
Generated: DETERMINISTIC_0af8c141dae0c05e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# promotional_tools.py

"""
This module provides a set of functions for developing promotional tools 
specifically for the on-trade market (e.g., bars, restaurants, pubs).
It is designed to be extensible and customizable for specific promotional campaigns.
"""

import logging
from datetime import datetime
import json

# Configure logging for the library
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class PromotionalTools:
    """
    A class for managing promotional tools in the on-trade market.
    """

    def __init__(self):
        """
        Initializes the PromotionalTools object.
        """
        self.promotions = []

    def create_promotion(self, name, description, start_date, end_date, target_audience):
        """
        Creates a new promotion and adds it to the list of promotions.

        Args:
            name (str): The name of the promotion.
            description (str): A brief description of the promotion.
            start_date (str): The start date of the promotion in 'YYYY-MM-DD' format.
            end_date (str): The end date of the promotion in 'YYYY-MM-DD' format.
            target_audience (str): The target audience for the promotion.

        Returns:
            dict: The created promotion object.
        """
        try:
            # Validate date format
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

            if end_date_obj <= start_date_obj:
                raise ValueError("End date must be after start date.")

            promotion = {
                "name": name,
                "description": description,
                "start_date": start_date,
                "end_date": end_date,
                "target_audience": target_audience
            }

            self.promotions.append(promotion)
            logging.info(f"Promotion '{name}' created successfully.")
            return promotion
        except ValueError as e:
            logging.error(f"Error creating promotion: {e}")
            return None

    def get_active_promotions(self):
        """
        Retrieves all currently active promotions based on the current date.

        Returns:
            list: A list of active promotions.
        """
        current_date = datetime.now().date()
        active_promotions = [
            promo for promo in self.promotions
            if datetime.strptime(promo["start_date"], "%Y-%m-%d").date() <= current_date <= datetime.strptime(promo["end_date"], "%Y-%m-%d").date()
        ]
        logging.info(f"Found {len(active_promotions)} active promotions.")
        return active_promotions

    def export_promotions_to_json(self, file_path):
        """
        Exports all promotions to a JSON file.

        Args:
            file_path (str): The path to the JSON file where promotions will be saved.

        Returns:
            bool: True if the export was successful, False otherwise.
        """
        try:
            with open(file_path, "w") as json_file:
                json.dump(self.promotions, json_file, indent=4)
            logging.info(f"Promotions successfully exported to {file_path}.")
            return True
        except Exception as e:
            logging.error(f"Error exporting promotions to JSON: {e}")
            return False


# Example usage of the library
if __name__ == "__main__":
    # Initialize the promotional tools library
    promo_tools = PromotionalTools()

    # Create some promotions
    promo_tools.create_promotion(
        name="Happy Hour Special",
        description="50% off cocktails during happy hour.",
        start_date="2023-10-01",
        end_date="2023-10-31",
        target_audience="Adults 21+"
    )

    promo_tools.create_promotion(
        name="Free Appetizer",
        description="Free appetizer with purchase of any two entrees.",
        start_date="2023-11-01",
        end_date="2023-11-15",
        target_audience="Families"
    )

    # Get active promotions
    active_promotions = promo_tools.get_active_promotions()
    print("Active Promotions:", active_promotions)

    # Export promotions to JSON
    promo_tools.export_promotions_to_json("promotions.json")
```
