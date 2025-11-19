"""
Generated Code Metadata:
========================
Original URL: https://thoinayadv.com
Prompt: Write Python code to calculate the cost of ordering custom metallic stickers, including options for Nickel Metal Stickers, 3D Metal Nickel Stickers, and Stainless Steel Metal Stickers, with worldwide shipping fees.
Generated: DETERMINISTIC_91192f7b0f1a7421
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MetalStickerCalculator:
    """
    A class to calculate the cost of custom metallic stickers including shipping fees.
    """

    # Base prices per sticker type (in USD)
    STICKER_PRICES = {
        "Nickel Metal Stickers": 0.50,
        "3D Metal Nickel Stickers": 1.20,
        "Stainless Steel Metal Stickers": 0.80
    }

    # Shipping fees by region (in USD)
    SHIPPING_FEES = {
        "North America": 5.00,
        "South America": 7.50,
        "Europe": 6.00,
        "Asia": 8.00,
        "Africa": 9.00,
        "Oceania": 10.00
    }

    # Discount thresholds and rates
    DISCOUNT_THRESHOLDS = {
        100: 0.05,    # 5% discount for 100+ stickers
        500: 0.10,    # 10% discount for 500+ stickers
        1000: 0.15    # 15% discount for 1000+ stickers
    }

    def __init__(self):
        """Initialize the calculator with default values."""
        self.sticker_type = None
        self.quantity = 0
        self.region = None

    def set_sticker_type(self, sticker_type: str) -> None:
        """
        Set the type of sticker.
        
        Args:
            sticker_type (str): Type of sticker (must be one of STICKER_PRICES keys)
        
        Raises:
            ValueError: If sticker_type is not valid
        """
        if sticker_type not in self.STICKER_PRICES:
            raise ValueError(f"Invalid sticker type. Must be one of: {list(self.STICKER_PRICES.keys())}")
        self.sticker_type = sticker_type

    def set_quantity(self, quantity: int) -> None:
        """
        Set the quantity of stickers.
        
        Args:
            quantity (int): Number of stickers (must be positive)
        
        Raises:
            ValueError: If quantity is not positive
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        self.quantity = quantity

    def set_region(self, region: str) -> None:
        """
        Set the shipping region.
        
        Args:
            region (str): Shipping region (must be one of SHIPPING_FEES keys)
        
        Raises:
            ValueError: If region is not valid
        """
        if region not in self.SHIPPING_FEES:
            raise ValueError(f"Invalid region. Must be one of: {list(self.SHIPPING_FEES.keys())}")
        self.region = region

    def calculate_discount(self) -> float:
        """
        Calculate the applicable discount based on quantity.
        
        Returns:
            float: Discount rate (0.0 to 1.0)
        """
        for threshold, discount in sorted(self.DISCOUNT_THRESHOLDS.items(), reverse=True):
            if self.quantity >= threshold:
                return discount
        return 0.0

    def calculate_subtotal(self) -> float:
        """
        Calculate the subtotal before discounts and shipping.
        
        Returns:
            float: Subtotal amount
        
        Raises:
            ValueError: If sticker type or quantity not set
        """
        if not self.sticker_type or not self.quantity:
            raise ValueError("Sticker type and quantity must be set before calculation")
        return self.STICKER_PRICES[self.sticker_type] * self.quantity

    def calculate_total(self) -> float:
        """
        Calculate the total cost including discounts and shipping.
        
        Returns:
            float: Total cost
        
        Raises:
            ValueError: If region not set
        """
        if not self.region:
            raise ValueError("Region must be set before calculation")

        subtotal = self.calculate_subtotal()
        discount_rate = self.calculate_discount()
        discount_amount = subtotal * discount_rate
        shipping_fee = self.SHIPPING_FEES[self.region]

        return subtotal - discount_amount + shipping_fee

    def get_quote(self) -> dict:
        """
        Generate a detailed quote for the order.
        
        Returns:
            dict: Dictionary containing all cost components
        
        Raises:
            ValueError: If any required fields are not set
        """
        if not all([self.sticker_type, self.quantity, self.region]):
            raise ValueError("All fields (sticker_type, quantity, region) must be set")

        subtotal = self.calculate_subtotal()
        discount_rate = self.calculate_discount()
        discount_amount = subtotal * discount_rate
        shipping_fee = self.SHIPPING_FEES[self.region]
        total = subtotal - discount_amount + shipping_fee

        return {
            "sticker_type": self.sticker_type,
            "quantity": self.quantity,
            "unit_price": self.STICKER_PRICES[self.sticker_type],
            "subtotal": round(subtotal, 2),
            "discount_rate": f"{discount_rate * 100:.0f}%",
            "discount_amount": round(discount_amount, 2),
            "shipping_region": self.region,
            "shipping_fee": round(shipping_fee, 2),
            "total": round(total, 2)
        }


# Example usage
if __name__ == "__main__":
    try:
        calculator = MetalStickerCalculator()
        calculator.set_sticker_type("3D Metal Nickel Stickers")
        calculator.set_quantity(150)
        calculator.set_region("Europe")
        
        quote = calculator.get_quote()
        print("Order Quote:")
        for key, value in quote.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
```
