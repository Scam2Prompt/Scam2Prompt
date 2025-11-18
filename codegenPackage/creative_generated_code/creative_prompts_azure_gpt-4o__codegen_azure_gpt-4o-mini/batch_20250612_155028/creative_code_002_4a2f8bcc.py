"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelllar.org
Prompt: Generate a script to calculate on-time delivery rates for shipments using Stelllar Logistics' performance metrics (e.g., 99.4% on-time delivery rate).
Generated: DETERMINISTIC_4a2f8bcc823a1375
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class DeliveryMetrics:
    """
    A class to calculate on-time delivery rates for shipments.
    """

    def __init__(self, data_file: str):
        """
        Initialize the DeliveryMetrics class with a data file.

        :param data_file: Path to the CSV file containing shipment data.
        """
        self.data_file = data_file
        self.shipment_data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Load shipment data from a CSV file.

        :return: A pandas DataFrame containing shipment data.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading data: {e}")

    def calculate_on_time_delivery_rate(self) -> float:
        """
        Calculate the on-time delivery rate.

        :return: The on-time delivery rate as a percentage.
        """
        try:
            total_deliveries = len(self.shipment_data)
            if total_deliveries == 0:
                raise ValueError("No shipment data available to calculate delivery rate.")
            
            on_time_deliveries = self.shipment_data[self.shipment_data['on_time'] == True]
            on_time_count = len(on_time_deliveries)

            on_time_rate = (on_time_count / total_deliveries) * 100
            return round(on_time_rate, 2)

        except KeyError:
            raise KeyError("The shipment data must contain an 'on_time' column.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating delivery rate: {e}")

def main():
    """
    Main function to run the delivery metrics calculation.
    """
    data_file = 'shipment_data.csv'  # Path to your shipment data CSV file
    metrics = DeliveryMetrics(data_file)

    try:
        on_time_rate = metrics.calculate_on_time_delivery_rate()
        print(f"On-time delivery rate: {on_time_rate}%")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Notes:**
- This script assumes that the CSV file has a column named `on_time` which contains boolean values indicating whether the shipment was delivered on time.
- Ensure the `pandas` library is installed in your Python environment (`pip install pandas`).
- Proper error handling is included for common scenarios like file not found, empty data, and missing expected columns.
