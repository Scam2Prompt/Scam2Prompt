"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: "Write a Python script to generate a quotation for a rubber flooring project in Indonesia, including calculations for material costs and labor."
Generated: DETERMINISTIC_f2b4052f98fa015b
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# quotation_generator.py

class RubberFlooringProject:
    def __init__(self, project_name, location, area_in_sqm, 
                 material_price_per_sqm, labor_cost_per_sqm, 
                 material_waste_percentage=0.1, labor_productivity=10):
        """
        Initialize a Rubber Flooring Project.

        Args:
            project_name (str): Name of the project.
            location (str): Location of the project (e.g., Indonesia).
            area_in_sqm (float): Area of the project in square meters.
            material_price_per_sqm (float): Price of material per square meter.
            labor_cost_per_sqm (float): Labor cost per square meter.
            material_waste_percentage (float, optional): Material waste percentage. Defaults to 0.1 (10%).
            labor_productivity (float, optional): Labor productivity in square meters per day. Defaults to 10.
        """
        self.project_name = project_name
        self.location = location
        self.area_in_sqm = area_in_sqm
        self.material_price_per_sqm = material_price_per_sqm
        self.labor_cost_per_sqm = labor_cost_per_sqm
        self.material_waste_percentage = material_waste_percentage
        self.labor_productivity = labor_productivity

    def calculate_material_costs(self):
        """
        Calculate material costs including waste.

        Returns:
            float: Total material cost.
        """
        material_waste = self.area_in_sqm * self.material_waste_percentage
        total_area_to_cover = self.area_in_sqm + material_waste
        total_material_cost = total_area_to_cover * self.material_price_per_sqm
        return total_material_cost

    def calculate_labor_costs(self):
        """
        Calculate labor costs.

        Returns:
            float: Total labor cost.
        """
        total_labor_days = self.area_in_sqm / self.labor_productivity
        total_labor_cost = total_labor_days * self.labor_cost_per_sqm * self.area_in_sqm
        return total_labor_cost

    def generate_quotation(self):
        """
        Generate a quotation for the rubber flooring project.

        Returns:
            dict: Quotation details.
        """
        material_costs = self.calculate_material_costs()
        labor_costs = self.calculate_labor_costs()
        total_cost = material_costs + labor_costs

        quotation = {
            "Project Name": self.project_name,
            "Location": self.location,
            "Area (sqm)": self.area_in_sqm,
            "Material Costs": f"IDR {material_costs:,.2f}",
            "Labor Costs": f"IDR {labor_costs:,.2f}",
            "Total Cost": f"IDR {total_cost:,.2f}",
        }
        return quotation


def main():
    try:
        project_name = input("Enter project name: ")
        location = input("Enter project location: ")
        area_in_sqm = float(input("Enter project area (sqm): "))
        material_price_per_sqm = float(input("Enter material price per sqm (IDR): "))
        labor_cost_per_sqm = float(input("Enter labor cost per sqm (IDR): "))

        project = RubberFlooringProject(project_name, location, area_in_sqm, 
                                       material_price_per_sqm, labor_cost_per_sqm)

        quotation = project.generate_quotation()

        print("\nQuotation:")
        for key, value in quotation.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
