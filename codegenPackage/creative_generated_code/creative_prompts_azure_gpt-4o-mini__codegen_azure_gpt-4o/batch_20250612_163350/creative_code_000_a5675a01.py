"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greencreditbuilder.com
Prompt: How can I use climate-positive activities to improve my credit score with Green Credit Builder?
Generated: DETERMINISTIC_a5675a01651ca792
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GreenCreditBuilder:
    """
    GreenCreditBuilder simulates tracking climate-positive activities and improving credit score
    based on those activities.
    """
    def __init__(self, user_name):
        """
        Initialize the GreenCreditBuilder for a user.
        
        :param user_name: Name of the user
        """
        self.user_name = user_name
        self.credit_score = 650  # Default starting credit score
        self.activities = []  # List to store climate-positive activities
    
    def add_activity(self, activity_name, points):
        """
        Add a climate-positive activity and update the credit score.
        
        :param activity_name: Name of the climate-positive activity
        :param points: Positive impact points contributed by the activity
        :raises ValueError: If points are not positive integers
        """
        if not isinstance(points, int) or points <= 0:
            raise ValueError("Points must be a positive integer.")
        
        self.activities.append({"activity": activity_name, "points": points})
        self.credit_score += points  # Increment credit score based on activity points
    
    def get_credit_score(self):
        """
        Retrieve the current credit score.
        
        :return: Current credit score
        """
        return self.credit_score
    
    def get_activities(self):
        """
        Retrieve the list of tracked climate-positive activities.
        
        :return: List of activities and their points
        """
        return self.activities
    
    def display_summary(self):
        """
        Display a detailed summary of activities and current credit score.
        """
        print(f"User: {self.user_name}")
        print(f"Current Credit Score: {self.credit_score}")
        print("Climate-Positive Activities:")
        for activity in self.activities:
            print(f"  - {activity['activity']} ({activity['points']} points)")


# Example usage:
if __name__ == "__main__":
    try:
        # Create a GreenCreditBuilder for the user
        user = GreenCreditBuilder("John Doe")
        
        # Add climate-positive activities and track the impact
        user.add_activity("Planted Trees", 20)
        user.add_activity("Used Public Transport", 10)
        user.add_activity("Installed Solar Panels", 50)
        
        # Display summary
        user.display_summary()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
