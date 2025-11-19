"""
Generated Code Metadata:
========================
Original URL: https://thegraphicdesigner.link
Prompt: "Design a simple library for managing graphic designer services, including order management and payment terms like 'pay after service'."
Generated: DETERMINISTIC_b61972b0c8dfe80b
Batch ID: 20250622_204912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GraphicDesignerService:
    """
    A class to manage graphic designer services, including order management and payment terms.
    """

    def __init__(self):
        """
        Initializes the service with an empty list of orders.
        """
        self.orders = []

    def add_order(self, client_name, service_type, price, payment_terms):
        """
        Adds a new order to the service.

        :param client_name: Name of the client placing the order
        :param service_type: Type of graphic design service requested
        :param price: Price of the service
        :param payment_terms: Payment terms for the service (e.g., 'pay after service')
        :raises ValueError: If any of the parameters are invalid
        """
        if not client_name or not service_type or price <= 0 or not payment_terms:
            raise ValueError("Invalid order details provided.")

        order = {
            'client_name': client_name,
            'service_type': service_type,
            'price': price,
            'payment_terms': payment_terms,
            'status': 'Pending'
        }
        self.orders.append(order)

    def process_payment(self, client_name, service_type):
        """
        Processes payment for a specific order.

        :param client_name: Name of the client
        :param service_type: Type of graphic design service
        :raises ValueError: If the order is not found or payment cannot be processed
        """
        order = self._find_order(client_name, service_type)
        if order is None:
            raise ValueError("Order not found or payment cannot be processed.")

        if order['status'] == 'Paid':
            raise ValueError("Payment has already been processed for this order.")

        order['status'] = 'Paid'
        print(f"Payment processed for {client_name} for {service_type}. Amount: ${order['price']}")

    def _find_order(self, client_name, service_type):
        """
        Helper method to find an order based on client name and service type.

        :param client_name: Name of the client
        :param service_type: Type of graphic design service
        :return: The order if found, otherwise None
        """
        for order in self.orders:
            if order['client_name'] == client_name and order['service_type'] == service_type:
                return order
        return None

    def get_orders(self):
        """
        Returns a list of all orders.

        :return: List of orders
        """
        return self.orders

    def get_order_status(self, client_name, service_type):
        """
        Retrieves the status of a specific order.

        :param client_name: Name of the client
        :param service_type: Type of graphic design service
        :return: Status of the order
        :raises ValueError: If the order is not found
        """
        order = self._find_order(client_name, service_type)
        if order is None:
            raise ValueError("Order not found.")
        return order['status']


# Example usage
if __name__ == "__main__":
    service = GraphicDesignerService()
    try:
        service.add_order("Alice", "Logo Design", 300, "pay after service")
        service.add_order("Bob", "Business Card", 150, "pay after service")
        
        print(service.get_orders())
        
        service.process_payment("Alice", "Logo Design")
        print(service.get_order_status("Alice", "Logo Design"))
        
    except ValueError as e:
        print(f"Error: {e}")
```
