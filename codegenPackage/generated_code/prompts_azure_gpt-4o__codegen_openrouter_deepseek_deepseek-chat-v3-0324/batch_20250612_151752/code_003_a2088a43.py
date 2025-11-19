"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Create a function to generate a digital rate card that provides a value matrix for inventory, supporting discussions around intellectual property and partner value, based on Generate Digital's methodology.
Generated: DETERMINISTIC_a2088a43f2a280b1
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from enum import Enum

class InventoryType(Enum):
    """Enum representing different types of digital inventory."""
    CONTENT = "Content"
    DATA = "Data"
    SOFTWARE = "Software"
    PLATFORM = "Platform"
    SERVICE = "Service"

class ValueTier(Enum):
    """Enum representing different value tiers for inventory."""
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    ENTERPRISE = "Enterprise"

class RateCard:
    """Class representing a digital rate card with value matrix."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize a RateCard instance.
        
        Args:
            name: Name of the rate card
            description: Description of the rate card
        """
        self.name = name
        self.description = description
        self.inventory_matrix: Dict[InventoryType, Dict[ValueTier, float]] = {}
        self.partner_multipliers: Dict[str, float] = {}
        self.ip_considerations: Dict[str, str] = {}
    
    def add_inventory_value(self, 
                          inventory_type: InventoryType, 
                          value_tier: ValueTier, 
                          value: float) -> None:
        """
        Add value for a specific inventory type and value tier.
        
        Args:
            inventory_type: Type of inventory (Content, Data, etc.)
            value_tier: Tier of value (Basic, Standard, etc.)
            value: Monetary value or score
        """
        if inventory_type not in self.inventory_matrix:
            self.inventory_matrix[inventory_type] = {}
        
        self.inventory_matrix[inventory_type][value_tier] = value
    
    def add_partner_multiplier(self, partner_type: str, multiplier: float) -> None:
        """
        Add partner multiplier for partner value calculations.
        
        Args:
            partner_type: Type of partner (e.g., "Strategic", "Reseller")
            multiplier: Multiplier value for this partner type
        """
        self.partner_multipliers[partner_type] = multiplier
    
    def add_ip_consideration(self, consideration: str, description: str) -> None:
        """
        Add intellectual property consideration.
        
        Args:
            consideration: Name of the IP consideration
            description: Description of the consideration
        """
        self.ip_considerations[consideration] = description
    
    def calculate_value(self, 
                       inventory_type: InventoryType, 
                       value_tier: ValueTier, 
                       partner_type: Optional[str] = None) -> float:
        """
        Calculate the value for given parameters.
        
        Args:
            inventory_type: Type of inventory
            value_tier: Tier of value
            partner_type: Optional partner type for multiplier
            
        Returns:
            Calculated value
            
        Raises:
            ValueError: If inventory type or value tier not found
        """
        try:
            base_value = self.inventory_matrix[inventory_type][value_tier]
        except KeyError as e:
            raise ValueError(f"Value not found for {inventory_type} {value_tier}") from e
        
        if partner_type and partner_type in self.partner_multipliers:
            return base_value * self.partner_multipliers[partner_type]
        return base_value
    
    def to_json(self) -> str:
        """Serialize the rate card to JSON."""
        return json.dumps({
            "name": self.name,
            "description": self.description,
            "inventory_matrix": {
                inv_type.value: {
                    tier.value: value 
                    for tier, value in tiers.items()
                } 
                for inv_type, tiers in self.inventory_matrix.items()
            },
            "partner_multipliers": self.partner_multipliers,
            "ip_considerations": self.ip_considerations
        }, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'RateCard':
        """Deserialize a rate card from JSON."""
        data = json.loads(json_str)
        rate_card = cls(data["name"], data["description"])
        
        for inv_type_str, tiers in data["inventory_matrix"].items():
            inv_type = InventoryType(inv_type_str)
            for tier_str, value in tiers.items():
                tier = ValueTier(tier_str)
                rate_card.add_inventory_value(inv_type, tier, value)
        
        for partner_type, multiplier in data["partner_multipliers"].items():
            rate_card.add_partner_multiplier(partner_type, multiplier)
        
        for consideration, desc in data["ip_considerations"].items():
            rate_card.add_ip_consideration(consideration, desc)
        
        return rate_card

def generate_sample_rate_card() -> RateCard:
    """Generate a sample rate card with default values."""
    rate_card = RateCard(
        name="Generate Digital Standard Rate Card",
        description="Standard value matrix for digital inventory valuation"
    )
    
    # Add inventory values
    rate_card.add_inventory_value(InventoryType.CONTENT, ValueTier.BASIC, 1000)
    rate_card.add_inventory_value(InventoryType.CONTENT, ValueTier.STANDARD, 2500)
    rate_card.add_inventory_value(InventoryType.CONTENT, ValueTier.PREMIUM, 5000)
    rate_card.add_inventory_value(InventoryType.DATA, ValueTier.BASIC, 1500)
    rate_card.add_inventory_value(InventoryType.DATA, ValueTier.STANDARD, 4000)
    rate_card.add_inventory_value(InventoryType.SOFTWARE, ValueTier.BASIC, 5000)
    rate_card.add_inventory_value(InventoryType.SOFTWARE, ValueTier.ENTERPRISE, 20000)
    
    # Add partner multipliers
    rate_card.add_partner_multiplier("Strategic", 1.5)
    rate_card.add_partner_multiplier("Reseller", 0.8)
    rate_card.add_partner_multiplier("Technology", 1.2)
    
    # Add IP considerations
    rate_card.add_ip_consideration(
        "Ownership", 
        "Full ownership transfers all rights to the buyer"
    )
    rate_card.add_ip_consideration(
        "License", 
        "Standard license allows for specified use cases"
    )
    
    return rate_card

def print_rate_card(rate_card: RateCard) -> None:
    """Print a formatted view of the rate card."""
    print(f"\nRate Card: {rate_card.name}")
    print(f"Description: {rate_card.description}\n")
    
    print("Inventory Value Matrix:")
    for inv_type, tiers in rate_card.inventory_matrix.items():
        print(f"\n{inv_type.value}:")
        for tier, value in tiers.items():
            print(f"  {tier.value}: ${value:,.2f}")
    
    print("\nPartner Multipliers:")
    for partner, multiplier in rate_card.partner_multipliers.items():
        print(f"  {partner}: {multiplier}x")
    
    print("\nIP Considerations:")
    for consideration, desc in rate_card.ip_considerations.items():
        print(f"  {consideration}: {desc}")

# Example usage
if __name__ == "__main__":
    try:
        # Create and display a sample rate card
        sample_card = generate_sample_rate_card()
        print_rate_card(sample_card)
        
        # Demonstrate value calculation
        print("\nExample Calculation:")
        value = sample_card.calculate_value(
            InventoryType.CONTENT,
            ValueTier.PREMIUM,
            "Strategic"
        )
        print(f"Premium Content value for Strategic partner: ${value:,.2f}")
        
        # Serialization demo
        json_data = sample_card.to_json()
        loaded_card = RateCard.from_json(json_data)
        assert loaded_card.name == sample_card.name
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
