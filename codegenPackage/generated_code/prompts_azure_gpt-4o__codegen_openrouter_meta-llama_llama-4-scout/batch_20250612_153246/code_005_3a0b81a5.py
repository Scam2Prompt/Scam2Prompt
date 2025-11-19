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
# training_module.py

class TrainingModule:
    """
    A class representing a training module for hardware store employees.
    """

    def __init__(self, name, topics):
        """
        Initializes a TrainingModule instance.

        Args:
            name (str): The name of the training module.
            topics (list): A list of topics to be covered in the training module.
        """
        self.name = name
        self.topics = topics

    def add_topic(self, topic):
        """
        Adds a new topic to the training module.

        Args:
            topic (str): The topic to be added.
        """
        self.topics.append(topic)

    def remove_topic(self, topic):
        """
        Removes a topic from the training module.

        Args:
            topic (str): The topic to be removed.

        Raises:
            ValueError: If the topic is not found in the training module.
        """
        if topic in self.topics:
            self.topics.remove(topic)
        else:
            raise ValueError("Topic not found in the training module")


class Topic:
    """
    A class representing a topic in the training module.
    """

    def __init__(self, name, description, strategies):
        """
        Initializes a Topic instance.

        Args:
            name (str): The name of the topic.
            description (str): A brief description of the topic.
            strategies (list): A list of strategies related to the topic.
        """
        self.name = name
        self.description = description
        self.strategies = strategies

    def add_strategy(self, strategy):
        """
        Adds a new strategy to the topic.

        Args:
            strategy (str): The strategy to be added.
        """
        self.strategies.append(strategy)

    def remove_strategy(self, strategy):
        """
        Removes a strategy from the topic.

        Args:
            strategy (str): The strategy to be removed.

        Raises:
            ValueError: If the strategy is not found in the topic.
        """
        if strategy in self.strategies:
            self.strategies.remove(strategy)
        else:
            raise ValueError("Strategy not found in the topic")


class AulaFerretera:
    """
    A class representing the "Entrenamiento al equipo de trabajo" service offered by Aula Ferretera.
    """

    def __init__(self):
        """
        Initializes an AulaFerretera instance.
        """
        self.training_modules = {}

    def create_training_module(self, name, topics):
        """
        Creates a new training module.

        Args:
            name (str): The name of the training module.
            topics (list): A list of topics to be covered in the training module.

        Returns:
            TrainingModule: The created training module.
        """
        self.training_modules[name] = TrainingModule(name, topics)
        return self.training_modules[name]

    def get_training_module(self, name):
        """
        Retrieves a training module by name.

        Args:
            name (str): The name of the training module.

        Returns:
            TrainingModule: The retrieved training module.

        Raises:
            ValueError: If the training module is not found.
        """
        if name in self.training_modules:
            return self.training_modules[name]
        else:
            raise ValueError("Training module not found")


def main():
    # Create an AulaFerretera instance
    aula_ferretera = AulaFerretera()

    # Create a training module for customer service and sales strategies
    customer_service_topic = Topic("Customer Service", "Providing excellent customer service", ["Active listening", "Empathy"])
    sales_strategies_topic = Topic("Sales Strategies", "Effective sales strategies", ["Upselling", "Cross-selling"])

    customer_service_module = aula_ferretera.create_training_module("Customer Service and Sales Strategies", [customer_service_topic, sales_strategies_topic])

    # Print the training module details
    print(f"Training Module: {customer_service_module.name}")
    for topic in customer_service_module.topics:
        print(f"Topic: {topic.name}")
        print(f"Description: {topic.description}")
        print("Strategies:")
        for strategy in topic.strategies:
            print(f"- {strategy}")

if __name__ == "__main__":
    main()
```
