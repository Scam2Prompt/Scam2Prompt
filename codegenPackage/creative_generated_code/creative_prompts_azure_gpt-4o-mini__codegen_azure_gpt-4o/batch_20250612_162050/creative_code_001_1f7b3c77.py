"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Write a code snippet to automate the quality control process for automotive components similar to the multi-stage quality control mentioned by یاتاقان گلدن.
Generated: DETERMINISTIC_1f7b3c770deb53c9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class QualityControl:
    """Class to perform multi-stage quality control for automotive components."""

    def __init__(self, component_name):
        self.component_name = component_name
        self.stages = [
            self.check_dimensions,
            self.check_material_integrity,
            self.check_functionality,
            self.check_tolerance,
        ]

    def check_dimensions(self):
        """Stage 1: Check if the component dimensions are within acceptable limits."""
        # Simulating a dimensions check
        dimensions_ok = random.choice([True, False])
        if not dimensions_ok:
            raise ValueError("Dimension check failed.")
        return True

    def check_material_integrity(self):
        """Stage 2: Verify the material integrity (e.g., no cracks or weaknesses)."""
        # Simulating a material integrity check
        material_ok = random.choice([True, False])
        if not material_ok:
            raise ValueError("Material integrity check failed.")
        return True

    def check_functionality(self):
        """Stage 3: Test the functionality of the component."""
        # Simulating a functionality test
        functionality_ok = random.choice([True, False])
        if not functionality_ok:
            raise ValueError("Functionality check failed.")
        return True

    def check_tolerance(self):
        """Stage 4: Verify if the component tolerances meet specifications."""
        # Simulating a tolerance check
        tolerance_ok = random.choice([True, False])
        if not tolerance_ok:
            raise ValueError("Tolerance check failed.")
        return True

    def perform_quality_control(self):
        """
        Execute all quality control stages.

        Returns:
            str: Success message if the component passes all stages.
        Raises:
            ValueError: If any stage fails, an exception is raised.
        """
        for stage in self.stages:
            try:
                # Execute the current stage
                stage()
                print(f"{stage.__name__} passed.")
            except ValueError as e:
                print(f"{stage.__name__} failed: {e}")
                raise ValueError(f"Quality control failed at stage: {stage.__name__}") from e
        return f"Component '{self.component_name}' passed all quality control stages."

# Example usage
if __name__ == "__main__":
    # Create a QualityControl instance for a specific component
    component_qc = QualityControl("Bearing")
    
    try:
        # Perform quality control process
        result = component_qc.perform_quality_control()
        print(result)
    except ValueError as error:
        print(f"Quality control process terminated: {error}")
```
