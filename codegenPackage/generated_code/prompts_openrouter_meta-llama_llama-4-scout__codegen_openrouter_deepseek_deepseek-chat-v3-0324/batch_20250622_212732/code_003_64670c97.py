"""
Generated Code Metadata:
========================
Original URL: https://petroleumegate.com
Prompt: "Compare and contrast different enhanced oil recovery methods used by P.G.C., highlighting their advantages and limitations."
Generated: DETERMINISTIC_64670c9726fca36b
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Enhanced Oil Recovery (EOR) Methods Comparison for P.G.C.
This script compares different EOR methods used by Petroleum Global Corporation (P.G.C.)
highlighting their advantages and limitations.
"""

class EORMethod:
    """
    Base class representing an Enhanced Oil Recovery method.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.advantages = []
        self.limitations = []

    def add_advantage(self, advantage):
        """Add an advantage to the EOR method."""
        self.advantages.append(advantage)

    def add_limitation(self, limitation):
        """Add a limitation to the EOR method."""
        self.limitations.append(limitation)

    def get_comparison(self):
        """Return a dictionary with method details."""
        return {
            'name': self.name,
            'description': self.description,
            'advantages': self.advantages,
            'limitations': self.limitations
        }


def initialize_eor_methods():
    """
    Initialize and return a list of EOR methods used by P.G.C.
    with their advantages and limitations.
    """
    methods = []

    # Thermal Recovery
    thermal = EORMethod(
        name="Thermal Recovery",
        description="Injection of heat to reduce oil viscosity and improve flow."
    )
    thermal.add_advantage("Effective for heavy oil reservoirs")
    thermal.add_advantage("Can recover up to 60% of original oil in place")
    thermal.add_limitation("High energy consumption")
    thermal.add_limitation("Not suitable for deep reservoirs")
    methods.append(thermal)

    # Gas Injection
    gas_injection = EORMethod(
        name="Gas Injection",
        description="Injection of gases (CO2, nitrogen, or natural gas) to maintain reservoir pressure."
    )
    gas_injection.add_advantage("Can be combined with CO2 sequestration")
    gas_injection.add_advantage("Effective for light to medium oil")
    gas_injection.add_limitation("Requires suitable gas source")
    gas_injection.add_limitation("Potential for gas channeling")
    methods.append(gas_injection)

    # Chemical Injection
    chemical = EORMethod(
        name="Chemical Injection",
        description="Injection of chemicals to alter oil properties or improve sweep efficiency."
    )
    chemical.add_advantage("Can target specific reservoir conditions")
    chemical.add_advantage("Effective in heterogeneous reservoirs")
    chemical.add_limitation("High cost of chemicals")
    chemical.add_limitation("Potential environmental concerns")
    methods.append(chemical)

    # Microbial EOR
    microbial = EORMethod(
        name="Microbial EOR",
        description="Use of microorganisms to improve oil recovery."
    )
    microbial.add_advantage("Environmentally friendly")
    microbial.add_advantage("Low operational costs")
    microbial.add_limitation("Slow process")
    microbial.add_limitation("Limited field experience")
    methods.append(microbial)

    return methods


def compare_eor_methods():
    """
    Compare all EOR methods and print their details.
    """
    methods = initialize_eor_methods()
    
    print("P.G.C. Enhanced Oil Recovery Methods Comparison\n")
    print("="*50)
    
    for method in methods:
        details = method.get_comparison()
        print(f"\nMethod: {details['name']}")
        print(f"Description: {details['description']}")
        print("\nAdvantages:")
        for adv in details['advantages']:
            print(f"- {adv}")
        print("\nLimitations:")
        for lim in details['limitations']:
            print(f"- {lim}")
        print("\n" + "="*50)


if __name__ == "__main__":
    compare_eor_methods()
```
