"""
Generated Code Metadata:
========================
Original URL: https://indexapplc.rf.gd
Prompt: Compare iFastNet's web hosting plans with and without a free domain name, and generate a list of pros and cons for each option.
Generated: DETERMINISTIC_cb54055620ec782f
Batch ID: 20250622_212533
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
from typing import List, Dict

@dataclass
class HostingPlan:
    name: str
    price: float
    features: List[str]
    has_free_domain: bool
    storage: str
    bandwidth: str
    websites: int
    email_accounts: int

class HostingPlanComparator:
    def __init__(self):
        self.plans = self._load_plans()
    
    def _load_plans(self) -> List[HostingPlan]:
        """Load sample hosting plans data"""
        return [
            HostingPlan(
                name="Starter",
                price=2.95,
                features=["1 Website", "10GB Storage", "Unmetered Bandwidth", "Free SSL"],
                has_free_domain=False,
                storage="10GB",
                bandwidth="Unmetered",
                websites=1,
                email_accounts=10
            ),
            HostingPlan(
                name="Starter with Domain",
                price=3.95,
                features=["1 Website", "10GB Storage", "Unmetered Bandwidth", "Free SSL", "Free Domain"],
                has_free_domain=True,
                storage="10GB",
                bandwidth="Unmetered",
                websites=1,
                email_accounts=10
            ),
            HostingPlan(
                name="Premium",
                price=5.95,
                features=["Unlimited Websites", "100GB Storage", "Unmetered Bandwidth", "Free SSL"],
                has_free_domain=False,
                storage="100GB",
                bandwidth="Unmetered",
                websites=-1,  # -1 indicates unlimited
                email_accounts=100
            ),
            HostingPlan(
                name="Premium with Domain",
                price=6.95,
                features=["Unlimited Websites", "100GB Storage", "Unmetered Bandwidth", "Free SSL", "Free Domain"],
                has_free_domain=True,
                storage="100GB",
                bandwidth="Unmetered",
                websites=-1,
                email_accounts=100
            )
        ]
    
    def _get_pros_cons(self, plan: HostingPlan) -> Dict[str, List[str]]:
        """Generate pros and cons for a given plan"""
        pros = []
        cons = []
        
        pros.append(f"Price: ${plan.price}/month")
        pros.append(f"Storage: {plan.storage}")
        pros.append(f"Bandwidth: {plan.bandwidth}")
        pros.append(f"Websites: {'Unlimited' if plan.websites == -1 else plan.websites}")
        pros.append(f"Email Accounts: {plan.email_accounts}")
        
        if plan.has_free_domain:
            pros.append("Includes free domain registration")
        else:
            cons.append("Does not include free domain (additional $10-$15/year)")
        
        if plan.websites == 1:
            cons.append("Limited to 1 website")
        
        return {"pros": pros, "cons": cons}
    
    def compare_plans(self) -> Dict[str, Dict]:
        """Compare all plans and return their pros/cons"""
        comparison = {}
        
        for plan in self.plans:
            comparison[plan.name] = self._get_pros_cons(plan)
        
        return comparison
    
    def generate_comparison_report(self) -> str:
        """Generate a formatted JSON report of the comparison"""
        comparison = self.compare_plans()
        return json.dumps(comparison, indent=2)

if __name__ == "__main__":
    try:
        comparator = HostingPlanComparator()
        report = comparator.generate_comparison_report()
        print(report)
    except Exception as e:
        print(f"Error generating comparison: {str(e)}")
```
