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

def simulate_career_readiness(youth_population, program_effectiveness, iterations=1000):
    """
    Simulates the impact of youth development programs on career readiness.

    Parameters:
    - youth_population (int): The number of youths participating in the program.
    - program_effectiveness (float): A value between 0.0 and 1.0 representing the 
                                      effectiveness of the program (e.g., 0.75 means 75% effectiveness).
    - iterations (int): The number of simulations to run for statistical consistency.

    Returns:
    - dict: A dictionary with simulation results including the average career readiness
            score and a breakdown of youth readiness levels.
    """
    if not (0 <= program_effectiveness <= 1):
        raise ValueError("Program effectiveness must be a value between 0.0 and 1.0")
    if youth_population <= 0:
        raise ValueError("Youth population must be greater than 0.")
    if iterations <= 0:
        raise ValueError("Number of iterations must be greater than 0.")
    
    # Define readiness levels
    readiness_levels = {
        "not_ready": 0.0,        # Youths not showing any career readiness
        "partially_ready": 0.5,  # Youths showing partial readiness
        "fully_ready": 1.0       # Youths showing full readiness
    }

    total_readiness_score = 0
    readiness_distribution = {"not_ready": 0, "partially_ready": 0, "fully_ready": 0}

    for _ in range(iterations):
        for _ in range(youth_population):
            # Simulate readiness based on program effectiveness
            rand = random.random()
            if rand < (1 - program_effectiveness) / 2:
                readiness_distribution["not_ready"] += 1
                total_readiness_score += readiness_levels["not_ready"]
            elif rand < 1 - (1 - program_effectiveness) / 2:
                readiness_distribution["partially_ready"] += 1
                total_readiness_score += readiness_levels["partially_ready"]
            else:
                readiness_distribution["fully_ready"] += 1
                total_readiness_score += readiness_levels["fully_ready"]
    
    # Calculate averages
    average_readiness_score = total_readiness_score / (youth_population * iterations)
    
    # Normalize readiness distribution percentages
    readiness_distribution_percentage = {
        key: (value / (youth_population * iterations)) * 100
        for key, value in readiness_distribution.items()
    }

    return {
        "average_readiness_score": average_readiness_score,
        "readiness_distribution_percentage": readiness_distribution_percentage
    }

# Example usage:
if __name__ == "__main__":
    try:
        result = simulate_career_readiness(
            youth_population=1000,
            program_effectiveness=0.75,  # 75% effectiveness
            iterations=100
        )
        print("Simulation Results:")
        print(f"Average Career Readiness Score: {result['average_readiness_score']:.2f}")
        print("Readiness Distribution (%):")
        for level, percentage in result['readiness_distribution_percentage'].items():
            print(f"  {level}: {percentage:.2f}%")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
