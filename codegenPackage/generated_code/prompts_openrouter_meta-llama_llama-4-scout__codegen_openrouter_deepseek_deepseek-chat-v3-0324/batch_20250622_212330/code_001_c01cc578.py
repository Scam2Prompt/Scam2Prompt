"""
Generated Code Metadata:
========================
Original URL: https://libertyaid.co
Prompt: What are the different types of Medicare Advantage plans, including PFFS, MSA, HMO, and PPO plans?
Generated: DETERMINISTIC_c01cc578a1346857
Batch ID: 20250622_212330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MedicareAdvantagePlan:
    """
    Represents a Medicare Advantage Plan with its core attributes.
    """
    def __init__(self, name: str, description: str, network_restrictions: str, referrals_required: bool, 
                 out_of_pocket_max: float, premium: float):
        """
        Initialize a Medicare Advantage Plan.
        
        Args:
            name (str): Name of the plan type (e.g., HMO, PPO)
            description (str): Brief description of the plan
            network_restrictions (str): Description of network restrictions
            referrals_required (bool): Whether referrals are needed for specialists
            out_of_pocket_max (float): Maximum out-of-pocket cost
            premium (float): Monthly premium cost
        """
        self.name = name
        self.description = description
        self.network_restrictions = network_restrictions
        self.referrals_required = referrals_required
        self.out_of_pocket_max = out_of_pocket_max
        self.premium = premium

    def __str__(self) -> str:
        """Return a string representation of the plan."""
        return (f"{self.name} Plan:\n"
                f"Description: {self.description}\n"
                f"Network Restrictions: {self.network_restrictions}\n"
                f"Referrals Required: {'Yes' if self.referrals_required else 'No'}\n"
                f"Out-of-Pocket Max: ${self.out_of_pocket_max:,.2f}\n"
                f"Monthly Premium: ${self.premium:,.2f}")


def get_medicare_advantage_plans() -> list[MedicareAdvantagePlan]:
    """
    Returns a list of common Medicare Advantage plan types with their attributes.
    
    Returns:
        list[MedicareAdvantagePlan]: List of Medicare Advantage plan objects
    """
    plans = [
        MedicareAdvantagePlan(
            name="HMO",
            description="Health Maintenance Organization plans with local network coverage",
            network_restrictions="Must use network providers except emergencies",
            referrals_required=True,
            out_of_pocket_max=6700.00,
            premium=0.00
        ),
        MedicareAdvantagePlan(
            name="PPO",
            description="Preferred Provider Organization plans with flexible provider options",
            network_restrictions="Lower costs for in-network providers but out-of-network covered",
            referrals_required=False,
            out_of_pocket_max=8300.00,
            premium=50.00
        ),
        MedicareAdvantagePlan(
            name="PFFS",
            description="Private Fee-for-Service plans that determine how much to pay providers",
            network_restrictions="Can see any Medicare-approved provider who accepts plan's terms",
            referrals_required=False,
            out_of_pocket_max=10000.00,
            premium=75.00
        ),
        MedicareAdvantagePlan(
            name="MSA",
            description="Medical Savings Account plans combining high-deductible insurance with bank account",
            network_restrictions="Can see any Medicare-approved provider",
            referrals_required=False,
            out_of_pocket_max=10000.00,
            premium=0.00
        ),
        MedicareAdvantagePlan(
            name="SNP",
            description="Special Needs Plans for people with specific diseases or characteristics",
            network_restrictions="Must use network providers except emergencies",
            referrals_required=True,
            out_of_pocket_max=6700.00,
            premium=0.00
        )
    ]
    return plans


def display_plans(plans: list[MedicareAdvantagePlan]) -> None:
    """
    Prints information about each Medicare Advantage plan.
    
    Args:
        plans (list[MedicareAdvantagePlan]): List of plans to display
    """
    for plan in plans:
        print(plan)
        print("-" * 50)


if __name__ == "__main__":
    try:
        plans = get_medicare_advantage_plans()
        display_plans(plans)
    except Exception as e:
        print(f"An error occurred while retrieving Medicare Advantage plans: {e}")
```
