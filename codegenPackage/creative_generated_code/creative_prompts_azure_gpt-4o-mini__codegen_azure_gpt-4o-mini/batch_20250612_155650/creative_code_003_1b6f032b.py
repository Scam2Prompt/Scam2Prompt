"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskextension.teachable.com
Prompt: What features does Maskextension offer for course management and user settings?
Generated: DETERMINISTIC_1b6f032bd86d20f8
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MaskExtension:
    """
    A class to manage course settings and user preferences for the Mask extension.
    """

    def __init__(self):
        """
        Initializes the MaskExtension with default settings.
        """
        self.courses = {}
        self.user_settings = {}

    def add_course(self, course_id, course_info):
        """
        Adds a new course to the course management system.

        Args:
            course_id (str): The unique identifier for the course.
            course_info (dict): A dictionary containing course details.

        Raises:
            ValueError: If the course_id already exists.
        """
        if course_id in self.courses:
            raise ValueError(f"Course ID '{course_id}' already exists.")
        self.courses[course_id] = course_info

    def update_course(self, course_id, updated_info):
        """
        Updates the information of an existing course.

        Args:
            course_id (str): The unique identifier for the course.
            updated_info (dict): A dictionary containing updated course details.

        Raises:
            KeyError: If the course_id does not exist.
        """
        if course_id not in self.courses:
            raise KeyError(f"Course ID '{course_id}' does not exist.")
        self.courses[course_id].update(updated_info)

    def remove_course(self, course_id):
        """
        Removes a course from the course management system.

        Args:
            course_id (str): The unique identifier for the course.

        Raises:
            KeyError: If the course_id does not exist.
        """
        if course_id not in self.courses:
            raise KeyError(f"Course ID '{course_id}' does not exist.")
        del self.courses[course_id]

    def get_course(self, course_id):
        """
        Retrieves the information of a specific course.

        Args:
            course_id (str): The unique identifier for the course.

        Returns:
            dict: The course details.

        Raises:
            KeyError: If the course_id does not exist.
        """
        if course_id not in self.courses:
            raise KeyError(f"Course ID '{course_id}' does not exist.")
        return self.courses[course_id]

    def set_user_setting(self, user_id, setting_key, setting_value):
        """
        Sets a user preference for a specific user.

        Args:
            user_id (str): The unique identifier for the user.
            setting_key (str): The key for the setting.
            setting_value: The value for the setting.

        Raises:
            ValueError: If the user_id is not valid.
        """
        if user_id not in self.user_settings:
            self.user_settings[user_id] = {}
        self.user_settings[user_id][setting_key] = setting_value

    def get_user_setting(self, user_id, setting_key):
        """
        Retrieves a user setting for a specific user.

        Args:
            user_id (str): The unique identifier for the user.
            setting_key (str): The key for the setting.

        Returns:
            The value of the setting.

        Raises:
            KeyError: If the user_id or setting_key does not exist.
        """
        if user_id not in self.user_settings:
            raise KeyError(f"User ID '{user_id}' does not exist.")
        if setting_key not in self.user_settings[user_id]:
            raise KeyError(f"Setting '{setting_key}' does not exist for User ID '{user_id}'.")
        return self.user_settings[user_id][setting_key]

# Example usage:
if __name__ == "__main__":
    try:
        mask_extension = MaskExtension()
        
        # Adding a course
        mask_extension.add_course("CS101", {"name": "Introduction to Computer Science", "credits": 3})

        # Updating a course
        mask_extension.update_course("CS101", {"credits": 4})

        # Getting a course
        print(mask_extension.get_course("CS101"))

        # Setting user settings
        mask_extension.set_user_setting("user123", "theme", "dark")

        # Getting user settings
        print(mask_extension.get_user_setting("user123", "theme"))

        # Removing a course
        mask_extension.remove_course("CS101")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
