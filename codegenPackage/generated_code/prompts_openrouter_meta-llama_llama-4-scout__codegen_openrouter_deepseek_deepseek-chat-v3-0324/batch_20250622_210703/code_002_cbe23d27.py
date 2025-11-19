"""
Generated Code Metadata:
========================
Original URL: https://dedicatusit.com
Prompt: Compare the services offered by Dedicatus-IT for Level 1, Level 2, Level 3, and Level 4 Dedicated Tech Engineers, and recommend which level is suitable for a specific MSP requirement.
Generated: DETERMINISTIC_cbe23d2788f5bbbf
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ServiceLevel:
    """
    Represents a service level offered by Dedicatus-IT with its features and capabilities.
    """
    def __init__(self, level: int, name: str, description: str, features: list, 
                 response_time: str, availability: str, cost: str):
        self.level = level
        self.name = name
        self.description = description
        self.features = features
        self.response_time = response_time
        self.availability = availability
        self.cost = cost

class MSPRequirement:
    """
    Represents the requirements of a Managed Service Provider (MSP).
    """
    def __init__(self, name: str, complexity: str, availability_needed: str, 
                 response_time_needed: str, budget: str):
        self.name = name
        self.complexity = complexity
        self.availability_needed = availability_needed
        self.response_time_needed = response_time_needed
        self.budget = budget

class ServiceComparator:
    """
    Compares Dedicatus-IT service levels and recommends the best fit for MSP requirements.
    """
    def __init__(self):
        self.service_levels = self._initialize_service_levels()
    
    def _initialize_service_levels(self) -> list:
        """Initialize and return the available service levels."""
        return [
            ServiceLevel(
                level=1,
                name="Level 1 - Basic Support",
                description="Entry-level support for basic IT issues",
                features=[
                    "Basic troubleshooting",
                    "Password resets",
                    "Software installation support",
                    "Email support"
                ],
                response_time="4 business hours",
                availability="Business hours (9-5)",
                cost="$50/hour"
            ),
            ServiceLevel(
                level=2,
                name="Level 2 - Intermediate Support",
                description="Support for more complex technical issues",
                features=[
                    "All Level 1 features",
                    "Network troubleshooting",
                    "Server maintenance",
                    "Basic security monitoring",
                    "Phone and email support"
                ],
                response_time="2 business hours",
                availability="Extended hours (7am-7pm)",
                cost="$75/hour"
            ),
            ServiceLevel(
                level=3,
                name="Level 3 - Advanced Support",
                description="Expert support for complex systems and infrastructure",
                features=[
                    "All Level 2 features",
                    "Advanced network configuration",
                    "Cloud infrastructure support",
                    "Security incident response",
                    "24/7 on-call availability",
                    "Dedicated account manager"
                ],
                response_time="1 hour",
                availability="24/7 with SLA",
                cost="$100/hour"
            ),
            ServiceLevel(
                level=4,
                name="Level 4 - Enterprise Support",
                description="Premium support for mission-critical systems",
                features=[
                    "All Level 3 features",
                    "Custom solutions development",
                    "Strategic IT planning",
                    "Executive-level reporting",
                    "Dedicated engineer(s)",
                    "Guaranteed response times"
                ],
                response_time="30 minutes",
                availability="24/7 with guaranteed SLA",
                cost="Custom pricing"
            )
        ]
    
    def recommend_service_level(self, requirement: MSPRequirement) -> ServiceLevel:
        """
        Recommends the most suitable service level based on MSP requirements.
        
        Args:
            requirement: The MSP's requirements
            
        Returns:
            The recommended ServiceLevel object
            
        Raises:
            ValueError: If no suitable service level is found
        """
        recommended_level = None
        
        for level in self.service_levels:
            # Check if the level meets the requirements
            if (self._matches_complexity(level.level, requirement.complexity) and
                self._matches_availability(level.availability, requirement.availability_needed) and
                self._matches_response_time(level.response_time, requirement.response_time_needed) and
                self._matches_budget(level.cost, requirement.budget)):
                
                if recommended_level is None or level.level > recommended_level.level:
                    recommended_level = level
        
        if recommended_level is None:
            raise ValueError("No suitable service level found for the given requirements")
        
        return recommended_level
    
    def _matches_complexity(self, level: int, complexity: str) -> bool:
        """Check if service level matches the complexity requirement."""
        complexity_mapping = {
            "basic": [1],
            "intermediate": [1, 2],
            "advanced": [1, 2, 3],
            "enterprise": [1, 2, 3, 4]
        }
        return level in complexity_mapping.get(complexity.lower(), [])
    
    def _matches_availability(self, level_availability: str, required_availability: str) -> bool:
        """Check if service level meets availability requirements."""
        availability_rank = {
            "business hours": 1,
            "extended hours": 2,
            "24/7": 3,
            "24/7 with sla": 4,
            "24/7 with guaranteed sla": 5
        }
        return (availability_rank.get(level_availability.lower(), 0) >= 
                availability_rank.get(required_availability.lower(), 0))
    
    def _matches_response_time(self, level_response: str, required_response: str) -> bool:
        """Check if service level meets response time requirements."""
        def parse_time(time_str):
            if "minute" in time_str:
                return int(time_str.split()[0])
            if "hour" in time_str:
                return int(time_str.split()[0]) * 60
            if "business" in time_str:  # e.g., "4 business hours"
                return int(time_str.split()[0]) * 60
            return float('inf')  # Default to worst case
        
        return parse_time(level_response) <= parse_time(required_response)
    
    def _matches_budget(self, level_cost: str, budget: str) -> bool:
        """Check if service level is within budget."""
        if level_cost.lower() == "custom pricing":
            return True  # Custom pricing can be negotiated
        
        try:
            level_price = float(level_cost.replace('$', '').replace('/hour', ''))
            budget_price = float(budget.replace('$', '').replace('/hour', ''))
            return level_price <= budget_price
        except ValueError:
            return False  # If parsing fails, assume it doesn't match

def main():
    """Example usage of the ServiceComparator."""
    try:
        # Example MSP requirements
        msp_req = MSPRequirement(
            name="Acme MSP",
            complexity="advanced",
            availability_needed="24/7",
            response_time_needed="1 hour",
            budget="$120/hour"
        )
        
        comparator = ServiceComparator()
        recommendation = comparator.recommend_service_level(msp_req)
        
        print(f"Recommended service level for {msp_req.name}:")
        print(f"Level: {recommendation.level} - {recommendation.name}")
        print(f"Description: {recommendation.description}")
        print(f"Features: {', '.join(recommendation.features)}")
        print(f"Response Time: {recommendation.response_time}")
        print(f"Availability: {recommendation.availability}")
        print(f"Cost: {recommendation.cost}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
