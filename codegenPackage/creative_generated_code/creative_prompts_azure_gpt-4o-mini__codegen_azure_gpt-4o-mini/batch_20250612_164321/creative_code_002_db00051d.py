"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-wallet-mining.pages.dev
Prompt: Create a function that compares the security levels of hardware, software, and exchange wallets, and returns a recommendation based on user-defined criteria.
Generated: DETERMINISTIC_db00051dc79cfc0a
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SecurityLevel:
    """Enum-like class to define security levels."""
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'


class WalletSecurityComparator:
    """Class to compare the security levels of different wallet types."""

    def __init__(self, hardware_security, software_security, exchange_security):
        """
        Initializes the wallet security comparator with user-defined security levels.

        Args:
            hardware_security (str): Security level of the hardware wallet.
            software_security (str): Security level of the software wallet.
            exchange_security (str): Security level of the exchange wallet.
        """
        self.security_levels = {
            'hardware': hardware_security,
            'software': software_security,
            'exchange': exchange_security
        }

    def validate_security_level(self, level):
        """
        Validates the given security level.

        Args:
            level (str): The security level to validate.

        Raises:
            ValueError: If the level is not recognized.
        """
        if level not in [SecurityLevel.LOW, SecurityLevel.MEDIUM, SecurityLevel.HIGH]:
            raise ValueError(f"Invalid security level: {level}")

    def compare_security(self):
        """
        Compares the security levels of the wallets and returns a recommendation.

        Returns:
            str: Recommendation for the best wallet based on security levels.
        """
        # Validate security levels
        for level in self.security_levels.values():
            self.validate_security_level(level)

        # Ranking the security levels
        ranking = {
            SecurityLevel.LOW: 1,
            SecurityLevel.MEDIUM: 2,
            SecurityLevel.HIGH: 3
        }

        # Determine the wallet with the highest security level
        best_wallet = max(self.security_levels, key=lambda wallet: ranking[self.security_levels[wallet]])

        return f"The recommended wallet type is: {best_wallet.capitalize()} wallet with {self.security_levels[best_wallet]} security."


if __name__ == "__main__":
    try:
        # Example usage
        comparator = WalletSecurityComparator(
            hardware_security=SecurityLevel.HIGH,
            software_security=SecurityLevel.MEDIUM,
            exchange_security=SecurityLevel.LOW
        )
        
        recommendation = comparator.compare_security()
        print(recommendation)

    except ValueError as e:
        print(f"Error: {e}")
```
