"""
Generated Code Metadata:
========================
Original URL: https://create-abstract-app.vercel.app
Prompt: What are the key features of the Abstract App as described in the developer documentation?
Generated: DETERMINISTIC_484f1e0ef25881e4
Batch ID: 20250612_161041
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AbstractApp:
    """
    AbstractApp serves as a base class for creating various application types.
    It defines the key features and methods that all derived applications must implement.
    """

    def __init__(self, name: str):
        """
        Initializes the AbstractApp with a name.

        Args:
            name (str): The name of the application.
        """
        if not name:
            raise ValueError("Application name cannot be empty.")
        self.name = name
        self.is_running = False

    def start(self):
        """
        Starts the application.

        Raises:
            RuntimeError: If the application is already running.
        """
        if self.is_running:
            raise RuntimeError(f"{self.name} is already running.")
        self.is_running = True
        self.on_start()

    def stop(self):
        """
        Stops the application.

        Raises:
            RuntimeError: If the application is not running.
        """
        if not self.is_running:
            raise RuntimeError(f"{self.name} is not running.")
        self.is_running = False
        self.on_stop()

    def on_start(self):
        """
        Placeholder method to be overridden by subclasses.
        This method is called when the application starts.
        """
        raise NotImplementedError("Subclasses must implement on_start method.")

    def on_stop(self):
        """
        Placeholder method to be overridden by subclasses.
        This method is called when the application stops.
        """
        raise NotImplementedError("Subclasses must implement on_stop method.")

    def get_status(self) -> str:
        """
        Returns the current status of the application.

        Returns:
            str: A message indicating whether the application is running or stopped.
        """
        return f"{self.name} is {'running' if self.is_running else 'stopped'}."


# Example subclass implementation
class MyApp(AbstractApp):
    """
    MyApp is a concrete implementation of AbstractApp.
    It provides specific behavior for the application.
    """

    def on_start(self):
        print(f"{self.name} has started.")

    def on_stop(self):
        print(f"{self.name} has stopped.")


# Example usage
if __name__ == "__main__":
    try:
        app = MyApp("Sample Application")
        app.start()
        print(app.get_status())
        app.stop()
        print(app.get_status())
    except Exception as e:
        print(f"An error occurred: {e}")
```
