"""
Generated Code Metadata:
========================
Original URL: https://io-gpu.pages.dev
Prompt: Provide code to calculate the cost savings of using io.net's GPU clusters compared to major public cloud services, factoring in pricing per hour and utilization rates.
Generated: DETERMINISTIC_ffde7e13508f74b9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class CloudProvider:
    """Represents a cloud provider with GPU pricing information."""
    name: str
    gpu_types: Dict[str, float]  # GPU type to hourly price mapping
    utilization_rate: float = 1.0  # Default to full utilization

class CostCalculator:
    """Calculates cost savings between io.net and other cloud providers."""
    
    def __init__(self, io_net_price: float, io_net_utilization: float = 1.0):
        """
        Initialize with io.net's base pricing.
        
        Args:
            io_net_price: Hourly price for io.net GPU
            io_net_utilization: Utilization rate (0.0 to 1.0)
        """
        self.io_net = CloudProvider(
            name="io.net",
            gpu_types={"default": io_net_price},
            utilization_rate=io_net_utilization
        )
        self.providers: List[CloudProvider] = []
    
    def add_provider(self, provider: CloudProvider) -> None:
        """Add a cloud provider for comparison."""
        self.providers.append(provider)
    
    def calculate_savings(self, gpu_type: str = "default", hours: float = 1.0) -> Dict[str, Dict[str, float]]:
        """
        Calculate cost savings compared to other providers.
        
        Args:
            gpu_type: Type of GPU to compare
            hours: Number of hours to calculate for
            
        Returns:
            Dictionary with cost and savings data for each provider
        """
        if not self.providers:
            raise ValueError("No providers added for comparison")
        
        io_net_cost = self._calculate_cost(self.io_net, gpu_type, hours)
        
        results = {}
        for provider in self.providers:
            provider_cost = self._calculate_cost(provider, gpu_type, hours)
            savings = provider_cost - io_net_cost
            savings_percent = (savings / provider_cost) * 100 if provider_cost > 0 else 0
            
            results[provider.name] = {
                "provider_cost": round(provider_cost, 2),
                "io_net_cost": round(io_net_cost, 2),
                "savings_amount": round(savings, 2),
                "savings_percent": round(savings_percent, 2),
                "hours": hours
            }
        
        return results
    
    def _calculate_cost(self, provider: CloudProvider, gpu_type: str, hours: float) -> float:
        """Calculate adjusted cost based on utilization rate."""
        try:
            base_price = provider.gpu_types[gpu_type]
        except KeyError:
            raise ValueError(f"GPU type '{gpu_type}' not found for provider {provider.name}")
        
        adjusted_price = base_price / provider.utilization_rate
        return adjusted_price * hours
    
    def to_json(self) -> str:
        """Serialize calculator data to JSON."""
        data = {
            "io_net": {
                "price": self.io_net.gpu_types["default"],
                "utilization": self.io_net.utilization_rate
            },
            "providers": [
                {
                    "name": p.name,
                    "gpu_types": p.gpu_types,
                    "utilization": p.utilization_rate
                } for p in self.providers
            ]
        }
        return json.dumps(data, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'CostCalculator':
        """Create CostCalculator from JSON data."""
        data = json.loads(json_str)
        calculator = cls(
            io_net_price=data["io_net"]["price"],
            io_net_utilization=data["io_net"]["utilization"]
        )
        
        for provider_data in data["providers"]:
            provider = CloudProvider(
                name=provider_data["name"],
                gpu_types=provider_data["gpu_types"],
                utilization_rate=provider_data["utilization"]
            )
            calculator.add_provider(provider)
        
        return calculator

# Example usage
if __name__ == "__main__":
    # Initialize with io.net pricing ($0.50/hour at 90% utilization)
    calculator = CostCalculator(io_net_price=0.50, io_net_utilization=0.9)
    
    # Add major cloud providers (example prices)
    calculator.add_provider(CloudProvider(
        name="AWS",
        gpu_types={
            "V100": 3.06,
            "A100": 4.096,
            "T4": 0.35
        },
        utilization_rate=0.7  # 70% utilization
    ))
    
    calculator.add_provider(CloudProvider(
        name="Google Cloud",
        gpu_types={
            "V100": 2.48,
            "A100": 3.67,
            "T4": 0.35
        },
        utilization_rate=0.75  # 75% utilization
    ))
    
    calculator.add_provider(CloudProvider(
        name="Azure",
        gpu_types={
            "V100": 2.99,
            "A100": 3.96,
            "T4": 0.40
        },
        utilization_rate=0.65  # 65% utilization
    ))
    
    # Calculate savings for different scenarios
    scenarios = [
        {"gpu_type": "V100", "hours": 1},
        {"gpu_type": "A100", "hours": 8},
        {"gpu_type": "T4", "hours": 720}  # 1 month
    ]
    
    for scenario in scenarios:
        print(f"\nScenario: {scenario['gpu_type']} for {scenario['hours']} hours")
        results = calculator.calculate_savings(**scenario)
        for provider, data in results.items():
            print(f"{provider}:")
            print(f"  Cost: ${data['provider_cost']} vs io.net ${data['io_net_cost']}")
            print(f"  Savings: ${data['savings_amount']} ({data['savings_percent']}%)")
```
