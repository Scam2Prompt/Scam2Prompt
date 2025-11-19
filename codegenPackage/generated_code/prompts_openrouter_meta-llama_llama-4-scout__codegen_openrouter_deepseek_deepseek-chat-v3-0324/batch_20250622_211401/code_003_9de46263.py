"""
Generated Code Metadata:
========================
Original URL: https://optimisenow.net
Prompt: "Design a workflow optimization strategy for a company looking to outsource key business functions to specialized service providers using business process outsourcing (BPO)."
Generated: DETERMINISTIC_9de4626390bdd74d
Batch ID: 20250622_211401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Optional
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BPOFunction(Enum):
    """Enum representing different business functions that can be outsourced."""
    CUSTOMER_SERVICE = auto()
    IT_SUPPORT = auto()
    ACCOUNTING = auto()
    HUMAN_RESOURCES = auto()
    MARKETING = auto()

class ServiceProvider:
    """Class representing a BPO service provider."""
    def __init__(self, name: str, specialties: List[BPOFunction], cost: float, rating: float):
        """
        Initialize a service provider.
        
        Args:
            name: Name of the provider
            specialties: List of BPO functions they specialize in
            cost: Cost per unit (e.g., per hour, per task)
            rating: Quality rating (0-5 scale)
        """
        self.name = name
        self.specialties = specialties
        self.cost = cost
        self.rating = rating

    def __str__(self):
        return f"{self.name} (Specialties: {[s.name for s in self.specialties]}, Cost: {self.cost}, Rating: {self.rating})"

class BPOOptimizer:
    """Class to optimize BPO workflow and provider selection."""
    def __init__(self):
        self.providers: List[ServiceProvider] = []
    
    def add_provider(self, provider: ServiceProvider) -> None:
        """Add a service provider to the optimizer's database."""
        if not isinstance(provider, ServiceProvider):
            raise ValueError("Provider must be an instance of ServiceProvider")
        self.providers.append(provider)
        logger.info(f"Added provider: {provider.name}")
    
    def find_providers(
        self, 
        function: BPOFunction, 
        max_cost: Optional[float] = None, 
        min_rating: Optional[float] = None
    ) -> List[ServiceProvider]:
        """
        Find providers that match the criteria.
        
        Args:
            function: BPO function needed
            max_cost: Maximum acceptable cost (optional)
            min_rating: Minimum acceptable rating (optional)
            
        Returns:
            List of matching ServiceProvider objects
        """
        if not isinstance(function, BPOFunction):
            raise ValueError("Function must be a BPOFunction enum value")
            
        matches = [
            p for p in self.providers 
            if function in p.specialties
            and (max_cost is None or p.cost <= max_cost)
            and (min_rating is None or p.rating >= min_rating)
        ]
        
        # Sort by best value (rating/cost ratio)
        matches.sort(key=lambda p: p.rating/p.cost, reverse=True)
        
        logger.info(f"Found {len(matches)} providers for {function.name}")
        return matches
    
    def optimize_workflow(
        self, 
        functions: List[BPOFunction], 
        budget: float, 
        min_rating: float = 3.0
    ) -> Dict[BPOFunction, ServiceProvider]:
        """
        Optimize provider selection for multiple functions within budget.
        
        Args:
            functions: List of BPO functions needed
            budget: Total available budget
            min_rating: Minimum acceptable rating for providers
            
        Returns:
            Dictionary mapping functions to selected providers
            
        Raises:
            ValueError: If no valid provider combination fits the budget
        """
        if not functions:
            raise ValueError("At least one function must be specified")
            
        # Get all possible providers for each function
        provider_options = {
            func: self.find_providers(func, min_rating=min_rating)
            for func in functions
        }
        
        # Check if any function has no providers
        for func, providers in provider_options.items():
            if not providers:
                raise ValueError(f"No providers available for {func.name} with given constraints")
        
        # Greedy algorithm to select providers
        selected = {}
        remaining_budget = budget
        
        # Sort functions by cost of cheapest provider (to maximize functions covered)
        functions_sorted = sorted(
            functions,
            key=lambda f: provider_options[f][0].cost
        )
        
        for func in functions_sorted:
            # Select the best affordable provider
            for provider in provider_options[func]:
                if provider.cost <= remaining_budget:
                    selected[func] = provider
                    remaining_budget -= provider.cost
                    break
            else:
                # No provider found within remaining budget
                raise ValueError(f"Cannot find provider for {func.name} within remaining budget")
        
        logger.info(f"Optimized workflow selected {len(selected)} providers within budget")
        return selected

# Example usage
if __name__ == "__main__":
    try:
        optimizer = BPOOptimizer()
        
        # Add sample providers
        optimizer.add_provider(ServiceProvider(
            "Acme Support", 
            [BPOFunction.CUSTOMER_SERVICE, BPOFunction.IT_SUPPORT], 
            25.0, 
            4.2
        ))
        optimizer.add_provider(ServiceProvider(
            "Global HR", 
            [BPOFunction.HUMAN_RESOURCES], 
            40.0, 
            4.5
        ))
        optimizer.add_provider(ServiceProvider(
            "Budget Accounting", 
            [BPOFunction.ACCOUNTING], 
            20.0, 
            3.8
        ))
        
        # Optimize workflow
        functions_needed = [
            BPOFunction.CUSTOMER_SERVICE,
            BPOFunction.ACCOUNTING,
            BPOFunction.HUMAN_RESOURCES
        ]
        result = optimizer.optimize_workflow(functions_needed, budget=100.0)
        
        # Print results
        print("Optimized Provider Selection:")
        for func, provider in result.items():
            print(f"{func.name}: {provider}")
            
    except Exception as e:
        logger.error(f"Error in workflow optimization: {e}")
        raise
```
