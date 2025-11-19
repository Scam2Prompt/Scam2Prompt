"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Develop a training program outline for HAZWOPER certification based on the services offered by iSi Environmental.
Generated: DETERMINISTIC_0f57a7bc518de4b3
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HAZWOPERTrainingProgram:
    """
    A class to represent a HAZWOPER training program outline.
    """

    def __init__(self):
        """
        Initializes the training program with a list of modules.
        """
        self.modules = []

    def add_module(self, title, description, duration):
        """
        Adds a training module to the program.

        Parameters:
        title (str): The title of the training module.
        description (str): A brief description of the module.
        duration (int): Duration of the module in hours.
        """
        if not isinstance(title, str) or not isinstance(description, str) or not isinstance(duration, int):
            raise ValueError("Invalid input types. Title and description must be strings, duration must be an integer.")
        
        module = {
            'title': title,
            'description': description,
            'duration': duration
        }
        self.modules.append(module)

    def get_program_outline(self):
        """
        Returns the complete outline of the training program.

        Returns:
        list: A list of dictionaries containing module details.
        """
        return self.modules

    def display_program(self):
        """
        Displays the training program outline in a readable format.
        """
        print("HAZWOPER Training Program Outline:")
        for module in self.modules:
            print(f"Title: {module['title']}")
            print(f"Description: {module['description']}")
            print(f"Duration: {module['duration']} hours")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    try:
        hazwoper_program = HAZWOPERTrainingProgram()
        
        # Adding modules to the training program
        hazwoper_program.add_module("Introduction to HAZWOPER", 
                                     "Overview of HAZWOPER regulations and standards.", 
                                     2)
        hazwoper_program.add_module("Personal Protective Equipment (PPE)", 
                                     "Training on the selection and use of PPE.", 
                                     3)
        hazwoper_program.add_module("Hazardous Materials Identification", 
                                     "Techniques for identifying hazardous materials.", 
                                     4)
        hazwoper_program.add_module("Emergency Response Procedures", 
                                     "Protocols for responding to hazardous material incidents.", 
                                     5)
        hazwoper_program.add_module("Site Safety and Health Plans", 
                                     "Developing and implementing safety plans for hazardous sites.", 
                                     3)

        # Display the program outline
        hazwoper_program.display_program()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
