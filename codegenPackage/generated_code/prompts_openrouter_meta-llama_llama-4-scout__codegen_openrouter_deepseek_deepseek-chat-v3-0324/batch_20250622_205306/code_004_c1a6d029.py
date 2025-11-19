"""
Generated Code Metadata:
========================
Original URL: https://opensea-opensea-60ff.mainnet.rpcpool.com
Prompt: Compare the features of Triton One's Solana RPC service with other similar services, and provide a recommendation on which one to use for a specific use case.
Generated: DETERMINISTIC_c1a6d029dc7a5c4b
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, List, Optional
from enum import Enum

class RPCServices(Enum):
    TRITON_ONE = "Triton One"
    QUICKNODE = "QuickNode"
    ALCHEMY = "Alchemy"
    ANKR = "Ankr"
    CHAINSTACK = "Chainstack"

class RPCSpecs:
    def __init__(
        self,
        name: RPCServices,
        throughput: int,
        latency: float,
        reliability: float,
        cost: float,
        features: List[str],
        regions: List[str]
    ):
        self.name = name
        self.throughput = throughput  # requests per second
        self.latency = latency  # milliseconds
        self.reliability = reliability  # uptime percentage
        self.cost = cost  # USD per million requests
        self.features = features  # list of supported features
        self.regions = regions  # list of available regions

class RPCComparator:
    def __init__(self):
        self.services = {
            RPCServices.TRITON_ONE: RPCSpecs(
                name=RPCServices.TRITON_ONE,
                throughput=5000,
                latency=50,
                reliability=99.9,
                cost=10.0,
                features=["private endpoints", "archive data", "websockets", "dedicated nodes"],
                regions=["us-east", "eu-west", "asia-southeast"]
            ),
            RPCServices.QUICKNODE: RPCSpecs(
                name=RPCServices.QUICKNODE,
                throughput=3000,
                latency=70,
                reliability=99.5,
                cost=15.0,
                features=["private endpoints", "archive data", "websockets"],
                regions=["us-east", "eu-west"]
            ),
            RPCServices.ALCHEMY: RPCSpecs(
                name=RPCServices.ALCHEMY,
                throughput=4000,
                latency=60,
                reliability=99.7,
                cost=12.0,
                features=["private endpoints", "archive data", "websockets", "analytics"],
                regions=["us-east", "eu-west", "asia-southeast"]
            ),
            RPCServices.ANKR: RPCSpecs(
                name=RPCServices.ANKR,
                throughput=2000,
                latency=80,
                reliability=99.0,
                cost=8.0,
                features=["private endpoints", "websockets"],
                regions=["us-east", "eu-west"]
            ),
            RPCServices.CHAINSTACK: RPCSpecs(
                name=RPCServices.CHAINSTACK,
                throughput=2500,
                latency=75,
                reliability=99.2,
                cost=9.0,
                features=["private endpoints", "archive data"],
                regions=["us-east", "eu-west"]
            )
        }

    def compare_features(self) -> Dict[RPCServices, RPCSpecs]:
        """Return a dictionary comparing all RPC services."""
        return self.services

    def recommend_service(
        self,
        priority: str,
        required_features: Optional[List[str]] = None,
        region: Optional[str] = None,
        budget: Optional[float] = None
    ) -> RPCServices:
        """
        Recommend the best RPC service based on priority and requirements.
        
        Args:
            priority: One of "performance", "cost", "reliability", or "features"
            required_features: List of required features
            region: Required region availability
            budget: Maximum cost per million requests
            
        Returns:
            Recommended RPCServices enum
        """
        filtered_services = self._filter_services(required_features, region, budget)
        
        if priority == "performance":
            return min(filtered_services.values(), key=lambda x: (x.latency, -x.throughput)).name
        elif priority == "cost":
            return min(filtered_services.values(), key=lambda x: x.cost).name
        elif priority == "reliability":
            return max(filtered_services.values(), key=lambda x: x.reliability).name
        elif priority == "features":
            return max(filtered_services.values(), key=lambda x: len(x.features)).name
        else:
            raise ValueError("Invalid priority specified")

    def _filter_services(
        self,
        required_features: Optional[List[str]] = None,
        region: Optional[str] = None,
        budget: Optional[float] = None
    ) -> Dict[RPCServices, RPCSpecs]:
        """Filter services based on requirements."""
        filtered = self.services.copy()
        
        if required_features:
            filtered = {
                k: v for k, v in filtered.items() 
                if all(feature in v.features for feature in required_features)
            }
        
        if region:
            filtered = {
                k: v for k, v in filtered.items() 
                if region in v.regions
            }
        
        if budget is not None:
            filtered = {
                k: v for k, v in filtered.items() 
                if v.cost <= budget
            }
        
        return filtered

# Example usage
if __name__ == "__main__":
    comparator = RPCComparator()
    
    # Compare all features
    all_features = comparator.compare_features()
    for service, specs in all_features.items():
        print(f"\n{service.value} Features:")
        print(f"Throughput: {specs.throughput} req/s")
        print(f"Latency: {specs.latency}ms")
        print(f"Reliability: {specs.reliability}%")
        print(f"Cost: ${specs.cost}/million requests")
        print(f"Features: {', '.join(specs.features)}")
        print(f"Regions: {', '.join(specs.regions)}")
    
    # Get recommendation
    use_case = "high performance trading bot requiring websockets in us-east"
    recommendation = comparator.recommend_service(
        priority="performance",
        required_features=["websockets"],
        region="us-east"
    )
    print(f"\nRecommended service for '{use_case}': {recommendation.value}")
```
