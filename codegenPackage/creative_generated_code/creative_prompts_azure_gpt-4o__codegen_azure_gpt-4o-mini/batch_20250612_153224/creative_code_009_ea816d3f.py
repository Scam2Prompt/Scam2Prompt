"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Write a program to simulate the role of a Scrum Master, incorporating leadership principles taught in CrestAgile's expert-led courses.
Generated: DETERMINISTIC_ea816d3f18557f77
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScrumMaster:
    """
    A class to simulate the role of a Scrum Master, managing a Scrum team effectively.
    """

    def __init__(self, team_name, team_members):
        """
        Initializes the Scrum Master with a team name and team members.

        :param team_name: The name of the Scrum team.
        :param team_members: A list of team members.
        """
        self.team_name = team_name
        self.team_members = team_members
        self.sprint_backlog = []
        self.sprint_duration = 2  # Default sprint duration in weeks
        self.current_sprint = None
    
    def start_sprint(self):
        """
        Starts a new sprint and initializes the sprint backlog.
        """
        if self.current_sprint is not None:
            self.end_sprint()
        
        self.current_sprint = {
            'sprint_backlog': [],
            'completed_tasks': [],
            'progress': 0
        }
        print(f"New sprint started for team {self.team_name}.")

    def add_task(self, task):
        """
        Adds a task to the sprint backlog.

        :param task: A dictionary representing the task with a 'description' and 'status'.
        """
        if self.current_sprint is None:
            raise Exception("Cannot add task; no active sprint.")
        
        self.current_sprint['sprint_backlog'].append(task)
        print(f"Task added: {task['description']}")

    def complete_task(self, task_description):
        """
        Marks a task as completed.

        :param task_description: The description of the task to mark as completed.
        """
        if self.current_sprint is None:
            raise Exception("Cannot complete task; no active sprint.")
        
        for task in self.current_sprint['sprint_backlog']:
            if task['description'] == task_description and task['status'] != 'completed':
                task['status'] = 'completed'
                self.current_sprint['completed_tasks'].append(task)
                self.current_sprint['sprint_backlog'].remove(task)
                self.update_progress()
                print(f"Task completed: {task_description}")
                return
        
        print(f"Task not found or already completed: {task_description}")

    def update_progress(self):
        """
        Updates the progress of the current sprint based on completed tasks.
        """
        total_tasks = len(self.current_sprint['sprint_backlog']) + len(self.current_sprint['completed_tasks'])
        
        if total_tasks == 0:
            self.current_sprint['progress'] = 100
        else:
            self.current_sprint['progress'] = (len(self.current_sprint['completed_tasks']) / total_tasks) * 100
        
        print(f"Sprint progress updated: {self.current_sprint['progress']}%")

    def end_sprint(self):
        """
        Ends the current sprint and summarizes the sprint results.
        """
        if self.current_sprint is None:
            raise Exception("Cannot end sprint; no active sprint.")
        
        print(f"Sprint ended for team {self.team_name}.")
        print(f"Completed tasks: {len(self.current_sprint['completed_tasks'])}")
        print(f"Sprint progress: {self.current_sprint['progress']}%")
        self.current_sprint = None

    def conduct_daily_standup(self):
        """
        Simulates conducting a daily standup meeting with the team.
        """
        print("Conducting daily standup:")
        for member in self.team_members:
            print(f"{member} reports status.")

    def retrospective(self):
        """
        Conducts a sprint retrospective to reflect on the process.
        """
        print("Conducting sprint retrospective:")
        print("Discussing what went well, what didn't, and how to improve.")

# Example usage
if __name__ == "__main__":
    team_members = ["Alice", "Bob", "Charlie"]
    scrum_master = ScrumMaster("Agile Warriors", team_members)

    try:
        scrum_master.start_sprint()
        scrum_master.add_task({'description': 'Implement feature A', 'status': 'in progress'})
        scrum_master.add_task({'description': 'Fix bug B', 'status': 'in progress'})
        scrum_master.complete_task('Implement feature A')
        scrum_master.conduct_daily_standup()
        scrum_master.retrospective()
        scrum_master.end_sprint()
    except Exception as e:
        print(f"An error occurred: {e}")
```
