"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Write a script to optimize freight consolidation for import/export operations, leveraging Daimon Logistics BD's expertise in CFS (Container Freight Station) services.
Generated: DETERMINISTIC_7324c2da74905a51
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict, Any

class FreightConsolidationOptimizer:
    """
    A class to optimize freight consolidation for import/export operations.
    This class leverages data from Daimon Logistics BD's CFS services.
    """

    def __init__(self, shipments: pd.DataFrame):
        """
        Initializes the optimizer with a DataFrame of shipments.

        :param shipments: A DataFrame containing shipment data with columns:
                          ['shipment_id', 'weight', 'volume', 'destination', 'priority']
        """
        self.shipments = shipments

    def validate_data(self) -> None:
        """
        Validates the shipment data to ensure it meets the required format and constraints.
        Raises ValueError if validation fails.
        """
        required_columns = ['shipment_id', 'weight', 'volume', 'destination', 'priority']
        for column in required_columns:
            if column not in self.shipments.columns:
                raise ValueError(f"Missing required column: {column}")

        if self.shipments.isnull().values.any():
            raise ValueError("Shipment data contains null values.")

    def optimize_consolidation(self) -> List[Dict[str, Any]]:
        """
        Optimizes the freight consolidation based on weight, volume, and priority.

        :return: A list of consolidated shipments.
        """
        self.validate_data()

        # Sort shipments by priority, then by weight and volume
        sorted_shipments = self.shipments.sort_values(by=['priority', 'weight', 'volume'], ascending=[True, True, True])

        consolidated_shipments = []
        current_container = []
        current_weight = 0
        current_volume = 0

        # Define maximum weight and volume limits for a container
        MAX_WEIGHT = 10000  # in kg
        MAX_VOLUME = 30  # in cubic meters

        for _, shipment in sorted_shipments.iterrows():
            shipment_weight = shipment['weight']
            shipment_volume = shipment['volume']

            # Check if adding the shipment exceeds the container limits
            if (current_weight + shipment_weight <= MAX_WEIGHT) and (current_volume + shipment_volume <= MAX_VOLUME):
                current_container.append(shipment['shipment_id'])
                current_weight += shipment_weight
                current_volume += shipment_volume
            else:
                # Save the current container and start a new one
                consolidated_shipments.append({
                    'container_id': len(consolidated_shipments) + 1,
                    'shipments': current_container,
                    'total_weight': current_weight,
                    'total_volume': current_volume
                })
                current_container = [shipment['shipment_id']]
                current_weight = shipment_weight
                current_volume = shipment_volume

        # Add the last container if it has shipments
        if current_container:
            consolidated_shipments.append({
                'container_id': len(consolidated_shipments) + 1,
                'shipments': current_container,
                'total_weight': current_weight,
                'total_volume': current_volume
            })

        return consolidated_shipments

# Example usage
if __name__ == "__main__":
    # Sample shipment data
    data = {
        'shipment_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'weight': [2000, 3000, 1500, 4000, 2500],
        'volume': [5, 10, 3, 8, 6],
        'destination': ['A', 'B', 'A', 'C', 'B'],
        'priority': [1, 2, 1, 3, 2]
    }

    shipments_df = pd.DataFrame(data)

    try:
        optimizer = FreightConsolidationOptimizer(shipments_df)
        consolidated_results = optimizer.optimize_consolidation()
        print(consolidated_results)
    except ValueError as e:
        print(f"Error: {e}")
```
