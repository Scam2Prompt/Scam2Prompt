"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Create a Python script to generate a catalog of iPhone cases with different designs and prices, similar to the ones listed on Glisten's website.
Generated: DETERMINISTIC_cd391a8e4233b33b
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import random
from datetime import datetime
from typing import List, Dict, Optional

class iPhoneCaseCatalog:
    """
    A class to generate and manage a catalog of iPhone cases with various designs and prices.
    """
    
    def __init__(self):
        self.cases = []
        self.designs = [
            "Floral", "Geometric", "Abstract", "Minimalist", "Vintage",
            "Marble", "Wooden", "Transparent", "Glitter", "Cartoon"
        ]
        self.materials = ["Silicone", "Plastic", "Leather", "Metal", "TPU"]
        self.colors = ["Black", "White", "Red", "Blue", "Green", "Gold", "Silver", "Rose Gold"]
        self.iphone_models = ["iPhone 13", "iPhone 13 Pro", "iPhone 13 Pro Max", "iPhone 14", "iPhone 14 Pro", "iPhone 14 Pro Max"]
    
    def generate_case(self, case_id: int) -> Dict[str, Optional[str]]:
        """
        Generate a single iPhone case with random attributes.
        
        Args:
            case_id (int): Unique identifier for the case.
            
        Returns:
            Dict[str, Optional[str]]: Dictionary containing case attributes.
        """
        design = random.choice(self.designs)
        material = random.choice(self.materials)
        color = random.choice(self.colors)
        model = random.choice(self.iphone_models)
        price = round(random.uniform(10.0, 50.0), 2)
        
        return {
            "id": case_id,
            "design": design,
            "material": material,
            "color": color,
            "model": model,
            "price": price,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def generate_catalog(self, num_cases: int) -> List[Dict[str, Optional[str]]]:
        """
        Generate a catalog of iPhone cases.
        
        Args:
            num_cases (int): Number of cases to generate.
            
        Returns:
            List[Dict[str, Optional[str]]]: List of generated cases.
        """
        if num_cases <= 0:
            raise ValueError("Number of cases must be greater than 0.")
        
        self.cases = [self.generate_case(i) for i in range(1, num_cases + 1)]
        return self.cases
    
    def export_to_csv(self, filename: str) -> None:
        """
        Export the catalog to a CSV file.
        
        Args:
            filename (str): Name of the CSV file to export to.
            
        Raises:
            ValueError: If no cases are available to export.
            IOError: If there is an issue writing to the file.
        """
        if not self.cases:
            raise ValueError("No cases available to export.")
        
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.cases[0].keys())
                writer.writeheader()
                writer.writerows(self.cases)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")

def main():
    """
    Main function to demonstrate the usage of iPhoneCaseCatalog.
    """
    try:
        catalog = iPhoneCaseCatalog()
        catalog.generate_catalog(50)  # Generate 50 cases
        catalog.export_to_csv("iphone_case_catalog.csv")
        print("Catalog generated and exported successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
