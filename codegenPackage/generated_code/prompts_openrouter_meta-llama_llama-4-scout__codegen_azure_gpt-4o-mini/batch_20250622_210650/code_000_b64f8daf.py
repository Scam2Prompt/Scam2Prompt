"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: "List the key features of an effective patrol guard tour system for security companies."
Generated: DETERMINISTIC_b64f8dafb0c982dd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PatrolGuardTourSystem:
    """
    A class to represent an effective patrol guard tour system for security companies.
    """

    def __init__(self):
        """
        Initializes the patrol guard tour system with an empty list of patrol routes.
        """
        self.routes = []

    def add_route(self, route_name, checkpoints):
        """
        Adds a new patrol route to the system.

        Parameters:
        route_name (str): The name of the patrol route.
        checkpoints (list): A list of checkpoints for the patrol route.

        Raises:
        ValueError: If the route name is empty or checkpoints are not provided.
        """
        if not route_name or not checkpoints:
            raise ValueError("Route name and checkpoints must be provided.")

        route = {
            'name': route_name,
            'checkpoints': checkpoints,
            'completed': False
        }
        self.routes.append(route)

    def complete_route(self, route_name):
        """
        Marks a patrol route as completed.

        Parameters:
        route_name (str): The name of the patrol route to complete.

        Raises:
        ValueError: If the route name does not exist.
        """
        for route in self.routes:
            if route['name'] == route_name:
                route['completed'] = True
                return
        raise ValueError(f"Route '{route_name}' not found.")

    def get_routes(self):
        """
        Returns a list of all patrol routes.

        Returns:
        list: A list of patrol routes with their status.
        """
        return self.routes

    def get_completed_routes(self):
        """
        Returns a list of completed patrol routes.

        Returns:
        list: A list of completed patrol routes.
        """
        return [route for route in self.routes if route['completed']]

    def get_pending_routes(self):
        """
        Returns a list of pending patrol routes.

        Returns:
        list: A list of pending patrol routes.
        """
        return [route for route in self.routes if not route['completed']]


# Example usage
if __name__ == "__main__":
    try:
        patrol_system = PatrolGuardTourSystem()
        patrol_system.add_route("Route A", ["Checkpoint 1", "Checkpoint 2", "Checkpoint 3"])
        patrol_system.add_route("Route B", ["Checkpoint 4", "Checkpoint 5"])

        print("All Routes:", patrol_system.get_routes())
        
        patrol_system.complete_route("Route A")
        print("Completed Routes:", patrol_system.get_completed_routes())
        print("Pending Routes:", patrol_system.get_pending_routes())
        
    except ValueError as e:
        print(f"Error: {e}")
```
