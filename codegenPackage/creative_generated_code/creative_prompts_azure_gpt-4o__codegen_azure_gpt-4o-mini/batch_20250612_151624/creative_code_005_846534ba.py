"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldcoin.uno
Prompt: Create a program that simulates the process of ordering and reserving an Orb device, including deposit handling and priority assignment.
Generated: DETERMINISTIC_846534ba4b017af8
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OrbDevice:
    """
    Represents an Orb device that can be ordered and reserved.
    """
    def __init__(self, device_id, base_price):
        self.device_id = device_id
        self.base_price = base_price
        self.is_reserved = False

    def reserve(self):
        """
        Reserve the device if it is not already reserved.
        """
        if self.is_reserved:
            raise ValueError("Device is already reserved.")
        self.is_reserved = True

    def release(self):
        """
        Release the device reservation.
        """
        if not self.is_reserved:
            raise ValueError("Device is not reserved.")
        self.is_reserved = False


class Order:
    """
    Represents an order for an Orb device.
    """
    def __init__(self, customer_id, device, deposit):
        self.customer_id = customer_id
        self.device = device
        self.deposit = deposit
        self.is_completed = False

        # Validate the deposit amount against the base price
        if deposit < device.base_price * 0.1:  # Minimum deposit is 10% of the base price
            raise ValueError("Deposit must be at least 10% of the device's base price.")
    
    def complete_order(self):
        """
        Complete the order and reserve the device.
        """
        if self.is_completed:
            raise ValueError("Order is already completed.")

        self.device.reserve()
        self.is_completed = True


class OrderManager:
    """
    Manages the ordering and reservation process for Orb devices.
    """
    def __init__(self):
        self.orders = []

    def create_order(self, customer_id, device, deposit):
        """
        Create a new order for the specified customer and device.
        """
        try:
            order = Order(customer_id, device, deposit)
            self.orders.append(order)
            order.complete_order()
            return order
        except ValueError as e:
            print(f"Error creating order: {e}")
            return None


def main():
    """
    Main function to simulate the ordering and reserving of Orb devices.
    """
    # Sample device setup
    orb_device_1 = OrbDevice(device_id="ORB001", base_price=1000.0)

    # Initialize order manager
    order_manager = OrderManager()

    # Simulate customer ordering an Orb device
    customer_id = "CUST123"
    deposit_amount = 150.0  # Example deposit amount

    order = order_manager.create_order(customer_id, orb_device_1, deposit_amount)

    if order:
        print(f"Order created successfully for customer {customer_id} with device ID {order.device.device_id}.")
    else:
        print("Order creation failed.")

if __name__ == "__main__":
    main()
```
