"""
Generated Code Metadata:
========================
Original URL: https://airtm9.com
Prompt: Compare and recommend website hosting plans on Hostinger for a successful online project, considering speed, security, and user-friendliness.
Generated: DETERMINISTIC_5b9ceb308216556a
Batch ID: 20250622_212122
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
from typing import List, Dict, Optional

class HostingPlan:
    """Represents a hosting plan from Hostinger."""
    
    def __init__(
        self,
        name: str,
        price: float,
        storage: str,
        bandwidth: str,
        free_domain: bool,
        ssl: bool,
        performance: str,
        user_friendliness: str,
        security_features: List[str]
    ):
        self.name = name
        self.price = price
        self.storage = storage
        self.bandwidth = bandwidth
        self.free_domain = free_domain
        self.ssl = ssl
        self.performance = performance  # e.g., "High", "Medium", "Low"
        self.user_friendliness = user_friendliness  # e.g., "High", "Medium", "Low"
        self.security_features = security_features

    def __str__(self) -> str:
        return (
            f"Plan: {self.name}\n"
            f"Price: ${self.price}/mo\n"
            f"Storage: {self.storage}\n"
            f"Bandwidth: {self.bandwidth}\n"
            f"Free Domain: {'Yes' if self.free_domain else 'No'}\n"
            f"SSL: {'Yes' if self.ssl else 'No'}\n"
            f"Performance: {self.performance}\n"
            f"User-Friendliness: {self.user_friendliness}\n"
            f"Security Features: {', '.join(self.security_features)}\n"
        )

class HostingPlanComparator:
    """Compares Hostinger hosting plans based on project requirements."""
    
    def __init__(self):
        self.plans = self._fetch_hostinger_plans()
    
    def _fetch_hostinger_plans(self) -> List[HostingPlan]:
        """Fetch and parse Hostinger plans (mock implementation)."""
        # Note: In a real-world scenario, this would scrape Hostinger's website or use an API.
        # This is a mock implementation for demonstration purposes.
        return [
            HostingPlan(
                name="Single Shared Hosting",
                price=1.99,
                storage="50GB SSD",
                bandwidth="100GB",
                free_domain=False,
                ssl=True,
                performance="Medium",
                user_friendliness="High",
                security_features=["SSL", "Weekly Backups"]
            ),
            HostingPlan(
                name="Premium Shared Hosting",
                price=2.99,
                storage="100GB SSD",
                bandwidth="Unlimited",
                free_domain=True,
                ssl=True,
                performance="High",
                user_friendliness="High",
                security_features=["SSL", "Daily Backups", "Cloudflare Protection"]
            ),
            HostingPlan(
                name="Business Shared Hosting",
                price=4.99,
                storage="200GB SSD",
                bandwidth="Unlimited",
                free_domain=True,
                ssl=True,
                performance="High",
                user_friendliness="High",
                security_features=["SSL", "Daily Backups", "Cloudflare Protection", "CDN"]
            )
        ]
    
    def recommend_plan(
        self,
        min_storage: Optional[str] = None,
        min_bandwidth: Optional[str] = None,
        require_free_domain: bool = False,
        require_ssl: bool = True,
        min_performance: Optional[str] = None,
        min_user_friendliness: Optional[str] = None,
        required_security_features: Optional[List[str]] = None
    ) -> List[HostingPlan]:
        """
        Recommends plans based on the given criteria.
        
        Args:
            min_storage: Minimum storage requirement (e.g., "100GB SSD").
            min_bandwidth: Minimum bandwidth requirement (e.g., "Unlimited").
            require_free_domain: Whether a free domain is required.
            require_ssl: Whether SSL is required.
            min_performance: Minimum performance level ("High", "Medium", "Low").
            min_user_friendliness: Minimum user-friendliness level ("High", "Medium", "Low").
            required_security_features: List of required security features.
        
        Returns:
            List of recommended HostingPlan objects.
        """
        recommended = []
        
        for plan in self.plans:
            # Check storage
            if min_storage and self._compare_storage(plan.storage, min_storage) < 0:
                continue
                
            # Check bandwidth
            if min_bandwidth and self._compare_bandwidth(plan.bandwidth, min_bandwidth) < 0:
                continue
                
            # Check free domain
            if require_free_domain and not plan.free_domain:
                continue
                
            # Check SSL
            if require_ssl and not plan.ssl:
                continue
                
            # Check performance
            if min_performance and self._compare_rating(plan.performance, min_performance) < 0:
                continue
                
            # Check user-friendliness
            if min_user_friendliness and self._compare_rating(plan.user_friendliness, min_user_friendliness) < 0:
                continue
                
            # Check security features
            if required_security_features and not all(
                feature in plan.security_features for feature in required_security_features
            ):
                continue
                
            recommended.append(plan)
        
        return recommended
    
    def _compare_storage(self, storage_a: str, storage_b: str) -> int:
        """Compare two storage values (e.g., '50GB SSD' vs '100GB SSD')."""
        a_value = int(''.join(filter(str.isdigit, storage_a)))
        b_value = int(''.join(filter(str.isdigit, storage_b)))
        return a_value - b_value
    
    def _compare_bandwidth(self, bandwidth_a: str, bandwidth_b: str) -> int:
        """Compare two bandwidth values (e.g., '100GB' vs 'Unlimited')."""
        if bandwidth_a == "Unlimited" and bandwidth_b != "Unlimited":
            return 1
        elif bandwidth_a != "Unlimited" and bandwidth_b == "Unlimited":
            return -1
        elif bandwidth_a == "Unlimited" and bandwidth_b == "Unlimited":
            return 0
        else:
            a_value = int(''.join(filter(str.isdigit, bandwidth_a)))
            b_value = int(''.join(filter(str.isdigit, bandwidth_b)))
            return a_value - b_value
    
    def _compare_rating(self, rating_a: str, rating_b: str) -> int:
        """Compare two rating values (e.g., 'High' vs 'Medium')."""
        ratings = {"Low": 1, "Medium": 2, "High": 3}
        return ratings.get(rating_a, 0) - ratings.get(rating_b, 0)

def main():
    """Main function to demonstrate the HostingPlanComparator."""
    comparator = HostingPlanComparator()
    
    print("All Hostinger Plans:")
    for plan in comparator.plans:
        print(plan)
    
    print("\nRecommended Plans for a Successful Online Project:")
    recommended = comparator.recommend_plan(
        min_storage="100GB SSD",
        min_bandwidth="Unlimited",
        require_free_domain=True,
        require_ssl=True,
        min_performance="High",
        min_user_friendliness="High",
        required_security_features=["SSL", "Daily Backups"]
    )
    
    if not recommended:
        print("No plans match the criteria.")
    else:
        for plan in recommended:
            print(plan)

if __name__ == "__main__":
    main()
```
