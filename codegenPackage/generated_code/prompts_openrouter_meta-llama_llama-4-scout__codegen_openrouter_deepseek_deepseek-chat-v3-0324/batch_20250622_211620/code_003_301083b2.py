"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: "Compare and contrast managed IT services, including monitoring, maintenance, and support, offered by different providers."
Generated: DETERMINISTIC_301083b2fe5a8eef
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum

class ServiceLevel(Enum):
    """Enum representing different service levels offered by providers."""
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

@dataclass
class ServiceFeature:
    """Class representing a specific feature within a managed IT service."""
    name: str
    description: str
    included_in: List[ServiceLevel] = field(default_factory=list)

@dataclass
class ManagedService:
    """Class representing a managed IT service provider."""
    provider_name: str
    services_offered: Dict[str, List[ServiceFeature]]  # Key: service type, Value: list of features
    pricing: Dict[ServiceLevel, float]
    sla_uptime: Dict[ServiceLevel, float]  # SLA uptime percentage per service level
    support_channels: List[str]  # e.g., Phone, Email, Chat
    
    def compare_with(self, other: 'ManagedService', service_type: str) -> Dict[str, dict]:
        """
        Compare this provider with another for a specific service type.
        
        Args:
            other: Another ManagedService instance to compare with
            service_type: Type of service to compare (e.g., "monitoring")
            
        Returns:
            Dictionary with comparison results
        """
        if service_type not in self.services_offered or service_type not in other.services_offered:
            raise ValueError(f"Service type '{service_type}' not offered by both providers")
            
        comparison = {
            "provider_a": self.provider_name,
            "provider_b": other.provider_name,
            "service_type": service_type,
            "features": {
                "common": [],
                "unique_to_a": [],
                "unique_to_b": []
            },
            "pricing": {},
            "sla": {}
        }
        
        # Compare features
        features_a = {f.name for f in self.services_offered[service_type]}
        features_b = {f.name for f in other.services_offered[service_type]}
        
        comparison["features"]["common"] = list(features_a & features_b)
        comparison["features"]["unique_to_a"] = list(features_a - features_b)
        comparison["features"]["unique_to_b"] = list(features_b - features_a)
        
        # Compare pricing and SLA
        for level in ServiceLevel:
            if level in self.pricing and level in other.pricing:
                comparison["pricing"][level.value] = {
                    self.provider_name: self.pricing[level],
                    other.provider_name: other.pricing[level]
                }
                
            if level in self.sla_uptime and level in other.sla_uptime:
                comparison["sla"][level.value] = {
                    self.provider_name: self.sla_uptime[level],
                    other.provider_name: other.sla_uptime[level]
                }
                
        return comparison

def load_providers_from_json(file_path: str) -> List[ManagedService]:
    """
    Load provider data from a JSON file.
    
    Args:
        file_path: Path to JSON file containing provider data
        
    Returns:
        List of ManagedService instances
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file contains invalid data
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Provider data file not found at {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in provider data file")
    
    providers = []
    for provider_data in data.get("providers", []):
        try:
            services = {}
            for service_type, features in provider_data["services_offered"].items():
                services[service_type] = [
                    ServiceFeature(
                        name=feature["name"],
                        description=feature["description"],
                        included_in=[ServiceLevel(level) for level in feature.get("included_in", [])]
                    ) for feature in features
                ]
            
            provider = ManagedService(
                provider_name=provider_data["provider_name"],
                services_offered=services,
                pricing={ServiceLevel(k): v for k, v in provider_data["pricing"].items()},
                sla_uptime={ServiceLevel(k): v for k, v in provider_data["sla_uptime"].items()},
                support_channels=provider_data["support_channels"]
            )
            providers.append(provider)
        except KeyError as e:
            raise ValueError(f"Missing required field in provider data: {e}")
    
    return providers

def generate_comparison_report(providers: List[ManagedService], output_file: Optional[str] = None) -> dict:
    """
    Generate a comprehensive comparison report for all providers.
    
    Args:
        providers: List of ManagedService instances to compare
        output_file: Optional file path to save JSON report
        
    Returns:
        Dictionary containing full comparison report
    """
    if len(providers) < 2:
        raise ValueError("At least two providers required for comparison")
    
    report = {
        "providers": [p.provider_name for p in providers],
        "comparisons": {}
    }
    
    # Get all unique service types across providers
    service_types = set()
    for provider in providers:
        service_types.update(provider.services_offered.keys())
    
    # Compare each service type across all provider pairs
    for service_type in service_types:
        report["comparisons"][service_type] = []
        for i in range(len(providers)):
            for j in range(i + 1, len(providers)):
                comparison = providers[i].compare_with(providers[j], service_type)
                report["comparisons"][service_type].append(comparison)
    
    if output_file:
        try:
            with open(output_file, 'w') as f:
                json.dump(report, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save report to file: {e}")
    
    return report

# Example usage
if __name__ == "__main__":
    try:
        # Load provider data
        providers = load_providers_from_json("providers.json")
        
        # Generate and print comparison report
        report = generate_comparison_report(providers, "comparison_report.json")
        print("Comparison report generated successfully.")
        
    except Exception as e:
        print(f"Error: {e}")
```
