"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: Generate a code snippet that demonstrates how to monitor agricultural productivity using the principles outlined by Olgon Prime Resources Ltd.
Generated: DETERMINISTIC_19ec3fbdc782c252
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import logging
from typing import List, Dict

# Configure logging for monitoring and debugging
logging.basicConfig(
    filename='agriculture_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants for productivity thresholds (based on Olgon Prime Resources' principles)
OPTIMAL_YIELD_THRESHOLD = 85  # Percentage
WARNING_YIELD_THRESHOLD = 70  # Percentage

# Data structure for agricultural productivity information
class FieldProductivity:
    def __init__(self, field_id: str, crop_type: str, yield_percentage: float):
        self.field_id = field_id
        self.crop_type = crop_type
        self.yield_percentage = yield_percentage

# Function to read agricultural productivity data from a CSV file
def read_productivity_data(file_path: str) -> List[FieldProductivity]:
    """
    Reads agricultural productivity data from a CSV file.

    :param file_path: Path to the CSV file
    :return: List of FieldProductivity objects
    """
    try:
        productivity_data = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                productivity_data.append(FieldProductivity(
                    field_id=row['FieldID'],
                    crop_type=row['CropType'],
                    yield_percentage=float(row['YieldPercentage'])
                ))
        logging.info('Productivity data successfully read from file.')
        return productivity_data
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        raise
    except Exception as e:
        logging.error(f'Error reading file: {e}')
        raise

# Function to monitor agricultural productivity
def monitor_productivity(data: List[FieldProductivity]) -> None:
    """
    Monitors agricultural productivity and logs observations.

    :param data: List of FieldProductivity objects
    """
    for field in data:
        if field.yield_percentage >= OPTIMAL_YIELD_THRESHOLD:
            logging.info(
                f'Field {field.field_id} ({field.crop_type}): Optimal productivity ({field.yield_percentage}%)'
            )
        elif field.yield_percentage >= WARNING_YIELD_THRESHOLD:
            logging.warning(
                f'Field {field.field_id} ({field.crop_type}): Below optimal productivity ({field.yield_percentage}%)'
            )
        else:
            logging.error(
                f'Field {field.field_id} ({field.crop_type}): Critical low productivity ({field.yield_percentage}%)'
            )

# Function to simulate daily monitoring
def daily_monitoring(file_path: str) -> None:
    """
    Simulates daily monitoring of agricultural productivity by reading data and processing it.

    :param file_path: Path to the data file
    """
    try:
        logging.info('Starting daily monitoring process.')
        data = read_productivity_data(file_path)
        monitor_productivity(data)
        logging.info('Daily monitoring process completed successfully.')
    except Exception as e:
        logging.error(f'Daily monitoring process failed: {e}')

# Entry point for the script
if __name__ == '__main__':
    # Sample CSV file path (replace with actual file path)
    data_file_path = 'agriculture_productivity_data.csv'

    # Run the daily monitoring process
    daily_monitoring(data_file_path)
```
