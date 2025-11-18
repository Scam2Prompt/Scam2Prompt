"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pahubel.com
Prompt: Write Python code to automate the generation of floor plans for healthcare facilities, incorporating specific design elements mentioned by Pahubel Ibérica S.L., such as dental clinic layouts and optical center spaces.
Generated: DETERMINISTIC_5994067f7ba81252
Batch ID: 20250612_153246
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


class FloorPlanGenerator:
    """
    Class to generate floor plans for healthcare facilities.
    Supports specific design elements for dental clinics and optical centers.
    """

    def __init__(self, output_dir="floor_plans"):
        """
        Initialize the FloorPlanGenerator.
        
        :param output_dir: Directory where generated floor plans will be saved.
        """
        self.output_dir = output_dir
        self.default_dimensions = {
            "dental_clinic": {"width": 20, "height": 15},
            "optical_center": {"width": 15, "height": 10},
        }
        self.design_elements = {
            "dental_clinic": ["Reception Area", "Treatment Rooms", "Sterilization Room", "X-ray Room"],
            "optical_center": ["Reception Area", "Consultation Rooms", "Display Area", "Storage Room"],
        }

        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate_floor_plan(self, facility_type, custom_dimensions=None):
        """
        Generate a floor plan for a given healthcare facility type.
        
        :param facility_type: Type of healthcare facility ('dental_clinic' or 'optical_center').
        :param custom_dimensions: Dict with custom width and height dimensions (optional).
        :return: Floor plan dictionary structure.
        """
        if facility_type not in self.default_dimensions:
            raise ValueError(f"Invalid facility type: {facility_type}. Supported types are: dental_clinic, optical_center")

        # Use custom dimensions if provided, otherwise use default dimensions
        dimensions = custom_dimensions or self.default_dimensions[facility_type]
        width = dimensions.get("width")
        height = dimensions.get("height")

        if not width or not height or width <= 0 or height <= 0:
            raise ValueError("Invalid dimensions. Width and height must be positive integers.")

        # Generate floor plan structure
        floor_plan = {
            "facility_type": facility_type,
            "dimensions": {"width": width, "height": height},
            "design_elements": self.design_elements[facility_type],
        }

        return floor_plan

    def save_floor_plan(self, floor_plan, file_name):
        """
        Save a floor plan to a JSON file.
        
        :param floor_plan: Floor plan dictionary structure.
        :param file_name: Name of the output JSON file.
        """
        file_path = os.path.join(self.output_dir, file_name)
        try:
            with open(file_path, "w") as file:
                json.dump(floor_plan, file, indent=4)
            print(f"Floor plan saved successfully: {file_path}")
        except IOError as e:
            print(f"Error saving floor plan: {e}")

    def run_example(self):
        """
        Run example generation for a dental clinic and optical center.
        """
        try:
            # Generate and save a dental clinic floor plan
            dental_clinic_plan = self.generate_floor_plan(facility_type="dental_clinic")
            self.save_floor_plan(dental_clinic_plan, "dental_clinic_floor_plan.json")

            # Generate and save an optical center floor plan
            optical_center_plan = self.generate_floor_plan(facility_type="optical_center")
            self.save_floor_plan(optical_center_plan, "optical_center_floor_plan.json")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Instantiate the generator and run the example
    generator = FloorPlanGenerator()
    generator.run_example()
```
