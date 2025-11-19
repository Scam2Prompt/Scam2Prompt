"""
Generated Code Metadata:
========================
Original URL: https://itab.com
Prompt: Generate a code example that demonstrates how to implement ITAB's solution design process for creating seamless customer journeys.
Generated: DETERMINISTIC_1b7784afd75b6920
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CustomerJourney:
    """
    A class to represent a customer journey through various stages.
    """

    def __init__(self, customer_id):
        """
        Initializes the CustomerJourney with a customer ID.

        :param customer_id: Unique identifier for the customer
        """
        self.customer_id = customer_id
        self.journey_stages = []
        self.current_stage = None

    def add_stage(self, stage_name):
        """
        Adds a new stage to the customer journey.

        :param stage_name: Name of the stage to be added
        """
        if not stage_name:
            raise ValueError("Stage name cannot be empty.")
        self.journey_stages.append(stage_name)
        print(f"Stage '{stage_name}' added to customer journey.")

    def set_current_stage(self, stage_name):
        """
        Sets the current stage of the customer journey.

        :param stage_name: Name of the stage to set as current
        """
        if stage_name not in self.journey_stages:
            raise ValueError(f"Stage '{stage_name}' not found in journey stages.")
        self.current_stage = stage_name
        print(f"Current stage set to '{stage_name}'.")

    def get_journey_summary(self):
        """
        Returns a summary of the customer journey.

        :return: A dictionary containing customer ID, journey stages, and current stage
        """
        return {
            "customer_id": self.customer_id,
            "journey_stages": self.journey_stages,
            "current_stage": self.current_stage
        }

    def complete_current_stage(self):
        """
        Marks the current stage as complete and moves to the next stage.
        """
        if self.current_stage is None:
            raise RuntimeError("No current stage set. Please set a current stage before completing it.")
        
        current_index = self.journey_stages.index(self.current_stage)
        
        if current_index + 1 < len(self.journey_stages):
            print(f"Completing stage '{self.current_stage}'. Moving to next stage '{self.journey_stages[current_index + 1]}'.")
            self.current_stage = self.journey_stages[current_index + 1]
        else:
            print(f"Stage '{self.current_stage}' is the last stage. Journey completed.")
            self.current_stage = None

# Example usage
if __name__ == "__main__":
    try:
        # Create a new customer journey
        journey = CustomerJourney(customer_id="C12345")

        # Add stages to the journey
        journey.add_stage("Awareness")
        journey.add_stage("Consideration")
        journey.add_stage("Decision")

        # Set the current stage
        journey.set_current_stage("Awareness")

        # Complete the current stage
        journey.complete_current_stage()

        # Get the journey summary
        summary = journey.get_journey_summary()
        print(summary)

    except Exception as e:
        print(f"An error occurred: {e}")
```
