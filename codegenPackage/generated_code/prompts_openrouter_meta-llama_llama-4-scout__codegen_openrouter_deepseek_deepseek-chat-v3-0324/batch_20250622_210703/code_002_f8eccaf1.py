"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Compare and contrast the advantages of enamel, acrylic, and epoxy coatings for exterior surfaces in Mornington Peninsula, and recommend the best option for a commercial painting project in the region.
Generated: DETERMINISTIC_f8eccaf19933ef43
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script analyzes and compares enamel, acrylic, and epoxy coatings for exterior surfaces
in Mornington Peninsula, Australia, considering local climate conditions.
It recommends the best option for a commercial painting project in the region.
"""

import enum
from dataclasses import dataclass
from typing import List, Dict

class ClimateFactor(enum.Enum):
    """Climate factors relevant to coating performance in Mornington Peninsula"""
    UV_EXPOSURE = "High UV exposure"
    SALT_AIR = "Coastal salt air"
    TEMPERATURE_FLUCTUATION = "Moderate temperature fluctuations"
    RAINFALL = "Moderate rainfall"
    HUMIDITY = "Moderate humidity"

class CoatingType(enum.Enum):
    """Types of coatings being compared"""
    ENAMEL = "Enamel"
    ACRYLIC = "Acrylic"
    EPOXY = "Epoxy"

@dataclass
class CoatingProperty:
    """Properties of each coating type"""
    durability: int  # 1-10 scale
    uv_resistance: int  # 1-10 scale
    moisture_resistance: int  # 1-10 scale
    salt_resistance: int  # 1-10 scale
    ease_of_application: int  # 1-10 scale
    cost: int  # 1-10 scale (1=lowest)
    maintenance_frequency: int  # years between recoating

@dataclass
class CoatingAnalysis:
    """Analysis of a coating type against climate factors"""
    coating_type: CoatingType
    properties: CoatingProperty
    climate_suitability: Dict[ClimateFactor, bool]
    advantages: List[str]
    disadvantages: List[str]

def analyze_coatings() -> Dict[CoatingType, CoatingAnalysis]:
    """Analyze and compare coating types for Mornington Peninsula conditions"""
    coating_properties = {
        CoatingType.ENAMEL: CoatingProperty(
            durability=7,
            uv_resistance=6,
            moisture_resistance=5,
            salt_resistance=4,
            ease_of_application=6,
            cost=4,
            maintenance_frequency=5
        ),
        CoatingType.ACRYLIC: CoatingProperty(
            durability=8,
            uv_resistance=9,
            moisture_resistance=8,
            salt_resistance=7,
            ease_of_application=8,
            cost=6,
            maintenance_frequency=7
        ),
        CoatingType.EPOXY: CoatingProperty(
            durability=9,
            uv_resistance=5,
            moisture_resistance=9,
            salt_resistance=9,
            ease_of_application=5,
            cost=8,
            maintenance_frequency=8
        )
    }

    analyses = {
        CoatingType.ENAMEL: CoatingAnalysis(
            coating_type=CoatingType.ENAMEL,
            properties=coating_properties[CoatingType.ENAMEL],
            climate_suitability={
                ClimateFactor.UV_EXPOSURE: True,
                ClimateFactor.SALT_AIR: False,
                ClimateFactor.TEMPERATURE_FLUCTUATION: True,
                ClimateFactor.RAINFALL: False,
                ClimateFactor.HUMIDITY: False
            },
            advantages=[
                "Good durability",
                "Moderate UV resistance",
                "Lower cost"
            ],
            disadvantages=[
                "Poor salt resistance",
                "Requires frequent maintenance",
                "Not ideal for humid conditions"
            ]
        ),
        CoatingType.ACRYLIC: CoatingAnalysis(
            coating_type=CoatingType.ACRYLIC,
            properties=coating_properties[CoatingType.ACRYLIC],
            climate_suitability={
                ClimateFactor.UV_EXPOSURE: True,
                ClimateFactor.SALT_AIR: True,
                ClimateFactor.TEMPERATURE_FLUCTUATION: True,
                ClimateFactor.RAINFALL: True,
                ClimateFactor.HUMIDITY: True
            },
            advantages=[
                "Excellent UV resistance",
                "Good moisture resistance",
                "Moderate salt resistance",
                "Easy to apply"
            ],
            disadvantages=[
                "Higher cost than enamel",
                "Less durable than epoxy"
            ]
        ),
        CoatingType.EPOXY: CoatingAnalysis(
            coating_type=CoatingType.EPOXY,
            properties=coating_properties[CoatingType.EPOXY],
            climate_suitability={
                ClimateFactor.UV_EXPOSURE: False,
                ClimateFactor.SALT_AIR: True,
                ClimateFactor.TEMPERATURE_FLUCTUATION: True,
                ClimateFactor.RAINFALL: True,
                ClimateFactor.HUMIDITY: True
            },
            advantages=[
                "Excellent durability",
                "Superior moisture resistance",
                "Excellent salt resistance",
                "Long maintenance intervals"
            ],
            disadvantages=[
                "Poor UV resistance",
                "Difficult application",
                "Highest cost"
            ]
        )
    }
    
    return analyses

def recommend_coating(analyses: Dict[CoatingType, CoatingAnalysis]) -> CoatingType:
    """Determine the best coating for commercial projects in Mornington Peninsula"""
    # Weighting factors based on commercial project priorities
    weights = {
        'durability': 0.2,
        'uv_resistance': 0.25,
        'moisture_resistance': 0.15,
        'salt_resistance': 0.2,
        'ease_of_application': 0.05,
        'cost': 0.1,
        'maintenance_frequency': 0.05
    }
    
    scores = {}
    for coating_type, analysis in analyses.items():
        prop = analysis.properties
        score = (
            prop.durability * weights['durability'] +
            prop.uv_resistance * weights['uv_resistance'] +
            prop.moisture_resistance * weights['moisture_resistance'] +
            prop.salt_resistance * weights['salt_resistance'] +
            prop.ease_of_application * weights['ease_of_application'] +
            (10 - prop.cost) * weights['cost'] +  # Invert cost (higher is worse)
            prop.maintenance_frequency * weights['maintenance_frequency']
        )
        scores[coating_type] = score
    
    return max(scores.items(), key=lambda x: x[1])[0]

def generate_report(analyses: Dict[CoatingType, CoatingAnalysis], recommendation: CoatingType) -> str:
    """Generate a formatted report of the analysis"""
    report = []
    report.append("COATING COMPARISON REPORT FOR MORNINGTON PENINSULA")
    report.append("="*50)
    report.append("\nCLIMATE CONSIDERATIONS:")
    for factor in ClimateFactor:
        report.append(f"- {factor.value}")
    
    report.append("\nCOATING ANALYSIS:")
    for coating_type, analysis in analyses.items():
        report.append(f"\n{coating_type.value.upper()}")
        report.append("-"*len(coating_type.value))
        report.append(f"Advantages: {', '.join(analysis.advantages)}")
        report.append(f"Disadvantages: {', '.join(analysis.disadvantages)}")
        report.append("Climate suitability:")
        for factor, suitable in analysis.climate_suitability.items():
            status = "✓" if suitable else "✗"
            report.append(f"  {status} {factor.value}")
    
    report.append("\nRECOMMENDATION:")
    report.append(f"For commercial projects in Mornington Peninsula, the recommended coating is: {recommendation.value}")
    
    return "\n".join(report)

def main():
    """Main execution function"""
    try:
        analyses = analyze_coatings()
        recommendation = recommend_coating(analyses)
        report = generate_report(analyses, recommendation)
        print(report)
    except Exception as e:
        print(f"Error generating coating analysis: {str(e)}")

if __name__ == "__main__":
    main()
```
