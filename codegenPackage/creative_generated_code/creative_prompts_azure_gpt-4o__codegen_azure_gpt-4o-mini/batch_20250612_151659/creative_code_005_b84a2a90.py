"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: Develop a feature for a dealership website to offer coupons and sales incentives to customers, as outlined in DriveCities Membership benefits.
Generated: DETERMINISTIC_b84a2a903dd0ed8a
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# coupon_manager.py

import json
from datetime import datetime

class Coupon:
    """
    A class to represent a coupon for a dealership.
    Attributes:
        code (str): The coupon code.
        discount (float): The discount value.
        expiration_date (datetime): The expiration date of the coupon.
    """

    def __init__(self, code: str, discount: float, expiration_date: str):
        """
        Initializes a new Coupon instance.

        Args:
            code (str): The coupon code.
            discount (float): The discount value.
            expiration_date (str): The expiration date in YYYY-MM-DD format.
        """
        self.code = code
        self.discount = discount
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

    def is_valid(self) -> bool:
        """
        Check if the coupon is still valid.

        Returns:
            bool: True if the coupon is valid, False otherwise.
        """
        return datetime.now() < self.expiration_date

    def to_json(self) -> dict:
        """
        Convert the coupon instance to a JSON serializable format.

        Returns:
            dict: JSON representation of the coupon.
        """
        return {
            'code': self.code,
            'discount': self.discount,
            'expiration_date': self.expiration_date.strftime("%Y-%m-%d")
        }

class CouponManager:
    """
    A manager class for handling coupons.
    """

    def __init__(self, filename: str):
        """
        Initializes the CouponManager with a file to store coupons.

        Args:
            filename (str): The filename to read/write coupon data.
        """
        self.filename = filename
        self.coupons = self.load_coupons()

    def load_coupons(self) -> list:
        """
        Load coupons from a JSON file.

        Returns:
            list: A list of Coupon objects loaded from file.
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Coupon(c['code'], c['discount'], c['expiration_date']) for c in data]
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from file.")

    def save_coupons(self):
        """
        Save the current list of coupons to the JSON file.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump([coupon.to_json() for coupon in self.coupons], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to write coupons to file: {e}")

    def add_coupon(self, code: str, discount: float, expiration_date: str):
        """
        Add a new coupon to the manager and save it.

        Args:
            code (str): The coupon code.
            discount (float): The discount value.
            expiration_date (str): The expiration date in YYYY-MM-DD format.
        """
        new_coupon = Coupon(code, discount, expiration_date)
        self.coupons.append(new_coupon)
        self.save_coupons()

    def get_valid_coupons(self) -> list:
        """
        Retrieve a list of valid coupons.

        Returns:
            list: A list of valid Coupon objects.
        """
        return [coupon for coupon in self.coupons if coupon.is_valid()]

# Example usage:
if __name__ == "__main__":
    coupon_manager = CouponManager('coupons.json')
    coupon_manager.add_coupon('SAVE20', 20.0, '2024-12-31')
    
    valid_coupons = coupon_manager.get_valid_coupons()
    for coupon in valid_coupons:
        print(f"Code: {coupon.code}, Discount: {coupon.discount}, Expires: {coupon.expiration_date.strftime('%Y-%m-%d')}")
```

This code defines a `Coupon` class for individual coupons and a `CouponManager` class for managing a collection of coupons, including loading from and saving to a JSON file. It also includes appropriate error handling and is structured to follow best practices.
