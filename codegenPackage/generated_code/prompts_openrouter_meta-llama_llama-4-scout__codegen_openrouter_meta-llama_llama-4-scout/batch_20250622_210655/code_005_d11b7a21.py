"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: "Design a digital course outline for learning architectural and interior design principles, including topics such as space planning, material selection, and 3D modeling."
Generated: DETERMINISTIC_d11b7a21f2886e9c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_outline.py

class CourseOutline:
    """
    A class representing a digital course outline for learning architectural and interior design principles.
    """

    def __init__(self):
        """
        Initializes a CourseOutline object with a list of topics.
        """
        self.topics = []

    def add_topic(self, topic):
        """
        Adds a topic to the course outline.

        Args:
            topic (Topic): A Topic object representing a topic in the course outline.
        """
        self.topics.append(topic)

    def view_course_outline(self):
        """
        Prints the course outline with all topics and subtopics.
        """
        for i, topic in enumerate(self.topics, start=1):
            print(f"{i}. {topic.name}")
            for j, subtopic in enumerate(topic.subtopics, start=1):
                print(f"  {j}. {subtopic}")


class Topic:
    """
    A class representing a topic in the course outline.
    """

    def __init__(self, name):
        """
        Initializes a Topic object with a name and an empty list of subtopics.

        Args:
            name (str): The name of the topic.
        """
        self.name = name
        self.subtopics = []

    def add_subtopic(self, subtopic):
        """
        Adds a subtopic to the topic.

        Args:
            subtopic (str): A subtopic of the topic.
        """
        self.subtopics.append(subtopic)


def main():
    try:
        # Create a course outline
        course_outline = CourseOutline()

        # Create topics
        space_planning = Topic("Space Planning")
        material_selection = Topic("Material Selection")
        three_d_modeling = Topic("3D Modeling")

        # Add subtopics to topics
        space_planning.add_subtopic("Principles of Space Planning")
        space_planning.add_subtopic("Measuring and Calculating Space")
        space_planning.add_subtopic("Creating a Floor Plan")

        material_selection.add_subtopic("Types of Building Materials")
        material_selection.add_subtopic("Sustainable Materials")
        material_selection.add_subtopic("Material Properties and Applications")

        three_d_modeling.add_subtopic("Introduction to 3D Modeling Software")
        three_d_modeling.add_subtopic("Creating 3D Models")
        three_d_modeling.add_subtopic("Rendering and Visualization")

        # Add topics to course outline
        course_outline.add_topic(space_planning)
        course_outline.add_topic(material_selection)
        course_outline.add_topic(three_d_modeling)

        # View course outline
        course_outline.view_course_outline()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
