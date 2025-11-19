"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: "Develop an IT training program for employees, including topics on cybersecurity, cloud computing, and software development best practices."
Generated: DETERMINISTIC_fbb5fcada4e278f7
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TrainingProgram:
    """
    A class to represent an IT training program for employees.
    """

    def __init__(self):
        """
        Initializes the training program with predefined topics.
        """
        self.topics = {
            "Cybersecurity": [],
            "Cloud Computing": [],
            "Software Development Best Practices": []
        }

    def add_topic(self, category, topic):
        """
        Adds a new topic to a specified category.

        Parameters:
        category (str): The category to which the topic belongs.
        topic (str): The topic to be added.

        Raises:
        ValueError: If the category is not valid.
        """
        if category not in self.topics:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.topics.keys())}")

        self.topics[category].append(topic)

    def remove_topic(self, category, topic):
        """
        Removes a topic from a specified category.

        Parameters:
        category (str): The category from which the topic will be removed.
        topic (str): The topic to be removed.

        Raises:
        ValueError: If the category is not valid or the topic does not exist.
        """
        if category not in self.topics:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.topics.keys())}")

        try:
            self.topics[category].remove(topic)
        except ValueError:
            raise ValueError(f"Topic '{topic}' not found in category '{category}'.")

    def get_topics(self):
        """
        Returns the current topics in the training program.

        Returns:
        dict: A dictionary containing categories and their respective topics.
        """
        return self.topics

    def display_program(self):
        """
        Displays the training program topics in a formatted manner.
        """
        print("IT Training Program Topics:")
        for category, topics in self.topics.items():
            print(f"\n{category}:")
            if topics:
                for topic in topics:
                    print(f" - {topic}")
            else:
                print(" - No topics added yet.")

# Example usage
if __name__ == "__main__":
    try:
        training_program = TrainingProgram()
        training_program.add_topic("Cybersecurity", "Phishing Awareness")
        training_program.add_topic("Cloud Computing", "Introduction to AWS")
        training_program.add_topic("Software Development Best Practices", "Code Review Techniques")

        training_program.display_program()

        # Removing a topic
        training_program.remove_topic("Cybersecurity", "Phishing Awareness")
        training_program.display_program()

    except ValueError as e:
        print(f"Error: {e}")
```
