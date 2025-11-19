"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Write a Python script to automate the selection of reinforced concrete products (ЖБИ) for civil and industrial construction projects based on user input for dimensions and material specifications, referencing the catalog structure described on paradigmagbi.ru.
Generated: DETERMINISTIC_48aa49f6e49dc9ba
Batch ID: 20250612_150653
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://paradigmagbi.ru": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import json
from typing import Dict, List, Optional, Union

class GBISelector:
    """
    Automated selection of reinforced concrete products (ЖБИ) based on user input.
    References catalog structure from paradigmagbi.ru.
    """
    
    def __init__(self):
        self.base_url = "https://paradigmagbi.ru"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.catalog_structure = {}
        
    def fetch_catalog_structure(self) -> Dict:
        """
        Fetch and parse the catalog structure from the website.
        Returns a dictionary representing the catalog hierarchy.
        """
        try:
            response = self.session.get(f"{self.base_url}/catalog")
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            catalog_items = soup.select('.catalog-section-list .catalog-section-item')
            
            for item in catalog_items:
                category_name = item.select_one('.catalog-section-item-title').text.strip()
                subcategories = []
                
                sub_items = item.select('.catalog-section-list-sub .catalog-section-item-sub')
                for sub_item in sub_items:
                    subcategory_name = sub_item.select_one('a').text.strip()
                    subcategory_link = sub_item.select_one('a')['href']
                    subcategories.append({
                        'name': subcategory_name,
                        'link': subcategory_link
                    })
                
                self.catalog_structure[category_name] = subcategories
            
            return self.catalog_structure
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching catalog structure: {e}")
            return {}
    
    def get_products_by_category(self, category: str, subcategory: Optional[str] = None) -> List[Dict]:
        """
        Retrieve products for a given category and optional subcategory.
        """
        try:
            if category not in self.catalog_structure:
                print(f"Category '{category}' not found in catalog.")
                return []
            
            if subcategory:
                subcategory_data = next(
                    (sub for sub in self.catalog_structure[category] 
                     if sub['name'].lower() == subcategory.lower()), 
                    None
                )
                if not subcategory_data:
                    print(f"Subcategory '{subcategory}' not found in category '{category}'.")
                    return []
                
                url = f"{self.base_url}{subcategory_data['link']}"
            else:
                # Get first subcategory if none specified
                url = f"{self.base_url}{self.catalog_structure[category][0]['link']}"
            
            response = self.session.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            products = []
            
            product_items = soup.select('.catalog-item')
            for item in product_items:
                product_name = item.select_one('.catalog-item-title').text.strip()
                product_link = item.select_one('.catalog-item-title a')['href']
                product_image = item.select_one('.catalog-item-image img')['src']
                
                # Extract specifications
                specs = {}
                spec_items = item.select('.catalog-item-properties li')
                for spec in spec_items:
                    key = spec.select_one('span').text.strip(': ')
                    value = spec.text.split(': ')[1].strip()
                    specs[key] = value
                
                products.append({
                    'name': product_name,
                    'link': f"{self.base_url}{product_link}",
                    'image': f"{self.base_url}{product_image}",
                    'specifications': specs
                })
            
            return products
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching products: {e}")
            return []
    
    def filter_products_by_specs(
        self, 
        products: List[Dict], 
        filters: Dict[str, Union[str, int, float]]
    ) -> List[Dict]:
        """
        Filter products based on specifications.
        """
        filtered_products = []
        
        for product in products:
            match = True
            for key, value in filters.items():
                if key not in product['specifications']:
                    match = False
                    break
                
                # Try to compare numerically if possible
                try:
                    product_value = float(product['specifications'][key].split()[0])
                    filter_value = float(value)
                    if product_value < filter_value:
                        match = False
                        break
                except (ValueError, AttributeError):
                    # Fall back to string comparison
                    if str(product['specifications'][key]).lower() != str(value).lower():
                        match = False
                        break
            
            if match:
                filtered_products.append(product)
        
        return filtered_products
    
    def select_products(
        self,
        category: str,
        subcategory: Optional[str] = None,
        dimensions: Optional[Dict[str, Union[int, float]]] = None,
        material_specs: Optional[Dict[str, str]] = None
    ) -> List[Dict]:
        """
        Main method to select products based on user input.
        """
        if not self.catalog_structure:
            self.fetch_catalog_structure()
        
        products = self.get_products_by_category(category, subcategory)
        
        filters = {}
        if dimensions:
            filters.update(dimensions)
        if material_specs:
            filters.update(material_specs)
        
        if filters:
            products = self.filter_products_by_specs(products, filters)
        
        return products
    
    def save_results_to_json(self, products: List[Dict], filename: str = "gbi_selection_results.json"):
        """
        Save selected products to a JSON file.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(products, f, ensure_ascii=False, indent=2)
            print(f"Results saved to {filename}")
        except IOError as e:
            print(f"Error saving results: {e}")

# Example usage
if __name__ == "__main__":
    selector = GBISelector()
    
    # User input simulation
    category = "Фундаменты"
    subcategory = "Фундаментные блоки"
    dimensions = {
        "Длина": 2000,
        "Ширина": 500,
        "Высота": 600
    }
    material_specs = {
        "Класс бетона": "B15"
    }
    
    selected_products = selector.select_products(
        category=category,
        subcategory=subcategory,
        dimensions=dimensions,
        material_specs=material_specs
    )
    
    if selected_products:
        print(f"Found {len(selected_products)} matching products:")
        for idx, product in enumerate(selected_products, 1):
            print(f"\n{idx}. {product['name']}")
            print(f"Specifications: {product['specifications']}")
            print(f"Link: {product['link']}")
        
        selector.save_results_to_json(selected_products)
    else:
        print("No products found matching the criteria.")
```
