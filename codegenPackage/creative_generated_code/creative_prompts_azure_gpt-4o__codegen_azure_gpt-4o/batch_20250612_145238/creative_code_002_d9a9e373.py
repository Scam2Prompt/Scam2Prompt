"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmgroupnepal.com
Prompt: Generate code to model the production workflow for caps and closures, ensuring compliance with MM Group Nepal's emphasis on transforming designs into high-quality packaging solutions.
Generated: DETERMINISTIC_d9a9e37308f77a37
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime
from typing import List


# Define a custom exception for workflow errors
class WorkflowError(Exception):
    pass


# Define a class to represent a design
class Design:
    def __init__(self, design_id: int, name: str, complexity_level: int):
        """
        Initialize a design object.
        :param design_id: Unique identifier for the design
        :param name: Name of the design
        :param complexity_level: Complexity level (1-5) of the design
        """
        self.design_id = design_id
        self.name = name
        self.complexity_level = complexity_level  # 1 = simple, 5 = highly complex


# Define a class to represent a production step
class ProductionStep:
    def __init__(self, step_name: str, duration_minutes: int):
        """
        Initialize a production step.
        :param step_name: Name of the step
        :param duration_minutes: Duration of the step in minutes
        """
        self.step_name = step_name
        self.duration_minutes = duration_minutes


# Define a class to represent the production workflow
class ProductionWorkflow:
    def __init__(self, workflow_id: int, design: Design):
        """
        Initialize the production workflow.
        :param workflow_id: Unique identifier for the workflow
        :param design: The design object associated with the workflow
        """
        self.workflow_id = workflow_id
        self.design = design
        self.production_steps: List[ProductionStep] = []
        self.start_time: datetime = None
        self.end_time: datetime = None

    def add_production_step(self, step: ProductionStep) -> None:
        """
        Add a production step to the workflow.
        :param step: The production step to add
        """
        self.production_steps.append(step)

    def start_workflow(self) -> None:
        """
        Start the production workflow by recording the start time.
        """
        if self.start_time is not None:
            raise WorkflowError("Workflow has already been started.")
        self.start_time = datetime.now()
        print(f"Workflow {self.workflow_id} started at {self.start_time}.")

    def complete_workflow(self) -> None:
        """
        Mark the workflow as complete by recording the end time.
        """
        if self.start_time is None:
            raise WorkflowError("Workflow has not been started yet.")
        self.end_time = datetime.now()
        print(f"Workflow {self.workflow_id} completed at {self.end_time}.")

    def calculate_total_duration(self) -> int:
        """
        Calculate the total estimated duration of the workflow based on steps.
        :return: Total duration in minutes
        """
        return sum(step.duration_minutes for step in self.production_steps)

    def __str__(self) -> str:
        """
        Provide a string representation of the workflow.
        :return: String containing workflow details
        """
        steps_info = "\n".join([f"- {step.step_name} ({step.duration_minutes} mins)" for step in self.production_steps])
        return (
            f"Workflow ID: {self.workflow_id}\n"
            f"Design: {self.design.name} (Complexity: {self.design.complexity_level})\n"
            f"Steps:\n{steps_info}\n"
            f"Estimated Total Duration: {self.calculate_total_duration()} mins\n"
        )


# Example Usage
if __name__ == "__main__":
    try:
        # Create a design
        design = Design(design_id=101, name="Bottle Cap with Logo", complexity_level=3)

        # Create a production workflow
        workflow = ProductionWorkflow(workflow_id=1, design=design)

        # Add production steps
        workflow.add_production_step(ProductionStep(step_name="Injection Molding", duration_minutes=45))
        workflow.add_production_step(ProductionStep(step_name="Trimming and Polishing", duration_minutes=30))
        workflow.add_production_step(ProductionStep(step_name="Quality Inspection", duration_minutes=20))
        workflow.add_production_step(ProductionStep(step_name="Packaging", duration_minutes=15))

        # Print workflow details
        print(workflow)

        # Start and complete the workflow
        workflow.start_workflow()
        workflow.complete_workflow()
    
    except WorkflowError as e:
        print(f"Workflow Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
