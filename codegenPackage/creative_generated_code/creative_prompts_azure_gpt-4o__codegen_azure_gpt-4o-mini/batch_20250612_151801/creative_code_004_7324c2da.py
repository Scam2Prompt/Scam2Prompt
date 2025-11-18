"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Write a script to optimize freight consolidation for import/export operations, leveraging Daimon Logistics BD's expertise in CFS (Container Freight Station) services.
Generated: DETERMINISTIC_7324c2da74905a51
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict, Tuple

class FreightConsolidationOptimizer:
    """
    A class to optimize freight consolidation for import/export operations
    based on provided container and shipment data.
    """

    def __init__(self, shipments: pd.DataFrame, container_capacity: float):
        """
        Initializes the optimizer with shipment data and container capacity.

        Args:
            shipments (pd.DataFrame): DataFrame containing shipment data with weight and volume.
            container_capacity (float): Maximum capacity of the container.
        """
        self.shipments = shipments
        self.container_capacity = container_capacity

    def optimize_consolidation(self) -> List[List[Dict]]:
        """
        Optimizes the consolidation of shipments into containers.

        Returns:
            List[List[Dict]]: A list of containers, each containing a list of shipments.
        """
        containers = []
        current_container = []
        current_weight = 0.0
        current_volume = 0.0

        for index, shipment in self.shipments.iterrows():
            weight = shipment['weight']
            volume = shipment['volume']

            # Check if adding the shipment exceeds the capacity
            if (current_weight + weight <= self.container_capacity) and (current_volume + volume <= self.container_capacity):
                current_container.append(shipment.to_dict())
                current_weight += weight
                current_volume += volume
            else:
                # If current container is full, save it and start a new one
                if current_container:
                    containers.append(current_container)
                current_container = [shipment.to_dict()]
                current_weight = weight
                current_volume = volume

        # Don't forget to add the last container if it has shipments
        if current_container:
            containers.append(current_container)

        return containers

def load_shipment_data(file_path: str) -> pd.DataFrame:
    """
    Loads shipment data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing shipment data.

    Returns:
        pd.DataFrame: DataFrame containing the loaded shipment data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the CSV data is malformed.
    """
    try:
        shipments = pd.read_csv(file_path)
        if 'weight' not in shipments.columns or 'volume' not in shipments.columns:
            raise ValueError("CSV must contain 'weight' and 'volume' columns.")
        return shipments
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: The specified file '{file_path}' does not exist.") from e
    except pd.errors.EmptyDataError:
        raise ValueError("Error: No data found in the CSV file.")
    except Exception as e:
        raise ValueError(f"An error occurred while loading the CSV file: {str(e)}") from e

def main(file_path: str, container_capacity: float):
    """
    Main function to execute the freight consolidation optimization process.

    Args:
        file_path (str): Path to the CSV file containing shipment data.
        container_capacity (float): Maximum capacity of the container.
    """
    try:
        shipments = load_shipment_data(file_path)
        optimizer = FreightConsolidationOptimizer(shipments, container_capacity)
        consolidated_containers = optimizer.optimize_consolidation()

        # Output results
        for idx, container in enumerate(consolidated_containers):
            print(f"Container {idx + 1}:")
            for shipment in container:
                print(f"  Shipment ID: {shipment['id']} | Weight: {shipment['weight']} | Volume: {shipment['volume']}")
            print()
    except Exception as e:
        print(f"Error during consolidation optimization: {str(e)}")

if __name__ == "__main__":
    # Example usage: specify the CSV file path and container capacity
    FILE_PATH = "shipments.csv"  # Replace with your actual file path
    CONTAINER_CAPACITY = 1000.0    # Example capacity in weight/volume units

    main(FILE_PATH, CONTAINER_CAPACITY)
```
