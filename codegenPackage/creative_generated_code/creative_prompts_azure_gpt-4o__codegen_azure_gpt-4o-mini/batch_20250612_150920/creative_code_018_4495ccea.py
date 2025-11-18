"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Provide an example of a coaching session plan for personal development, referencing the "Biti coach" program on edukacija.net.
Generated: DETERMINISTIC_4495ccea25b824a2
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CoachingSession:
    """
    A class to represent a coaching session for personal development.
    
    Attributes:
        session_title (str): Title of the coaching session.
        objectives (list): List of objectives to achieve in the session.
        duration (int): Duration of the session in minutes.
        materials (list): List of materials needed for the session.
    """
    
    def __init__(self, session_title, objectives, duration, materials):
        """
        Initializes a CoachingSession with the provided title, objectives,
        duration, and materials.
        
        Parameters:
            session_title (str): The title of the session.
            objectives (list): The objectives for the session.
            duration (int): Duration in minutes.
            materials (list): Materials needed for the session.
        """
        self.session_title = session_title
        self.objectives = objectives
        self.duration = duration
        self.materials = materials

    def display_session_plan(self):
        """
        Displays the details of the coaching session plan.
        """
        print(f"Session Title: {self.session_title}")
        print("Objectives:")
        for objective in self.objectives:
            print(f"- {objective}")
        print(f"Duration: {self.duration} minutes")
        print("Materials Needed:")
        for material in self.materials:
            print(f"- {material}")

    def validate_session(self):
        """
        Validates the session details for correctness.
        
        Raises:
            ValueError: If the session duration is not a positive integer.
        """
        if not isinstance(self.duration, int) or self.duration <= 0:
            raise ValueError("Duration must be a positive integer.")

# Example usage
def main():
    try:
        # Define the details of the coaching session
        session_title = "Personal Development Coaching: Biti Coach Program"
        objectives = [
            "Identify personal strengths and weaknesses.",
            "Set actionable personal development goals.",
            "Develop strategies for overcoming obstacles."
        ]
        duration = 60  # in minutes
        materials = [
            "Notebook",
            "Pen",
            "Printed handouts from edukacija.net",
            "Feedback forms"
        ]
        
        # Create a CoachingSession instance
        session = CoachingSession(session_title, objectives, duration, materials)
        
        # Validate the session details
        session.validate_session()
        
        # Display the session plan
        session.display_session_plan()
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
