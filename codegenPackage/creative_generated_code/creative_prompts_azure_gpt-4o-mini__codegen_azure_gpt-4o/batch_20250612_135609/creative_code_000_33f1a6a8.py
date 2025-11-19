"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peacecitycontracting.com
Prompt: Generate a code snippet for a construction project management application that includes features for building construction, renovation works, and fit-out works.
Generated: DETERMINISTIC_33f1a6a8923932a9
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Project:
    """
    Represents a generic construction project.
    """

    def __init__(self, name, start_date, end_date, budget):
        """
        Initialize a project with its basic details.

        :param name: Name of the project
        :param start_date: Project start date (datetime object)
        :param end_date: Project end date (datetime object)
        :param budget: Budget allocated for the project (float)
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = "Not Started"  # Possible values: Not Started, In Progress, Completed

    def update_status(self, new_status):
        """
        Update the status of the project.

        :param new_status: New status of the project (string)
        """
        if new_status not in ["Not Started", "In Progress", "Completed"]:
            raise ValueError("Invalid status value. Use 'Not Started', 'In Progress', or 'Completed'.")
        self.status = new_status

    def __str__(self):
        """
        String representation of the project details.
        """
        return f"Project: {self.name}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nBudget: ${self.budget}\nStatus: {self.status}"


class BuildingConstruction(Project):
    """
    Represents a building construction project.
    """

    def __init__(self, name, start_date, end_date, budget, building_type):
        """
        Initialize a building construction project with additional details.

        :param building_type: Type of building (string)
        """
        super().__init__(name, start_date, end_date, budget)
        self.building_type = building_type  # Example: Residential, Commercial, Industrial

    def __str__(self):
        """
        String representation of the building construction project details.
        """
        return super().__str__() + f"\nBuilding Type: {self.building_type}"


class RenovationWorks(Project):
    """
    Represents a renovation works project.
    """

    def __init__(self, name, start_date, end_date, budget, renovation_area):
        """
        Initialize a renovation works project with additional details.

        :param renovation_area: Area of renovation (string)
        """
        super().__init__(name, start_date, end_date, budget)
        self.renovation_area = renovation_area  # Example: Kitchen, Bathroom, Office Space

    def __str__(self):
        """
        String representation of the renovation works project details.
        """
        return super().__str__() + f"\nRenovation Area: {self.renovation_area}"


class FitOutWorks(Project):
    """
    Represents a fit-out works project.
    """

    def __init__(self, name, start_date, end_date, budget, fit_out_scope):
        """
        Initialize a fit-out works project with additional details.

        :param fit_out_scope: Scope of the fit-out (string)
        """
        super().__init__(name, start_date, end_date, budget)
        self.fit_out_scope = fit_out_scope  # Example: Interior Design, Furniture Installation

    def __str__(self):
        """
        String representation of the fit-out works project details.
        """
        return super().__str__() + f"\nFit-Out Scope: {self.fit_out_scope}"


def create_project(project_type, name, start_date, end_date, budget, extra_detail):
    """
    Factory function to create a project based on its type.

    :param project_type: Type of project ('BuildingConstruction', 'RenovationWorks', 'FitOutWorks')
    :param name: Name of the project
    :param start_date: Project start date (datetime object)
    :param end_date: Project end date (datetime object)
    :param budget: Budget allocated for the project (float)
    :param extra_detail: Additional detail required for the specific project type
    :return: An instance of the appropriate project class
    """
    if project_type == "BuildingConstruction":
        return BuildingConstruction(name, start_date, end_date, budget, extra_detail)
    elif project_type == "RenovationWorks":
        return RenovationWorks(name, start_date, end_date, budget, extra_detail)
    elif project_type == "FitOutWorks":
        return FitOutWorks(name, start_date, end_date, budget, extra_detail)
    else:
        raise ValueError("Invalid project type. Use 'BuildingConstruction', 'RenovationWorks', or 'FitOutWorks'.")


# Example usage:
if __name__ == "__main__":
    try:
        # Create a building construction project
        bc_project = create_project(
            "BuildingConstruction",
            "Skyscraper Construction",
            datetime.datetime(2023, 1, 1),
            datetime.datetime(2024, 12, 31),
            5000000.0,
            "Commercial"
        )
        print(bc_project)

        # Create a renovation works project
        rw_project = create_project(
            "RenovationWorks",
            "Office Renovation",
            datetime.datetime(2023, 5, 1),
            datetime.datetime(2023, 8, 31),
            200000.0,
            "Office Space"
        )
        print(rw_project)

        # Create a fit-out works project
        fo_project = create_project(
            "FitOutWorks",
            "Corporate Interior Design",
            datetime.datetime(2023, 3, 1),
            datetime.datetime(2023, 6, 30),
            150000.0,
            "Interior Design"
        )
        print(fo_project)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
