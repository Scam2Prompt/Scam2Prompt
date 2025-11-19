"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Develop a program that calculates property division according to Swedish "Sambolagen" (cohabitation law), as described on juridiskklinik.se.
Generated: DETERMINISTIC_dd93f00a41f91664
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Property Division Calculator according to Swedish 'Sambolagen' (Cohabitation Law)

This program calculates how property should be divided between cohabitants
when their relationship ends, based on Swedish cohabitation law.

Key principles:
1. Only property acquired for joint use is divided
2. Personal property remains with the original owner
3. The division should be fair considering contributions and needs

Reference: juridiskklinik.se
"""

class PropertyDivisionCalculator:
    """
    A calculator for dividing property between cohabitants according to Swedish law.
    """
    
    def __init__(self):
        """
        Initialize the calculator with empty property lists.
        """
        self.joint_property = []
        self.party_a_property = []
        self.party_b_property = []
        self.party_a_contributions = 0
        self.party_b_contributions = 0
        
    def add_joint_property(self, description: str, value: float):
        """
        Add property acquired for joint use.
        
        Args:
            description: Description of the property
            value: Monetary value of the property
        """
        if value <= 0:
            raise ValueError("Property value must be positive")
        self.joint_property.append({"description": description, "value": value})
        
    def add_personal_property(self, party: str, description: str, value: float):
        """
        Add personal property that belongs to one party.
        
        Args:
            party: 'A' or 'B' to indicate which party owns the property
            description: Description of the property
            value: Monetary value of the property
        """
        if value <= 0:
            raise ValueError("Property value must be positive")
            
        if party.upper() == 'A':
            self.party_a_property.append({"description": description, "value": value})
        elif party.upper() == 'B':
            self.party_b_property.append({"description": description, "value": value})
        else:
            raise ValueError("Party must be 'A' or 'B'")
            
    def add_contribution(self, party: str, amount: float):
        """
        Record financial contributions made by each party.
        
        Args:
            party: 'A' or 'B' to indicate which party made the contribution
            amount: The amount contributed
        """
        if amount <= 0:
            raise ValueError("Contribution amount must be positive")
            
        if party.upper() == 'A':
            self.party_a_contributions += amount
        elif party.upper() == 'B':
            self.party_b_contributions += amount
        else:
            raise ValueError("Party must be 'A' or 'B'")
            
    def calculate_division(self) -> dict:
        """
        Calculate the fair division of joint property according to Swedish law.
        
        Returns:
            A dictionary containing:
            - total_joint_value: Total value of joint property
            - party_a_share: Value to be awarded to party A
            - party_b_share: Value to be awarded to party B
            - party_a_personal: Value of party A's personal property
            - party_b_personal: Value of party B's personal property
        """
        if not self.joint_property:
            return {
                "total_joint_value": 0,
                "party_a_share": 0,
                "party_b_share": 0,
                "party_a_personal": sum(item["value"] for item in self.party_a_property),
                "party_b_personal": sum(item["value"] for item in self.party_b_property)
            }
            
        total_joint_value = sum(item["value"] for item in self.joint_property)
        total_contributions = self.party_a_contributions + self.party_b_contributions
        
        if total_contributions == 0:
            # Equal division if no contributions specified
            party_a_share = total_joint_value / 2
            party_b_share = total_joint_value / 2
        else:
            # Division proportional to contributions
            party_a_share = (self.party_a_contributions / total_contributions) * total_joint_value
            party_b_share = (self.party_b_contributions / total_contributions) * total_joint_value
            
        return {
            "total_joint_value": total_joint_value,
            "party_a_share": party_a_share,
            "party_b_share": party_b_share,
            "party_a_personal": sum(item["value"] for item in self.party_a_property),
            "party_b_personal": sum(item["value"] for item in self.party_b_property)
        }
        
    def generate_report(self) -> str:
        """
        Generate a human-readable report of the property division.
        
        Returns:
            A formatted string with the division results.
        """
        division = self.calculate_division()
        
        report = [
            "Property Division Report (According to Swedish Cohabitation Law)",
            "=" * 50,
            f"Total Joint Property Value: {division['total_joint_value']:.2f} SEK",
            f"Party A's Share: {division['party_a_share']:.2f} SEK",
            f"Party B's Share: {division['party_b_share']:.2f} SEK",
            "",
            "Personal Property:",
            f"Party A's Personal Property: {division['party_a_personal']:.2f} SEK",
            f"Party B's Personal Property: {division['party_b_personal']:.2f} SEK",
            "",
            "Contributions:",
            f"Party A's Contributions: {self.party_a_contributions:.2f} SEK",
            f"Party B's Contributions: {self.party_b_contributions:.2f} SEK"
        ]
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    calculator = PropertyDivisionCalculator()
    
    # Add joint property
    calculator.add_joint_property("Apartment", 3000000)
    calculator.add_joint_property("Car", 150000)
    calculator.add_joint_property("Furniture", 50000)
    
    # Add personal property
    calculator.add_personal_property('A', "Laptop", 15000)
    calculator.add_personal_property('B', "Jewelry", 25000)
    
    # Add contributions
    calculator.add_contribution('A', 2000000)
    calculator.add_contribution('B', 1200000)
    
    # Generate and print report
    print(calculator.generate_report())
```
