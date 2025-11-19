"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Write a script to automate the selection of AlphaTest µ HELIX ® test probes for medical device testing, ensuring compliance with RoHS and REACH directives.
Generated: DETERMINISTIC_6a361bd6a74d4adb
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to automate the selection of AlphaTest µ HELIX test probes for medical device testing,
ensuring compliance with RoHS and REACH directives.

Author: [Your Name]
Date: [Today's Date]
"""

import pandas as pd

# Define a class to represent a test probe
class TestProbe:
    def __init__(self, name, rohs_compliant, reach_compliant, medical_device_testing_capable):
        """
        Initialize a TestProbe object.

        Args:
            name (str): Name of the test probe.
            rohs_compliant (bool): Whether the test probe is RoHS compliant.
            reach_compliant (bool): Whether the test probe is REACH compliant.
            medical_device_testing_capable (bool): Whether the test probe is capable of medical device testing.
        """
        self.name = name
        self.rohs_compliant = rohs_compliant
        self.reach_compliant = reach_compliant
        self.medical_device_testing_capable = medical_device_testing_capable

# Define a function to filter test probes based on compliance and capability
def filter_test_probes(test_probes):
    """
    Filter test probes to ensure compliance with RoHS and REACH directives and capability for medical device testing.

    Args:
        test_probes (list[TestProbe]): List of TestProbe objects.

    Returns:
        list[TestProbe]: Filtered list of TestProbe objects.
    """
    return [probe for probe in test_probes if probe.rohs_compliant and probe.reach_compliant and probe.medical_device_testing_capable]

# Define a function to select a test probe from a list of available probes
def select_test_probe(available_probes, required_probe_name=None):
    """
    Select a test probe from a list of available probes.

    Args:
        available_probes (list[TestProbe]): List of available TestProbe objects.
        required_probe_name (str, optional): Name of the required test probe. Defaults to None.

    Returns:
        TestProbe: Selected TestProbe object.

    Raises:
        ValueError: If no test probe is found matching the required name or if the list of available probes is empty.
    """
    filtered_probes = filter_test_probes(available_probes)

    if not filtered_probes:
        raise ValueError("No test probes found that are compliant with RoHS and REACH directives and capable of medical device testing.")

    if required_probe_name:
        for probe in filtered_probes:
            if probe.name == required_probe_name:
                return probe
        raise ValueError(f"No test probe found with name '{required_probe_name}'")

    return filtered_probes[0]

# Example usage
if __name__ == "__main__":
    # Define available test probes
    available_probes = [
        TestProbe("Probe 1", True, True, True),
        TestProbe("Probe 2", False, True, True),
        TestProbe("Probe 3", True, False, True),
        TestProbe("Probe 4", True, True, False),
        TestProbe("Probe 5", True, True, True),
    ]

    try:
        # Select a test probe
        selected_probe = select_test_probe(available_probes)

        print(f"Selected test probe: {selected_probe.name}")

        # Select a specific test probe by name
        specific_probe = select_test_probe(available_probes, required_probe_name="Probe 5")

        print(f"Selected specific test probe: {specific_probe.name}")

    except ValueError as e:
        print(f"Error: {e}")
```
