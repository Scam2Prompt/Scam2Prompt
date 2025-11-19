"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caraproductions.co.ke
Prompt: Create a detailed plan for a corporate media training program, incorporating Cara Productions' training services to improve media relations skills in Kenya.
Generated: DETERMINISTIC_98e0b5dd8e66b4b8
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MediaTrainingProgram:
    """
    A class to represent a corporate media training program.

    Attributes:
    ----------
    company_name : str
        The name of the company offering the training services.
    location : str
        The location where the training will be conducted.
    program_details : dict
        A dictionary containing details about the training program.
    """

    def __init__(self, company_name: str, location: str):
        """
        Initializes the MediaTrainingProgram with company name and location.

        Parameters:
        ----------
        company_name : str
            Name of the training services provider.
        location : str
            Location of the training.
        """
        self.company_name = company_name
        self.location = location
        self.program_details = {
            "objectives": [],
            "modules": [],
            "duration": "",
            "cost": 0.0,
            "participants": []
        }

    def add_objective(self, objective: str):
        """
        Adds an objective to the training program.

        Parameters:
        ----------
        objective : str
            The training objective to be added.
        """
        self.program_details["objectives"].append(objective)

    def add_module(self, module: str):
        """
        Adds a module to the training program.

        Parameters:
        ----------
        module : str
            The training module to be added.
        """
        self.program_details["modules"].append(module)

    def set_duration(self, duration: str):
        """
        Sets the duration of the training program.

        Parameters:
        ----------
        duration : str
            The duration of the training, e.g., '2 days', '1 week'.
        """
        self.program_details["duration"] = duration

    def set_cost(self, cost: float):
        """
        Sets the cost of the training program.

        Parameters:
        ----------
        cost : float
            The cost of the training program.
        """
        if cost < 0:
            raise ValueError("Cost cannot be negative.")
        self.program_details["cost"] = cost

    def add_participant(self, participant: str):
        """
        Adds a participant to the training program.

        Parameters:
        ----------
        participant : str
            The name of the participant to be added.
        """
        self.program_details["participants"].append(participant)

    def generate_plan(self) -> dict:
        """
        Generates the training plan as a dictionary.

        Returns:
        -------
        dict
            A structured overview of the media training program.
        """
        return {
            "company": self.company_name,
            "location": self.location,
            "details": self.program_details
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the media training program
        training_program = MediaTrainingProgram("Cara Productions", "Nairobi, Kenya")

        # Define the training program objectives
        training_program.add_objective("Enhance media relations skills.")
        training_program.add_objective("Improve crisis communication strategies.")
        training_program.add_objective("Develop effective messaging techniques.")

        # Define the training modules
        training_program.add_module("Introduction to Media Relations")
        training_program.add_module("Crisis Management in Media")
        training_program.add_module("Crafting Effective Messages")

        # Set the duration and cost
        training_program.set_duration("3 days")
        training_program.set_cost(1500.00)

        # Add participants
        training_program.add_participant("John Doe")
        training_program.add_participant("Jane Smith")

        # Generate and print the training plan
        plan = training_program.generate_plan()
        print(plan)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
