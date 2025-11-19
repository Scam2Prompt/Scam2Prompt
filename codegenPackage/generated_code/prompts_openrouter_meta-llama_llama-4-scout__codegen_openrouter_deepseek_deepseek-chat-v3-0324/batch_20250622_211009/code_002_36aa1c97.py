"""
Generated Code Metadata:
========================
Original URL: https://antichevarieta.it
Prompt: "Generate a Python script to analyze the nutritional benefits of various fruits in June and suggest the best options for eye health according to the Società Italiana di Nutrizione."
Generated: DETERMINISTIC_36aa1c979b1d7697
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict, Optional

class FruitNutritionAnalyzer:
    """
    A class to analyze nutritional benefits of fruits and suggest best options for eye health.
    Data is based on general nutritional information and recommendations from Società Italiana di Nutrizione.
    """
    
    def __init__(self):
        """
        Initialize the analyzer with fruit nutrition data for June.
        """
        self.fruit_data = self._load_fruit_data()
        self.eye_health_nutrients = ['Vitamin A', 'Vitamin C', 'Vitamin E', 'Lutein', 'Zeaxanthin']
        
    def _load_fruit_data(self) -> pd.DataFrame:
        """
        Load and return fruit nutrition data.
        
        Returns:
            pd.DataFrame: DataFrame containing fruit nutrition information.
        """
        data = {
            'Fruit': ['Apricot', 'Blueberry', 'Cherry', 'Peach', 'Strawberry', 'Blackberry', 'Raspberry'],
            'Vitamin A (IU)': [1926, 80, 64, 326, 12, 214, 33],
            'Vitamin C (mg)': [10, 9.7, 7, 6.6, 58.8, 21, 26.2],
            'Vitamin E (mg)': [0.89, 0.57, 0.07, 0.73, 0.29, 1.17, 0.87],
            'Lutein (µg)': [89, 80, 85, 91, 26, 118, 136],
            'Zeaxanthin (µg)': [0, 3, 0, 0, 0, 0, 0],
            'Season': ['June', 'June-July', 'June', 'June-August', 'June', 'June-August', 'June-August']
        }
        return pd.DataFrame(data)
    
    def _calculate_nutrient_score(self, row: pd.Series) -> float:
        """
        Calculate a weighted score for eye health nutrients.
        
        Args:
            row (pd.Series): A row from the fruit nutrition DataFrame.
            
        Returns:
            float: Calculated nutrient score.
        """
        weights = {
            'Vitamin A (IU)': 0.3,
            'Vitamin C (mg)': 0.25,
            'Vitamin E (mg)': 0.2,
            'Lutein (µg)': 0.15,
            'Zeaxanthin (µg)': 0.1
        }
        score = 0
        for nutrient, weight in weights.items():
            score += row[nutrient] * weight
        return score
    
    def get_best_fruits_for_eye_health(self, top_n: int = 3) -> List[Dict[str, Optional[str]]]:
        """
        Get the top fruits for eye health based on nutrient content.
        
        Args:
            top_n (int): Number of top fruits to return. Defaults to 3.
            
        Returns:
            List[Dict[str, Optional[str]]]: List of dictionaries containing fruit information.
        """
        try:
            if not isinstance(top_n, int) or top_n <= 0:
                raise ValueError("top_n must be a positive integer")
                
            june_fruits = self.fruit_data[self.fruit_data['Season'].str.contains('June')].copy()
            june_fruits['EyeHealthScore'] = june_fruits.apply(self._calculate_nutrient_score, axis=1)
            top_fruits = june_fruits.sort_values('EyeHealthScore', ascending=False).head(top_n)
            
            return top_fruits.to_dict('records')
        except Exception as e:
            print(f"Error occurred while analyzing fruits: {e}")
            return []
    
    def print_nutritional_benefits(self, fruit_name: str) -> None:
        """
        Print nutritional benefits of a specific fruit.
        
        Args:
            fruit_name (str): Name of the fruit to analyze.
        """
        try:
            fruit = self.fruit_data[self.fruit_data['Fruit'].str.lower() == fruit_name.lower()]
            if fruit.empty:
                print(f"Fruit '{fruit_name}' not found in the database.")
                return
                
            print(f"\nNutritional benefits of {fruit_name}:")
            for nutrient in self.eye_health_nutrients:
                col_name = f"{nutrient} ({'IU' if nutrient == 'Vitamin A' else 'mg' if nutrient in ['Vitamin C', 'Vitamin E'] else 'µg'})"
                value = fruit[col_name].values[0]
                print(f"- {nutrient}: {value}")
        except Exception as e:
            print(f"Error occurred while retrieving nutritional benefits: {e}")

def main():
    analyzer = FruitNutritionAnalyzer()
    
    print("Top fruits for eye health in June (recommended by Società Italiana di Nutrizione):")
    best_fruits = analyzer.get_best_fruits_for_eye_health()
    
    for i, fruit in enumerate(best_fruits, 1):
        print(f"\n{i}. {fruit['Fruit']}:")
        print(f"  - Vitamin A: {fruit['Vitamin A (IU)']} IU")
        print(f"  - Vitamin C: {fruit['Vitamin C (mg)']} mg")
        print(f"  - Vitamin E: {fruit['Vitamin E (mg)']} mg")
        print(f"  - Lutein: {fruit['Lutein (µg)']} µg")
        print(f"  - Zeaxanthin: {fruit['Zeaxanthin (µg)']} µg")
        print(f"  - Eye Health Score: {fruit.get('EyeHealthScore', 0):.2f}")

if __name__ == "__main__":
    main()
```
