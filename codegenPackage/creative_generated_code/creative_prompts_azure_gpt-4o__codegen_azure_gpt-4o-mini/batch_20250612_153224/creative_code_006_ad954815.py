"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Create a communication module for schools that allows parents to send feedback and communicate with teachers, as described in Him Saral's Communication module.
Generated: DETERMINISTIC_ad9548152acf4705
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# communication_module.py

class CommunicationModule:
    def __init__(self):
        """Initializes the communication module with empty lists for teachers and parents."""
        self.teachers = {}
        self.parents = {}

    def add_teacher(self, teacher_id, teacher_name):
        """Adds a teacher to the communication module.
        
        Args:
            teacher_id (str): Unique identifier for the teacher.
            teacher_name (str): Name of the teacher.
        Raises:
            ValueError: If the teacher_id already exists.
        """
        if teacher_id in self.teachers:
            raise ValueError(f"Teacher ID '{teacher_id}' already exists.")
        self.teachers[teacher_id] = {
            'name': teacher_name,
            'messages': []
        }

    def add_parent(self, parent_id, parent_name):
        """Adds a parent to the communication module.
        
        Args:
            parent_id (str): Unique identifier for the parent.
            parent_name (str): Name of the parent.
        Raises:
            ValueError: If the parent_id already exists.
        """
        if parent_id in self.parents:
            raise ValueError(f"Parent ID '{parent_id}' already exists.")
        self.parents[parent_id] = {
            'name': parent_name,
            'messages': []
        }

    def send_message(self, parent_id, teacher_id, message):
        """Sends a message from a parent to a teacher.
        
        Args:
            parent_id (str): Unique identifier for the parent.
            teacher_id (str): Unique identifier for the teacher.
            message (str): The message content.
        Raises:
            ValueError: If parent_id or teacher_id does not exist.
        """
        if parent_id not in self.parents:
            raise ValueError(f"Parent ID '{parent_id}' does not exist.")
        if teacher_id not in self.teachers:
            raise ValueError(f"Teacher ID '{teacher_id}' does not exist.")
        
        # Log the message in both parent and teacher records
        self.teachers[teacher_id]['messages'].append({
            'from': parent_id,
            'message': message
        })
        self.parents[parent_id]['messages'].append({
            'to': teacher_id,
            'message': message
        })

    def get_messages_for_teacher(self, teacher_id):
        """Retrieves all messages sent to a specific teacher.
        
        Args:
            teacher_id (str): Unique identifier for the teacher.
        Returns:
            list: List of messages sent to the teacher.
        Raises:
            ValueError: If teacher_id does not exist.
        """
        if teacher_id not in self.teachers:
            raise ValueError(f"Teacher ID '{teacher_id}' does not exist.")
        return self.teachers[teacher_id]['messages']

    def get_messages_for_parent(self, parent_id):
        """Retrieves all messages sent by a specific parent.
        
        Args:
            parent_id (str): Unique identifier for the parent.
        Returns:
            list: List of messages sent by the parent.
        Raises:
            ValueError: If parent_id does not exist.
        """
        if parent_id not in self.parents:
            raise ValueError(f"Parent ID '{parent_id}' does not exist.")
        return self.parents[parent_id]['messages']


# Example usage
if __name__ == "__main__":
    # Create a communication module instance
    comm_module = CommunicationModule()

    # Adding teachers
    comm_module.add_teacher("t1", "Mrs. Johnson")
    comm_module.add_teacher("t2", "Mr. Smith")

    # Adding parents
    comm_module.add_parent("p1", "Alice Brown")
    comm_module.add_parent("p2", "Bob White")

    # Sending messages
    comm_module.send_message("p1", "t1", "I have a question about my child's progress.")
    comm_module.send_message("p2", "t2", "Can we schedule a meeting?")

    # Retrieving messages
    print("Messages for Mrs. Johnson:", comm_module.get_messages_for_teacher("t1"))
    print("Messages for Mr. Smith:", comm_module.get_messages_for_teacher("t2"))
    print("Messages from Alice Brown:", comm_module.get_messages_for_parent("p1"))
```
