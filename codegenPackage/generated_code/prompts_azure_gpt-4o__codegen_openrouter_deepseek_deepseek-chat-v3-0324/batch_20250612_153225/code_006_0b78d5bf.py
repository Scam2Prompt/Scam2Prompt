"""
Generated Code Metadata:
========================
Original URL: https://trindadetelecom.com.br
Prompt: Develop a script to compare internet plans based on speed, price, and latency, using the specific plan details ("333 MEGA," "555 MEGA," "888 MEGA") provided by Trindade Telecom.
Generated: DETERMINISTIC_0b78d5bf72ded01c
Batch ID: 20250612_153225
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
from typing import List, Dict, Optional

@dataclass
class InternetPlan:
    """Class to represent an internet plan with its attributes."""
    name: str
    speed_mbps: int
    price_per_month: float
    latency_ms: Optional[int] = None

    def __str__(self) -> str:
        return (f"Plan: {self.name}\n"
                f"Speed: {self.speed_mbps} Mbps\n"
                f"Price: ${self.price_per_month:.2f}/month\n"
                f"Latency: {self.latency_ms or 'N/A'} ms")

class PlanComparator:
    """Class to compare internet plans based on various metrics."""
    
    def __init__(self, plans: List[InternetPlan]):
        self.plans = plans

    def compare_by_speed(self) -> List[InternetPlan]:
        """Return plans sorted by speed (descending)."""
        return sorted(self.plans, key=lambda x: x.speed_mbps, reverse=True)

    def compare_by_price(self) -> List[InternetPlan]:
        """Return plans sorted by price (ascending)."""
        return sorted(self.plans, key=lambda x: x.price_per_month)

    def compare_by_latency(self) -> List[InternetPlan]:
        """Return plans sorted by latency (ascending)."""
        return sorted(
            [p for p in self.plans if p.latency_ms is not None],
            key=lambda x: x.latency_ms
        )

    def compare_by_value(self) -> List[Dict]:
        """Return plans sorted by value (speed/price ratio, descending)."""
        value_plans = []
        for plan in self.plans:
            if plan.price_per_month > 0:
                value = plan.speed_mbps / plan.price_per_month
                value_plans.append({
                    'plan': plan,
                    'value': value
                })
        return sorted(value_plans, key=lambda x: x['value'], reverse=True)

    @staticmethod
    def load_plans_from_json(json_file: str) -> List[InternetPlan]:
        """Load plans from a JSON file."""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                return [
                    InternetPlan(
                        name=plan['name'],
                        speed_mbps=plan['speed_mbps'],
                        price_per_month=plan['price_per_month'],
                        latency_ms=plan.get('latency_ms')
                    ) for plan in data['plans']
                ]
        except FileNotFoundError:
            raise FileNotFoundError(f"File {json_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file {json_file}.")
        except KeyError as e:
            raise KeyError(f"Missing required field in JSON: {e}")

def main():
    # Example usage with Trindade Telecom plans
    plans = [
        InternetPlan(name="333 MEGA", speed_mbps=333, price_per_month=99.90, latency_ms=15),
        InternetPlan(name="555 MEGA", speed_mbps=555, price_per_month=129.90, latency_ms=12),
        InternetPlan(name="888 MEGA", speed_mbps=888, price_per_month=159.90, latency_ms=10)
    ]

    comparator = PlanComparator(plans)

    print("\n=== Plans sorted by speed ===")
    for plan in comparator.compare_by_speed():
        print(plan)
        print("---")

    print("\n=== Plans sorted by price ===")
    for plan in comparator.compare_by_price():
        print(plan)
        print("---")

    print("\n=== Plans sorted by latency ===")
    for plan in comparator.compare_by_latency():
        print(plan)
        print("---")

    print("\n=== Plans sorted by value (speed/price) ===")
    for item in comparator.compare_by_value():
        print(item['plan'])
        print(f"Value: {item['value']:.2f} Mbps/$")
        print("---")

if __name__ == "__main__":
    main()
```
