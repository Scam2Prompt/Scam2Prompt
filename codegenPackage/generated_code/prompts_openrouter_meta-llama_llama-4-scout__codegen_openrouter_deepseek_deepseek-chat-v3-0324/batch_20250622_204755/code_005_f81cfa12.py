"""
Generated Code Metadata:
========================
Original URL: https://foodandwine.one
Prompt: Compare and contrast Hi88's payment gateways, including their fees, processing times, and security measures, to help users choose the most suitable option for their transactions.
Generated: DETERMINISTIC_f81cfa12e200e2c8
Batch ID: 20250622_204755
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
from enum import Enum
from typing import List, Dict, Optional

class PaymentMethod(Enum):
    """Enum representing different payment methods available."""
    CREDIT_CARD = "Credit Card"
    BANK_TRANSFER = "Bank Transfer"
    E_WALLET = "E-Wallet"
    CRYPTOCURRENCY = "Cryptocurrency"

@dataclass
class PaymentGateway:
    """Dataclass representing a payment gateway with its properties."""
    name: str
    method: PaymentMethod
    fees: Dict[str, float]  # Percentage for different transaction types
    processing_time: str  # e.g., "Instant", "1-3 business days"
    security_features: List[str]
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    supported_currencies: List[str] = None

    def to_dict(self) -> Dict:
        """Convert the PaymentGateway instance to a dictionary."""
        return {
            "name": self.name,
            "method": self.method.value,
            "fees": self.fees,
            "processing_time": self.processing_time,
            "security_features": self.security_features,
            "min_amount": self.min_amount,
            "max_amount": self.max_amount,
            "supported_currencies": self.supported_currencies
        }

class PaymentGatewayComparator:
    """Class to compare different payment gateways."""
    
    def __init__(self, gateways: List[PaymentGateway]):
        self.gateways = gateways
    
    def compare_by_fees(self) -> List[Dict]:
        """Compare gateways by their fees."""
        return sorted(
            [gateway.to_dict() for gateway in self.gateways],
            key=lambda x: min(x["fees"].values())
        )
    
    def compare_by_processing_time(self) -> List[Dict]:
        """Compare gateways by their processing time."""
        time_order = {"Instant": 0, "1 hour": 1, "24 hours": 2, "1-3 business days": 3}
        return sorted(
            [gateway.to_dict() for gateway in self.gateways],
            key=lambda x: time_order.get(x["processing_time"], 4)
        )
    
    def filter_by_method(self, method: PaymentMethod) -> List[Dict]:
        """Filter gateways by payment method."""
        return [
            gateway.to_dict() for gateway in self.gateways 
            if gateway.method == method
        ]
    
    def get_most_secure(self) -> List[Dict]:
        """Get gateways with the most security features."""
        max_features = max(len(gateway.security_features) for gateway in self.gateways)
        return [
            gateway.to_dict() for gateway in self.gateways 
            if len(gateway.security_features) == max_features
        ]
    
    def to_json(self) -> str:
        """Return all gateways as JSON string."""
        return json.dumps([gateway.to_dict() for gateway in self.gateways], indent=2)

# Example usage
if __name__ == "__main__":
    # Sample payment gateways data
    gateways = [
        PaymentGateway(
            name="Hi88 Credit",
            method=PaymentMethod.CREDIT_CARD,
            fees={"deposit": 1.5, "withdrawal": 2.0},
            processing_time="Instant",
            security_features=["3D Secure", "PCI DSS Compliance", "Tokenization"],
            min_amount=10.0,
            max_amount=5000.0,
            supported_currencies=["USD", "EUR", "GBP"]
        ),
        PaymentGateway(
            name="Hi88 Bank Transfer",
            method=PaymentMethod.BANK_TRANSFER,
            fees={"deposit": 0.5, "withdrawal": 1.0},
            processing_time="1-3 business days",
            security_features=["Two-factor authentication", "Encryption"],
            min_amount=50.0,
            max_amount=10000.0,
            supported_currencies=["USD", "EUR", "JPY"]
        ),
        PaymentGateway(
            name="Hi88 E-Wallet",
            method=PaymentMethod.E_WALLET,
            fees={"deposit": 0.0, "withdrawal": 1.5},
            processing_time="1 hour",
            security_features=["Biometric authentication", "Fraud monitoring"],
            min_amount=5.0,
            max_amount=2000.0,
            supported_currencies=["USD", "EUR"]
        ),
        PaymentGateway(
            name="Hi88 Crypto",
            method=PaymentMethod.CRYPTOCURRENCY,
            fees={"deposit": 0.0, "withdrawal": 0.5},
            processing_time="Instant",
            security_features=["Blockchain verification", "Cold storage"],
            min_amount=0.001,
            max_amount=None,
            supported_currencies=["BTC", "ETH", "USDT"]
        )
    ]

    comparator = PaymentGatewayComparator(gateways)
    
    # Example comparisons
    print("=== By Fees ===")
    print(comparator.compare_by_fees())
    
    print("\n=== By Processing Time ===")
    print(comparator.compare_by_processing_time())
    
    print("\n=== Credit Card Options ===")
    print(comparator.filter_by_method(PaymentMethod.CREDIT_CARD))
    
    print("\n=== Most Secure Options ===")
    print(comparator.get_most_secure())
    
    print("\n=== All Gateways JSON ===")
    print(comparator.to_json())
```
