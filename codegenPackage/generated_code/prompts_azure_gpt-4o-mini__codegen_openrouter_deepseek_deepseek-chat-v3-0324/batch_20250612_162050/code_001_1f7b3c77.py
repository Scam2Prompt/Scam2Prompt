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
import random
import time
from enum import Enum, auto
from typing import List, Dict, Optional

class QualityStatus(Enum):
    """Enum representing the possible quality statuses of a component."""
    PASS = auto()
    FAIL = auto()
    PENDING = auto()

class Component:
    """Class representing an automotive component undergoing quality control."""
    def __init__(self, component_id: str):
        self.component_id = component_id
        self.status = QualityStatus.PENDING
        self.test_results: Dict[str, QualityStatus] = {}
        self.defects: List[str] = []

    def add_test_result(self, test_name: str, status: QualityStatus, defect: Optional[str] = None) -> None:
        """Add a test result to the component."""
        self.test_results[test_name] = status
        if status == QualityStatus.FAIL and defect:
            self.defects.append(defect)
        self._update_overall_status()

    def _update_overall_status(self) -> None:
        """Update the overall status based on individual test results."""
        if any(result == QualityStatus.FAIL for result in self.test_results.values()):
            self.status = QualityStatus.FAIL
        elif all(result == QualityStatus.PASS for result in self.test_results.values()):
            self.status = QualityStatus.PASS

    def __str__(self) -> str:
        return f"Component {self.component_id} - Status: {self.status.name}"

class QualityControlStation:
    """Class representing a quality control station with specific tests."""
    def __init__(self, station_name: str, test_names: List[str]):
        self.station_name = station_name
        self.test_names = test_names

    def run_tests(self, component: Component) -> None:
        """Run all tests for the component at this station."""
        print(f"Running tests at {self.station_name} for {component.component_id}")
        for test_name in self.test_names:
            time.sleep(0.5)  # Simulate test execution time
            # Simulate test results (90% pass rate)
            if random.random() < 0.9:
                component.add_test_result(test_name, QualityStatus.PASS)
                print(f"  {test_name}: PASS")
            else:
                defect = f"Defect found in {test_name}"
                component.add_test_result(test_name, QualityStatus.FAIL, defect)
                print(f"  {test_name}: FAIL - {defect}")

class QualityControlPipeline:
    """Class representing the multi-stage quality control pipeline."""
    def __init__(self):
        self.stations: List[QualityControlStation] = []
        self.components: List[Component] = []

    def add_station(self, station: QualityControlStation) -> None:
        """Add a quality control station to the pipeline."""
        self.stations.append(station)

    def add_component(self, component: Component) -> None:
        """Add a component to the quality control pipeline."""
        self.components.append(component)

    def run_pipeline(self) -> None:
        """Run all components through the quality control pipeline."""
        for component in self.components:
            print(f"\nProcessing {component.component_id}")
            for station in self.stations:
                station.run_tests(component)
                if component.status == QualityStatus.FAIL:
                    print(f"Component {component.component_id} failed at {station.station_name}")
                    break  # Stop further testing if component fails
            print(f"Final status for {component.component_id}: {component.status.name}")
            if component.defects:
                print("Defects found:", ", ".join(component.defects))

def main():
    """Main function to demonstrate the quality control process."""
    # Create quality control pipeline
    pipeline = QualityControlPipeline()

    # Add quality control stations with their respective tests
    pipeline.add_station(QualityControlStation("Dimensional Check", ["Length", "Width", "Height"]))
    pipeline.add_station(QualityControlStation("Material Test", ["Hardness", "Composition"]))
    pipeline.add_station(QualityControlStation("Functional Test", ["Rotation", "Load Capacity"]))

    # Add components to be tested
    for i in range(1, 6):  # Testing 5 components
        pipeline.add_component(Component(f"COMP-{i:03d}"))

    # Run the quality control pipeline
    pipeline.run_pipeline()

if __name__ == "__main__":
    main()
```
