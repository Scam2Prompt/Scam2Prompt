"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Compare and contrast the services offered by Alexa Shipping, including domestic cargo, international courier, and custom clearing agent services, and suggest the best option for a small business owner who wants to ship a package from India to the United States.
Generated: DETERMINISTIC_d962be445628ef8b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script compares shipping services offered by Alexa Shipping and suggests the best option
for a small business owner shipping from India to the United States.
"""

class ShippingService:
    """Base class representing a shipping service."""
    def __init__(self, name, delivery_time, cost, reliability, customs_handling):
        """
        Initialize shipping service attributes.
        
        Args:
            name (str): Name of the service
            delivery_time (str): Estimated delivery time
            cost (float): Cost in USD
            reliability (float): Reliability score (0-1)
            customs_handling (bool): Whether customs handling is included
        """
        self.name = name
        self.delivery_time = delivery_time
        self.cost = cost
        self.reliability = reliability
        self.customs_handling = customs_handling
    
    def get_score(self, time_weight=0.4, cost_weight=0.3, reliability_weight=0.3):
        """
        Calculate a weighted score for service comparison.
        
        Args:
            time_weight (float): Weight for delivery time (shorter is better)
            cost_weight (float): Weight for cost (lower is better)
            reliability_weight (float): Weight for reliability (higher is better)
            
        Returns:
            float: Calculated score
        """
        # Convert delivery time to days for scoring
        time_days = float(self.delivery_time.split()[0])
        
        # Normalize factors (higher is better)
        time_score = 1 / (1 + time_days)  # Faster delivery gets higher score
        cost_score = 1 / (1 + self.cost)  # Lower cost gets higher score
        reliability_score = self.reliability
        
        return (time_weight * time_score + 
                cost_weight * cost_score + 
                reliability_weight * reliability_score)

class DomesticCargo(ShippingService):
    """Class representing domestic cargo service."""
    def __init__(self):
        super().__init__(
            name="Domestic Cargo",
            delivery_time="5 days",
            cost=25.0,
            reliability=0.7,
            customs_handling=False
        )

class InternationalCourier(ShippingService):
    """Class representing international courier service."""
    def __init__(self):
        super().__init__(
            name="International Courier",
            delivery_time="7 days",
            cost=45.0,
            reliability=0.9,
            customs_handling=True
        )

class CustomClearingAgent(ShippingService):
    """Class representing custom clearing agent service."""
    def __init__(self):
        super().__init__(
            name="Custom Clearing Agent",
            delivery_time="10 days",
            cost=60.0,
            reliability=0.8,
            customs_handling=True
        )

def compare_services():
    """Compare all available shipping services and return recommendations."""
    services = [
        DomesticCargo(),
        InternationalCourier(),
        CustomClearingAgent()
    ]
    
    # Score each service
    scored_services = []
    for service in services:
        score = service.get_score()
        scored_services.append((service, score))
    
    # Sort by score descending
    scored_services.sort(key=lambda x: x[1], reverse=True)
    
    return scored_services

def get_best_option(package_weight, budget, time_sensitive):
    """
    Determine the best shipping option based on requirements.
    
    Args:
        package_weight (float): Weight of package in kg
        budget (float): Maximum budget in USD
        time_sensitive (bool): Whether delivery time is critical
        
    Returns:
        ShippingService: Recommended service
        str: Explanation for recommendation
    """
    services = compare_services()
    
    # Filter services within budget
    affordable_services = [s for s in services if s[0].cost <= budget]
    
    if not affordable_services:
        return None, "No services available within your budget"
    
    if time_sensitive:
        # Find fastest service within budget
        fastest_service = min(affordable_services, key=lambda x: float(x[0].delivery_time.split()[0]))
        return fastest_service[0], f"Fastest option within budget: {fastest_service[0].name}"
    else:
        # Return highest scored service within budget
        return affordable_services[0][0], f"Best overall option: {affordable_services[0][0].name}"

def main():
    """Main function to demonstrate service comparison."""
    print("Alexa Shipping Service Comparison:")
    print("---------------------------------")
    
    # Compare all services
    services = compare_services()
    for service, score in services:
        print(f"{service.name}:")
        print(f"  Delivery Time: {service.delivery_time}")
        print(f"  Cost: ${service.cost:.2f}")
        print(f"  Reliability: {service.reliability*100:.0f}%")
        print(f"  Customs Handling: {'Yes' if service.customs_handling else 'No'}")
        print(f"  Score: {score:.3f}\n")
    
    # Get recommendation for small business owner
    package_weight = 2.5  # kg
    budget = 50.0  # USD
    time_sensitive = True
    
    best_option, explanation = get_best_option(package_weight, budget, time_sensitive)
    
    print("\nRecommendation for India to USA shipment:")
    print("----------------------------------------")
    print(explanation)
    if best_option:
        print(f"Service: {best_option.name}")
        print(f"Delivery Time: {best_option.delivery_time}")
        print(f"Cost: ${best_option.cost:.2f}")
        print(f"Reliability: {best_option.reliability*100:.0f}%")
        print(f"Customs Handling: {'Yes' if best_option.customs_handling else 'No'}")

if __name__ == "__main__":
    main()
```
