"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Develop a program to calculate the cost of automatic garage door installations and repairs, incorporating Trimatic's approach of offering free studies and budgets.
Generated: DETERMINISTIC_3fa7821143ef9c8d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GarageDoorService:
    """
    A class to represent a garage door installation and repair service.
    """

    def __init__(self):
        self.installation_cost_per_square_foot = 50.0  # Cost per square foot for installation
        self.repair_cost_per_hour = 75.0  # Cost per hour for repairs
        self.free_study = True  # Indicates if a free study is offered

    def calculate_installation_cost(self, width: float, height: float) -> float:
        """
        Calculate the cost of garage door installation based on dimensions.

        Parameters:
        width (float): The width of the garage door in feet.
        height (float): The height of the garage door in feet.

        Returns:
        float: The total cost of installation.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        
        area = width * height  # Calculate area in square feet
        total_cost = area * self.installation_cost_per_square_foot
        return total_cost

    def calculate_repair_cost(self, hours: float) -> float:
        """
        Calculate the cost of garage door repairs based on time spent.

        Parameters:
        hours (float): The number of hours spent on repairs.

        Returns:
        float: The total cost of repairs.
        """
        if hours < 0:
            raise ValueError("Hours must be a non-negative value.")
        
        total_cost = hours * self.repair_cost_per_hour
        return total_cost

    def offer_free_study(self) -> str:
        """
        Offer a free study and budget for potential customers.

        Returns:
        str: A message indicating the offer of a free study.
        """
        if self.free_study:
            return "We offer a free study and budget for your garage door installation or repair."
        return "Free study is not available at this time."


def main():
    """
    Main function to demonstrate the GarageDoorService functionality.
    """
    service = GarageDoorService()

    # Example usage
    try:
        # Calculate installation cost
        width = 10.0  # Width in feet
        height = 8.0  # Height in feet
        installation_cost = service.calculate_installation_cost(width, height)
        print(f"Installation cost for a {width}x{height} garage door: ${installation_cost:.2f}")

        # Calculate repair cost
        repair_hours = 2.5  # Hours spent on repairs
        repair_cost = service.calculate_repair_cost(repair_hours)
        print(f"Repair cost for {repair_hours} hours: ${repair_cost:.2f}")

        # Offer free study
        print(service.offer_free_study())

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
