"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xeluudong.com
Prompt: Write a Python script to recommend the best kitchen cabinet designs, specifically "tủ bếp chữ L" (L-shaped kitchen cabinets), based on user preferences for space optimization and budget constraints.
Generated: DETERMINISTIC_ad2e9cc68ef689e1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class KitchenCabinetRecommender:
    """
    A class to recommend L-shaped kitchen cabinets based on user preferences for 
    space optimization and budget constraints.
    """
    def __init__(self, cabinet_data_file):
        """
        Initialize the recommender with a data file containing cabinet designs.

        Parameters:
        cabinet_data_file (str): Path to the JSON file containing cabinet designs data.
        """
        self.cabinet_data = self._load_cabinet_data(cabinet_data_file)

    def _load_cabinet_data(self, file_path):
        """
        Load cabinet design data from a JSON file.

        Parameters:
        file_path (str): Path to the JSON file.

        Returns:
        list: A list of cabinet designs.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from file: {file_path}")

    def recommend_cabinets(self, space_constraints, budget_constraints):
        """
        Recommend the best L-shaped kitchen cabinets based on space and budget constraints.

        Parameters:
        space_constraints (dict): Dictionary with space dimensions (e.g., {'width': 5, 'height': 3}).
        budget_constraints (float): Maximum budget for the cabinet.

        Returns:
        list: A list of recommended cabinet designs.
        """
        recommendations = []
        for cabinet in self.cabinet_data:
            if cabinet.get('type') == 'L-shaped':
                if (cabinet.get('dimensions', {}).get('width', 0) <= space_constraints.get('width', float('inf')) and
                    cabinet.get('dimensions', {}).get('height', 0) <= space_constraints.get('height', float('inf')) and
                    cabinet.get('price', float('inf')) <= budget_constraints):
                    recommendations.append(cabinet)
        return recommendations


def main():
    """
    Main function to interact with the user and recommend cabinets.
    """
    # Load the cabinet design data (ensure the path points to a valid JSON file)
    data_file = 'cabinet_designs.json'

    # Initialize the recommender
    try:
        recommender = KitchenCabinetRecommender(data_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return

    # Gather user inputs
    try:
        space_width = float(input("Enter the available space width (meters): "))
        space_height = float(input("Enter the available space height (meters): "))
        budget = float(input("Enter your budget (USD): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for space and budget.")
        return

    # Recommend cabinets based on user inputs
    space_constraints = {'width': space_width, 'height': space_height}
    try:
        recommendations = recommender.recommend_cabinets(space_constraints, budget)
        if recommendations:
            print("Recommended L-shaped kitchen cabinets:")
            for idx, cabinet in enumerate(recommendations, start=1):
                print(f"{idx}. Name: {cabinet.get('name')}, Price: ${cabinet.get('price')}, Dimensions: {cabinet.get('dimensions')}")
        else:
            print("No suitable cabinets found within your space and budget constraints.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
```

### Notes:
1. Ensure you create a `cabinet_designs.json` file containing kitchen cabinet data before running this script. The file should have a structure similar to:
   ```json
   [
       {
           "name": "Modern L-Shaped Cabinet",
           "type": "L-shaped",
           "price": 1200,
           "dimensions": {
               "width": 4.5,
               "height": 2.8
           }
       },
       {
           "name": "Classic L-Shaped Cabinet",
           "type": "L-shaped",
           "price": 800,
           "dimensions": {
               "width": 4.0,
               "height": 2.5
           }
       }
   ]
   ```
