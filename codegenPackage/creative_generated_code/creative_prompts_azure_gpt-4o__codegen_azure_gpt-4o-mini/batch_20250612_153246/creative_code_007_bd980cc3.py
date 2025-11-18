"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Create a program to generate reports on the reliability and efficiency of maritime supply services, incorporating metrics such as delivery timeliness and product quality as emphasized by Supply Marine.
Generated: DETERMINISTIC_bd980cc304922a99
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaritimeSupplyReport:
    """
    A class to generate reports on the reliability and efficiency of maritime supply services.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the MaritimeSupplyReport with the given data.

        Args:
            data (pd.DataFrame): A DataFrame containing supply service data.
        """
        self.data = data

    def preprocess_data(self) -> None:
        """
        Preprocess the data by converting dates and handling missing values.
        """
        try:
            # Convert delivery_date to datetime
            self.data['delivery_date'] = pd.to_datetime(self.data['delivery_date'], errors='coerce')
            self.data['order_date'] = pd.to_datetime(self.data['order_date'], errors='coerce')

            # Drop rows with missing values
            self.data.dropna(inplace=True)
            logging.info("Data preprocessing complete.")
        except Exception as e:
            logging.error(f"Error in preprocessing data: {e}")

    def calculate_delivery_timeliness(self) -> float:
        """
        Calculates the percentage of on-time deliveries.

        Returns:
            float: Percentage of on-time deliveries.
        """
        try:
            self.data['on_time'] = self.data['delivery_date'] <= self.data['expected_delivery_date']
            on_time_percentage = self.data['on_time'].mean() * 100
            logging.info(f"Calculated on-time delivery percentage: {on_time_percentage:.2f}%")
            return on_time_percentage
        except Exception as e:
            logging.error(f"Error calculating delivery timeliness: {e}")
            return 0.0

    def calculate_product_quality(self) -> float:
        """
        Calculates the average product quality score.

        Returns:
            float: Average product quality score.
        """
        try:
            avg_quality = self.data['product_quality'].mean()
            logging.info(f"Calculated average product quality score: {avg_quality:.2f}")
            return avg_quality
        except Exception as e:
            logging.error(f"Error calculating product quality: {e}")
            return 0.0

    def generate_report(self) -> Dict[str, float]:
        """
        Generates a report summarizing delivery timeliness and product quality.

        Returns:
            Dict[str, float]: A dictionary containing the report metrics.
        """
        try:
            self.preprocess_data()
            report = {
                "Delivery Timeliness (%)": self.calculate_delivery_timeliness(),
                "Average Product Quality": self.calculate_product_quality()
            }
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            return {}

def main():
    # Sample data for demonstration purposes
    sample_data = {
        'order_date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'delivery_date': ['2023-01-05', '2023-01-05', '2023-01-04'],
        'expected_delivery_date': ['2023-01-06', '2023-01-05', '2023-01-05'],
        'product_quality': [4.5, 3.8, 4.0]  # Quality scores from 1 to 5
    }

    try:
        # Convert sample data to DataFrame
        df = pd.DataFrame(sample_data)

        # Create a report instance
        report_generator = MaritimeSupplyReport(df)

        # Generate the report
        report = report_generator.generate_report()
        print(report)

    except Exception as e:
        logging.error(f"Error in main execution: {e}")

if __name__ == '__main__':
    main()
```
