"""
Generated Code Metadata:
========================
Original URL: https://dhcpbrazz.blogspot.com
Prompt: Compare the features and pricing of the CADEIRA GAMER XZONE CGR-01-GR with similar products from other brands, and provide a recommendation for a gamer looking for an ergonomic chair.
Generated: DETERMINISTIC_5d702e9ef7389772
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict, Optional

class Product:
    def __init__(self, name: str, brand: str, price: float, features: List[str]):
        self.name = name
        self.brand = brand
        self.price = price
        self.features = features

    def __repr__(self):
        return f"Product(name={self.name}, brand={self.brand}, price={self.price})"

class ChairComparator:
    def __init__(self):
        self.products = []
        self.feature_weights = {
            'ergonomic': 0.3,
            'adjustable': 0.2,
            'material': 0.15,
            'lumbar_support': 0.2,
            'headrest': 0.15
        }

    def add_product(self, product: Product):
        """Add a product to the comparison list."""
        self.products.append(product)

    def scrape_product_info(self, url: str) -> Optional[Product]:
        """
        Scrape product information from a given URL.
        Note: This is a placeholder implementation. In production, you would need to:
        1. Handle different website structures
        2. Respect robots.txt
        3. Implement proper error handling
        """
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Placeholder selectors - would need to be customized per site
            name = soup.select_one('h1.product-title').text.strip()
            brand = soup.select_one('span.brand-name').text.strip()
            price_text = soup.select_one('span.price').text.strip()
            price = float(price_text.replace('$', '').replace(',', ''))
            
            features = []
            feature_elements = soup.select('ul.features li')
            for feat in feature_elements:
                features.append(feat.text.strip())
            
            return Product(name, brand, price, features)
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            return None

    def calculate_score(self, product: Product) -> float:
        """Calculate a weighted score based on product features."""
        score = 0
        features_lower = [f.lower() for f in product.features]
        
        if 'ergonomic' in features_lower:
            score += self.feature_weights['ergonomic']
        if any('adjustable' in f for f in features_lower):
            score += self.feature_weights['adjustable']
        if 'lumbar support' in features_lower:
            score += self.feature_weights['lumbar_support']
        if 'headrest' in features_lower:
            score += self.feature_weights['headrest']
        
        # Normalize price impact (lower price is better)
        max_price = max(p.price for p in self.products) if self.products else product.price
        price_score = 1 - (product.price / max_price)
        score += price_score * 0.5  # Price has 50% weight in total score
        
        return score

    def compare_products(self) -> pd.DataFrame:
        """Compare all products and return a DataFrame with results."""
        if not self.products:
            raise ValueError("No products to compare")
        
        comparison_data = []
        for product in self.products:
            score = self.calculate_score(product)
            comparison_data.append({
                'Name': product.name,
                'Brand': product.brand,
                'Price': product.price,
                'Features': ', '.join(product.features),
                'Score': round(score, 2)
            })
        
        df = pd.DataFrame(comparison_data)
        return df.sort_values('Score', ascending=False)

    def get_recommendation(self) -> Dict:
        """Get the top recommendation based on comparison."""
        comparison_df = self.compare_products()
        best_product = comparison_df.iloc[0]
        
        return {
            'recommendation': best_product['Name'],
            'brand': best_product['Brand'],
            'price': best_product['Price'],
            'score': best_product['Score'],
            'reason': "Best combination of ergonomic features and value"
        }

# Example usage
if __name__ == "__main__":
    comparator = ChairComparator()
    
    # Add the CADEIRA GAMER XZONE CGR-01-GR (mock data)
    xzone = Product(
        name="CADEIRA GAMER XZONE CGR-01-GR",
        brand="XZONE",
        price=299.99,
        features=[
            "Ergonomic design",
            "Adjustable height",
            "Lumbar support",
            "PU leather material",
            "360-degree swivel"
        ]
    )
    comparator.add_product(xzone)
    
    # Add competing products (mock data)
    dxracer = Product(
        name="DXRacer Racing Series",
        brand="DXRacer",
        price=349.99,
        features=[
            "Ergonomic racing design",
            "Adjustable armrests",
            "Lumbar support pillow",
            "Steel frame construction",
            "Multi-tilt mechanism"
        ]
    )
    comparator.add_product(dxracer)
    
    secretlab = Product(
        name="Secretlab Titan Evo",
        brand="Secretlab",
        price=429.00,
        features=[
            "Premium ergonomic design",
            "Full-length lumbar support",
            "Memory foam head pillow",
            "Cold-cure foam cushions",
            "4D armrests"
        ]
    )
    comparator.add_product(secretlab)
    
    # Compare and get recommendation
    try:
        comparison = comparator.compare_products()
        print("Product Comparison:")
        print(comparison.to_string(index=False))
        
        recommendation = comparator.get_recommendation()
        print("\nRecommendation:")
        for key, value in recommendation.items():
            print(f"{key.capitalize()}: {value}")
    except Exception as e:
        print(f"Error during comparison: {str(e)}")
```
