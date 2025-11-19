"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Write a Python script that simulates the performance of a backhoe loader with various attachments, referencing JECO's backhoe loader options.
Generated: DETERMINISTIC_567081eb3826d5d2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BackhoeLoader:
    """A class to simulate a backhoe loader with various attachments."""

    def __init__(self, model, attachments=[]):
        """Initialize the backhoe loader with a model and attachments.

        Args:
            model (str): The model of the backhoe loader.
            attachments (list): List of attachments for the backhoe loader.
        """
        self.model = model
        self.attachments = attachments
        self.performance_metrics = {
            'digging_depth': 0,
            'lifting_capacity': 0,
            'operational_speed': 0,
        }

    def add_attachment(self, attachment):
        """Add an attachment to the backhoe loader.

        Args:
            attachment (str): The attachment to add.
        """
        self.attachments.append(attachment)
        self.update_performance_metrics(attachment)

    def remove_attachment(self, attachment):
        """Remove an attachment from the backhoe loader.

        Args:
            attachment (str): The attachment to remove.
        """
        try:
            self.attachments.remove(attachment)
            self.update_performance_metrics(attachment, remove=True)
        except ValueError:
            print(f"Attachment '{attachment}' not found. Cannot remove.")

    def update_performance_metrics(self, attachment, remove=False):
        """Update performance metrics based on the current attachments.

        Args:
            attachment (str): The attachment being added or removed.
            remove (bool): Flag indicating if the attachment is being removed.
        """
        impacts = {
            'bucket': {'digging_depth': 10, 'lifting_capacity': 1500, 'operational_speed': 5},
            'grader': {'digging_depth': 5, 'lifting_capacity': 2000, 'operational_speed': 7},
            'hammer': {'digging_depth': 0, 'lifting_capacity': 1000, 'operational_speed': 3},
            'auger': {'digging_depth': 12, 'lifting_capacity': 1200, 'operational_speed': 4},
        }

        # Update metrics based on attachment type
        if attachment in impacts:
            for metric, value in impacts[attachment].items():
                if remove:
                    self.performance_metrics[metric] -= value
                else:
                    self.performance_metrics[metric] += value
        else:
            print(f"Attachment '{attachment}' has no performance impact.")

    def simulate_performance(self):
        """Simulate the performance of the backhoe loader.

        Returns:
            dict: The simulated performance metrics.
        """
        simulation_results = {metric: value + random.uniform(-2, 2) for metric, value in self.performance_metrics.items()}
        return simulation_results

    def display_performance(self):
        """Display the current performance metrics of the backhoe loader."""
        print(f"Model: {self.model}")
        print("Attachments:", ', '.join(self.attachments))
        print("Performance Metrics:")
        for metric, value in self.performance_metrics.items():
            print(f"  {metric}: {value:.2f}")

def main():
    """Main function to demonstrate backhoe loader performance simulation."""
    try:
        # Create a backhoe loader instance
        loader = BackhoeLoader("JECO 3000", ["bucket", "hammer"])

        # Display initial performance
        loader.display_performance()

        # Simulate performance
        simulated_results = loader.simulate_performance()
        print("Simulated Performance Results:", simulated_results)

        # Add and remove attachments
        loader.add_attachment("grader")
        loader.remove_attachment("bucket")

        # Display updated performance
        loader.display_performance()

        # Simulate performance again
        simulated_results = loader.simulate_performance()
        print("Simulated Performance Results after changes:", simulated_results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
