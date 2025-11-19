"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Generate a script to design a custom test fixture using AlphaTest µ HELIX ® compliant pogo style probes for testing BGA and QFN components.
Generated: DETERMINISTIC_1dade4eb0b9ee921
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Script to design a custom test fixture using AlphaTest µ HELIX ® compliant pogo style probes 
for testing BGA and QFN components.

Author: [Your Name]
Date: [Today's Date]
"""

import math

class Probe:
    def __init__(self, x, y, z):
        """
        Initialize a probe with its position.

        Args:
            x (float): X-coordinate of the probe.
            y (float): Y-coordinate of the probe.
            z (float): Z-coordinate of the probe.
        """
        self.x = x
        self.y = y
        self.z = z

class Component:
    def __init__(self, type, pitch, size):
        """
        Initialize a component with its type, pitch, and size.

        Args:
            type (str): Type of the component (BGA or QFN).
            pitch (float): Pitch of the component.
            size (tuple): Size of the component (width, length).
        """
        self.type = type
        self.pitch = pitch
        self.size = size

class TestFixture:
    def __init__(self, component, probe_pitch, probe_size):
        """
        Initialize a test fixture with a component, probe pitch, and probe size.

        Args:
            component (Component): Component to be tested.
            probe_pitch (float): Pitch of the probes.
            probe_size (tuple): Size of the probes (diameter, length).
        """
        self.component = component
        self.probe_pitch = probe_pitch
        self.probe_size = probe_size
        self.probes = []

    def design_fixture(self):
        """
        Design the test fixture by calculating probe positions.

        Raises:
            ValueError: If the component type is not supported.
        """
        if self.component.type not in ['BGA', 'QFN']:
            raise ValueError("Unsupported component type")

        # Calculate probe positions based on component type and pitch
        if self.component.type == 'BGA':
            self._design_bga_fixture()
        elif self.component.type == 'QFN':
            self._design_qfn_fixture()

    def _design_bga_fixture(self):
        """
        Design the test fixture for a BGA component.
        """
        # Calculate probe positions in a grid pattern
        for x in range(int(self.component.size[0] / self.component.pitch)):
            for y in range(int(self.component.size[1] / self.component.pitch)):
                probe_x = x * self.component.pitch
                probe_y = y * self.component.pitch
                probe_z = 0  # Assuming a flat fixture
                self.probes.append(Probe(probe_x, probe_y, probe_z))

    def _design_qfn_fixture(self):
        """
        Design the test fixture for a QFN component.
        """
        # Calculate probe positions along the perimeter of the component
        for x in range(int(self.component.size[0] / self.component.pitch)):
            probe_x = x * self.component.pitch
            probe_y = 0
            probe_z = 0  # Assuming a flat fixture
            self.probes.append(Probe(probe_x, probe_y, probe_z))

        for y in range(int(self.component.size[1] / self.component.pitch)):
            probe_x = self.component.size[0]
            probe_y = y * self.component.pitch
            probe_z = 0  # Assuming a flat fixture
            self.probes.append(Probe(probe_x, probe_y, probe_z))

    def validate_fixture(self):
        """
        Validate the test fixture by checking probe positions and sizes.

        Raises:
            ValueError: If a probe position or size is invalid.
        """
        for probe in self.probes:
            if probe.x < 0 or probe.y < 0 or probe.z < 0:
                raise ValueError("Invalid probe position")

            if self.probe_size[0] <= 0 or self.probe_size[1] <= 0:
                raise ValueError("Invalid probe size")

    def generate_gbl_file(self, filename):
        """
        Generate a GBL file for the test fixture.

        Args:
            filename (str): Name of the output file.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(filename, 'w') as f:
                f.write("# GBL file for test fixture\n")
                for probe in self.probes:
                    f.write(f"Probe {probe.x:.2f},{probe.y:.2f},{probe.z:.2f}\n")
        except IOError as e:
            raise IOError(f"Failed to write GBL file: {e}")

def main():
    # Example usage
    component = Component('BGA', 0.5, (10, 10))
    fixture = TestFixture(component, 0.2, (0.1, 1.0))
    fixture.design_fixture()
    fixture.validate_fixture()
    fixture.generate_gbl_file('fixture.gbl')

if __name__ == "__main__":
    main()
```
