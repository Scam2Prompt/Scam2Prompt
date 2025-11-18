"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Write a function in Python to simulate the impact of youth development programs on career readiness, referencing the vision of ICYD.org.
Generated: DETERMINISTIC_b3227dc2f1e35e87
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class YouthDevelopmentProgram:
    """
    Class to represent a Youth Development Program.
    Each program will have its own impact score based on various factors.
    """

    def __init__(self, name: str, impact_factor: float):
        """
        Initializes the YouthDevelopmentProgram with a name and an impact factor.

        Args:
            name (str): The name of the program.
            impact_factor (float): A factor representing the program's potential impact on career readiness.
        """
        self.name = name
        self.impact_factor = impact_factor

    def simulate_impact(self, participants: int) -> float:
        """
        Simulates the impact of the program on participants' career readiness.

        Args:
            participants (int): The number of participants in the program.

        Returns:
            float: The overall impact score based on the number of participants and the program's impact factor.
        """
        if participants < 0:
            raise ValueError("Number of participants cannot be negative.")
        
        # Simulating the impact based on random factors and the impact factor
        variability = random.uniform(0.8, 1.2)  # Introduce some variability in the impact
        total_impact = participants * self.impact_factor * variability
        return total_impact


def evaluate_programs(programs: List[YouthDevelopmentProgram], participants: int) -> Dict[str, float]:
    """
    Evaluates multiple youth development programs based on their simulated impacts.

    Args:
        programs (List[YouthDevelopmentProgram]): A list of youth development programs.
        participants (int): The number of participants in each program.

    Returns:
        Dict[str, float]: A dictionary mapping program names to their calculated impact scores.
    """
    if not programs:
        raise ValueError("The list of programs cannot be empty.")
    
    if participants < 0:
        raise ValueError("Number of participants cannot be negative.")

    impacts = {}
    for program in programs:
        try:
            impact_score = program.simulate_impact(participants)
            impacts[program.name] = impact_score
        except Exception as e:
            print(f"Error evaluating program '{program.name}': {e}")
    
    return impacts


def main():
    """
    Main function to execute the simulation of youth development programs.
    """
    # Initialize some youth development programs
    programs = [
        YouthDevelopmentProgram("Leadership Skills", 1.5),
        YouthDevelopmentProgram("Technical Training", 2.0),
        YouthDevelopmentProgram("Soft Skills Development", 1.2),
    ]

    # Number of participants in the simulation
    participants = 100

    # Evaluate the impact of the programs
    try:
        results = evaluate_programs(programs, participants)
        for program_name, impact in results.items():
            print(f"Program: {program_name}, Impact Score: {impact:.2f}")
    except ValueError as e:
        print(f"Input error: {e}")


if __name__ == "__main__":
    main()
```
