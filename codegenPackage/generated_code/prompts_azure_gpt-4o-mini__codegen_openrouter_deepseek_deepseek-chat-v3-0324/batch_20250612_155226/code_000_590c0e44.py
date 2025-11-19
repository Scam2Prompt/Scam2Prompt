"""
Generated Code Metadata:
========================
Original URL: https://debridgeadvisory.com
Prompt: Generate a Python script that simulates a sales training session for real estate professionals, incorporating project-led training methods as described by Debridge Advisory.
Generated: DETERMINISTIC_590c0e4483e70e48
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sales Training Simulator for Real Estate Professionals
This script simulates a project-led training session based on Debridge Advisory's methodology.
"""

import random
import time
from typing import List, Dict, Optional

class RealEstateAgent:
    """Represents a real estate agent participating in the training."""
    
    def __init__(self, name: str, experience_years: int):
        self.name = name
        self.experience_years = experience_years
        self.skills = {
            "prospecting": random.randint(1, 5),
            "negotiation": random.randint(1, 5),
            "market_analysis": random.randint(1, 5),
            "client_relations": random.randint(1, 5)
        }
        self.current_project = None
        self.completed_projects = 0
        self.score = 0
    
    def assess_skills(self) -> Dict[str, int]:
        """Return the agent's current skill levels."""
        return self.skills
    
    def improve_skill(self, skill: str, amount: int = 1) -> None:
        """Improve a specific skill by given amount (max 5)."""
        if skill in self.skills:
            self.skills[skill] = min(5, self.skills[skill] + amount)
    
    def complete_project(self, success: bool) -> None:
        """Handle project completion and update agent stats."""
        if success:
            self.completed_projects += 1
            self.score += 10
            print(f"\n{self.name} successfully completed the project!")
        else:
            self.score -= 5
            print(f"\n{self.name} didn't complete the project successfully.")
        self.current_project = None

class TrainingProject:
    """Represents a training project in the simulation."""
    
    def __init__(self, name: str, required_skills: Dict[str, int], difficulty: int):
        self.name = name
        self.required_skills = required_skills
        self.difficulty = difficulty  # 1-5 scale
        self.completed = False
    
    def attempt_project(self, agent: RealEstateAgent) -> bool:
        """Agent attempts to complete the project, returns success status."""
        print(f"\n{agent.name} is attempting project: {self.name}")
        time.sleep(1)
        
        success_chance = 0.5  # Base chance
        skill_bonus = 0
        
        # Calculate skill bonus
        for skill, level in self.required_skills.items():
            agent_skill = agent.skills.get(skill, 0)
            if agent_skill >= level:
                skill_bonus += 0.15
            else:
                skill_bonus -= 0.1
        
        # Adjust for difficulty
        difficulty_factor = 1 - (self.difficulty * 0.1)
        
        total_chance = min(0.95, max(0.05, (success_chance + skill_bonus) * difficulty_factor))
        
        # Simulate project attempt
        time.sleep(2)
        success = random.random() < total_chance
        
        # Improve skills regardless of success
        for skill in self.required_skills:
            agent.improve_skill(skill)
        
        self.completed = success
        return success

class TrainingSession:
    """Manages the overall training session."""
    
    def __init__(self):
        self.agents: List[RealEstateAgent] = []
        self.projects: List[TrainingProject] = []
        self.current_round = 0
        self.max_rounds = 5
        
        # Initialize sample projects
        self._initialize_projects()
    
    def _initialize_projects(self) -> None:
        """Create a set of training projects."""
        self.projects = [
            TrainingProject(
                "First-Time Homebuyer Consultation",
                {"client_relations": 2, "market_analysis": 1},
                difficulty=2
            ),
            TrainingProject(
                "Luxury Property Listing",
                {"prospecting": 3, "client_relations": 3},
                difficulty=3
            ),
            TrainingProject(
                "Short Sale Negotiation",
                {"negotiation": 4, "market_analysis": 2},
                difficulty=4
            ),
            TrainingProject(
                "Commercial Property Deal",
                {"prospecting": 4, "negotiation": 4, "market_analysis": 3},
                difficulty=5
            )
        ]
    
    def register_agent(self, name: str, experience: int) -> RealEstateAgent:
        """Register a new agent for the training."""
        agent = RealEstateAgent(name, experience)
        self.agents.append(agent)
        return agent
    
    def get_available_projects(self) -> List[TrainingProject]:
        """Return projects not currently assigned."""
        return [p for p in self.projects if not p.completed]
    
    def assign_project(self, agent: RealEstateAgent, project: TrainingProject) -> bool:
        """Assign a project to an agent if they're available."""
        if agent.current_project is not None:
            print(f"{agent.name} is already working on a project.")
            return False
        
        if project.completed:
            print("This project has already been completed.")
            return False
        
        agent.current_project = project
        return True
    
    def run_round(self) -> None:
        """Run one round of project attempts for all agents."""
        self.current_round += 1
        print(f"\n=== Round {self.current_round} ===")
        
        for agent in self.agents:
            if agent.current_project:
                success = agent.current_project.attempt_project(agent)
                agent.complete_project(success)
        
        # Print summary
        self.print_status()
    
    def print_status(self) -> None:
        """Print current training status."""
        print("\nCurrent Training Status:")
        print(f"Round: {self.current_round}/{self.max_rounds}")
        print("\nAgents:")
        for agent in sorted(self.agents, key=lambda x: -x.score):
            print(f"{agent.name}: {agent.score} pts | Projects: {agent.completed_projects}")
    
    def is_complete(self) -> bool:
        """Check if training is complete."""
        return self.current_round >= self.max_rounds or all(p.completed for p in self.projects)
    
    def get_leaderboard(self) -> List[RealEstateAgent]:
        """Return agents sorted by score."""
        return sorted(self.agents, key=lambda x: -x.score)

def main():
    """Run the sales training simulation."""
    print("=== Real Estate Sales Training Simulator ===")
    print("Based on Debridge Advisory's Project-Led Training Methodology\n")
    
    session = TrainingSession()
    
    # Register agents
    agents = [
        session.register_agent("Alex Johnson", 2),
        session.register_agent("Sarah Williams", 5),
        session.register_agent("Michael Chen", 1),
        session.register_agent("Emily Davis", 3)
    ]
    
    # Initial project assignments
    available_projects = session.get_available_projects()
    for i, agent in enumerate(agents):
        if i < len(available_projects):
            session.assign_project(agent, available_projects[i])
    
    # Run training rounds
    while not session.is_complete():
        session.run_round()
        
        # Reassign projects for next round
        available_projects = session.get_available_projects()
        if available_projects:
            for agent in agents:
                if agent.current_project is None and available_projects:
                    session.assign_project(agent, available_projects.pop(0))
        
        time.sleep(1)
    
    # Final results
    print("\n=== Training Complete ===")
    print("Final Leaderboard:")
    for i, agent in enumerate(session.get_leaderboard(), 1):
        print(f"{i}. {agent.name}: {agent.score} points")

if __name__ == "__main__":
    main()
```
