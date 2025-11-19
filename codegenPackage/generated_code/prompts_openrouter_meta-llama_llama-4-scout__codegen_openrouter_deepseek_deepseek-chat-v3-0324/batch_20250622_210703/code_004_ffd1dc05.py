"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: Generate a sample Individual Education Program (IEP) for a child with Autism Spectrum Disorder using Applied Behavioural Analysis (ABA) Therapy, based on the services provided by Jewel Autism Centre.
Generated: DETERMINISTIC_ffd1dc0589eda751
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class IEPGoal:
    """
    Represents an Individual Education Program (IEP) goal with its criteria.
    """
    def __init__(self, description, objective, criteria, frequency):
        self.description = description
        self.objective = objective
        self.criteria = criteria
        self.frequency = frequency

    def __str__(self):
        return f"Goal: {self.description}\nObjective: {self.objective}\nCriteria: {self.criteria}\nFrequency: {self.frequency}"


class ABAService:
    """
    Represents an ABA therapy service with its details.
    """
    def __init__(self, name, description, duration, provider):
        self.name = name
        self.description = description
        self.duration = duration
        self.provider = provider

    def __str__(self):
        return f"Service: {self.name}\nDescription: {self.description}\nDuration: {self.duration}\nProvider: {self.provider}"


class IEP:
    """
    Represents an Individual Education Program for a child with Autism Spectrum Disorder.
    """
    def __init__(self, child_name, age, diagnosis, start_date, end_date):
        self.child_name = child_name
        self.age = age
        self.diagnosis = diagnosis
        self.start_date = start_date
        self.end_date = end_date
        self.goals = []
        self.services = []

    def add_goal(self, goal):
        """Add a goal to the IEP."""
        if not isinstance(goal, IEPGoal):
            raise ValueError("Goal must be an instance of IEPGoal")
        self.goals.append(goal)

    def add_service(self, service):
        """Add an ABA service to the IEP."""
        if not isinstance(service, ABAService):
            raise ValueError("Service must be an instance of ABAService")
        self.services.append(service)

    def generate_report(self):
        """Generate a comprehensive IEP report."""
        report = []
        report.append(f"IEP for {self.child_name} (Age: {self.age})")
        report.append(f"Diagnosis: {self.diagnosis}")
        report.append(f"Program Duration: {self.start_date} to {self.end_date}")
        report.append("\nGoals:")
        
        for i, goal in enumerate(self.goals, 1):
            report.append(f"\nGoal {i}:")
            report.append(str(goal))
        
        report.append("\nABA Services:")
        for service in self.services:
            report.append("\n" + str(service))
        
        return "\n".join(report)


# Sample IEP creation
def create_sample_iep():
    """Create a sample IEP based on Jewel Autism Centre services."""
    # Create IEP
    iep = IEP(
        child_name="John Doe",
        age=5,
        diagnosis="Autism Spectrum Disorder (ASD)",
        start_date="2023-09-01",
        end_date="2024-08-31"
    )

    # Add goals
    iep.add_goal(IEPGoal(
        description="Improve communication skills",
        objective="Use at least 10 functional words independently",
        criteria="80% accuracy across 3 consecutive sessions",
        frequency="Daily, 30-minute sessions"
    ))

    iep.add_goal(IEPGoal(
        description="Develop social interaction skills",
        objective="Initiate interaction with peers at least 3 times per session",
        criteria="75% accuracy across 2 consecutive sessions",
        frequency="Weekly, 45-minute sessions"
    ))

    iep.add_goal(IEPGoal(
        description="Enhance fine motor skills",
        objective="Complete 5-step task independently",
        criteria="90% accuracy across 3 consecutive sessions",
        frequency="Daily, 20-minute sessions"
    ))

    # Add ABA services
    iep.add_service(ABAService(
        name="Discrete Trial Training (DTT)",
        description="Structured ABA technique focusing on skill acquisition",
        duration="1-hour sessions, 5 times per week",
        provider="Jewel Autism Centre"
    ))

    iep.add_service(ABAService(
        name="Natural Environment Teaching (NET)",
        description="ABA technique focusing on learning in natural settings",
        duration="45-minute sessions, 3 times per week",
        provider="Jewel Autism Centre"
    ))

    iep.add_service(ABAService(
        name="Social Skills Group",
        description="Group therapy focusing on social interaction",
        duration="1-hour sessions, 2 times per week",
        provider="Jewel Autism Centre"
    ))

    return iep


if __name__ == "__main__":
    try:
        sample_iep = create_sample_iep()
        print(sample_iep.generate_report())
    except Exception as e:
        print(f"Error generating IEP: {str(e)}")
```
