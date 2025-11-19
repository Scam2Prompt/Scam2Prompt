"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Write a sample implementation plan for a custom software project that includes evaluation, design, and delivery phases, inspired by MetaCode's methodology.
Generated: DETERMINISTIC_33f69b869eaddfe1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Software Project Implementation Plan
Inspired by MetaCode's Methodology
"""

class ImplementationPlan:
    """
    A class representing the implementation plan for a custom software project.
    Includes evaluation, design, and delivery phases.
    """
    
    def __init__(self, project_name, client_name):
        """
        Initialize the implementation plan with project details.
        
        Args:
            project_name (str): Name of the project
            client_name (str): Name of the client
        """
        self.project_name = project_name
        self.client_name = client_name
        self.phases = {
            'evaluation': [],
            'design': [],
            'delivery': []
        }
        self.current_phase = None
        self.completed_phases = []
        self.project_status = "Not Started"
        
    def add_evaluation_task(self, task_name, description, duration_days):
        """
        Add a task to the evaluation phase.
        
        Args:
            task_name (str): Name of the task
            description (str): Description of the task
            duration_days (int): Estimated duration in days
        """
        self._add_task('evaluation', task_name, description, duration_days)
        
    def add_design_task(self, task_name, description, duration_days):
        """
        Add a task to the design phase.
        
        Args:
            task_name (str): Name of the task
            description (str): Description of the task
            duration_days (int): Estimated duration in days
        """
        self._add_task('design', task_name, description, duration_days)
        
    def add_delivery_task(self, task_name, description, duration_days):
        """
        Add a task to the delivery phase.
        
        Args:
            task_name (str): Name of the task
            description (str): Description of the task
            duration_days (int): Estimated duration in days
        """
        self._add_task('delivery', task_name, description, duration_days)
        
    def _add_task(self, phase, task_name, description, duration_days):
        """
        Internal method to add a task to a specific phase.
        
        Args:
            phase (str): Phase name ('evaluation', 'design', or 'delivery')
            task_name (str): Name of the task
            description (str): Description of the task
            duration_days (int): Estimated duration in days
            
        Raises:
            ValueError: If phase is invalid
        """
        if phase not in self.phases:
            raise ValueError(f"Invalid phase: {phase}. Must be one of {list(self.phases.keys())}")
            
        task = {
            'name': task_name,
            'description': description,
            'duration_days': duration_days,
            'status': 'Pending'
        }
        self.phases[phase].append(task)
        
    def start_phase(self, phase_name):
        """
        Mark a phase as started.
        
        Args:
            phase_name (str): Name of the phase to start
            
        Raises:
            ValueError: If phase is invalid or already completed
        """
        if phase_name not in self.phases:
            raise ValueError(f"Invalid phase: {phase_name}")
        if phase_name in self.completed_phases:
            raise ValueError(f"Phase {phase_name} already completed")
            
        self.current_phase = phase_name
        self.project_status = f"In Progress - {phase_name.capitalize()} Phase"
        
    def complete_phase(self, phase_name):
        """
        Mark a phase as completed.
        
        Args:
            phase_name (str): Name of the phase to complete
            
        Raises:
            ValueError: If phase is invalid, not started, or already completed
        """
        if phase_name not in self.phases:
            raise ValueError(f"Invalid phase: {phase_name}")
        if phase_name not in self.completed_phases and phase_name != self.current_phase:
            raise ValueError(f"Phase {phase_name} not started")
        if phase_name in self.completed_phases:
            raise ValueError(f"Phase {phase_name} already completed")
            
        self.completed_phases.append(phase_name)
        self.current_phase = None
        
        if len(self.completed_phases) == len(self.phases):
            self.project_status = "Completed"
        else:
            self.project_status = "Partially Completed"
            
    def get_project_summary(self):
        """
        Generate a summary of the project status.
        
        Returns:
            dict: Project summary including name, client, status, and phase details
        """
        return {
            'project_name': self.project_name,
            'client_name': self.client_name,
            'status': self.project_status,
            'current_phase': self.current_phase,
            'completed_phases': self.completed_phases,
            'phases': {
                phase: {
                    'task_count': len(tasks),
                    'completed_tasks': sum(1 for t in tasks if t['status'] == 'Completed')
                }
                for phase, tasks in self.phases.items()
            }
        }
        
    def update_task_status(self, phase_name, task_name, new_status):
        """
        Update the status of a specific task.
        
        Args:
            phase_name (str): Name of the phase containing the task
            task_name (str): Name of the task to update
            new_status (str): New status for the task
            
        Raises:
            ValueError: If phase or task is not found, or status is invalid
        """
        valid_statuses = ['Pending', 'In Progress', 'Completed', 'Blocked']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
            
        if phase_name not in self.phases:
            raise ValueError(f"Phase {phase_name} not found")
            
        task_found = False
        for task in self.phases[phase_name]:
            if task['name'] == task_name:
                task['status'] = new_status
                task_found = True
                break
                
        if not task_found:
            raise ValueError(f"Task {task_name} not found in phase {phase_name}")


# Example usage
if __name__ == "__main__":
    # Create a new implementation plan
    project = ImplementationPlan("E-Commerce Platform", "Acme Corp")
    
    # Add evaluation phase tasks
    project.add_evaluation_task("Requirement Gathering", "Collect and document client requirements", 5)
    project.add_evaluation_task("Feasibility Study", "Assess technical and economic feasibility", 3)
    
    # Add design phase tasks
    project.add_design_task("System Architecture", "Design high-level system architecture", 7)
    project.add_design_task("Database Design", "Design database schema and relationships", 4)
    
    # Add delivery phase tasks
    project.add_delivery_task("Implementation", "Develop the software solution", 14)
    project.add_delivery_task("Testing", "Perform QA and user acceptance testing", 7)
    project.add_delivery_task("Deployment", "Deploy solution to production environment", 2)
    
    # Execute the plan
    project.start_phase("evaluation")
    project.update_task_status("evaluation", "Requirement Gathering", "Completed")
    project.update_task_status("evaluation", "Feasibility Study", "Completed")
    project.complete_phase("evaluation")
    
    project.start_phase("design")
    project.update_task_status("design", "System Architecture", "In Progress")
    
    # Print project summary
    print(project.get_project_summary())
```
