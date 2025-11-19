"""
Generated Code Metadata:
========================
Original URL: https://dao-magi-alpha.web.app
Prompt: Generate a program that dynamically calculates the trading fees and royalties for an NFT transaction using the Open Creator Protocol features described on the webpage.
Generated: DETERMINISTIC_543fdf7fcf47e298
Batch ID: 20250612_150557
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
class RoyaltyRecipient:
    address: str
    percentage: float

@dataclass
class FeeStructure:
    platform_fee_percentage: float
    royalty_recipients: List[RoyaltyRecipient]

class NFTTransactionCalculator:
    """
    A class to calculate trading fees and royalties for NFT transactions
    following the Open Creator Protocol.
    """
    
    def __init__(self, fee_structure: FeeStructure):
        """
        Initialize the calculator with the fee structure.
        
        Args:
            fee_structure: FeeStructure containing platform fee and royalty recipients
        """
        self.fee_structure = fee_structure
        
    def validate_fee_structure(self) -> bool:
        """
        Validate that the fee structure is correct:
        - Platform fee is between 0 and 100
        - Royalty percentages sum to <= 100
        - All percentages are positive
        
        Returns:
            bool: True if valid, False otherwise
        """
        total_royalty = sum(r.percentage for r in self.fee_structure.royalty_recipients)
        
        if not (0 <= self.fee_structure.platform_fee_percentage <= 100):
            return False
        if total_royalty > 100:
            return False
        if any(r.percentage < 0 for r in self.fee_structure.royalty_recipients):
            return False
            
        return True
    
    def calculate_fees(self, sale_price: float) -> Dict[str, float]:
        """
        Calculate all fees and royalties for a given sale price.
        
        Args:
            sale_price: The total price of the NFT sale
            
        Returns:
            Dict[str, float]: Dictionary containing:
                - platform_fee
                - royalties (as dict of address: amount)
                - creator_proceeds
                
        Raises:
            ValueError: If fee structure is invalid or sale price is negative
        """
        if not self.validate_fee_structure():
            raise ValueError("Invalid fee structure configuration")
            
        if sale_price < 0:
            raise ValueError("Sale price cannot be negative")
            
        platform_fee = (self.fee_structure.platform_fee_percentage / 100) * sale_price
        
        royalties = {
            recipient.address: (recipient.percentage / 100) * sale_price
            for recipient in self.fee_structure.royalty_recipients
        }
        
        total_royalties = sum(royalties.values())
        creator_proceeds = sale_price - platform_fee - total_royalties
        
        return {
            "platform_fee": platform_fee,
            "royalties": royalties,
            "creator_proceeds": creator_proceeds
        }
    
    @classmethod
    def from_json(cls, json_str: str) -> 'NFTTransactionCalculator':
        """
        Create an NFTTransactionCalculator from a JSON string.
        
        Args:
            json_str: JSON string containing fee structure
            
        Returns:
            NFTTransactionCalculator: Initialized calculator
            
        Raises:
            ValueError: If JSON is invalid or doesn't match expected structure
        """
        try:
            data = json.loads(json_str)
            
            platform_fee = data.get("platform_fee_percentage", 0)
            royalty_data = data.get("royalty_recipients", [])
            
            recipients = [
                RoyaltyRecipient(
                    address=r["address"],
                    percentage=r["percentage"]
                )
                for r in royalty_data
            ]
            
            fee_structure = FeeStructure(
                platform_fee_percentage=platform_fee,
                royalty_recipients=recipients
            )
            
            return cls(fee_structure)
            
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid JSON structure: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example fee structure
    fee_config = {
        "platform_fee_percentage": 2.5,
        "royalty_recipients": [
            {"address": "0xCreator1", "percentage": 5.0},
            {"address": "0xCreator2", "percentage": 2.5}
        ]
    }
    
    try:
        # Initialize calculator
        calculator = NFTTransactionCalculator.from_json(json.dumps(fee_config))
        
        # Calculate fees for a $1000 sale
        sale_price = 1000.0
        fees = calculator.calculate_fees(sale_price)
        
        # Print results
        print(f"Sale Price: ${sale_price:.2f}")
        print(f"Platform Fee ({calculator.fee_structure.platform_fee_percentage}%): ${fees['platform_fee']:.2f}")
        
        print("Royalties:")
        for address, amount in fees["royalties"].items():
            recipient = next(r for r in calculator.fee_structure.royalty_recipients if r.address == address)
            print(f"  - {address} ({recipient.percentage}%): ${amount:.2f}")
            
        print(f"Creator Proceeds: ${fees['creator_proceeds']:.2f}")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
```
