"""
Generated Code Metadata:
========================
Original URL: https://familiaprevilife.com
Prompt: Compare the features and benefits of different health and wellness products, including Pro Adulto and Colágeno Hidrolizado CH+H, using a decision-making algorithm.
Generated: DETERMINISTIC_9cdd1d08b91f097a
Batch ID: 20250622_211323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List, Tuple

class HealthProduct:
    """Represents a health and wellness product with its features and benefits."""
    
    def __init__(self, name: str, features: Dict[str, float], benefits: Dict[str, float]):
        """
        Initialize a health product with its name, features, and benefits.
        
        Args:
            name: Name of the product.
            features: Dictionary of features (e.g., {'ingredient_strength': 0.8}).
            benefits: Dictionary of benefits (e.g., {'joint_health': 0.9}).
        """
        self.name = name
        self.features = features
        self.benefits = benefits

class ProductComparator:
    """Compares health products using a weighted decision-making algorithm."""
    
    def __init__(self, feature_weights: Dict[str, float], benefit_weights: Dict[str, float]):
        """
        Initialize the comparator with weights for features and benefits.
        
        Args:
            feature_weights: Dictionary of weights for each feature (sum should be ~1.0).
            benefit_weights: Dictionary of weights for each benefit (sum should be ~1.0).
        """
        self.feature_weights = feature_weights
        self.benefit_weights = benefit_weights
    
    def _validate_weights(self, weights: Dict[str, float]) -> bool:
        """Validate that weights sum to approximately 1.0."""
        total = sum(weights.values())
        return abs(total - 1.0) < 1e-6
    
    def _calculate_score(self, product: HealthProduct) -> float:
        """
        Calculate a weighted score for the product.
        
        Args:
            product: HealthProduct to score.
            
        Returns:
            Weighted score (higher is better).
        """
        if not (self._validate_weights(self.feature_weights) and self._validate_weights(self.benefit_weights)):
            raise ValueError("Feature or benefit weights do not sum to 1.0")
        
        # Calculate feature score
        feature_score = sum(
            product.features[feature] * weight 
            for feature, weight in self.feature_weights.items()
            if feature in product.features
        )
        
        # Calculate benefit score
        benefit_score = sum(
            product.benefits[benefit] * weight 
            for benefit, weight in self.benefit_weights.items()
            if benefit in product.benefits
        )
        
        # Combined score (50% features, 50% benefits)
        return 0.5 * feature_score + 0.5 * benefit_score
    
    def compare(self, products: List[HealthProduct]) -> List[Tuple[str, float]]:
        """
        Compare a list of products and return sorted scores.
        
        Args:
            products: List of HealthProduct objects to compare.
            
        Returns:
            List of tuples (product_name, score) sorted by score descending.
        """
        scored_products = []
        for product in products:
            try:
                score = self._calculate_score(product)
                scored_products.append((product.name, score))
            except ValueError as e:
                print(f"Error scoring product {product.name}: {e}")
                continue
        
        # Sort by score descending
        return sorted(scored_products, key=lambda x: x[1], reverse=True)

# Example usage
if __name__ == "__main__":
    # Define products
    pro_adulto = HealthProduct(
        name="Pro Adulto",
        features={
            "ingredient_strength": 0.9,
            "digestibility": 0.7,
            "purity": 0.8
        },
        benefits={
            "energy": 0.8,
            "vitality": 0.9,
            "longevity": 0.7
        }
    )
    
    collagen = HealthProduct(
        name="Colágeno Hidrolizado CH+H",
        features={
            "ingredient_strength": 0.8,
            "digestibility": 0.9,
            "purity": 0.9
        },
        benefits={
            "joint_health": 0.9,
            "skin_health": 0.8,
            "bone_strength": 0.7
        }
    )
    
    # Define weights (should sum to 1.0 for each category)
    feature_weights = {
        "ingredient_strength": 0.4,
        "digestibility": 0.3,
        "purity": 0.3
    }
    
    benefit_weights = {
        "energy": 0.3,
        "vitality": 0.4,
        "longevity": 0.3,
        "joint_health": 0.3,
        "skin_health": 0.3,
        "bone_strength": 0.4
    }
    
    # Compare products
    comparator = ProductComparator(feature_weights, benefit_weights)
    results = comparator.compare([pro_adulto, collagen])
    
    # Display results
    print("Product Comparison Results:")
    for name, score in results:
        print(f"{name}: {score:.2f}")
```
