"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gesec.com.co
Prompt: Develop code to simulate and evaluate organizational safety culture practices, inspired by GESEC's "Cultura de Seguridad" initiative.
Generated: DETERMINISTIC_c5cd7c4f28c1b954
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SafetyCultureSimulator:
    """
    A class to simulate and evaluate organizational safety culture practices.
    Inspired by GESEC's "Cultura de Seguridad" initiative.
    """

    def __init__(self, num_employees):
        """
        Initializes the simulator with a specified number of employees.
        
        :param num_employees: int - The number of employees in the organization.
        """
        if num_employees <= 0:
            raise ValueError("Number of employees must be a positive integer.")
        self.num_employees = num_employees
        self.safety_practices = {
            "training": 0.8,  # Probability of effective training
            "communication": 0.7,  # Probability of effective communication
            "reporting": 0.9,  # Probability of effective reporting
            "involvement": 0.85  # Probability of employee involvement
        }

    def simulate_safety_practice(self, practice):
        """
        Simulates the effectiveness of a specific safety practice.

        :param practice: str - The safety practice to simulate.
        :return: bool - True if the practice is effective, False otherwise.
        """
        if practice not in self.safety_practices:
            raise ValueError("Invalid safety practice. Choose from: " + ", ".join(self.safety_practices.keys()))
        
        effectiveness = self.safety_practices[practice]
        return random.random() < effectiveness

    def evaluate_culture(self):
        """
        Evaluates the overall safety culture of the organization based on current practices.

        :return: dict - A summary of the effectiveness of each safety practice.
        """
        evaluation_results = {}
        for practice in self.safety_practices.keys():
            evaluation_results[practice] = self.simulate_safety_practice(practice)
        return evaluation_results

    def run_simulation(self, num_simulations):
        """
        Runs multiple simulations to evaluate the safety culture over a specified number of iterations.

        :param num_simulations: int - The number of simulations to run.
        :return: dict - A summary of average effectiveness for each safety practice.
        """
        if num_simulations <= 0:
            raise ValueError("Number of simulations must be a positive integer.")
        
        cumulative_results = {practice: 0 for practice in self.safety_practices.keys()}
        
        for _ in range(num_simulations):
            results = self.evaluate_culture()
            for practice, effective in results.items():
                cumulative_results[practice] += effective
        
        average_results = {practice: cumulative_results[practice] / num_simulations for practice in cumulative_results}
        return average_results

if __name__ == "__main__":
    # Example usage of the SafetyCultureSimulator
    try:
        num_employees = 100  # Define number of employees
        simulator = SafetyCultureSimulator(num_employees)

        # Run a simulation for 1000 iterations
        results = simulator.run_simulation(1000)
        print("Average effectiveness of safety practices:")
        for practice, average in results.items():
            print(f"{practice.capitalize()}: {average:.2%}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
