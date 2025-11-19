"""
Generated Code Metadata:
========================
Original URL: https://play.dee.casino
Prompt: "How can I create a simple sports betting odds calculator using Python libraries?"
Generated: DETERMINISTIC_5590f750f0a2c200
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Union, Optional

class OddsCalculator:
    """
    A simple sports betting odds calculator that converts between different odds formats
    and calculates potential payouts.
    
    Supported formats:
    - Decimal (e.g., 2.50)
    - Fractional (e.g., 3/2)
    - American (e.g., +150 or -200)
    """

    def __init__(self):
        pass

    @staticmethod
    def decimal_to_american(decimal_odds: float) -> Union[str, None]:
        """
        Convert decimal odds to American odds format.
        
        Args:
            decimal_odds: Decimal odds as a float (e.g., 2.50)
            
        Returns:
            str: American odds (e.g., "+150" or "-200")
            None: If input is invalid
        """
        if not isinstance(decimal_odds, (int, float)) or decimal_odds < 1.0:
            return None
            
        if decimal_odds >= 2.0:
            return f"+{int((decimal_odds - 1) * 100)}"
        else:
            return f"-{int(100 / (decimal_odds - 1))}"

    @staticmethod
    def american_to_decimal(american_odds: str) -> Union[float, None]:
        """
        Convert American odds to decimal odds format.
        
        Args:
            american_odds: American odds as string (e.g., "+150" or "-200")
            
        Returns:
            float: Decimal odds
            None: If input is invalid
        """
        try:
            value = int(american_odds)
        except ValueError:
            return None
            
        if value >= 100:
            return (value / 100) + 1
        elif value <= -100:
            return (100 / abs(value)) + 1
        else:
            return None

    @staticmethod
    def fractional_to_decimal(fractional_odds: str) -> Union[float, None]:
        """
        Convert fractional odds to decimal odds format.
        
        Args:
            fractional_odds: Fractional odds as string (e.g., "3/2")
            
        Returns:
            float: Decimal odds
            None: If input is invalid
        """
        try:
            numerator, denominator = map(int, fractional_odds.split('/'))
            if denominator == 0:
                return None
            return (numerator / denominator) + 1
        except (ValueError, AttributeError):
            return None

    @staticmethod
    def decimal_to_fractional(decimal_odds: float) -> Union[str, None]:
        """
        Convert decimal odds to fractional odds format.
        
        Args:
            decimal_odds: Decimal odds as float (e.g., 2.50)
            
        Returns:
            str: Fractional odds (e.g., "3/2")
            None: If input is invalid
        """
        if not isinstance(decimal_odds, (int, float)) or decimal_odds < 1.0:
            return None
            
        from fractions import Fraction
        try:
            frac = Fraction(decimal_odds - 1).limit_denominator(100)
            return f"{frac.numerator}/{frac.denominator}"
        except (ValueError, TypeError):
            return None

    @staticmethod
    def calculate_payout(bet_amount: float, odds: Union[float, str], odds_format: str = "decimal") -> Union[float, None]:
        """
        Calculate the potential payout for a given bet.
        
        Args:
            bet_amount: Amount wagered
            odds: Odds in any supported format
            odds_format: Format of provided odds ('decimal', 'fractional', 'american')
            
        Returns:
            float: Total payout (stake + winnings)
            None: If inputs are invalid
        """
        if not isinstance(bet_amount, (int, float)) or bet_amount <= 0:
            return None
            
        decimal_odds = None
        
        if odds_format == "decimal":
            if not isinstance(odds, (int, float)) or odds < 1.0:
                return None
            decimal_odds = odds
        elif odds_format == "fractional":
            if not isinstance(odds, str):
                return None
            decimal_odds = OddsCalculator.fractional_to_decimal(odds)
        elif odds_format == "american":
            if not isinstance(odds, str):
                return None
            decimal_odds = OddsCalculator.american_to_decimal(odds)
        else:
            return None
            
        if decimal_odds is None:
            return None
            
        return bet_amount * decimal_odds

def main():
    """Command-line interface for the odds calculator."""
    calculator = OddsCalculator()
    
    print("Sports Betting Odds Calculator")
    print("Supported formats: decimal (2.5), fractional (3/2), american (+150)")
    print("Enter 'q' to quit")
    
    while True:
        try:
            user_input = input("\nEnter odds and bet amount (format: odds_type odds amount): ").strip()
            if user_input.lower() == 'q':
                break
                
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Format: odds_type odds amount")
                continue
                
            odds_type, odds_str, amount_str = parts
            
            try:
                bet_amount = float(amount_str)
            except ValueError:
                print("Invalid bet amount")
                continue
                
            if odds_type not in ["decimal", "fractional", "american"]:
                print("Invalid odds type. Use: decimal, fractional, or american")
                continue
                
            payout = calculator.calculate_payout(bet_amount, odds_str if odds_type != "decimal" else float(odds_str), odds_type)
            
            if payout is None:
                print("Invalid odds format")
            else:
                print(f"Potential payout: ${payout:.2f}")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
