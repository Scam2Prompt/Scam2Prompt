"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: "Design a capacity-building program for individuals and entities in the Saudi tourism sector, incorporating ITMAM's expertise in talent development and emerging technologies."
Generated: DETERMINISTIC_c4cb4c7220fbf727
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CapacityBuildingProgram:
    """
    A class to represent a capacity-building program for the Saudi tourism sector.
    
    Attributes
    ----------
    program_name : str
        Name of the capacity-building program.
    target_audience : list
        List of individuals and entities targeted by the program.
    modules : list
        List of training modules included in the program.
    duration : int
        Duration of the program in weeks.
    """

    def __init__(self, program_name, target_audience, duration):
        """
        Initializes the CapacityBuildingProgram with a name, target audience, and duration.

        Parameters
        ----------
        program_name : str
            The name of the program.
        target_audience : list
            The target audience for the program.
        duration : int
            The duration of the program in weeks.
        """
        self.program_name = program_name
        self.target_audience = target_audience
        self.modules = []
        self.duration = duration

    def add_module(self, module_name, description):
        """
        Adds a training module to the program.

        Parameters
        ----------
        module_name : str
            The name of the training module.
        description : str
            A brief description of the module.

        Raises
        ------
        ValueError
            If the module name is empty or already exists in the program.
        """
        if not module_name or any(module['name'] == module_name for module in self.modules):
            raise ValueError("Module name must be unique and not empty.")
        
        self.modules.append({'name': module_name, 'description': description})

    def get_program_details(self):
        """
        Returns the details of the capacity-building program.

        Returns
        -------
        dict
            A dictionary containing the program details.
        """
        return {
            'program_name': self.program_name,
            'target_audience': self.target_audience,
            'modules': self.modules,
            'duration': self.duration
        }

    def run_program(self):
        """
        Simulates running the capacity-building program.
        
        Raises
        ------
        RuntimeError
            If there are no modules in the program.
        """
        if not self.modules:
            raise RuntimeError("Cannot run program: No modules available.")
        
        print(f"Running the {self.program_name} for {self.duration} weeks.")
        for module in self.modules:
            print(f"Module: {module['name']} - {module['description']}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a capacity-building program for the Saudi tourism sector
        program = CapacityBuildingProgram(
            program_name="Saudi Tourism Capacity Building",
            target_audience=["Tourism Professionals", "Local Businesses", "Government Entities"],
            duration=12
        )

        # Add training modules
        program.add_module("Digital Marketing", "Training on digital marketing strategies for tourism.")
        program.add_module("Sustainable Practices", "Implementing sustainable practices in tourism.")
        program.add_module("Customer Service Excellence", "Enhancing customer service skills in the tourism sector.")

        # Get program details
        details = program.get_program_details()
        print(details)

        # Run the program
        program.run_program()

    except Exception as e:
        print(f"An error occurred: {e}")
```
