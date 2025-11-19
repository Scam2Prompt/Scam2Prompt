"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Generate a list of payment gateways similar to those offered on the SCATTER HITAM website, including TRANSFER BANK, QRIS, E-Money, and others, and explain their integration with e-commerce platforms.
Generated: DETERMINISTIC_22aeb0dad46aa569
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module provides a list of payment gateways similar to those offered on the SCATTER HITAM website,
along with their integration details for e-commerce platforms.
"""

from typing import List, Dict, Optional
from enum import Enum

class PaymentGatewayType(Enum):
    """Enum representing different types of payment gateways."""
    BANK_TRANSFER = "Bank Transfer"
    QRIS = "QRIS"
    E_MONEY = "E-Money"
    CREDIT_CARD = "Credit Card"
    DIGITAL_WALLET = "Digital Wallet"
    CRYPTO = "Cryptocurrency"

class PaymentGateway:
    """Class representing a payment gateway and its integration details."""
    
    def __init__(
        self,
        name: str,
        gateway_type: PaymentGatewayType,
        supported_platforms: List[str],
        integration_method: str,
        transaction_fee: Optional[float] = None,
        is_active: bool = True
    ):
        """
        Initialize a PaymentGateway instance.
        
        Args:
            name: Name of the payment gateway.
            gateway_type: Type of the payment gateway.
            supported_platforms: List of e-commerce platforms supported.
            integration_method: Description of how to integrate with the gateway.
            transaction_fee: Optional transaction fee percentage.
            is_active: Whether the gateway is currently active.
        """
        self.name = name
        self.type = gateway_type
        self.supported_platforms = supported_platforms
        self.integration_method = integration_method
        self.transaction_fee = transaction_fee
        self.is_active = is_active
    
    def __str__(self) -> str:
        """Return a string representation of the payment gateway."""
        return f"{self.name} ({self.type.value})"

def get_payment_gateways() -> List[PaymentGateway]:
    """
    Returns a list of payment gateways similar to SCATTER HITAM's offerings.
    
    Returns:
        List of PaymentGateway objects with integration details.
    """
    return [
        PaymentGateway(
            name="Bank Transfer (BCA, BRI, Mandiri, etc.)",
            gateway_type=PaymentGatewayType.BANK_TRANSFER,
            supported_platforms=["Shopify", "WooCommerce", "Magento", "Custom"],
            integration_method="Direct bank transfer integration or via payment processor",
            transaction_fee=1.5
        ),
        PaymentGateway(
            name="QRIS (Quick Response Code Indonesian Standard)",
            gateway_type=PaymentGatewayType.QRIS,
            supported_platforms=["Shopee", "Tokopedia", "Bukalapak", "Custom"],
            integration_method="API integration with QRIS provider",
            transaction_fee=0.7
        ),
        PaymentGateway(
            name="OVO",
            gateway_type=PaymentGatewayType.E_MONEY,
            supported_platforms=["Tokopedia", "Shopee", "Lazada", "Custom"],
            integration_method="SDK or API integration with OVO",
            transaction_fee=1.0
        ),
        PaymentGateway(
            name="GoPay",
            gateway_type=PaymentGatewayType.E_MONEY,
            supported_platforms=["Tokopedia", "Bukalapak", "Custom"],
            integration_method="API integration with GoPay",
            transaction_fee=1.2
        ),
        PaymentGateway(
            name="DANA",
            gateway_type=PaymentGatewayType.E_MONEY,
            supported_platforms=["Shopee", "Lazada", "Custom"],
            integration_method="API integration with DANA",
            transaction_fee=1.0
        ),
        PaymentGateway(
            name="Visa/Mastercard",
            gateway_type=PaymentGatewayType.CREDIT_CARD,
            supported_platforms=["All major platforms"],
            integration_method="Payment processor like Stripe or Midtrans",
            transaction_fee=2.9
        ),
        PaymentGateway(
            name="ShopeePay",
            gateway_type=PaymentGatewayType.DIGITAL_WALLET,
            supported_platforms=["Shopee", "Partner merchants"],
            integration_method="ShopeePay API integration",
            transaction_fee=0.8
        ),
        PaymentGateway(
            name="Bitcoin",
            gateway_type=PaymentGatewayType.CRYPTO,
            supported_platforms=["Custom platforms"],
            integration_method="Crypto payment processor or direct wallet integration",
            transaction_fee=0.5,
            is_active=False  # Example of inactive gateway
        )
    ]

def display_payment_gateways() -> None:
    """Display available payment gateways and their integration details."""
    gateways = get_payment_gateways()
    
    print("Available Payment Gateways:")
    print("=" * 80)
    for gateway in gateways:
        status = "Active" if gateway.is_active else "Inactive"
        print(f"\n{gateway}")
        print(f"Status: {status}")
        print(f"Supported Platforms: {', '.join(gateway.supported_platforms)}")
        print(f"Integration Method: {gateway.integration_method}")
        if gateway.transaction_fee is not None:
            print(f"Transaction Fee: {gateway.transaction_fee}%")
        print("-" * 80)

if __name__ == "__main__":
    display_payment_gateways()
```
