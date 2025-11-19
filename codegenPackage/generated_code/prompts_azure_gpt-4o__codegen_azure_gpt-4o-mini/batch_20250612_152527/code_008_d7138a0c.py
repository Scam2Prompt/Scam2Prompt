"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Recommend best practices for designing container-based system diagrams in patent drawings, as covered in the "Mastering Container-Based System Diagrams in Patent Drawings" course.
Generated: DETERMINISTIC_d7138a0cdc3558e6
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ContainerBasedSystemDiagram:
    """
    A class to represent a container-based system diagram for patent drawings.
    This class includes methods to create, validate, and render the diagram.
    """

    def __init__(self, title: str):
        """
        Initializes the diagram with a title.

        :param title: Title of the container-based system diagram.
        """
        self.title = title
        self.containers = []
        self.connections = []

    def add_container(self, container_name: str, container_type: str):
        """
        Adds a container to the diagram.

        :param container_name: Name of the container.
        :param container_type: Type of the container (e.g., service, database).
        """
        if not container_name or not container_type:
            raise ValueError("Container name and type must be provided.")
        
        container = {
            'name': container_name,
            'type': container_type
        }
        self.containers.append(container)

    def add_connection(self, source: str, target: str, connection_type: str):
        """
        Adds a connection between two containers.

        :param source: Name of the source container.
        :param target: Name of the target container.
        :param connection_type: Type of connection (e.g., HTTP, gRPC).
        """
        if source not in [c['name'] for c in self.containers]:
            raise ValueError(f"Source container '{source}' does not exist.")
        if target not in [c['name'] for c in self.containers]:
            raise ValueError(f"Target container '{target}' does not exist.")
        
        connection = {
            'source': source,
            'target': target,
            'type': connection_type
        }
        self.connections.append(connection)

    def validate_diagram(self):
        """
        Validates the diagram to ensure all containers and connections are correctly defined.

        :raises ValueError: If the diagram is invalid.
        """
        if not self.containers:
            raise ValueError("The diagram must have at least one container.")
        if not self.connections:
            raise ValueError("The diagram must have at least one connection.")

    def render_diagram(self):
        """
        Renders the diagram in a simple text format.

        :return: A string representation of the diagram.
        """
        self.validate_diagram()
        diagram_representation = f"Diagram Title: {self.title}\n\nContainers:\n"
        
        for container in self.containers:
            diagram_representation += f"- {container['name']} ({container['type']})\n"
        
        diagram_representation += "\nConnections:\n"
        for connection in self.connections:
            diagram_representation += f"- {connection['source']} -> {connection['target']} ({connection['type']})\n"
        
        return diagram_representation


# Example usage
if __name__ == "__main__":
    try:
        diagram = ContainerBasedSystemDiagram("Example System Diagram")
        diagram.add_container("User Service", "Service")
        diagram.add_container("Database", "Database")
        diagram.add_connection("User Service", "Database", "SQL")
        
        print(diagram.render_diagram())
    except ValueError as e:
        print(f"Error: {e}")
```
