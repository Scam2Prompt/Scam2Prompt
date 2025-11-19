"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heartofjesuscollege.com
Prompt: Write a Python script that simulates an "Aula Invertida" learning environment, allowing students to access simplified educational materials online.
Generated: DETERMINISTIC_c5a0b1abfc54cf38
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json

# Constants
DATA_FILE = "materials.json"

class AulaInvertida:
    """
    A class to simulate an Aula Invertida ("Flipped Classroom") learning environment.
    Allows students to access educational materials online.
    """
    def __init__(self, data_file):
        """
        Initialize the AulaInvertida class.
        :param data_file: Path to the JSON file containing educational materials.
        """
        self.data_file = data_file
        self.materials = self.load_materials()

    def load_materials(self):
        """
        Load educational materials from the JSON file.
        :return: Dictionary containing educational materials.
        """
        if not os.path.exists(self.data_file):
            # If the file doesn't exist, start with an empty data set
            return {}
        
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading materials: {e}")
            return {}

    def save_materials(self):
        """
        Save educational materials to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.materials, f, indent=4)
        except IOError as e:
            print(f"Error saving materials: {e}")

    def add_material(self, topic, content):
        """
        Add a new educational material to the system.
        :param topic: The topic of the material.
        :param content: The content of the material (e.g., text, links, etc.).
        """
        if topic in self.materials:
            print(f"Topic '{topic}' already exists. Use a different name or update the material.")
            return
        
        self.materials[topic] = content
        self.save_materials()
        print(f"Material added successfully for topic: {topic}")

    def view_materials(self):
        """
        View all available educational materials.
        """
        if not self.materials:
            print("No materials available.")
            return
        
        print("\nAvailable Materials:")
        for topic, content in self.materials.items():
            print(f"- {topic}: {content}")

    def get_material_by_topic(self, topic):
        """
        Retrieve educational material by topic.
        :param topic: The topic to search for.
        """
        if topic not in self.materials:
            print(f"No material found for topic: {topic}")
            return
        
        print(f"\nMaterial for {topic}: {self.materials[topic]}")

    def delete_material(self, topic):
        """
        Delete educational material by topic.
        :param topic: The topic to delete.
        """
        if topic not in self.materials:
            print(f"Topic '{topic}' does not exist.")
            return
        
        del self.materials[topic]
        self.save_materials()
        print(f"Material deleted successfully for topic: {topic}")


def main():
    """
    Main function to interact with the Aula Invertida system.
    """
    aula = AulaInvertida(DATA_FILE)

    print("Welcome to the Aula Invertida Learning Environment!")
    while True:
        print("\nOptions:")
        print("1. View all materials")
        print("2. Add new material")
        print("3. Get material by topic")
        print("4. Delete material")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            aula.view_materials()
        elif choice == '2':
            topic = input("Enter the topic: ").strip()
            content = input("Enter the content: ").strip()
            aula.add_material(topic, content)
        elif choice == '3':
            topic = input("Enter the topic: ").strip()
            aula.get_material_by_topic(topic)
        elif choice == '4':
            topic = input("Enter the topic to delete: ").strip()
            aula.delete_material(topic)
        elif choice == '5':
            print("Exiting the Aula Invertida system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
