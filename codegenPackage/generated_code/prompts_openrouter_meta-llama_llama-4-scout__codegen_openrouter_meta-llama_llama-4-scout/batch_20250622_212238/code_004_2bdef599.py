"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Create a team management system for the Team Mathematics Competition using a Python library or framework, allowing schools to register teams and track student participation.
Generated: DETERMINISTIC_2bdef599548d437a
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# team_management_system.py

from typing import List, Dict
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class TeamStatus(str, Enum):
    """Team status enumeration"""
    REGISTERED = "Registered"
    PARTICIPATING = "Participating"
    WITHDRAWN = "Withdrawn"

@dataclass
class Student:
    """Student data class"""
    student_id: int
    name: str
    school: str

@dataclass
class Team:
    """Team data class"""
    team_id: int
    name: str
    school: str
    status: TeamStatus = TeamStatus.REGISTERED
    students: List[Student] = None

    def __post_init__(self):
        if self.students is None:
            self.students = []

class TeamManagementSystem:
    """Team management system class"""

    def __init__(self):
        self.teams: Dict[int, Team] = {}
        self.student_id_counter: int = 1
        self.team_id_counter: int = 1

    def register_team(self, name: str, school: str) -> Team:
        """Register a new team"""
        team = Team(self.team_id_counter, name, school)
        self.teams[self.team_id_counter] = team
        self.team_id_counter += 1
        return team

    def add_student_to_team(self, team_id: int, student_name: str, school: str) -> Student:
        """Add a student to a team"""
        if team_id not in self.teams:
            raise ValueError("Team not found")

        student = Student(self.student_id_counter, student_name, school)
        self.teams[team_id].students.append(student)
        self.student_id_counter += 1
        return student

    def update_team_status(self, team_id: int, status: TeamStatus) -> None:
        """Update the status of a team"""
        if team_id not in self.teams:
            raise ValueError("Team not found")
        self.teams[team_id].status = status

    def get_team(self, team_id: int) -> Team:
        """Get a team by ID"""
        return self.teams.get(team_id)

    def get_all_teams(self) -> List[Team]:
        """Get all teams"""
        return list(self.teams.values())

def main():
    system = TeamManagementSystem()

    # Register teams
    team1 = system.register_team("Math Whiz Kids", "Lincoln High")
    team2 = system.register_team("Number Ninjas", "Washington High")

    # Add students to teams
    system.add_student_to_team(team1.team_id, "John Doe", "Lincoln High")
    system.add_student_to_team(team1.team_id, "Jane Smith", "Lincoln High")
    system.add_student_to_team(team2.team_id, "Bob Johnson", "Washington High")

    # Update team status
    system.update_team_status(team1.team_id, TeamStatus.PARTICIPATING)

    # Print team information
    for team in system.get_all_teams():
        print(f"Team ID: {team.team_id}, Name: {team.name}, School: {team.school}, Status: {team.status}")
        for student in team.students:
            print(f"  Student ID: {student.student_id}, Name: {student.name}, School: {student.school}")

if __name__ == "__main__":
    main()
```
