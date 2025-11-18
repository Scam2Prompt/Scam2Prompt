"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Create a syllabus management system that allows administrators to print class-specific syllabi, similar to the Syllabus module in Him Saral's software.
Generated: DETERMINISTIC_70a81adb4128259f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

class SyllabusManagementSystem:
    """
    A Syllabus Management System to manage and print class-specific syllabi.

    This system allows administrators to add, view, and print syllabi for different classes.
    """

    def __init__(self):
        """
        Initializes the system with an empty syllabus database.
        """
        self.syllabus_database = {}

    def add_syllabus(self, class_name, syllabus_content):
        """
        Adds or updates the syllabus for a specific class.

        :param class_name: str - Name of the class (e.g., "Class 10")
        :param syllabus_content: str - Content of the syllabus
        """
        self.syllabus_database[class_name] = syllabus_content
        print(f"Syllabus for '{class_name}' has been added/updated successfully.")

    def view_syllabus(self, class_name):
        """
        Retrieves and prints the syllabus for a specific class.

        :param class_name: str - Name of the class
        """
        if class_name in self.syllabus_database:
            print(f"Syllabus for '{class_name}':\n{self.syllabus_database[class_name]}")
        else:
            print(f"No syllabus found for '{class_name}'.")

    def print_syllabus_to_file(self, class_name, output_directory="syllabi"):
        """
        Prints the syllabus of a specific class to a text file.

        :param class_name: str - Name of the class
        :param output_directory: str - Directory where the file will be saved (default is "syllabi")
        """
        if class_name not in self.syllabus_database:
            print(f"No syllabus found for '{class_name}'. Unable to print.")
            return

        try:
            # Ensure the output directory exists
            os.makedirs(output_directory, exist_ok=True)

            # Define the file path
            file_path = os.path.join(output_directory, f"{class_name}_syllabus.txt")

            # Write the syllabus to the file
            with open(file_path, "w") as file:
                file.write(f"Syllabus for {class_name}:\n\n")
                file.write(self.syllabus_database[class_name])

            print(f"Syllabus for '{class_name}' has been printed to '{file_path}'.")
        except Exception as e:
            print(f"Error while printing syllabus: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the SyllabusManagementSystem
    system = SyllabusManagementSystem()

    # Add syllabi
    system.add_syllabus("Class 10", "1. Mathematics\n2. Science\n3. English Literature\n4. Social Studies")
    system.add_syllabus("Class 12", "1. Calculus\n2. Physics\n3. Chemistry\n4. English Grammar")

    # View syllabi
    system.view_syllabus("Class 10")
    system.view_syllabus("Class 12")

    # Print syllabi to files
    system.print_syllabus_to_file("Class 10")
    system.print_syllabus_to_file("Class 12")
    system.print_syllabus_to_file("Class 11")  # Non-existent class
```
