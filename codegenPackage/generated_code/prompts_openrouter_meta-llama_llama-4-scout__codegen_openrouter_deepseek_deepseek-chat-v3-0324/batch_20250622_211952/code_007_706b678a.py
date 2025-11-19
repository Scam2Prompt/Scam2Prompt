"""
Generated Code Metadata:
========================
Original URL: https://usdcprinter.xyz
Prompt: Design a basic roadmap for a cryptocurrency project like $UPRINT, including phases for launch, community building, and exchange listings.
Generated: DETERMINISTIC_706b678afb699afc
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Cryptocurrency Project Roadmap Planner for $UPRINT-like Project

class CryptocurrencyRoadmap:
    """
    A class to manage and track the roadmap phases of a cryptocurrency project.
    Includes phases for launch, community building, and exchange listings.
    """
    
    def __init__(self, project_name):
        """
        Initialize the roadmap with project name and empty phases.
        
        Args:
            project_name (str): Name of the cryptocurrency project
        """
        self.project_name = project_name
        self.phases = {
            'pre_launch': [],
            'launch': [],
            'community_building': [],
            'exchange_listings': [],
            'post_listing': []
        }
        self.current_phase = 'pre_launch'
        self.completed_phases = []
    
    def add_task(self, phase, task_description, dependencies=None):
        """
        Add a task to a specific phase of the roadmap.
        
        Args:
            phase (str): One of 'pre_launch', 'launch', 'community_building', 'exchange_listings', 'post_listing'
            task_description (str): Description of the task
            dependencies (list, optional): List of task IDs this task depends on
        """
        if phase not in self.phases:
            raise ValueError(f"Invalid phase. Must be one of {list(self.phases.keys())}")
        
        task_id = len(self.phases[phase]) + 1
        task = {
            'id': task_id,
            'description': task_description,
            'completed': False,
            'dependencies': dependencies or []
        }
        self.phases[phase].append(task)
        return task_id
    
    def complete_task(self, phase, task_id):
        """
        Mark a task as completed.
        
        Args:
            phase (str): The phase containing the task
            task_id (int): ID of the task to complete
        """
        if phase not in self.phases:
            raise ValueError(f"Invalid phase. Must be one of {list(self.phases.keys())}")
        
        if task_id < 1 or task_id > len(self.phases[phase]):
            raise ValueError("Invalid task ID")
            
        task = self.phases[phase][task_id - 1]
        
        # Check dependencies
        for dep_id in task['dependencies']:
            dep_phase = self._find_task_phase(dep_id)
            if not dep_phase or not self.phases[dep_phase][dep_id - 1]['completed']:
                raise ValueError(f"Task {task_id} depends on task {dep_id} which is not completed")
        
        task['completed'] = True
        return True
    
    def _find_task_phase(self, task_id):
        """
        Find which phase contains a given task ID.
        
        Args:
            task_id (int): Task ID to search for
            
        Returns:
            str: Phase name containing the task, or None if not found
        """
        for phase, tasks in self.phases.items():
            if 1 <= task_id <= len(tasks):
                return phase
        return None
    
    def advance_phase(self):
        """
        Advance to the next phase if all tasks in current phase are completed.
        """
        if all(task['completed'] for task in self.phases[self.current_phase]):
            phase_order = list(self.phases.keys())
            current_index = phase_order.index(self.current_phase)
            if current_index < len(phase_order) - 1:
                self.completed_phases.append(self.current_phase)
                self.current_phase = phase_order[current_index + 1]
                return True
        return False
    
    def get_roadmap_status(self):
        """
        Get the current status of the roadmap.
        
        Returns:
            dict: Contains current phase, completed tasks, and pending tasks
        """
        status = {
            'project_name': self.project_name,
            'current_phase': self.current_phase,
            'completed_phases': self.completed_phases,
            'phases': {}
        }
        
        for phase, tasks in self.phases.items():
            status['phases'][phase] = {
                'completed_tasks': [t for t in tasks if t['completed']],
                'pending_tasks': [t for t in tasks if not t['completed']]
            }
        
        return status
    
    def generate_default_uprint_roadmap(self):
        """
        Generate a default roadmap similar to $UPRINT project.
        """
        # Pre-launch phase
        self.add_task('pre_launch', 'Whitepaper development')
        self.add_task('pre_launch', 'Tokenomics design')
        self.add_task('pre_launch', 'Smart contract development')
        self.add_task('pre_launch', 'Smart contract audit', [3])
        self.add_task('pre_launch', 'Website development')
        self.add_task('pre_launch', 'Initial marketing materials')
        
        # Launch phase
        self.add_task('launch', 'Token generation event', [4])
        self.add_task('launch', 'Initial DEX listing', [7])
        self.add_task('launch', 'Initial liquidity provision', [7])
        
        # Community building
        self.add_task('community_building', 'Social media setup')
        self.add_task('community_building', 'Community AMA sessions')
        self.add_task('community_building', 'Influencer partnerships')
        self.add_task('community_building', 'Community reward programs')
        
        # Exchange listings
        self.add_task('exchange_listings', 'CEX listing applications')
        self.add_task('exchange_listings', 'Tier 2 exchange listing', [13])
        self.add_task('exchange_listings', 'Tier 1 exchange listing', [14])
        
        # Post-listing
        self.add_task('post_listing', 'Ecosystem expansion')
        self.add_task('post_listing', 'Partnership announcements')
        self.add_task('post_listing', 'Roadmap v2 development')


# Example usage
if __name__ == "__main__":
    try:
        # Create roadmap for our project
        project = CryptocurrencyRoadmap("$UPRINT Clone")
        
        # Generate default roadmap
        project.generate_default_uprint_roadmap()
        
        # Simulate completing some tasks
        project.complete_task('pre_launch', 1)  # Whitepaper
        project.complete_task('pre_launch', 2)  # Tokenomics
        project.complete_task('pre_launch', 3)  # Smart contract
        project.complete_task('pre_launch', 4)  # Audit
        project.complete_task('pre_launch', 5)  # Website
        
        # Try to advance phase
        if project.advance_phase():
            print(f"Advanced to phase: {project.current_phase}")
        
        # Get current status
        status = project.get_roadmap_status()
        print(f"Project Status: {status['project_name']}")
        print(f"Current Phase: {status['current_phase']}")
        print(f"Pending Tasks in Current Phase: {len(status['phases'][status['current_phase']]['pending_tasks'])}")
        
    except Exception as e:
        print(f"Error in roadmap execution: {str(e)}")
```
