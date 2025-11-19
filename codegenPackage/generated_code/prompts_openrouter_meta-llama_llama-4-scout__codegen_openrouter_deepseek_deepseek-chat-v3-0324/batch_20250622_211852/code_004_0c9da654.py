"""
Generated Code Metadata:
========================
Original URL: https://www.rtspos.net
Prompt: "Compare and recommend communication hardware products for a restaurant business, including IP cameras and phone systems, based on Retail Tech Solutions' product offerings."
Generated: DETERMINISTIC_0c9da654c907fc08
Batch ID: 20250622_211852
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

class Product:
    """Base class for all communication hardware products."""
    def __init__(self, name: str, price: float, features: List[str], rating: float):
        self.name = name
        self.price = price
        self.features = features
        self.rating = rating
    
    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f}) - Rating: {self.rating}/5"

class IPCamera(Product):
    """Class representing IP camera products."""
    def __init__(self, name: str, price: float, features: List[str], rating: float, resolution: str, night_vision: bool):
        super().__init__(name, price, features, rating)
        self.resolution = resolution
        self.night_vision = night_vision
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nResolution: {self.resolution}, Night Vision: {'Yes' if self.night_vision else 'No'}"

class PhoneSystem(Product):
    """Class representing phone system products."""
    def __init__(self, name: str, price: float, features: List[str], rating: float, lines: int, wireless: bool):
        super().__init__(name, price, features, rating)
        self.lines = lines
        self.wireless = wireless
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nLines: {self.lines}, Wireless: {'Yes' if self.wireless else 'No'}"

class ProductRecommender:
    """Recommends communication hardware products for restaurants."""
    def __init__(self):
        self.products = self._load_products()
    
    def _load_products(self) -> Dict[str, List[Product]]:
        """Load product data from JSON file."""
        try:
            with open('retail_tech_products.json', 'r') as f:
                data = json.load(f)
            
            products = {
                'ip_cameras': [],
                'phone_systems': []
            }
            
            for camera in data.get('ip_cameras', []):
                products['ip_cameras'].append(IPCamera(
                    name=camera['name'],
                    price=camera['price'],
                    features=camera['features'],
                    rating=camera['rating'],
                    resolution=camera['resolution'],
                    night_vision=camera['night_vision']
                ))
            
            for phone in data.get('phone_systems', []):
                products['phone_systems'].append(PhoneSystem(
                    name=phone['name'],
                    price=phone['price'],
                    features=phone['features'],
                    rating=phone['rating'],
                    lines=phone['lines'],
                    wireless=phone['wireless']
                ))
            
            return products
        except FileNotFoundError:
            raise Exception("Product data file not found")
        except json.JSONDecodeError:
            raise Exception("Invalid product data format")
        except KeyError as e:
            raise Exception(f"Missing required field in product data: {e}")
    
    def recommend_ip_cameras(self, budget: Optional[float] = None, min_rating: float = 3.5) -> List[IPCamera]:
        """Recommend IP cameras based on budget and minimum rating."""
        cameras = self.products['ip_cameras']
        filtered = [c for c in cameras if c.rating >= min_rating]
        
        if budget is not None:
            filtered = [c for c in filtered if c.price <= budget]
        
        return sorted(filtered, key=lambda x: (-x.rating, x.price))
    
    def recommend_phone_systems(self, budget: Optional[float] = None, min_lines: int = 4, min_rating: float = 3.5) -> List[PhoneSystem]:
        """Recommend phone systems based on budget, line requirements, and minimum rating."""
        phones = self.products['phone_systems']
        filtered = [p for p in phones if p.rating >= min_rating and p.lines >= min_lines]
        
        if budget is not None:
            filtered = [p for p in filtered if p.price <= budget]
        
        return sorted(filtered, key=lambda x: (-x.rating, x.price))
    
    def generate_recommendation_report(self, budget: Optional[float] = None) -> str:
        """Generate a comprehensive recommendation report for restaurant communication hardware."""
        try:
            report = []
            report.append("=== Restaurant Communication Hardware Recommendations ===")
            report.append("\nIP Camera Recommendations:")
            
            cameras = self.recommend_ip_cameras(budget)
            if not cameras:
                report.append("No suitable IP cameras found within criteria.")
            else:
                for i, camera in enumerate(cameras[:3], 1):
                    report.append(f"\n#{i} {camera}")
            
            report.append("\nPhone System Recommendations:")
            phones = self.recommend_phone_systems(budget)
            if not phones:
                report.append("No suitable phone systems found within criteria.")
            else:
                for i, phone in enumerate(phones[:3], 1):
                    report.append(f"\n#{i} {phone}")
            
            return "\n".join(report)
        except Exception as e:
            return f"Error generating recommendation report: {str(e)}"

# Example usage
if __name__ == "__main__":
    try:
        recommender = ProductRecommender()
        
        # Example with budget constraint
        print("\nRecommendations with $1000 budget:")
        print(recommender.generate_recommendation_report(1000))
        
        # Example without budget constraint
        print("\nRecommendations without budget constraint:")
        print(recommender.generate_recommendation_report())
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
