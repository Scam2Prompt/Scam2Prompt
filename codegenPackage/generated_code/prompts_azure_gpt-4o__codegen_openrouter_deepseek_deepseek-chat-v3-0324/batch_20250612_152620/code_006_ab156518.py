"""
Generated Code Metadata:
========================
Original URL: https://sanshu-en.web.app
Prompt: Write a Python script to calculate the claimable SANSHU v2 token amounts based on post-snapshot token sales, using the rules outlined in the SANSHU FAQs.
Generated: DETERMINISTIC_ab15651845f5bd32
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from decimal import Decimal, getcontext
from typing import Dict, List, Tuple

# Set precision for Decimal calculations
getcontext().prec = 18

class SANSHUClaimCalculator:
    """
    Calculates claimable SANSHU v2 token amounts based on post-snapshot token sales.
    Follows the rules outlined in the SANSHU FAQs.
    """
    
    def __init__(self, snapshot_file: str, sales_file: str):
        """
        Initialize the calculator with snapshot and sales data files.
        
        Args:
            snapshot_file: Path to JSON file containing snapshot data
            sales_file: Path to JSON file containing sales data
        """
        self.snapshot_file = snapshot_file
        self.sales_file = sales_file
        self.snapshot_data = self._load_json_file(snapshot_file)
        self.sales_data = self._load_json_file(sales_file)
        
        # Validate data
        self._validate_data()
        
        # Calculate total original supply
        self.total_original_supply = sum(
            Decimal(str(balance)) for balance in self.snapshot_data.values()
        )
        
        # Calculate total sold amount
        self.total_sold = sum(
            Decimal(str(sale['amount'])) for sale in self.sales_data
        )
        
    def _load_json_file(self, file_path: str) -> Dict:
        """Load JSON data from file with error handling."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {file_path}")
    
    def _validate_data(self) -> None:
        """Validate the loaded snapshot and sales data."""
        if not isinstance(self.snapshot_data, dict):
            raise ValueError("Snapshot data must be a dictionary")
        
        if not isinstance(self.sales_data, list):
            raise ValueError("Sales data must be a list")
        
        for sale in self.sales_data:
            if not all(key in sale for key in ['amount', 'buyer']):
                raise ValueError("Each sale must have 'amount' and 'buyer' fields")
    
    def calculate_claims(self) -> Dict[str, Decimal]:
        """
        Calculate claimable amounts for all addresses.
        
        Returns:
            Dictionary mapping addresses to claimable amounts
        """
        claims = {}
        
        # Calculate claimable amounts for original holders
        for address, balance in self.snapshot_data.items():
            original_balance = Decimal(str(balance))
            claim_amount = self._calculate_holder_claim(original_balance)
            claims[address] = claim_amount
        
        # Calculate claimable amounts for buyers
        buyer_claims = self._calculate_buyer_claims()
        for address, amount in buyer_claims.items():
            if address in claims:
                claims[address] += amount
            else:
                claims[address] = amount
        
        return claims
    
    def _calculate_holder_claim(self, original_balance: Decimal) -> Decimal:
        """
        Calculate claimable amount for an original holder.
        
        Args:
            original_balance: Original balance from snapshot
            
        Returns:
            Claimable amount
        """
        if self.total_original_supply == 0:
            return Decimal(0)
        
        # Calculate the proportion of the original supply
        proportion = original_balance / self.total_original_supply
        
        # Calculate claimable amount (50% of original + proportional share of unsold)
        claimable = (original_balance * Decimal('0.5')) + (proportion * self.total_sold * Decimal('0.5'))
        
        return claimable
    
    def _calculate_buyer_claims(self) -> Dict[str, Decimal]:
        """
        Calculate claimable amounts for buyers.
        
        Returns:
            Dictionary mapping buyer addresses to claimable amounts
        """
        buyer_claims = {}
        
        for sale in self.sales_data:
            buyer = sale['buyer']
            amount = Decimal(str(sale['amount']))
            
            # Buyers get 50% of what they bought
            claimable = amount * Decimal('0.5')
            
            if buyer in buyer_claims:
                buyer_claims[buyer] += claimable
            else:
                buyer_claims[buyer] = claimable
        
        return buyer_claims
    
    def save_claims_to_file(self, output_file: str, claims: Dict[str, Decimal]) -> None:
        """
        Save claims to a JSON file with string representations of Decimal amounts.
        
        Args:
            output_file: Path to output file
            claims: Dictionary of claims to save
        """
        # Convert Decimal to string for JSON serialization
        claims_str = {addr: str(amount) for addr, amount in claims.items()}
        
        try:
            with open(output_file, 'w') as f:
                json.dump(claims_str, f, indent=2)
        except IOError as e:
            raise ValueError(f"Error writing to file {output_file}: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        calculator = SANSHUClaimCalculator(
            snapshot_file="snapshot.json",
            sales_file="sales.json"
        )
        
        claims = calculator.calculate_claims()
        calculator.save_claims_to_file("claims.json", claims)
        
        print("Claims calculated and saved successfully.")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
