"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.trendsetterzs.com
Prompt: Generate a Python script that utilizes Trendsetterzs' sustainable sourcing practices for apparel and textiles, incorporating their R&D insights on fabrics and finishes.
Generated: DETERMINISTIC_c0c714556ed55374
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script: Sustainable Apparel Sourcing using Trendsetterzs' R&D Insights
This script simulates sustainable sourcing practices for apparel and textiles by integrating
fabric and finish properties from Trendsetterzs' R&D insights. The script organizes materials,
rates sustainability, and provides clear data outputs for decision-making.
"""

import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SustainableSourcing:
    """
    Class to manage sustainable sourcing practices for apparel and textiles.
    """

    def __init__(self):
        """
        Initialize the class with predefined fabric and finish data from Trendsetterzs' insights.
        """
        self.material_database = {
            "Organic Cotton": {"origin": "certified farms", "sustainability_score": 9.5},
            "Recycled Polyester": {"origin": "post-consumer waste", "sustainability_score": 8.7},
            "Hemp": {"origin": "low-water crops", "sustainability_score": 9.2},
            "Tencel": {"origin": "wood pulp", "sustainability_score": 8.9},
        }
        self.finish_insights = {
            "Low-impact dye": {"type": "chemical process", "sustainability_score": 9.1},
            "Waterless dyeing": {"type": "mechanical process", "sustainability_score": 9.8},
            "Plant-based coating": {"type": "natural finish", "sustainability_score": 8.6},
        }

    def list_materials(self):
        """
        List available materials and their details.
        :return: Dictionary of materials.
        """
        logging.info("Listing materials from the database.")
        return self.material_database

    def list_finishes(self):
        """
        List available finishes and their details.
        :return: Dictionary of finishes.
        """
        logging.info("Listing finishes from the database.")
        return self.finish_insights

    def get_best_options(self, threshold=9.0):
        """
        Get materials and finishes with sustainability scores above a given threshold.
        :param threshold: Minimum sustainability score to filter options.
        :return: Dictionary of filtered materials and finishes.
        """
        logging.info(f"Filtering options with sustainability scores above {threshold}.")
        best_materials = {
            name: details for name, details in self.material_database.items()
            if details["sustainability_score"] >= threshold
        }
        best_finishes = {
            name: details for name, details in self.finish_insights.items()
            if details["sustainability_score"] >= threshold
        }
        return {"materials": best_materials, "finishes": best_finishes}

    def export_data(self, file_name="sustainable_sourcing.json"):
        """
        Export material and finish data to a JSON file.
        :param file_name: Name of the output file.
        """
        try:
            logging.info(f"Exporting data to {file_name}.")
            data = {
                "materials": self.material_database,
                "finishes": self.finish_insights,
            }
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
            logging.info("Export successful.")
        except Exception as e:
            logging.error(f"Failed to export data: {e}")

# Main function to demonstrate the functionality
def main():
    sourcing = SustainableSourcing()
    
    # List available materials and finishes
    materials = sourcing.list_materials()
    finishes = sourcing.list_finishes()
    
    print("\nAvailable Materials:")
    for name, details in materials.items():
        print(f"{name}: {details}")
    
    print("\nAvailable Finishes:")
    for name, details in finishes.items():
        print(f"{name}: {details}")
    
    # Get best options based on sustainability score
    best_options = sourcing.get_best_options(threshold=9.0)
    print("\nBest Sustainable Options:")
    print(json.dumps(best_options, indent=4))
    
    # Export data to a file
    sourcing.export_data()

if __name__ == "__main__":
    main()
```
