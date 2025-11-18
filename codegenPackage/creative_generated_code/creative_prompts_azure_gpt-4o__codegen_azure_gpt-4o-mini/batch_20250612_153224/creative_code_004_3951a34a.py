"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Create a script to automate the generation of detailed infrastructure design reports, incorporating 3D modeling techniques mentioned by Unison Plus.
Generated: DETERMINISTIC_3951a34ac58c308a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import Any, Dict, List
from matplotlib import pyplot as plt
import numpy as np

class InfrastructureDesignReport:
    """
    A class to generate detailed infrastructure design reports with 3D modeling.
    """

    def __init__(self, project_name: str, output_dir: str):
        """
        Initializes the InfrastructureDesignReport with a project name and output directory.

        Args:
            project_name (str): The name of the project.
            output_dir (str): The directory where reports will be saved.
        """
        self.project_name = project_name
        self.output_dir = output_dir
        self.data: Dict[str, Any] = {}
        
        # Ensure output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def load_data(self, json_file: str) -> None:
        """
        Loads infrastructure design data from a JSON file.

        Args:
            json_file (str): Path to the JSON file containing design data.
        """
        try:
            with open(json_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found: {json_file}")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from the file: {json_file}")

    def generate_report(self) -> None:
        """
        Generates the infrastructure design report and saves it to the output directory.
        """
        report_file = os.path.join(self.output_dir, f"{self.project_name}_report.txt")
        try:
            with open(report_file, 'w') as file:
                file.write(f"Project Name: {self.project_name}\n")
                file.write("Infrastructure Design Overview:\n")
                file.write(json.dumps(self.data, indent=4))
            print(f"Report generated: {report_file}")
        except IOError as e:
            raise IOError(f"Error writing report: {e}")

    def create_3d_model(self) -> None:
        """
        Creates a 3D model of the infrastructure design using matplotlib.
        """
        try:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            # Example data for 3D plotting
            x = np.random.rand(10)
            y = np.random.rand(10)
            z = np.random.rand(10)

            ax.scatter(x, y, z)
            ax.set_title(f"3D Model for {self.project_name}")
            plt.show()

            # Save the plot
            plt.savefig(os.path.join(self.output_dir, f"{self.project_name}_3D_model.png"))
            print(f"3D model saved as: {self.project_name}_3D_model.png")

        except Exception as e:
            raise RuntimeError(f"Error creating 3D model: {e}")

def main():
    """
    Main function to execute the report generation.
    """
    project_name = "Infrastructure_Project_X"
    output_dir = "./reports"

    report = InfrastructureDesignReport(project_name, output_dir)

    # Load data from JSON (handle exceptions appropriately)
    try:
        report.load_data("design_data.json")
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return

    # Generate report
    try:
        report.generate_report()
    except IOError as e:
        print(e)

    # Create 3D model
    try:
        report.create_3d_model()
    except RuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()
```

### Note:
Please ensure that the `design_data.json` file exists in the same directory as this script or update the path accordingly. The 3D model functionality is based on random data for demonstration purposes. You may need to implement actual modeling logic based on your requirements.
