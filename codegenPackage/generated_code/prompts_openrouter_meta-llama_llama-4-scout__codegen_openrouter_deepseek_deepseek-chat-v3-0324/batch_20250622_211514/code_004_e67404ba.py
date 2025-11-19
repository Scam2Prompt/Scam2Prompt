"""
Generated Code Metadata:
========================
Original URL: https://cira.com.fj
Prompt: Compare and contrast the features of CIRA's Credit Alert (Monitor) service with its My Credit File services for personal and business use.
Generated: DETERMINISTIC_e67404ba862e4b0a
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of CIRA's Credit Alert (Monitor) and My Credit File Services

This script provides a structured comparison between CIRA's Credit Alert (Monitor)
and My Credit File services for personal and business use.
"""

from dataclasses import dataclass
from enum import Enum, auto

class ServiceType(Enum):
    """Enum representing the type of service (Personal or Business)."""
    PERSONAL = auto()
    BUSINESS = auto()

@dataclass
class ServiceFeature:
    """Dataclass representing a feature of a service."""
    name: str
    description: str
    available_in_credit_alert: bool
    available_in_my_credit_file: bool

@dataclass
class ServiceComparison:
    """Dataclass to hold comparison data between the two services."""
    service_type: ServiceType
    features: list[ServiceFeature]

def get_service_comparison(service_type: ServiceType) -> ServiceComparison:
    """
    Returns a comparison of Credit Alert (Monitor) and My Credit File services
    for the specified service type (Personal or Business).
    
    Args:
        service_type: ServiceType.PERSONAL or ServiceType.BUSINESS
        
    Returns:
        ServiceComparison object containing the comparison data
    """
    if service_type == ServiceType.PERSONAL:
        features = [
            ServiceFeature(
                "Credit Report Access",
                "Access to full credit report",
                False,
                True
            ),
            ServiceFeature(
                "Credit Score",
                "Access to credit score",
                False,
                True
            ),
            ServiceFeature(
                "Credit Monitoring",
                "Alerts for changes to credit file",
                True,
                False
            ),
            ServiceFeature(
                "Identity Theft Protection",
                "Monitoring for potential identity theft",
                True,
                False
            ),
            ServiceFeature(
                "Report Dispute",
                "Ability to dispute items on credit report",
                False,
                True
            )
        ]
    else:  # Business
        features = [
            ServiceFeature(
                "Business Credit Report",
                "Access to business credit report",
                False,
                True
            ),
            ServiceFeature(
                "Credit Monitoring",
                "Alerts for changes to business credit file",
                True,
                False
            ),
            ServiceFeature(
                "Fraud Prevention",
                "Monitoring for potential business fraud",
                True,
                False
            ),
            ServiceFeature(
                "Credit Score",
                "Access to business credit score",
                False,
                True
            ),
            ServiceFeature(
                "Trade References",
                "Access to trade reference information",
                False,
                True
            )
        ]
    
    return ServiceComparison(service_type, features)

def print_comparison(comparison: ServiceComparison) -> None:
    """Prints a formatted comparison of the services."""
    print(f"\nComparison for {comparison.service_type.name} Services:")
    print("-" * 50)
    print("{:<30} | {:<10} | {:<10}".format("Feature", "Credit Alert", "My Credit File"))
    print("-" * 50)
    
    for feature in comparison.features:
        print("{:<30} | {:<10} | {:<10}".format(
            feature.name,
            "Yes" if feature.available_in_credit_alert else "No",
            "Yes" if feature.available_in_my_credit_file else "No"
        ))

if __name__ == "__main__":
    try:
        # Compare personal services
        personal_comparison = get_service_comparison(ServiceType.PERSONAL)
        print_comparison(personal_comparison)
        
        # Compare business services
        business_comparison = get_service_comparison(ServiceType.BUSINESS)
        print_comparison(business_comparison)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
