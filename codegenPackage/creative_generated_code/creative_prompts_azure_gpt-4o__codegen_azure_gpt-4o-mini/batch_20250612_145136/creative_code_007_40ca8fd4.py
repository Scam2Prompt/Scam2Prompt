"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geosatelites.com
Prompt: Write code to compare the resolution of satellite images (FORMOSAT-2, Pléiades, KOMPSAT-2) and generate a report, referencing the specifications mentioned on geosatelites.com.
Generated: DETERMINISTIC_40ca8fd40bb8a166
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class SatelliteImageComparator:
    """
    A class to compare the resolution of different satellite images.
    """

    def __init__(self):
        # Initialize a DataFrame to hold satellite specifications
        self.satellites_data = pd.DataFrame(columns=["Satellite", "Resolution (m)"])

    def add_satellite(self, name: str, resolution: float):
        """
        Adds a satellite's name and resolution to the DataFrame.

        :param name: The name of the satellite.
        :param resolution: The resolution of the satellite in meters.
        """
        if resolution <= 0:
            raise ValueError("Resolution must be a positive value.")
        self.satellites_data = self.satellites_data.append(
            {"Satellite": name, "Resolution (m)": resolution}, ignore_index=True
        )

    def compare_resolutions(self):
        """
        Compares the resolutions of the satellites and generates a report.

        :return: A DataFrame containing the comparison report.
        """
        if self.satellites_data.empty:
            raise ValueError("No satellite data available for comparison.")

        # Sort the satellites by resolution
        report = self.satellites_data.sort_values(by="Resolution (m)")
        report.reset_index(drop=True, inplace=True)
        return report

    def generate_report(self):
        """
        Generates a report from the comparison of satellite resolutions.

        :return: A string representation of the report.
        """
        report_df = self.compare_resolutions()
        report_string = "Satellite Resolution Comparison Report:\n\n"
        report_string += report_df.to_string(index=False) + "\n"
        return report_string


def main():
    """
    Main function to execute the satellite image comparison.
    """
    try:
        comparator = SatelliteImageComparator()
        
        # Add satellite data (resolutions sourced from geosatelites.com)
        comparator.add_satellite("FORMOSAT-2", 8.0)
        comparator.add_satellite("Pléiades", 0.5)
        comparator.add_satellite("KOMPSAT-2", 1.0)

        # Generate and print the report
        report = comparator.generate_report()
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
