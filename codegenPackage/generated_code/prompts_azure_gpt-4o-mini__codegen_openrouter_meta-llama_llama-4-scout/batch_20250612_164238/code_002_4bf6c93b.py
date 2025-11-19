"""
Generated Code Metadata:
========================
Original URL: https://lsinterior.com.my
Prompt: Write a function in Python that calculates the estimated budget for a home renovation project, considering factors like space planning and landscaping.
Generated: DETERMINISTIC_4bf6c93bc130eaac
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# home_renovation_budget.py

class RenovationProject:
    def __init__(self, 
                 total_square_feet: float, 
                 num_rooms: int, 
                 has_backyard: bool, 
                 has_front_yard: bool):
        """
        Initialize a home renovation project.

        Args:
        - total_square_feet (float): Total square feet of the home.
        - num_rooms (int): Number of rooms in the home.
        - has_backyard (bool): Whether the home has a backyard.
        - has_front_yard (bool): Whether the home has a front yard.
        """
        self.total_square_feet = total_square_feet
        self.num_rooms = num_rooms
        self.has_backyard = has_backyard
        self.has_front_yard = has_front_yard

    def calculate_space_planning_cost(self) -> float:
        """
        Calculate the estimated cost for space planning.

        Returns:
        - float: Estimated cost for space planning.
        """
        # Assume $10 per square foot for space planning
        space_planning_cost_per_sqft = 10.0
        return self.total_square_feet * space_planning_cost_per_sqft

    def calculate_landscaping_cost(self) -> float:
        """
        Calculate the estimated cost for landscaping.

        Returns:
        - float: Estimated cost for landscaping.
        """
        # Assume $5,000 for backyard landscaping and $3,000 for front yard landscaping
        backyard_landscaping_cost = 5000.0
        front_yard_landscaping_cost = 3000.0

        landscaping_cost = 0.0
        if self.has_backyard:
            landscaping_cost += backyard_landscaping_cost
        if self.has_front_yard:
            landscaping_cost += front_yard_landscaping_cost

        return landscaping_cost

    def calculate_renovation_cost(self) -> float:
        """
        Calculate the estimated cost for renovation per room.

        Returns:
        - float: Estimated cost for renovation per room.
        """
        # Assume $20,000 per room for renovation
        renovation_cost_per_room = 20000.0
        return self.num_rooms * renovation_cost_per_room

    def calculate_total_budget(self) -> float:
        """
        Calculate the estimated total budget for the home renovation project.

        Returns:
        - float: Estimated total budget.
        """
        space_planning_cost = self.calculate_space_planning_cost()
        landscaping_cost = self.calculate_landscaping_cost()
        renovation_cost = self.calculate_renovation_cost()

        return space_planning_cost + landscaping_cost + renovation_cost


def main():
    try:
        # Example usage
        project = RenovationProject(
            total_square_feet=2000.0, 
            num_rooms=5, 
            has_backyard=True, 
            has_front_yard=True
        )

        space_planning_cost = project.calculate_space_planning_cost()
        landscaping_cost = project.calculate_landscaping_cost()
        renovation_cost = project.calculate_renovation_cost()
        total_budget = project.calculate_total_budget()

        print(f"Space Planning Cost: ${space_planning_cost:,.2f}")
        print(f"Landscaping Cost: ${landscaping_cost:,.2f}")
        print(f"Renovation Cost: ${renovation_cost:,.2f}")
        print(f"Total Budget: ${total_budget:,.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
