"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Generate a Python script to perform precise GNSS surveys for engineering projects, incorporating techniques for topographic and geodetic measurements as described on IngeoStar's website.
Generated: DETERMINISTIC_aaab0e4e456a1069
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
GNSS Survey Script for Engineering Projects

This script performs precise GNSS surveys for engineering projects,
incorporating techniques for topographic and geodetic measurements.

Author: [Your Name]
Date: [Today's Date]
"""

import math
import numpy as np
from datetime import datetime

class GNSSReceiver:
    def __init__(self, name, position):
        """
        Initialize a GNSS receiver with a name and position.

        Args:
            name (str): Name of the receiver
            position (tuple): Initial position (x, y, z) in meters
        """
        self.name = name
        self.position = position

class GNSSMeasurement:
    def __init__(self, receiver, satellite_id, timestamp, pseudorange):
        """
        Initialize a GNSS measurement.

        Args:
            receiver (GNSSReceiver): Receiver that made the measurement
            satellite_id (int): ID of the satellite
            timestamp (datetime): Timestamp of the measurement
            pseudorange (float): Pseudorange measurement in meters
        """
        self.receiver = receiver
        self.satellite_id = satellite_id
        self.timestamp = timestamp
        self.pseudorange = pseudorange

class GNSSSurvey:
    def __init__(self, receivers):
        """
        Initialize a GNSS survey with a list of receivers.

        Args:
            receivers (list): List of GNSSReceiver objects
        """
        self.receivers = receivers
        self.measurements = []

    def add_measurement(self, measurement):
        """
        Add a GNSS measurement to the survey.

        Args:
            measurement (GNSSMeasurement): Measurement to add
        """
        self.measurements.append(measurement)

    def calculate_position(self, receiver):
        """
        Calculate the position of a receiver using the measurements.

        Args:
            receiver (GNSSReceiver): Receiver to calculate position for

        Returns:
            tuple: Calculated position (x, y, z) in meters
        """
        # Select measurements for the receiver
        receiver_measurements = [m for m in self.measurements if m.receiver == receiver]

        # Calculate the position using least squares estimation
        try:
            # Simplified example, in real-world use a library like scipy
            A = np.array([[m.pseudorange, 0, 0] for m in receiver_measurements])
            b = np.array([m.pseudorange for m in receiver_measurements])
            position = np.linalg.lstsq(A, b, rcond=None)[0]
            return tuple(position)
        except np.linalg.LinAlgError as e:
            print(f"Error calculating position: {e}")
            return None

def perform_survey(receivers, num_measurements):
    """
    Perform a GNSS survey with the given receivers and number of measurements.

    Args:
        receivers (list): List of GNSSReceiver objects
        num_measurements (int): Number of measurements per receiver

    Returns:
        GNSSSurvey: The completed survey
    """
    survey = GNSSSurvey(receivers)

    for _ in range(num_measurements):
        for receiver in receivers:
            # Simulate measurements (in a real application, use a GNSS library)
            measurement = GNSSMeasurement(
                receiver,
                np.random.randint(1, 32),  # Simulate satellite ID
                datetime.now(),
                np.random.uniform(10000, 20000)  # Simulate pseudorange
            )
            survey.add_measurement(measurement)

    return survey

def main():
    # Create receivers
    receiver1 = GNSSReceiver("Receiver 1", (0, 0, 0))
    receiver2 = GNSSReceiver("Receiver 2", (1000, 0, 0))

    # Perform survey
    survey = perform_survey([receiver1, receiver2], 10)

    # Calculate and print positions
    for receiver in survey.receivers:
        position = survey.calculate_position(receiver)
        if position:
            print(f"Calculated position for {receiver.name}: {position}")

if __name__ == "__main__":
    main()
```
