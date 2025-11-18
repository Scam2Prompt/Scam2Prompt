"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alu-air.com
Prompt: Generate Python code to calculate transportation efficiency metrics for aluminum-based products like alu-air©.
Generated: DETERMINISTIC_103557080789e37c
Batch ID: 20250612_155002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class TransportationEfficiencyCalculator:
    """
    A class to calculate transportation efficiency metrics for aluminum-based products like alu-air©.
    """

    def __init__(self, data):
        """
        Initializes the calculator with transportation data.

        :param data: A pandas DataFrame containing transportation metrics.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame")
        
        self.data = data

    def calculate_efficiency(self):
        """
        Calculates the transportation efficiency metrics.

        :return: A dictionary containing efficiency metrics.
        """
        try:
            total_distance = self.data['distance'].sum()
            total_weight = self.data['weight'].sum()
            total_emissions = self.data['emissions'].sum()

            efficiency_metrics = {
                'total_distance': total_distance,
                'total_weight': total_weight,
                'total_emissions': total_emissions,
                'efficiency_ratio': self._calculate_efficiency_ratio(total_distance, total_weight)
            }

            return efficiency_metrics
        
        except KeyError as e:
            raise KeyError(f"Missing expected column in the data: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred during efficiency calculation: {e}")

    def _calculate_efficiency_ratio(self, total_distance, total_weight):
        """
        Calculates the efficiency ratio based on distance and weight.

        :param total_distance: Total distance traveled.
        :param total_weight: Total weight of the transported goods.
        :return: The efficiency ratio.
        """
        if total_weight == 0:
            raise ValueError("Total weight cannot be zero when calculating efficiency ratio.")
        
        return total_distance / total_weight

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'distance': [100, 150, 200],  # distances in kilometers
        'weight': [10, 15, 20],        # weights in tons
        'emissions': [5, 7.5, 10]      # emissions in kg CO2
    }

    # Create a DataFrame
    df = pd.DataFrame(sample_data)

    # Instantiate the calculator
    calculator = TransportationEfficiencyCalculator(data=df)

    # Calculate the efficiency metrics
    try:
        efficiency_metrics = calculator.calculate_efficiency()
        print("Transportation Efficiency Metrics:")
        print(efficiency_metrics)
    except Exception as e:
        print(f"Error: {e}")
```
