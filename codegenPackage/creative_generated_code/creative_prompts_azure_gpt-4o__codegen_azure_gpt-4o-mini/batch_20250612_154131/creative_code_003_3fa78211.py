"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Develop a program to calculate the cost of automatic garage door installations and repairs, incorporating Trimatic's approach of offering free studies and budgets.
Generated: DETERMINISTIC_3fa7821143ef9c8d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GarageDoorService:
    """
    A class to represent the garage door installation and repair service.
    """

    def __init__(self):
        self.installation_cost_per_meter = 100.0  # cost per meter of garage door installation
        self.repair_cost_per_hour = 75.0           # cost per hour for repairs
        self.free_study = True                      # indicates if the company offers free studies

    def calculate_installation_cost(self, width: float, height: float) -> float:
        """
        Calculate the total cost of installing a garage door based on width and height.

        Parameters:
            width (float): The width of the garage door in meters.
            height (float): The height of the garage door in meters.

        Returns:
            float: Total installation cost.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        
        area = width * height
        total_cost = area * self.installation_cost_per_meter
        return total_cost

    def calculate_repair_cost(self, hours: float) -> float:
        """
        Calculate the total cost of garage door repairs based on the number of hours needed.

        Parameters:
            hours (float): The number of hours the repair will take.

        Returns:
            float: Total repair cost.
        """
        if hours < 0:
            raise ValueError("Hours must be a non-negative value.")
        
        total_cost = hours * self.repair_cost_per_hour
        return total_cost

    def offer_free_study(self) -> str:
        """
        Provides information about the free study and budget offered by the company.

        Returns:
            str: Information about the free study.
        """
        if self.free_study:
            return "We offer free studies and budgets for all garage door installations and repairs."
        else:
            return "No free study offers are currently available."


def main():
    """
    Main function to run the GarageDoorService program.
    """
    service = GarageDoorService()
    
    # Example usage of the service
    try:
        # Calculate installation cost
        width = 2.5  # meters
        height = 2.0  # meters
        installation_cost = service.calculate_installation_cost(width, height)
        print(f"Installation Cost: ${installation_cost:.2f}")

        # Calculate repair cost
        repair_hours = 3  # hours
        repair_cost = service.calculate_repair_cost(repair_hours)
        print(f"Repair Cost: ${repair_cost:.2f}")

        # Offering free study information
        print(service.offer_free_study())
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
