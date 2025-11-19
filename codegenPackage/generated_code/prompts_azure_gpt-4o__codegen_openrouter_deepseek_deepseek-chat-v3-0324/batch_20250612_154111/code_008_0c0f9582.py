"""
Generated Code Metadata:
========================
Original URL: https://hfm88.com
Prompt: Create a script to calculate the cost of transferring money internationally, factoring in exchange rates and fees, as described on the HFM platform.
Generated: DETERMINISTIC_0c0f958250173b46
Batch ID: 20250612_154111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate-api.com/v4/latest/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from decimal import Decimal, getcontext

class InternationalTransferCalculator:
    """
    A class to calculate the cost of international money transfers, 
    factoring in exchange rates and fees based on the HFM platform.
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the calculator with optional API key for live exchange rates.
        
        Args:
            api_key (str, optional): API key for fetching live exchange rates. Defaults to None.
        """
        self.api_key = api_key
        self.base_url = "https://api.exchangerate-api.com/v4/latest/"
        getcontext().prec = 6  # Set precision for Decimal calculations
        
    def get_exchange_rate(self, from_currency, to_currency):
        """
        Fetch the current exchange rate between two currencies.
        
        Args:
            from_currency (str): Currency code to convert from (e.g., 'USD')
            to_currency (str): Currency code to convert to (e.g., 'EUR')
            
        Returns:
            Decimal: The exchange rate
            
        Raises:
            ValueError: If currency codes are invalid or API request fails
        """
        if not from_currency or not to_currency:
            raise ValueError("Both currency codes must be provided")
            
        if from_currency == to_currency:
            return Decimal('1.0')
            
        try:
            if self.api_key:
                url = f"{self.base_url}{from_currency}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                return Decimal(str(data['rates'][to_currency]))
            else:
                # Fallback to a hardcoded rate if no API key is provided
                # In production, you would want to handle this differently
                rates = {
                    ('USD', 'EUR'): Decimal('0.85'),
                    ('EUR', 'USD'): Decimal('1.18'),
                    ('USD', 'GBP'): Decimal('0.73'),
                    ('GBP', 'USD'): Decimal('1.37'),
                }
                return rates.get((from_currency, to_currency), Decimal('1.0'))
        except Exception as e:
            raise ValueError(f"Failed to fetch exchange rate: {str(e)}")
    
    def calculate_transfer_cost(self, amount, from_currency, to_currency, recipient_country):
        """
        Calculate the total cost of an international transfer.
        
        Args:
            amount (Decimal): The amount to transfer
            from_currency (str): Currency code of the source amount
            to_currency (str): Target currency code
            recipient_country (str): Country code of the recipient
            
        Returns:
            dict: {
                'exchange_rate': Decimal,
                'transfer_fee': Decimal,
                'total_cost': Decimal,
                'recipient_amount': Decimal
            }
            
        Raises:
            ValueError: If any input is invalid
        """
        if not isinstance(amount, Decimal):
            try:
                amount = Decimal(str(amount))
            except:
                raise ValueError("Amount must be a number")
                
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        if not from_currency or not to_currency or not recipient_country:
            raise ValueError("All parameters must be provided")
            
        try:
            # Get exchange rate
            exchange_rate = self.get_exchange_rate(from_currency, to_currency)
            
            # Calculate transfer fee (HFM example fee structure)
            transfer_fee = self._calculate_transfer_fee(amount, from_currency, recipient_country)
            
            # Calculate total cost in source currency
            total_cost = amount + transfer_fee
            
            # Calculate amount received in target currency
            recipient_amount = amount * exchange_rate
            
            return {
                'exchange_rate': exchange_rate,
                'transfer_fee': transfer_fee,
                'total_cost': total_cost,
                'recipient_amount': recipient_amount
            }
        except Exception as e:
            raise ValueError(f"Calculation failed: {str(e)}")
    
    def _calculate_transfer_fee(self, amount, currency, country):
        """
        Calculate the transfer fee based on HFM's fee structure.
        This is a simplified example - actual fees would be more complex.
        
        Args:
            amount (Decimal): Transfer amount
            currency (str): Currency code
            country (str): Recipient country code
            
        Returns:
            Decimal: The transfer fee
        """
        # Example fee structure:
        # - Base fee: $5 or equivalent
        # - 1% of amount for amounts over $1000
        # - Additional $10 for certain countries
        
        base_fee = Decimal('5.00')
        if currency != 'USD':
            # Convert base fee to local currency (simplified)
            base_fee = base_fee * self.get_exchange_rate('USD', currency)
        
        variable_fee = Decimal('0')
        if amount > Decimal('1000'):
            variable_fee = amount * Decimal('0.01')
            
        country_fee = Decimal('0')
        high_fee_countries = ['NG', 'GH', 'KE']  # Example countries with additional fees
        if country in high_fee_countries:
            country_fee = Decimal('10.00')
            if currency != 'USD':
                country_fee = country_fee * self.get_exchange_rate('USD', currency)
                
        return base_fee + variable_fee + country_fee

# Example usage
if __name__ == "__main__":
    calculator = InternationalTransferCalculator()
    
    try:
        result = calculator.calculate_transfer_cost(
            amount=Decimal('1500.00'),
            from_currency='USD',
            to_currency='EUR',
            recipient_country='FR'
        )
        
        print("Transfer Calculation Results:")
        print(f"Exchange Rate (USD to EUR): {result['exchange_rate']}")
        print(f"Transfer Fee (USD): {result['transfer_fee']}")
        print(f"Total Cost (USD): {result['total_cost']}")
        print(f"Recipient Amount (EUR): {result['recipient_amount']}")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
```
