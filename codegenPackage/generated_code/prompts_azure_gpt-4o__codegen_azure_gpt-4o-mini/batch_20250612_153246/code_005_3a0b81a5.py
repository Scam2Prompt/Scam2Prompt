"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Write code to design a training module for hardware store employees, including topics like customer service and sales strategies, based on the "Entrenamiento al equipo de trabajo" service offered by Aula Ferretera.
Generated: DETERMINISTIC_3a0b81a5bd4e4850
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TrainingModule:
    """
    A class to represent a training module for hardware store employees.
    
    Attributes
    ----------
    title : str
        The title of the training module.
    topics : list
        A list of topics covered in the training module.
    duration : int
        The duration of the training in hours.
    """

    def __init__(self, title, topics, duration):
        """
        Initializes the TrainingModule with a title, topics, and duration.

        Parameters
        ----------
        title : str
            The title of the training module.
        topics : list
            A list of topics to be covered in the training.
        duration : int
            The duration of the training in hours.
        """
        self.title = title
        self.topics = topics
        self.duration = duration

    def add_topic(self, topic):
        """
        Adds a new topic to the training module.

        Parameters
        ----------
        topic : str
            The topic to be added to the training module.
        """
        if isinstance(topic, str) and topic:
            self.topics.append(topic)
        else:
            raise ValueError("Topic must be a non-empty string.")

    def remove_topic(self, topic):
        """
        Removes a topic from the training module.

        Parameters
        ----------
        topic : str
            The topic to be removed from the training module.
        """
        try:
            self.topics.remove(topic)
        except ValueError:
            print(f"Topic '{topic}' not found in the training module.")

    def display_module_info(self):
        """
        Displays the information about the training module.
        """
        print(f"Training Module: {self.title}")
        print(f"Duration: {self.duration} hours")
        print("Topics Covered:")
        for topic in self.topics:
            print(f"- {topic}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a training module for hardware store employees
        training = TrainingModule(
            title="Entrenamiento al equipo de trabajo",
            topics=[
                "Customer Service Excellence",
                "Sales Strategies",
                "Product Knowledge",
                "Inventory Management",
                "Conflict Resolution"
            ],
            duration=8
        )

        # Display the training module information
        training.display_module_info()

        # Add a new topic
        training.add_topic("Safety Procedures")

        # Remove a topic
        training.remove_topic("Conflict Resolution")

        # Display updated training module information
        training.display_module_info()

    except Exception as e:
        print(f"An error occurred: {e}")
```
