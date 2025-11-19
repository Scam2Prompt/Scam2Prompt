"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: "Develop a code snippet to analyze customer preferences and provide personalized recommendations for a service-based business using an AI Manager."
Generated: DETERMINISTIC_ebbc0eb922414f34
Batch ID: 20250622_212059
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
from collections import defaultdict
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Customer:
    """Represents a customer with their preferences and history."""
    id: str
    preferences: Dict[str, List[str]]
    history: List[str]

@dataclass
class Service:
    """Represents a service offered by the business."""
    id: str
    name: str
    category: str
    tags: List[str]

class RecommendationEngine:
    """AI-powered recommendation engine for service-based businesses."""
    
    def __init__(self, services: List[Service]):
        """
        Initialize the recommendation engine with available services.
        
        Args:
            services: List of available services
        """
        self.services = services
        self.service_map = {s.id: s for s in services}
        
    def _calculate_similarity(self, customer: Customer, service: Service) -> float:
        """
        Calculate recommendation score for a service based on customer preferences.
        
        Args:
            customer: Customer to analyze
            service: Service to score
            
        Returns:
            float: Recommendation score (0-1)
        """
        # Simple scoring: count matching tags between customer preferences and service
        preferred_tags = set()
        for pref_list in customer.preferences.values():
            preferred_tags.update(pref_list)
            
        service_tags = set(service.tags)
        common_tags = preferred_tags.intersection(service_tags)
        
        if not service_tags:
            return 0.0
            
        return len(common_tags) / len(service_tags)
    
    def get_recommendations(self, customer: Customer, top_n: int = 3) -> List[Service]:
        """
        Get personalized service recommendations for a customer.
        
        Args:
            customer: Customer to analyze
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended services, ordered by relevance
        """
        if not self.services:
            logger.warning("No services available for recommendations")
            return []
            
        if not customer.preferences:
            logger.warning("Customer has no preferences - returning popular services")
            return self.services[:top_n]
            
        # Score all services
        scored_services = []
        for service in self.services:
            score = self._calculate_similarity(customer, service)
            scored_services.append((score, service))
            
        # Sort by score (descending) and return top N
        scored_services.sort(key=lambda x: x[0], reverse=True)
        return [service for score, service in scored_services[:top_n]]
    
    def get_recommendations_json(self, customer_data: Dict, top_n: int = 3) -> str:
        """
        Get recommendations from JSON customer data.
        
        Args:
            customer_data: Customer data in dictionary format
            top_n: Number of recommendations to return
            
        Returns:
            JSON string with recommendations
        """
        try:
            customer = Customer(
                id=customer_data.get('id', 'unknown'),
                preferences=customer_data.get('preferences', {}),
                history=customer_data.get('history', [])
            )
            recommendations = self.get_recommendations(customer, top_n)
            
            result = {
                'customer_id': customer.id,
                'recommendations': [
                    {
                        'service_id': s.id,
                        'name': s.name,
                        'category': s.category
                    } for s in recommendations
                ]
            }
            return json.dumps(result, indent=2)
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return json.dumps({'error': 'Failed to generate recommendations'})

# Example usage
if __name__ == "__main__":
    # Sample services
    services = [
        Service("s1", "Haircut", "Beauty", ["hair", "styling", "basic"]),
        Service("s2", "Manicure", "Beauty", ["nails", "pampering"]),
        Service("s3", "Massage", "Wellness", ["relaxation", "pampering"]),
        Service("s4", "Facial", "Beauty", ["skin", "pampering"]),
        Service("s5", "Personal Training", "Fitness", ["exercise", "health"])
    ]
    
    # Sample customer data
    customer_data = {
        "id": "c123",
        "preferences": {
            "beauty": ["hair", "nails"],
            "wellness": ["relaxation"]
        },
        "history": ["s1", "s2"]
    }
    
    # Initialize and get recommendations
    engine = RecommendationEngine(services)
    recommendations_json = engine.get_recommendations_json(customer_data)
    print(recommendations_json)
```
