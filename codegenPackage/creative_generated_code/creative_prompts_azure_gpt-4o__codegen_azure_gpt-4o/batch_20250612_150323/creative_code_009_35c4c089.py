"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Recommend algorithms for detecting production bottlenecks in textile factories using real-time data from sewing machines, inspired by OpenSeam's analytics capabilities.
Generated: DETERMINISTIC_35c4c0895733e56d
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s Python code that utilizes a simplified example to detect production bottlenecks in textile factories by analyzing real-time data from sewing machines. It uses a data-driven approach inspired by OpenSeam's analytics capabilities.

```python
import pandas as pd
import numpy as np
from datetime import datetime
from typing import List


class ProductionBottleneckDetector:
    """
    A class to detect production bottlenecks in textile factories using real-time data from sewing machines.
    """
    
    def __init__(self, machine_ids: List[int]):
        """
        Initialize the detector with a list of machine IDs.

        :param machine_ids: List of sewing machine IDs.
        """
        self.machine_ids = machine_ids
        self.data_frame = pd.DataFrame()

    def ingest_real_time_data(self, machine_id: int, timestamp: datetime, operation_time: float):
        """
        Ingest real-time data into the system.

        :param machine_id: ID of the sewing machine.
        :param timestamp: Timestamp of the operation.
        :param operation_time: Time (in seconds) taken for the operation.
        """
        # Validate input data
        if machine_id not in self.machine_ids:
            raise ValueError(f"Invalid machine ID: {machine_id}")
        
        if operation_time < 0:
            raise ValueError("Operation time cannot be negative.")
        
        # Append the new record to the internal data frame
        new_data = pd.DataFrame({
            "MachineID": [machine_id],
            "Timestamp": [timestamp],
            "OperationTime": [operation_time]
        })
        self.data_frame = pd.concat([self.data_frame, new_data], ignore_index=True)

    def detect_bottlenecks(self, window_size: int = 10) -> pd.DataFrame:
        """
        Detect bottlenecks by analyzing operation times over a sliding window.

        :param window_size: The number of recent operations to consider for each machine.
        :return: DataFrame with bottleneck analysis results.
        """
        if self.data_frame.empty:
            raise ValueError("No data available for analysis.")

        # Sort data by timestamp for accurate processing
        self.data_frame.sort_values(by="Timestamp", inplace=True)

        bottleneck_results = []

        # Analyze each machine's data
        for machine_id in self.machine_ids:
            machine_data = self.data_frame[self.data_frame['MachineID'] == machine_id]
            
            if machine_data.shape[0] < window_size:
                continue  # Skip machines with insufficient data
            
            # Calculate moving average of operation times
            machine_data["MovingAvg"] = machine_data["OperationTime"].rolling(window=window_size).mean()

            # Identify bottlenecks where moving average exceeds threshold
            threshold = machine_data["OperationTime"].mean() * 1.5  # Example threshold: 1.5x average operation time
            bottlenecks = machine_data[machine_data["MovingAvg"] > threshold]
            
            for _, row in bottlenecks.iterrows():
                bottleneck_results.append({
                    "MachineID": row["MachineID"],
                    "Timestamp": row["Timestamp"],
                    "MovingAvg": row["MovingAvg"],
                    "Threshold": threshold
                })

        return pd.DataFrame(bottleneck_results)

    def export_bottleneck_report(self, filepath: str):
        """
        Export the bottleneck report to a CSV file.

        :param filepath: Path to the output file.
        """
        bottleneck_data = self.detect_bottlenecks()
        bottleneck_data.to_csv(filepath, index=False)
        print(f"Bottleneck report saved to {filepath}")


# Example usage
if __name__ == "__main__":
    # Initialize the detector with a sample list of machine IDs
    detector = ProductionBottleneckDetector(machine_ids=[1, 2, 3, 4])

    # Simulate real-time data ingestion
    detector.ingest_real_time_data(machine_id=1, timestamp=datetime.now(), operation_time=5.0)
    detector.ingest_real_time_data(machine_id=1, timestamp=datetime.now(), operation_time=6.2)
    detector.ingest_real_time_data(machine_id=2, timestamp=datetime.now(), operation_time=4.8)
    detector.ingest_real_time_data(machine_id=2, timestamp=datetime.now(), operation_time=7.1)

    # Detect bottlenecks and display results
    bottleneck_df = detector.detect_bottlenecks(window_size=2)
    print("Detected bottlenecks:")
    print(bottleneck_df)

    # Export report to CSV
    detector.export_bottleneck_report(filepath="bottleneck_report.csv")
```

This code provides a structured solution to identify bottlenecks based on operation times across sewing machines in real-time. It uses rolling averages and thresholds to flag potential bottlenecks, which can be saved into a CSV report for further analysis.
