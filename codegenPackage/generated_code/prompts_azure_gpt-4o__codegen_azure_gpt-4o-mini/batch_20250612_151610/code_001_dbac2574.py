"""
Generated Code Metadata:
========================
Original URL: https://koveindustrial.com
Prompt: Generate a script to recommend suitable industrial belts for mining applications, using the categories "FAJAS ANTIABRASIVAS" and "FAJAS DE ARRASTRE ANTIABRASIVAS OSR" from KOVE Industrial.
Generated: DETERMINISTIC_dbac25748195100c
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IndustrialBeltRecommender:
    def __init__(self, data_source):
        """
        Initializes the recommender with a data source.

        :param data_source: Path to the JSON file containing belt data.
        """
        self.data_source = data_source
        self.belts = self.load_data()

    def load_data(self):
        """
        Loads belt data from the specified JSON file.

        :return: List of belts if successful, empty list otherwise.
        """
        try:
            with open(self.data_source, 'r') as file:
                belts = json.load(file)
                logging.info("Belt data loaded successfully.")
                return belts
        except FileNotFoundError:
            logging.error("Data source file not found.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON data.")
            return []

    def recommend_belts(self, category):
        """
        Recommends belts based on the specified category.

        :param category: The category of belts to recommend.
        :return: List of recommended belts.
        """
        recommended = [belt for belt in self.belts if belt.get('category') == category]
        if not recommended:
            logging.warning(f"No belts found for category: {category}")
        return recommended

    def display_recommendations(self, recommendations):
        """
        Displays the recommended belts in a user-friendly format.

        :param recommendations: List of recommended belts.
        """
        if recommendations:
            print("Recommended Belts:")
            for belt in recommendations:
                print(f"- {belt['name']} (Category: {belt['category']}, Specs: {belt['specs']})")
        else:
            print("No recommendations available.")

def main():
    # Path to the JSON data file
    data_file = 'belts_data.json'
    
    # Create an instance of the recommender
    recommender = IndustrialBeltRecommender(data_file)
    
    # Define categories for recommendation
    categories = [
        "FAJAS ANTIABRASIVAS",
        "FAJAS DE ARRASTRE ANTIABRASIVAS OSR"
    ]
    
    # Recommend belts for each category
    for category in categories:
        recommendations = recommender.recommend_belts(category)
        recommender.display_recommendations(recommendations)

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `belts_data.json` file exists in the same directory as this script and contains the appropriate structure for the belt data. The expected structure is a list of dictionaries, where each dictionary represents a belt with keys like `name`, `category`, and `specs`.
