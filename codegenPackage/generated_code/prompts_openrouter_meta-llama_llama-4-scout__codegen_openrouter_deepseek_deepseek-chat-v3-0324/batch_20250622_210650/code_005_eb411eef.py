"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: "Compare and contrast different types of alarm systems (e.g., wired vs. wireless) for a commercial building, considering factors like reliability, scalability, and cost-effectiveness."
Generated: DETERMINISTIC_eb411eefdbbba365
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Alarm System Comparison Tool for Commercial Buildings

This script compares different types of alarm systems (wired vs. wireless)
based on reliability, scalability, and cost-effectiveness.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict

class AlarmType(Enum):
    WIRED = auto()
    WIRELESS = auto()
    HYBRID = auto()

@dataclass
class AlarmSystem:
    """Represents an alarm system with its characteristics."""
    name: str
    system_type: AlarmType
    reliability_score: float  # 0-10 scale
    scalability_score: float  # 0-10 scale
    cost_effectiveness_score: float  # 0-10 scale
    installation_cost: float  # in USD
    monthly_cost: float  # in USD
    description: str

def compare_alarm_systems(systems: List[AlarmSystem]) -> Dict[str, AlarmSystem]:
    """
    Compare alarm systems and return the best option for each category.
    
    Args:
        systems: List of AlarmSystem objects to compare
        
    Returns:
        Dictionary with best system for each category
    """
    results = {
        "most_reliable": max(systems, key=lambda x: x.reliability_score),
        "most_scalable": max(systems, key=lambda x: x.scalability_score),
        "most_cost_effective": max(systems, key=lambda x: x.cost_effectiveness_score),
        "lowest_installation_cost": min(systems, key=lambda x: x.installation_cost),
        "lowest_monthly_cost": min(systems, key=lambda x: x.monthly_cost)
    }
    return results

def generate_comparison_report(systems: List[AlarmSystem]) -> str:
    """
    Generate a formatted comparison report of alarm systems.
    
    Args:
        systems: List of AlarmSystem objects to compare
        
    Returns:
        Formatted string report
    """
    comparison = compare_alarm_systems(systems)
    report = []
    
    report.append("ALARM SYSTEM COMPARISON REPORT")
    report.append("=" * 30)
    
    for system in systems:
        report.append(f"\nSystem: {system.name} ({system.system_type.name})")
        report.append(f"Description: {system.description}")
        report.append(f"Reliability: {system.reliability_score}/10")
        report.append(f"Scalability: {system.scalability_score}/10")
        report.append(f"Cost-effectiveness: {system.cost_effectiveness_score}/10")
        report.append(f"Installation Cost: ${system.installation_cost:,.2f}")
        report.append(f"Monthly Cost: ${system.monthly_cost:,.2f}")
    
    report.append("\nBEST OPTIONS:")
    report.append("-" * 30)
    for category, system in comparison.items():
        report.append(f"{category.replace('_', ' ').title()}: {system.name}")
    
    return "\n".join(report)

# Example usage
if __name__ == "__main__":
    # Sample alarm systems data
    systems = [
        AlarmSystem(
            name="SecureWired Pro",
            system_type=AlarmType.WIRED,
            reliability_score=9.5,
            scalability_score=7.0,
            cost_effectiveness_score=8.0,
            installation_cost=15000,
            monthly_cost=50,
            description="High-reliability wired system with extensive coverage"
        ),
        AlarmSystem(
            name="FlexiWireless X",
            system_type=AlarmType.WIRELESS,
            reliability_score=8.0,
            scalability_score=9.5,
            cost_effectiveness_score=9.0,
            installation_cost=8000,
            monthly_cost=75,
            description="Flexible wireless system with easy expansion"
        ),
        AlarmSystem(
            name="HybridGuard Plus",
            system_type=AlarmType.HYBRID,
            reliability_score=9.0,
            scalability_score=8.5,
            cost_effectiveness_score=8.5,
            installation_cost=12000,
            monthly_cost=60,
            description="Combines wired reliability with wireless flexibility"
        )
    ]
    
    try:
        report = generate_comparison_report(systems)
        print(report)
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
