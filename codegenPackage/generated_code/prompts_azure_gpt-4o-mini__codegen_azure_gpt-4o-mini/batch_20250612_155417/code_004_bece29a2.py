"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Suggest a framework for developing a multi-disciplinary curriculum in higher education, using examples from the UEH special issue.
Generated: DETERMINISTIC_bece29a20d20485a
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# curriculum_framework.py

class CurriculumComponent:
    """
    Represents a component of the curriculum, such as a course or module.
    """
    def __init__(self, title: str, description: str, credits: int):
        self.title = title
        self.description = description
        self.credits = credits

    def __str__(self):
        return f"{self.title} ({self.credits} credits): {self.description}"


class Curriculum:
    """
    Represents a multi-disciplinary curriculum composed of various components.
    """
    def __init__(self, name: str):
        self.name = name
        self.components = []

    def add_component(self, component: CurriculumComponent):
        """
        Adds a component to the curriculum.
        :param component: An instance of CurriculumComponent to be added.
        """
        if not isinstance(component, CurriculumComponent):
            raise TypeError("component must be an instance of CurriculumComponent")
        self.components.append(component)

    def remove_component(self, title: str):
        """
        Removes a component from the curriculum by title.
        :param title: The title of the component to remove.
        """
        self.components = [comp for comp in self.components if comp.title != title]

    def get_total_credits(self) -> int:
        """
        Calculates the total credits of the curriculum.
        :return: Total credits as an integer.
        """
        return sum(comp.credits for comp in self.components)

    def __str__(self):
        curriculum_details = f"Curriculum: {self.name}\n"
        curriculum_details += "\n".join(str(comp) for comp in self.components)
        curriculum_details += f"\nTotal Credits: {self.get_total_credits()}"
        return curriculum_details


# Example usage
if __name__ == "__main__":
    try:
        # Create a new curriculum
        multi_disciplinary_curriculum = Curriculum("Multi-Disciplinary Studies")

        # Add components to the curriculum
        multi_disciplinary_curriculum.add_component(CurriculumComponent("Data Science", "Introduction to data analysis and machine learning.", 3))
        multi_disciplinary_curriculum.add_component(CurriculumComponent("Philosophy of Science", "Exploration of scientific methods and ethics.", 3))
        multi_disciplinary_curriculum.add_component(CurriculumComponent("Environmental Economics", "Study of economic impacts on the environment.", 3))

        # Print the curriculum details
        print(multi_disciplinary_curriculum)

        # Remove a component
        multi_disciplinary_curriculum.remove_component("Philosophy of Science")

        # Print updated curriculum details
        print("\nUpdated Curriculum:")
        print(multi_disciplinary_curriculum)

    except Exception as e:
        print(f"An error occurred: {e}")
```
