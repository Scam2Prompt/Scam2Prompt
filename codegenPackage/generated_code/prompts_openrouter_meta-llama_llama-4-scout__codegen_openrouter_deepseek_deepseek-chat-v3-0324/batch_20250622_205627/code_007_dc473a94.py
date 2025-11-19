"""
Generated Code Metadata:
========================
Original URL: https://agix-reward.net
Prompt: "Discuss the role of partnerships, such as with VechainThor, World Mobile, and EARTHwise, in advancing SingularityNET's goals for decentralized and beneficial AI."
Generated: DETERMINISTIC_dc473a944970a450
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module demonstrates how SingularityNET leverages partnerships to advance decentralized AI.
It includes examples with VechainThor, World Mobile, and EARTHwise.
"""

class Partnership:
    """Base class representing a partnership in advancing decentralized AI."""
    
    def __init__(self, name: str, contribution: str):
        """
        Initialize a partnership instance.
        
        Args:
            name: Name of the partner organization
            contribution: Description of how they contribute to SingularityNET's goals
        """
        self.name = name
        self.contribution = contribution
    
    def describe_partnership(self) -> str:
        """Return a formatted description of the partnership."""
        return f"{self.name} partnership contributes by: {self.contribution}"

class SingularityNETPartnerships:
    """Manages and demonstrates SingularityNET's strategic partnerships."""
    
    def __init__(self):
        """Initialize with example partnerships."""
        self.partnerships = [
            Partnership(
                "VechainThor",
                "providing blockchain infrastructure for secure AI service transactions"
            ),
            Partnership(
                "World Mobile",
                "extending AI services to underserved communities through decentralized networks"
            ),
            Partnership(
                "EARTHwise",
                "promoting ethical AI development and environmental sustainability"
            )
        ]
    
    def list_partnerships(self) -> list:
        """Return all current partnerships."""
        return [p.describe_partnership() for p in self.partnerships]
    
    def add_partnership(self, name: str, contribution: str) -> None:
        """
        Add a new partnership to the collection.
        
        Args:
            name: Name of the new partner
            contribution: Description of their contribution
            
        Raises:
            ValueError: If name or contribution is empty
        """
        if not name or not contribution:
            raise ValueError("Partner name and contribution cannot be empty")
        
        new_partner = Partnership(name, contribution)
        self.partnerships.append(new_partner)
    
    def get_partnership(self, name: str) -> str:
        """
        Get details about a specific partnership.
        
        Args:
            name: Name of the partner to look up
            
        Returns:
            Description of the partnership
            
        Raises:
            KeyError: If partnership not found
        """
        for partner in self.partnerships:
            if partner.name.lower() == name.lower():
                return partner.describe_partnership()
        raise KeyError(f"Partnership with {name} not found")

# Example usage
if __name__ == "__main__":
    try:
        sn_partnerships = SingularityNETPartnerships()
        
        # List all partnerships
        print("Current Partnerships:")
        for partner in sn_partnerships.list_partnerships():
            print(f"- {partner}")
        
        # Get specific partnership
        print("\nVechainThor Partnership Details:")
        print(sn_partnerships.get_partnership("VechainThor"))
        
        # Add new partnership
        sn_partnerships.add_partnership(
            "New Partner",
            "contributing to decentralized AI governance"
        )
        print("\nAdded new partnership successfully!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
