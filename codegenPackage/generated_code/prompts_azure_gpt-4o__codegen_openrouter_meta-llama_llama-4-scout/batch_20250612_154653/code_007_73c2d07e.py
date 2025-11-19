"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Write a function to calculate the economic impact of biotech partnerships, similar to CSL Seqirus UK's collaborations with Canadian life sciences ecosystems.
Generated: DETERMINISTIC_73c2d07e1c1d9011
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# economic_impact_calculator.py

from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Partnership:
    """Represents a biotech partnership."""
    name: str
    investment: float  # in million dollars
    jobs_created: int
    revenue_generated: float  # in million dollars

def calculate_economic_impact(partnerships: List[Partnership]) -> Dict[str, float]:
    """
    Calculates the economic impact of biotech partnerships.

    Args:
    partnerships (List[Partnership]): A list of Partnership objects.

    Returns:
    Dict[str, float]: A dictionary containing the total investment, total jobs created, and total revenue generated.
    """
    try:
        total_investment = sum(partnership.investment for partnership in partnerships)
        total_jobs_created = sum(partnership.jobs_created for partnership in partnerships)
        total_revenue_generated = sum(partnership.revenue_generated for partnership in partnerships)

        economic_impact = {
            "total_investment": total_investment,
            "total_jobs_created": total_jobs_created,
            "total_revenue_generated": total_revenue_generated,
            "return_on_investment": total_revenue_generated / total_investment if total_investment > 0 else 0,
            "jobs_per_million_dollar_investment": total_jobs_created / total_investment if total_investment > 0 else 0,
        }

        return economic_impact

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {}

def main():
    # Example usage:
    partnerships = [
        Partnership("CSL Seqirus UK", 10.0, 50, 20.0),
        Partnership("Canadian Life Sciences", 5.0, 20, 10.0),
    ]

    economic_impact = calculate_economic_impact(partnerships)
    print("Economic Impact:")
    for key, value in economic_impact.items():
        print(f"{key.capitalize().replace('_', ' ')}: {value:.2f}")

if __name__ == "__main__":
    main()
```
