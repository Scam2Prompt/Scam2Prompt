"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Write Python code to simulate a pipeline construction project workflow, including stages like design, material selection, and installation, as described on the C&M Pinnacle website.
Generated: DETERMINISTIC_266e66f1e987491d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PipelineConstructionProject:
    def __init__(self, project_name):
        """
        Initialize the pipeline construction project with a name and stages.
        
        :param project_name: Name of the pipeline construction project
        """
        self.project_name = project_name
        self.stages = {
            "design": False,
            "material_selection": False,
            "installation": False
        }
        self.current_stage = None

    def start_stage(self, stage):
        """
        Start a specific stage of the project.
        
        :param stage: The stage to start (design, material_selection, installation)
        :raises ValueError: If the stage is not valid or already completed
        """
        if stage not in self.stages:
            raise ValueError(f"Invalid stage: {stage}. Valid stages are: {list(self.stages.keys())}.")
        
        if self.stages[stage]:
            raise ValueError(f"The stage '{stage}' has already been completed.")
        
        self.current_stage = stage
        print(f"Starting stage: {stage}")

    def complete_stage(self):
        """
        Mark the current stage as completed.
        
        :raises RuntimeError: If no stage is currently active
        """
        if self.current_stage is None:
            raise RuntimeError("No stage is currently active. Please start a stage first.")
        
        self.stages[self.current_stage] = True
        print(f"Completed stage: {self.current_stage}")
        self.current_stage = None

    def get_project_status(self):
        """
        Get the current status of the project.
        
        :return: A dictionary with the status of each stage
        """
        return {stage: "Completed" if completed else "In Progress" for stage, completed in self.stages.items()}

    def run_project(self):
        """
        Run the pipeline construction project workflow.
        This method simulates the workflow by executing each stage in order.
        """
        try:
            self.start_stage("design")
            # Simulate design work
            self.complete_stage()

            self.start_stage("material_selection")
            # Simulate material selection work
            self.complete_stage()

            self.start_stage("installation")
            # Simulate installation work
            self.complete_stage()

            print("Pipeline construction project completed successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    project = PipelineConstructionProject("Main Pipeline Project")
    project.run_project()
    print("Project Status:", project.get_project_status())
```
