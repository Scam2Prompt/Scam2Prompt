"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Write a script to simulate the operation of a "Patates Paketleme Makinesi," including input parameters like packaging speed and product weight, referencing the technical details from the CEMNAZ Makine website.
Generated: DETERMINISTIC_30d62e2622b76fe5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PatatesPaketlemeMakinesi:
    """
    A class to simulate the operation of a Patates Paketleme Makinesi (Potato Packaging Machine).
    
    Attributes:
        packaging_speed (float): The speed of the packaging process in packets per minute.
        product_weight (float): The weight of each product in grams.
    """

    def __init__(self, packaging_speed: float, product_weight: float):
        """
        Initializes the packaging machine with specified speed and product weight.
        
        Args:
            packaging_speed (float): The speed of the packaging process.
            product_weight (float): The weight of each product.
        
        Raises:
            ValueError: If packaging_speed or product_weight is non-positive.
        """
        if packaging_speed <= 0:
            raise ValueError("Packaging speed must be a positive value.")
        if product_weight <= 0:
            raise ValueError("Product weight must be a positive value.")
        
        self.packaging_speed = packaging_speed
        self.product_weight = product_weight

    def simulate_packaging(self, duration: float) -> int:
        """
        Simulates the packaging operation for a given duration.
        
        Args:
            duration (float): The duration of the operation in minutes.
        
        Returns:
            int: The total number of packets produced during the operation.
        
        Raises:
            ValueError: If duration is non-positive.
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive value.")
        
        # Calculate the total number of packets produced
        total_packets = int(self.packaging_speed * duration)
        return total_packets

    def calculate_total_weight(self, packets: int) -> float:
        """
        Calculates the total weight of the packaged products.
        
        Args:
            packets (int): The number of packets produced.
        
        Returns:
            float: The total weight of the packaged products in grams.
        
        Raises:
            ValueError: If packets is negative.
        """
        if packets < 0:
            raise ValueError("Number of packets cannot be negative.")
        
        total_weight = packets * self.product_weight
        return total_weight

def main():
    """
    Main function to run the simulation of the Patates Paketleme Makinesi.
    """
    try:
        # Initialize the packaging machine with speed and weight
        machine = PatatesPaketlemeMakinesi(packaging_speed=30.0, product_weight=250.0)  # 30 packets/min, 250g each
        
        # Simulate packaging for a specific duration
        duration = 10.0  # in minutes
        packets_produced = machine.simulate_packaging(duration)
        
        # Calculate the total weight of the produced packets
        total_weight = machine.calculate_total_weight(packets_produced)
        
        # Output the results
        print(f"Packets produced: {packets_produced}")
        print(f"Total weight of packaged products: {total_weight} grams")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
