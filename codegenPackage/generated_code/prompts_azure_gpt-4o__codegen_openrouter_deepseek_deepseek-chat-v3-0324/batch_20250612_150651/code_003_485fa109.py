"""
Generated Code Metadata:
========================
Original URL: https://notclosn.top
Prompt: Provide a step-by-step guide to implement a pricing strategy calculator for freelancers using Python, based on the strategies for client acquisition and pricing discussed in the КарьераОнлайн program.
Generated: DETERMINISTIC_485fa10927540ff3
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Freelancer Pricing Strategy Calculator
This tool helps freelancers determine optimal pricing based on various strategies.
"""

import math
from enum import Enum
from typing import Optional, Dict, List, Tuple

class PricingStrategy(Enum):
    """Available pricing strategies for freelancers."""
    HOURLY_RATE = "Hourly Rate"
    PROJECT_BASED = "Project-Based"
    VALUE_BASED = "Value-Based"
    RETARGETING = "Retargeting"
    RETENTION = "Retention"

class ClientType(Enum):
    """Types of clients based on acquisition difficulty."""
    NEW = "New Client"
    EXISTING = "Existing Client"
    RETURNING = "Returning Client"

class PricingCalculator:
    """
    Calculates optimal pricing for freelancers based on different strategies.
    """
    
    def __init__(self):
        self.base_hourly_rate = 50  # Default base rate
        self.client_difficulty_multipliers = {
            ClientType.NEW: 1.0,
            ClientType.EXISTING: 0.9,
            ClientType.RETURNING: 0.8
        }
        self.strategy_multipliers = {
            PricingStrategy.HOURLY_RATE: 1.0,
            PricingStrategy.PROJECT_BASED: 1.2,
            PricingStrategy.VALUE_BASED: 1.5,
            PricingStrategy.RETARGETING: 0.9,
            PricingStrategy.RETENTION: 0.85
        }
    
    def set_base_hourly_rate(self, rate: float) -> None:
        """Set the base hourly rate for calculations."""
        if rate <= 0:
            raise ValueError("Hourly rate must be positive")
        self.base_hourly_rate = rate
    
    def calculate_hourly_rate(
        self,
        strategy: PricingStrategy,
        client_type: ClientType,
        experience_multiplier: float = 1.0
    ) -> float:
        """
        Calculate the hourly rate based on strategy and client type.
        
        Args:
            strategy: Pricing strategy to use
            client_type: Type of client
            experience_multiplier: Multiplier based on experience (default 1.0)
            
        Returns:
            Calculated hourly rate
        """
        if experience_multiplier <= 0:
            raise ValueError("Experience multiplier must be positive")
            
        base_rate = self.base_hourly_rate * experience_multiplier
        strategy_mult = self.strategy_multipliers.get(strategy, 1.0)
        client_mult = self.client_difficulty_multipliers.get(client_type, 1.0)
        
        return base_rate * strategy_mult * client_mult
    
    def calculate_project_price(
        self,
        estimated_hours: float,
        strategy: PricingStrategy,
        client_type: ClientType,
        experience_multiplier: float = 1.0,
        project_complexity: float = 1.0
    ) -> float:
        """
        Calculate project price based on estimated hours and strategy.
        
        Args:
            estimated_hours: Estimated hours to complete project
            strategy: Pricing strategy to use
            client_type: Type of client
            experience_multiplier: Multiplier based on experience (default 1.0)
            project_complexity: Complexity multiplier (default 1.0)
            
        Returns:
            Calculated project price
        """
        if estimated_hours <= 0:
            raise ValueError("Estimated hours must be positive")
        if project_complexity <= 0:
            raise ValueError("Project complexity must be positive")
            
        hourly_rate = self.calculate_hourly_rate(strategy, client_type, experience_multiplier)
        base_price = hourly_rate * estimated_hours
        return base_price * project_complexity
    
    def calculate_value_based_price(
        self,
        client_estimated_value: float,
        value_percentage: float = 0.1,
        min_price: Optional[float] = None
    ) -> float:
        """
        Calculate price based on value provided to client.
        
        Args:
            client_estimated_value: Value the project brings to client
            value_percentage: Percentage of value to charge (default 0.1)
            min_price: Minimum price to charge (optional)
            
        Returns:
            Calculated value-based price
        """
        if client_estimated_value <= 0:
            raise ValueError("Client value must be positive")
        if not 0 < value_percentage <= 1:
            raise ValueError("Value percentage must be between 0 and 1")
            
        price = client_estimated_value * value_percentage
        if min_price is not None and price < min_price:
            return min_price
        return price
    
    def suggest_pricing_strategies(
        self,
        client_type: ClientType,
        project_scope: str,
        client_budget: Optional[float] = None
    ) -> List[Tuple[PricingStrategy, float]]:
        """
        Suggest pricing strategies based on client and project characteristics.
        
        Args:
            client_type: Type of client
            project_scope: Scope of the project ('small', 'medium', 'large')
            client_budget: Client's budget if known (optional)
            
        Returns:
            List of suggested strategies with sample rates
        """
        scope_multipliers = {
            'small': 1.0,
            'medium': 1.3,
            'large': 1.7
        }
        
        if project_scope not in scope_multipliers:
            raise ValueError("Project scope must be 'small', 'medium', or 'large'")
            
        scope_mult = scope_multipliers[project_scope]
        suggestions = []
        
        # Always suggest hourly rate as baseline
        hourly_rate = self.calculate_hourly_rate(
            PricingStrategy.HOURLY_RATE,
            client_type
        ) * scope_mult
        suggestions.append((PricingStrategy.HOURLY_RATE, hourly_rate))
        
        # Suggest project-based for medium/large projects
        if project_scope in ['medium', 'large']:
            sample_hours = 10 if project_scope == 'medium' else 20
            project_price = self.calculate_project_price(
                sample_hours,
                PricingStrategy.PROJECT_BASED,
                client_type,
                project_complexity=scope_mult
            )
            suggestions.append((PricingStrategy.PROJECT_BASED, project_price))
        
        # Suggest value-based if budget is known and substantial
        if client_budget and client_budget > hourly_rate * 5:
            value_price = self.calculate_value_based_price(
                client_budget * 2,  # Assuming 2x ROI for client
                value_percentage=0.15
            )
            suggestions.append((PricingStrategy.VALUE_BASED, value_price))
        
        # Special strategies for existing/returning clients
        if client_type in [ClientType.EXISTING, ClientType.RETURNING]:
            retention_rate = self.calculate_hourly_rate(
                PricingStrategy.RETENTION,
                client_type
            ) * scope_mult
            suggestions.append((PricingStrategy.RETENTION, retention_rate))
        
        return suggestions

# Example usage
if __name__ == "__main__":
    calculator = PricingCalculator()
    calculator.set_base_hourly_rate(60)
    
    # Calculate hourly rate for a new client with value-based strategy
    hourly_rate = calculator.calculate_hourly_rate(
        PricingStrategy.VALUE_BASED,
        ClientType.NEW,
        experience_multiplier=1.2
    )
    print(f"Value-Based Hourly Rate: ${hourly_rate:.2f}")
    
    # Calculate project price for existing client
    project_price = calculator.calculate_project_price(
        estimated_hours=15,
        strategy=PricingStrategy.PROJECT_BASED,
        client_type=ClientType.EXISTING,
        project_complexity=1.3
    )
    print(f"Project-Based Price: ${project_price:.2f}")
    
    # Get strategy suggestions for a large project
    suggestions = calculator.suggest_pricing_strategies(
        client_type=ClientType.NEW,
        project_scope='large',
        client_budget=5000
    )
    
    print("\nSuggested Pricing Strategies:")
    for strategy, price in suggestions:
        print(f"{strategy.value}: ${price:.2f}")
```
