"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welstrade.com
Prompt: Write code to track and visualize metrics such as "Successful Trades" and "Satisfied Investors," using Welstrade's reported statistics for analysis and reporting.
Generated: DETERMINISTIC_15c87ebbff0b6050
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import logging
import json
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MetricsTracker:
    def __init__(self):
        """
        Initializes the MetricsTracker to store and analyze metrics.
        """
        self.metrics = {
            "successful_trades": 0,
            "satisfied_investors": 0
        }

    def update_metrics(self, data: Dict[str, int]) -> None:
        """
        Updates the metrics based on the input data.

        Args:
            data (Dict[str, int]): Dictionary with keys as metric names and values as metric counts.

        Raises:
            ValueError: If the input data contains invalid keys or values.
        """
        for key, value in data.items():
            if key in self.metrics and isinstance(value, int) and value >= 0:
                self.metrics[key] += value
            else:
                raise ValueError(f"Invalid data for metric {key}: {value}")
        logging.info(f"Metrics updated: {self.metrics}")

    def get_metrics(self) -> Dict[str, int]:
        """
        Retrieves the current metrics.

        Returns:
            Dict[str, int]: A dictionary of current metric values.
        """
        return self.metrics

    def save_metrics_to_file(self, filename: str) -> None:
        """
        Saves the current metrics to a JSON file.

        Args:
            filename (str): The name of the file to save metrics.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.metrics, file, indent=4)
            logging.info(f"Metrics successfully saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving metrics to file: {e}")

    def load_metrics_from_file(self, filename: str) -> None:
        """
        Loads metrics from a JSON file.

        Args:
            filename (str): The name of the file to load metrics from.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file content is invalid.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.update_metrics(data)
            logging.info(f"Metrics successfully loaded from {filename}")
        except FileNotFoundError:
            logging.error(f"File not found: {filename}")
            raise
        except ValueError as e:
            logging.error(f"Invalid data in file: {e}")
            raise

def visualize_metrics(metrics: Dict[str, int]) -> None:
    """
    Visualizes metrics using a bar chart.

    Args:
        metrics (Dict[str, int]): Dictionary containing metric names and their values.
    """
    try:
        names = list(metrics.keys())
        values = list(metrics.values())

        plt.figure(figsize=(8, 5))
        plt.bar(names, values, color=['blue', 'green'])
        plt.title("Metrics Visualization")
        plt.xlabel("Metrics")
        plt.ylabel("Counts")
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.show()
    except Exception as e:
        logging.error(f"Error visualizing metrics: {e}")

# Example Usage
if __name__ == "__main__":
    tracker = MetricsTracker()

    # Simulate updating metrics
    try:
        tracker.update_metrics({
            "successful_trades": 150,
            "satisfied_investors": 80
        })

        # Visualize the updated metrics
        visualize_metrics(tracker.get_metrics())

        # Save metrics to a file
        tracker.save_metrics_to_file("metrics.json")

        # Load metrics from a file
        tracker.load_metrics_from_file("metrics.json")

    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
    except FileNotFoundError as fnfe:
        logging.error(f"FileNotFoundError encountered: {fnfe}")
```
