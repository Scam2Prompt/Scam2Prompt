"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Create a detailed plan for a corporate media training program, incorporating Cara Productions' training services to improve media relations skills in Kenya.
Generated: DETERMINISTIC_98e0b5dd8e66b4b8
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MediaTrainingProgram:
    """
    A class to represent a corporate media training program.
    """

    def __init__(self, company_name, location):
        """
        Initializes the MediaTrainingProgram with company name and location.

        :param company_name: Name of the company organizing the training
        :param location: Location where the training will be held
        """
        self.company_name = company_name
        self.location = location
        self.modules = []
        self.participants = []

    def add_module(self, module_name, duration, description):
        """
        Adds a training module to the program.

        :param module_name: Name of the training module
        :param duration: Duration of the module in hours
        :param description: Description of the module content
        """
        module = {
            'name': module_name,
            'duration': duration,
            'description': description
        }
        self.modules.append(module)

    def register_participant(self, participant_name, email):
        """
        Registers a participant for the training program.

        :param participant_name: Name of the participant
        :param email: Email address of the participant
        :raises ValueError: If the email is not valid
        """
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address provided.")
        
        participant = {
            'name': participant_name,
            'email': email
        }
        self.participants.append(participant)

    @staticmethod
    def is_valid_email(email):
        """
        Validates the email format.

        :param email: Email address to validate
        :return: True if valid, False otherwise
        """
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def generate_training_plan(self):
        """
        Generates a detailed training plan.

        :return: A dictionary containing the training plan details
        """
        training_plan = {
            'company_name': self.company_name,
            'location': self.location,
            'modules': self.modules,
            'participants': self.participants
        }
        return training_plan

    def display_training_plan(self):
        """
        Displays the training plan in a readable format.
        """
        plan = self.generate_training_plan()
        print("Training Plan for:", plan['company_name'])
        print("Location:", plan['location'])
        print("\nModules:")
        for module in plan['modules']:
            print(f"- {module['name']} ({module['duration']} hours): {module['description']}")
        
        print("\nParticipants:")
        for participant in plan['participants']:
            print(f"- {participant['name']} ({participant['email']})")


# Example usage
if __name__ == "__main__":
    try:
        training_program = MediaTrainingProgram("Cara Productions", "Nairobi, Kenya")
        
        # Adding training modules
        training_program.add_module("Media Relations Basics", 2, "Introduction to media relations and its importance.")
        training_program.add_module("Crisis Communication", 3, "Strategies for effective communication during a crisis.")
        training_program.add_module("Interview Techniques", 2, "Best practices for handling media interviews.")
        
        # Registering participants
        training_program.register_participant("John Doe", "john.doe@example.com")
        training_program.register_participant("Jane Smith", "jane.smith@example.com")
        
        # Displaying the training plan
        training_program.display_training_plan()
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
