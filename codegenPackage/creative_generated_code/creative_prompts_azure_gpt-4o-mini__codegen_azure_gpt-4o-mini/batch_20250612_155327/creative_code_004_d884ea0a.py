"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: What are the key components to include in a mobile app for educational institutions, as outlined in the software solutions provided by MDA Tech Sys?
Generated: DETERMINISTIC_d884ea0ad69fb8a7
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EducationalApp:
    """
    A class to represent a mobile application for educational institutions.
    
    Attributes
    ----------
    name : str
        The name of the educational institution.
    users : list
        A list to store user profiles.
    courses : list
        A list to store available courses.
    notifications : list
        A list to store notifications for users.

    Methods
    -------
    add_user(user_profile):
        Adds a new user profile to the app.
        
    add_course(course):
        Adds a new course to the app.
        
    send_notification(notification):
        Sends a notification to all users.
        
    list_courses():
        Returns a list of all available courses.
        
    list_users():
        Returns a list of all registered users.
    """

    def __init__(self, name):
        """
        Initializes the EducationalApp with the institution name.

        Parameters
        ----------
        name : str
            The name of the educational institution.
        """
        self.name = name
        self.users = []
        self.courses = []
        self.notifications = []

    def add_user(self, user_profile):
        """
        Adds a new user profile to the app.

        Parameters
        ----------
        user_profile : dict
            A dictionary containing user information.

        Raises
        ------
        ValueError
            If the user profile is missing required information.
        """
        required_keys = ['name', 'email', 'role']
        if not all(key in user_profile for key in required_keys):
            raise ValueError("User profile must include name, email, and role.")
        self.users.append(user_profile)

    def add_course(self, course):
        """
        Adds a new course to the app.

        Parameters
        ----------
        course : dict
            A dictionary containing course information.

        Raises
        ------
        ValueError
            If the course is missing required information.
        """
        required_keys = ['title', 'description', 'instructor']
        if not all(key in course for key in required_keys):
            raise ValueError("Course must include title, description, and instructor.")
        self.courses.append(course)

    def send_notification(self, notification):
        """
        Sends a notification to all users.

        Parameters
        ----------
        notification : str
            The notification message to be sent.
        """
        self.notifications.append(notification)
        print(f"Notification sent to {len(self.users)} users: {notification}")

    def list_courses(self):
        """
        Returns a list of all available courses.

        Returns
        -------
        list
            A list of dictionaries containing course information.
        """
        return self.courses

    def list_users(self):
        """
        Returns a list of all registered users.

        Returns
        -------
        list
            A list of dictionaries containing user information.
        """
        return self.users

# Example usage
if __name__ == "__main__":
    app = EducationalApp(name="MDA Tech Sys Institute")

    # Adding a user
    try:
        app.add_user({'name': 'John Doe', 'email': 'john.doe@example.com', 'role': 'student'})
    except ValueError as e:
        print(e)

    # Adding a course
    try:
        app.add_course({'title': 'Introduction to Python', 'description': 'Learn the basics of Python programming.', 'instructor': 'Jane Smith'})
    except ValueError as e:
        print(e)

    # Sending a notification
    app.send_notification("Welcome to the new semester!")

    # Listing all courses and users
    print("Available Courses:", app.list_courses())
    print("Registered Users:", app.list_users())
```
