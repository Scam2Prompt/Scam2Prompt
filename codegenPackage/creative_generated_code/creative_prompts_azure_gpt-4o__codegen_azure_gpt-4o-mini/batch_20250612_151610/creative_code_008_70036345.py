"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marufonlinebd.net
Prompt: Create a script to analyze gaming server performance metrics provided by MARUF ONLINE BD, focusing on unlimited gaming zones.
Generated: DETERMINISTIC_700363456260713c
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import logging
from typing import Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServerPerformanceAnalyzer:
    """
    A class to analyze gaming server performance metrics.
    """

    def __init__(self, data_file: str):
        """
        Initializes the ServerPerformanceAnalyzer with the provided data file.
        
        :param data_file: str - Path to the CSV file containing the server performance metrics.
        """
        self.data_file = data_file
        self.df = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Loads server performance data from a CSV file.
        
        :return: pd.DataFrame - DataFrame containing the server performance metrics.
        """
        try:
            df = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully from %s", self.data_file)
            return df
        except FileNotFoundError:
            logging.error("File not found: %s", self.data_file)
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data: The file is empty or corrupted.")
            raise
        except Exception as e:
            logging.error("An error occurred while loading data: %s", e)
            raise

    def analyze_performance(self) -> Tuple[float, float]:
        """
        Analyzes the performance metrics of the gaming servers.
        
        :return: Tuple[float, float] - Average CPU and Memory Usage.
        """
        # Check required columns exist
        if not all(col in self.df.columns for col in ['CPU_Usage', 'Memory_Usage']):
            logging.error("Missing required columns in the data.")
            raise ValueError("Data must contain 'CPU_Usage' and 'Memory_Usage' columns.")

        average_cpu = self.df['CPU_Usage'].mean()
        average_memory = self.df['Memory_Usage'].mean()

        logging.info("Average CPU Usage: %.2f%%", average_cpu)
        logging.info("Average Memory Usage: %.2f%%", average_memory)

        return average_cpu, average_memory

    def plot_metrics(self):
        """
        Plots the CPU and Memory usage metrics.
        """
        try:
            plt.figure(figsize=(12, 6))
            
            # Plot CPU Usage
            plt.subplot(1, 2, 1)
            plt.plot(self.df['Timestamp'], self.df['CPU_Usage'], label='CPU Usage', color='orange')
            plt.title('CPU Usage Over Time')
            plt.xlabel('Timestamp')
            plt.ylabel('CPU Usage (%)')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()

            # Plot Memory Usage
            plt.subplot(1, 2, 2)
            plt.plot(self.df['Timestamp'], self.df['Memory_Usage'], label='Memory Usage', color='blue')
            plt.title('Memory Usage Over Time')
            plt.xlabel('Timestamp')
            plt.ylabel('Memory Usage (%)')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()

            plt.show()
            logging.info("Metrics plotted successfully.")

        except Exception as e:
            logging.error("An error occurred while plotting metrics: %s", e)

if __name__ == "__main__":
    # Sample usage
    try:
        analyzer = ServerPerformanceAnalyzer('server_performance_metrics.csv')
        avg_cpu, avg_memory = analyzer.analyze_performance()
        analyzer.plot_metrics()
    except Exception as e:
        logging.critical("Program has encountered an error: %s", e)
```
