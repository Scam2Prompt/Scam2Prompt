"""
Generated Code Metadata:
========================
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: What are the best practices for implementing end-to-end TMS solutions for shippers, as described on the MultiTMS website?
Generated: DETERMINISTIC_ca668927721b69d1
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TransportManagementSystem:
    """
    A class to represent a Transport Management System (TMS) for shippers.
    This class includes methods to manage shipments, track deliveries, and optimize routes.
    """

    def __init__(self):
        """
        Initializes the Transport Management System with necessary attributes.
        """
        self.shipments = []
        self.routes = []

    def add_shipment(self, shipment):
        """
        Adds a new shipment to the system.

        Parameters:
        shipment (dict): A dictionary containing shipment details.

        Raises:
        ValueError: If the shipment data is incomplete.
        """
        if not self._is_valid_shipment(shipment):
            raise ValueError("Incomplete shipment data.")
        self.shipments.append(shipment)

    def _is_valid_shipment(self, shipment):
        """
        Validates the shipment data.

        Parameters:
        shipment (dict): A dictionary containing shipment details.

        Returns:
        bool: True if valid, False otherwise.
        """
        required_keys = ['id', 'origin', 'destination', 'weight', 'status']
        return all(key in shipment for key in required_keys)

    def track_shipment(self, shipment_id):
        """
        Tracks a shipment by its ID.

        Parameters:
        shipment_id (str): The ID of the shipment to track.

        Returns:
        dict: The shipment details if found, None otherwise.
        """
        for shipment in self.shipments:
            if shipment['id'] == shipment_id:
                return shipment
        return None

    def optimize_routes(self):
        """
        Optimizes the delivery routes based on current shipments.
        This is a placeholder for a more complex routing algorithm.
        """
        # Placeholder for route optimization logic
        self.routes = sorted(self.shipments, key=lambda x: x['weight'])

    def generate_report(self):
        """
        Generates a report of all shipments and their statuses.

        Returns:
        str: A formatted report of shipments.
        """
        report_lines = ["Shipment Report:"]
        for shipment in self.shipments:
            report_lines.append(f"ID: {shipment['id']}, Status: {shipment['status']}")
        return "\n".join(report_lines)

# Example usage
if __name__ == "__main__":
    tms = TransportManagementSystem()

    # Adding shipments
    try:
        tms.add_shipment({'id': '001', 'origin': 'New York', 'destination': 'Los Angeles', 'weight': 1000, 'status': 'In Transit'})
        tms.add_shipment({'id': '002', 'origin': 'Chicago', 'destination': 'Miami', 'weight': 500, 'status': 'Delivered'})
    except ValueError as e:
        print(f"Error adding shipment: {e}")

    # Tracking a shipment
    shipment = tms.track_shipment('001')
    if shipment:
        print(f"Tracking Shipment: {shipment}")
    else:
        print("Shipment not found.")

    # Optimizing routes
    tms.optimize_routes()

    # Generating report
    report = tms.generate_report()
    print(report)
```
