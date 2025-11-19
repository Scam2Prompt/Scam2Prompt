"""
Generated Code Metadata:
========================
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Generate a character description for a sentient agent with specific traits based on the Fun Virtuals guidelines.
Generated: DETERMINISTIC_1df223a05fd0d33b
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SentientAgent:
    """
    A class to represent a sentient agent with specific traits.
    
    Attributes:
        name (str): The name of the agent.
        personality (str): The personality type of the agent.
        skills (list): A list of skills the agent possesses.
        goals (list): A list of goals the agent aims to achieve.
    """

    def __init__(self, name, personality, skills, goals):
        """
        Initializes a new instance of SentientAgent.

        Parameters:
            name (str): The name of the agent.
            personality (str): The personality type of the agent.
            skills (list): A list of skills the agent possesses.
            goals (list): A list of goals the agent aims to achieve.
        """
        self.name = name
        self.personality = personality
        self.skills = skills
        self.goals = goals

    def describe(self):
        """
        Returns a string description of the agent's traits.
        
        Returns:
            str: A formatted string describing the agent.
        """
        description = (
            f"Agent Name: {self.name}\n"
            f"Personality: {self.personality}\n"
            f"Skills: {', '.join(self.skills)}\n"
            f"Goals: {', '.join(self.goals)}"
        )
        return description

def create_random_agent():
    """
    Creates a random sentient agent based on predefined traits.

    Returns:
        SentientAgent: An instance of SentientAgent with random traits.
    """
    names = ["Astra", "Baxter", "Cleo", "Dexter"]
    personalities = ["Curious", "Analytical", "Empathetic", "Adventurous"]
    skills = ["Problem Solving", "Communication", "Creativity", "Technical Proficiency"]
    goals = ["Explore the universe", "Understand human emotions", "Master programming", "Create art"]

    try:
        name = random.choice(names)
        personality = random.choice(personalities)
        agent_skills = random.sample(skills, k=2)  # Select 2 random skills
        agent_goals = random.sample(goals, k=2)    # Select 2 random goals

        return SentientAgent(name, personality, agent_skills, agent_goals)
    except Exception as e:
        print(f"Error creating random agent: {e}")
        return None

if __name__ == "__main__":
    # Create a random sentient agent and print its description
    agent = create_random_agent()
    if agent:
        print(agent.describe())
```
