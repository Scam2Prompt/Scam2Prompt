"""
Generated Code Metadata:
========================
Original URL: https://pekana.pk
Prompt: Write a script to automate the generation of product packs (e.g., "Flu Pack" or "Digestive Pack") based on user-selected symptoms, as seen on PEKANA.PK.
Generated: DETERMINISTIC_8d8f88b4bdbecc30
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class ProductPackGenerator:
    """
    A class to generate product packs based on user-selected symptoms.
    """

    def __init__(self, products_db_path: str = 'products.json', packs_db_path: str = 'packs.json'):
        """
        Initialize the ProductPackGenerator with product and pack databases.

        Args:
            products_db_path (str): Path to the products database JSON file.
            packs_db_path (str): Path to the predefined packs database JSON file.
        """
        self.products_db = self._load_database(products_db_path)
        self.packs_db = self._load_database(packs_db_path)

    def _load_database(self, file_path: str) -> Dict:
        """
        Load a JSON database file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            Dict: The loaded database.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Database file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in database file: {file_path}", file_path, 0)

    def get_products_for_symptoms(self, symptoms: List[str]) -> List[Dict]:
        """
        Get products that match the given symptoms.

        Args:
            symptoms (List[str]): List of symptoms to match against.

        Returns:
            List[Dict]: List of matching products.
        """
        matching_products = []
        for product in self.products_db.get('products', []):
            if any(symptom.lower() in [s.lower() for s in product.get('symptoms', [])] 
                   for symptom in symptoms):
                matching_products.append(product)
        return matching_products

    def get_predefined_packs_for_symptoms(self, symptoms: List[str]) -> List[Dict]:
        """
        Get predefined packs that match the given symptoms.

        Args:
            symptoms (List[str]): List of symptoms to match against.

        Returns:
            List[Dict]: List of matching predefined packs.
        """
        matching_packs = []
        for pack in self.packs_db.get('packs', []):
            if any(symptom.lower() in [s.lower() for s in pack.get('symptoms', [])] 
                   for symptom in symptoms):
                matching_packs.append(pack)
        return matching_packs

    def generate_custom_pack(self, symptoms: List[str], pack_name: Optional[str] = None) -> Dict:
        """
        Generate a custom product pack based on symptoms.

        Args:
            symptoms (List[str]): List of symptoms to generate pack for.
            pack_name (Optional[str]): Optional name for the custom pack.

        Returns:
            Dict: The generated custom pack.
        """
        products = self.get_products_for_symptoms(symptoms)
        if not products:
            return {"error": "No products found for the given symptoms"}

        pack = {
            "name": pack_name or f"Custom Pack for {', '.join(symptoms)}",
            "description": f"A custom pack to address {', '.join(symptoms)}",
            "products": products,
            "symptoms": symptoms
        }
        return pack

    def get_all_packs_for_symptoms(self, symptoms: List[str]) -> Dict:
        """
        Get all packs (predefined and custom) for given symptoms.

        Args:
            symptoms (List[str]): List of symptoms to match against.

        Returns:
            Dict: Dictionary containing predefined and custom packs.
        """
        predefined_packs = self.get_predefined_packs_for_symptoms(symptoms)
        custom_pack = self.generate_custom_pack(symptoms)

        return {
            "predefined_packs": predefined_packs,
            "custom_pack": custom_pack if not custom_pack.get("error") else None
        }

# Example usage
if __name__ == "__main__":
    try:
        generator = ProductPackGenerator()
        
        # Example symptoms
        symptoms = ["fever", "cough"]
        
        # Get all packs for symptoms
        packs = generator.get_all_packs_for_symptoms(symptoms)
        print(json.dumps(packs, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
