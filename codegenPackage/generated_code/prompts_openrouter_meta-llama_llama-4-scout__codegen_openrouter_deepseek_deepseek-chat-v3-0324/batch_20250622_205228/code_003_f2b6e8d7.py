"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Develop a function to calculate rating-based impact scores for e-commerce products using data from reviews, price, and other relevant factors.
Generated: DETERMINISTIC_f2b6e8d79a13e963
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Review:
    rating: float
    helpful_votes: int
    verified_purchase: bool
    review_date: datetime

@dataclass
class Product:
    price: float
    average_rating: float
    review_count: int
    reviews: List[Review]
    category: str

class ImpactScoreCalculator:
    """
    Calculates impact scores for e-commerce products based on reviews, price, and other factors.
    """
    
    def __init__(self, 
                 rating_weight: float = 0.5,
                 recency_weight: float = 0.2,
                 helpfulness_weight: float = 0.15,
                 price_weight: float = 0.15,
                 min_reviews_threshold: int = 5):
        """
        Initialize calculator with configurable weights.
        
        Args:
            rating_weight: Weight for average rating (0-1)
            recency_weight: Weight for review recency (0-1)
            helpfulness_weight: Weight for review helpfulness (0-1)
            price_weight: Weight for price competitiveness (0-1)
            min_reviews_threshold: Minimum reviews required for calculation
        """
        self.rating_weight = rating_weight
        self.recency_weight = recency_weight
        self.helpfulness_weight = helpfulness_weight
        self.price_weight = price_weight
        self.min_reviews_threshold = min_reviews_threshold
        
        # Validate weights sum to 1
        total = sum([rating_weight, recency_weight, helpfulness_weight, price_weight])
        if not math.isclose(total, 1.0, rel_tol=1e-5):
            raise ValueError("Weights must sum to 1.0")
    
    def _normalize(self, value: float, min_val: float, max_val: float) -> float:
        """Normalize value between 0 and 1 based on min/max range."""
        if max_val <= min_val:
            return 0.0
        return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))
    
    def _calculate_rating_score(self, product: Product) -> float:
        """Calculate normalized rating score (0-1)."""
        return self._normalize(product.average_rating, 1.0, 5.0)
    
    def _calculate_recency_score(self, product: Product) -> float:
        """Calculate recency score based on most recent reviews."""
        if not product.reviews:
            return 0.0
            
        now = datetime.now()
        days_ago = [(now - r.review_date).days for r in product.reviews]
        avg_days_ago = sum(days_ago) / len(days_ago)
        
        # Normalize with 0 days = best (1), 365 days = worst (0)
        return 1.0 - self._normalize(avg_days_ago, 0.0, 365.0)
    
    def _calculate_helpfulness_score(self, product: Product) -> float:
        """Calculate helpfulness score based on votes."""
        if not product.reviews:
            return 0.0
            
        total_votes = sum(r.helpful_votes for r in product.reviews)
        avg_votes = total_votes / len(product.reviews)
        
        # Normalize with 0 votes = 0, 10+ votes = 1
        return self._normalize(avg_votes, 0.0, 10.0)
    
    def _calculate_price_score(self, product: Product, price_range: Dict[str, tuple]) -> float:
        """
        Calculate price competitiveness score.
        
        Args:
            product: Product to score
            price_range: Dict mapping categories to (min_price, max_price) tuples
        """
        if product.category not in price_range:
            return 0.5  # Default neutral score if category not found
            
        min_price, max_price = price_range[product.category]
        if max_price <= min_price:
            return 0.5
            
        # Lower price gets higher score (inverted normalization)
        return 1.0 - self._normalize(product.price, min_price, max_price)
    
    def calculate_impact_score(self, 
                              product: Product, 
                              price_range: Optional[Dict[str, tuple]] = None) -> float:
        """
        Calculate overall impact score (0-1) for a product.
        
        Args:
            product: Product to score
            price_range: Optional dict of category price ranges
            
        Returns:
            Impact score between 0 and 1
            
        Raises:
            ValueError: If product has insufficient reviews
        """
        if product.review_count < self.min_reviews_threshold:
            raise ValueError(f"Product has fewer than {self.min_reviews_threshold} reviews")
            
        if price_range is None:
            price_range = {}
            
        rating_score = self._calculate_rating_score(product)
        recency_score = self._calculate_recency_score(product)
        helpfulness_score = self._calculate_helpfulness_score(product)
        price_score = self._calculate_price_score(product, price_range)
        
        return (
            (rating_score * self.rating_weight) +
            (recency_score * self.recency_weight) +
            (helpfulness_score * self.helpfulness_weight) +
            (price_score * self.price_weight)
        )
```
