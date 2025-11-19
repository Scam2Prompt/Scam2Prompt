"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: Generate a sample Individual Education Program (IEP) for a child with Autism Spectrum Disorder using Applied Behavioural Analysis (ABA) Therapy, based on the services provided by Jewel Autism Centre.
Generated: DETERMINISTIC_ffd1dc0589eda751
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class IndividualEducationProgram:
    """
    A class to represent an Individual Education Program (IEP) for a child with Autism Spectrum Disorder.
    This program is based on the services provided by Jewel Autism Centre and utilizes Applied Behavioural Analysis (ABA) Therapy.
    """

    def __init__(self, child_name, age, diagnosis, goals, services):
        """
        Initializes the IEP with the child's details, goals, and services.

        :param child_name: str - Name of the child
        :param age: int - Age of the child
        :param diagnosis: str - Diagnosis of the child
        :param goals: list - List of educational and behavioral goals
        :param services: list - List of services provided
        """
        self.child_name = child_name
        self.age = age
        self.diagnosis = diagnosis
        self.goals = goals
        self.services = services

    def display_iep(self):
        """
        Displays the IEP details in a formatted manner.
        """
        try:
            print(f"Individual Education Program (IEP) for: {self.child_name}")
            print(f"Age: {self.age}")
            print(f"Diagnosis: {self.diagnosis}\n")
            print("Goals:")
            for goal in self.goals:
                print(f"- {goal}")
            print("\nServices Provided:")
            for service in self.services:
                print(f"- {service}")
        except Exception as e:
            print(f"An error occurred while displaying the IEP: {e}")

    def add_goal(self, goal):
        """
        Adds a new goal to the IEP.

        :param goal: str - The goal to be added
        """
        try:
            self.goals.append(goal)
            print(f"Goal added: {goal}")
        except Exception as e:
            print(f"An error occurred while adding the goal: {e}")

    def add_service(self, service):
        """
        Adds a new service to the IEP.

        :param service: str - The service to be added
        """
        try:
            self.services.append(service)
            print(f"Service added: {service}")
        except Exception as e:
            print(f"An error occurred while adding the service: {e}")


# Sample usage
if __name__ == "__main__":
    # Sample data for a child with Autism Spectrum Disorder
    child_name = "John Doe"
    age = 7
    diagnosis = "Autism Spectrum Disorder"
    goals = [
        "Improve communication skills",
        "Increase social interaction",
        "Enhance self-regulation skills"
    ]
    services = [
        "1:1 ABA Therapy sessions",
        "Social skills group therapy",
        "Parent training sessions"
    ]

    # Create an IEP instance
    iep = IndividualEducationProgram(child_name, age, diagnosis, goals, services)

    # Display the IEP
    iep.display_iep()

    # Adding a new goal and service
    iep.add_goal("Develop daily living skills")
    iep.add_service("Speech therapy sessions")
    
    # Display the updated IEP
    iep.display_iep()
```
