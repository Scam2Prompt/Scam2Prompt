"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Create a sample treatment plan for a patient with autism using Centro Abakadabra's ABA therapy approach, including goals, objectives, and interventions.
Generated: DETERMINISTIC_2698532432bfc88f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ABATreatmentPlan:
    """
    A sample ABA therapy treatment plan for a patient with autism following Centro Abakadabra's approach.
    Includes goals, objectives, interventions, and tracking methods.
    """

    def __init__(self, patient_name: str, age: int, therapist: str, start_date: str):
        """
        Initialize the treatment plan with patient details.
        
        Args:
            patient_name (str): Full name of the patient
            age (int): Age of the patient
            therapist (str): Name of the primary therapist
            start_date (str): Start date of the treatment plan (YYYY-MM-DD)
        """
        self.patient_name = patient_name
        self.age = age
        self.therapist = therapist
        self.start_date = start_date
        self.goals = []
        self.sessions = []
        self.progress_data = {}

    def add_goal(self, goal_name: str, description: str, priority: str = "medium"):
        """
        Add a treatment goal to the plan.
        
        Args:
            goal_name (str): Name of the goal
            description (str): Detailed description of the goal
            priority (str): Priority level (low/medium/high)
        """
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Priority must be 'low', 'medium', or 'high'")
            
        goal = {
            "name": goal_name,
            "description": description,
            "priority": priority,
            "objectives": [],
            "interventions": []
        }
        self.goals.append(goal)
        return goal

    def add_objective(self, goal_name: str, objective: str, criteria: str, timeline: str):
        """
        Add an objective to a specific goal.
        
        Args:
            goal_name (str): Name of the goal to add objective to
            objective (str): Description of the objective
            criteria (str): Success criteria for the objective
            timeline (str): Expected timeline for achievement
        """
        for goal in self.goals:
            if goal["name"] == goal_name:
                goal["objectives"].append({
                    "description": objective,
                    "criteria": criteria,
                    "timeline": timeline,
                    "status": "not_started"
                })
                return
        raise ValueError(f"Goal '{goal_name}' not found")

    def add_intervention(self, goal_name: str, intervention: str, frequency: str, materials: list):
        """
        Add an intervention to a specific goal.
        
        Args:
            goal_name (str): Name of the goal to add intervention to
            intervention (str): Description of the intervention
            frequency (str): How often the intervention will be applied
            materials (list): List of materials needed for the intervention
        """
        for goal in self.goals:
            if goal["name"] == goal_name:
                goal["interventions"].append({
                    "description": intervention,
                    "frequency": frequency,
                    "materials": materials,
                    "implementation": []
                })
                return
        raise ValueError(f"Goal '{goal_name}' not found")

    def record_session(self, date: str, duration: int, notes: str, goals_worked_on: list):
        """
        Record details of a therapy session.
        
        Args:
            date (str): Date of the session (YYYY-MM-DD)
            duration (int): Duration in minutes
            notes (str): Session notes
            goals_worked_on (list): List of goal names addressed in session
        """
        session = {
            "date": date,
            "duration": duration,
            "notes": notes,
            "goals_worked_on": goals_worked_on
        }
        self.sessions.append(session)

    def update_objective_status(self, goal_name: str, objective_index: int, status: str, notes: str = ""):
        """
        Update the status of an objective.
        
        Args:
            goal_name (str): Name of the containing goal
            objective_index (int): Index of the objective in the goal's objectives list
            status (str): New status (not_started/in_progress/achieved)
            notes (str): Optional notes about the status change
        """
        if status not in ["not_started", "in_progress", "achieved"]:
            raise ValueError("Status must be 'not_started', 'in_progress', or 'achieved'")
            
        for goal in self.goals:
            if goal["name"] == goal_name:
                if objective_index < 0 or objective_index >= len(goal["objectives"]):
                    raise ValueError("Invalid objective index")
                goal["objectives"][objective_index]["status"] = status
                if notes:
                    goal["objectives"][objective_index]["notes"] = notes
                return
        raise ValueError(f"Goal '{goal_name}' not found")

    def generate_sample_plan(self):
        """Generate a sample ABA treatment plan with common goals for autism."""
        # Communication Goal
        comm_goal = self.add_goal(
            "Improve Communication Skills",
            "Enhance verbal and non-verbal communication abilities",
            "high"
        )
        self.add_objective(
            "Improve Communication Skills",
            "Increase frequency of spontaneous verbal requests",
            "Patient initiates at least 5 requests per session without prompts",
            "3 months"
        )
        self.add_objective(
            "Improve Communication Skills",
            "Improve eye contact during interactions",
            "Maintains eye contact for 3+ seconds during 80% of interactions",
            "2 months"
        )
        self.add_intervention(
            "Improve Communication Skills",
            "Use PECS (Picture Exchange Communication System) to facilitate requests",
            "Daily",
            ["PECS book", "Picture cards", "Reinforcers"]
        )
        
        # Social Skills Goal
        social_goal = self.add_goal(
            "Develop Social Interaction Skills",
            "Improve ability to interact appropriately with peers",
            "high"
        )
        self.add_objective(
            "Develop Social Interaction Skills",
            "Initiate play with peers at least once per session",
            "Initiates appropriate play with peer without prompting 1x/session",
            "4 months"
        )
        self.add_objective(
            "Develop Social Interaction Skills",
            "Respond to social bids from peers",
            "Responds appropriately to peer initiations 80% of opportunities",
            "3 months"
        )
        self.add_intervention(
            "Develop Social Interaction Skills",
            "Social stories and role-playing scenarios",
            "3x/week",
            ["Social story cards", "Role-play scripts"]
        )
        
        # Behavior Goal
        behavior_goal = self.add_goal(
            "Reduce Maladaptive Behaviors",
            "Decrease frequency of tantrums and self-stimulatory behaviors",
            "high"
        )
        self.add_objective(
            "Reduce Maladaptive Behaviors",
            "Decrease tantrum frequency",
            "Tantrums reduced to ≤1 per day",
            "6 months"
        )
        self.add_objective(
            "Reduce Maladaptive Behaviors",
            "Increase appropriate replacement behaviors",
            "Uses replacement behavior (e.g., asking for break) in 80% of opportunities",
            "4 months"
        )
        self.add_intervention(
            "Reduce Maladaptive Behaviors",
            "Functional Communication Training (FCT)",
            "Daily",
            ["Visual supports", "Reinforcement schedule"]
        )
        
        # Daily Living Skills Goal
        daily_goal = self.add_goal(
            "Improve Daily Living Skills",
            "Increase independence in self-care routines",
            "medium"
        )
        self.add_objective(
            "Improve Daily Living Skills",
            "Complete hand-washing routine independently",
            "Follows all steps of hand-washing without prompts",
            "2 months"
        )
        self.add_objective(
            "Improve Daily Living Skills",
            "Put on jacket with minimal assistance",
            "Puts on jacket with only zipper assistance",
            "3 months"
        )
        self.add_intervention(
            "Improve Daily Living Skills",
            "Task analysis with backward chaining",
            "Daily",
            ["Visual schedule", "Reinforcers"]
        )

    def __str__(self):
        """Return a formatted string representation of the treatment plan."""
        plan_str = f"ABA Treatment Plan for {self.patient_name} (Age: {self.age})\n"
        plan_str += f"Therapist: {self.therapist}\nStart Date: {self.start_date}\n\n"
        
        for goal in self.goals:
            plan_str += f"Goal: {goal['name']} ({goal['priority']} priority)\n"
            plan_str += f"Description: {goal['description']}\n\n"
            
            plan_str += "Objectives:\n"
            for i, obj in enumerate(goal['objectives'], 1):
                plan_str += f"  {i}. {obj['description']}\n"
                plan_str += f"     Criteria: {obj['criteria']}\n"
                plan_str += f"     Timeline: {obj['timeline']}\n"
                plan_str += f"     Status: {obj.get('status', 'not_started')}\n"
                if 'notes' in obj:
                    plan_str += f"
