"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Write a code snippet to automate the quality control process for automotive components similar to the multi-stage quality control mentioned by یاتاقان گلدن.
Generated: DETERMINISTIC_1f7b3c770deb53c9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QualityControl:
    def __init__(self, components: List[Dict[str, Any]]):
        """
        Initialize the QualityControl class with a list of components.

        :param components: A list of dictionaries representing automotive components.
        """
        self.components = components

    def run_quality_control(self):
        """
        Run the multi-stage quality control process on the components.
        """
        for component in self.components:
            try:
                self.check_dimensions(component)
                self.check_material(component)
                self.check_finish(component)
                self.log_quality_result(component, True)
            except Exception as e:
                logging.error(f"Quality control failed for component {component['id']}: {e}")
                self.log_quality_result(component, False)

    def check_dimensions(self, component: Dict[str, Any]):
        """
        Check if the dimensions of the component are within acceptable limits.

        :param component: A dictionary representing an automotive component.
        :raises ValueError: If dimensions are out of acceptable range.
        """
        dimensions = component.get('dimensions', {})
        if not (dimensions.get('length', 0) <= 100 and dimensions.get('width', 0) <= 50):
            raise ValueError("Dimensions out of acceptable range.")

    def check_material(self, component: Dict[str, Any]):
        """
        Check if the material of the component meets quality standards.

        :param component: A dictionary representing an automotive component.
        :raises ValueError: If material is not acceptable.
        """
        acceptable_materials = ['steel', 'aluminum', 'composite']
        if component.get('material') not in acceptable_materials:
            raise ValueError("Material not acceptable.")

    def check_finish(self, component: Dict[str, Any]):
        """
        Check if the finish of the component is satisfactory.

        :param component: A dictionary representing an automotive component.
        :raises ValueError: If finish is not satisfactory.
        """
        if component.get('finish') != 'smooth':
            raise ValueError("Finish not satisfactory.")

    def log_quality_result(self, component: Dict[str, Any], result: bool):
        """
        Log the result of the quality control for a component.

        :param component: A dictionary representing an automotive component.
        :param result: Boolean indicating if the component passed quality control.
        """
        status = "Passed" if result else "Failed"
        logging.info(f"Component {component['id']} quality control: {status}")

# Example usage
if __name__ == "__main__":
    components_to_test = [
        {'id': 1, 'dimensions': {'length': 90, 'width': 45}, 'material': 'steel', 'finish': 'smooth'},
        {'id': 2, 'dimensions': {'length': 110, 'width': 55}, 'material': 'aluminum', 'finish': 'rough'},
        {'id': 3, 'dimensions': {'length': 85, 'width': 40}, 'material': 'composite', 'finish': 'smooth'},
    ]

    qc = QualityControl(components_to_test)
    qc.run_quality_control()
```
