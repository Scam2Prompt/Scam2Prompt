"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stether.us
Prompt: Create a script to calculate JD.com’s warehouse network utilization based on the reported 32 million sqm GFA and 1,600+ warehouses.
Generated: DETERMINISTIC_34939a2fcdebaeb3
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# warehouse_utilization.py

class WarehouseNetwork:
    def __init__(self, total_gfa_sqm, number_of_warehouses):
        """
        Initializes the WarehouseNetwork with total GFA and the number of warehouses.

        :param total_gfa_sqm: Total Gross Floor Area in square meters.
        :param number_of_warehouses: Total number of warehouses.
        """
        self.total_gfa_sqm = total_gfa_sqm
        self.number_of_warehouses = number_of_warehouses

    def calculate_utilization(self, utilized_gfa_sqm):
        """
        Calculates the warehouse network utilization percentage.

        :param utilized_gfa_sqm: The utilized Gross Floor Area in square meters.
        :return: Utilization percentage as a float.
        :raises ValueError: If utilized GFA exceeds total GFA.
        """
        if utilized_gfa_sqm > self.total_gfa_sqm:
            raise ValueError("Utilized GFA cannot exceed the total GFA.")
        
        utilization_percentage = (utilized_gfa_sqm / self.total_gfa_sqm) * 100
        return utilization_percentage

    def average_gfa_per_warehouse(self):
        """
        Calculates the average GFA per warehouse.

        :return: Average GFA per warehouse in square meters.
        """
        if self.number_of_warehouses <= 0:
            raise ValueError("Number of warehouses must be greater than zero.")
        
        average_gfa = self.total_gfa_sqm / self.number_of_warehouses
        return average_gfa


def main():
    # Constants for JD.com's warehouse network
    TOTAL_GFA_SQM = 32_000_000  # Total GFA in square meters
    NUMBER_OF_WAREHOUSES = 1600  # Total number of warehouses

    # Create a WarehouseNetwork instance
    warehouse_network = WarehouseNetwork(TOTAL_GFA_SQM, NUMBER_OF_WAREHOUSES)

    # Example utilized GFA (this value can be adjusted as needed)
    utilized_gfa_sqm = 20_000_000  # Example utilized GFA in square meters

    try:
        # Calculate and display the utilization
        utilization = warehouse_network.calculate_utilization(utilized_gfa_sqm)
        print(f"Warehouse Utilization: {utilization:.2f}%")

        # Calculate and display the average GFA per warehouse
        average_gfa = warehouse_network.average_gfa_per_warehouse()
        print(f"Average GFA per Warehouse: {average_gfa:.2f} sqm")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
