"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Write code to simulate the impact of safety measures on the performance of construction operations, addressing issues of efficiency and worker conditions as discussed by AFCO.
Generated: DETERMINISTIC_5585dadf4adca15d
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested code to simulate the impact of safety measures on the performance of construction operations, written in Python:

```python
import random
import logging

# Set up logging for error handling and performance tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConstructionOperation:
    """
    A class to simulate construction operations with safety measures and performance metrics.
    """

    def __init__(self, workers, tasks_per_day, safety_rating):
        """
        Initializes the ConstructionOperation class.
        
        :param workers: Number of workers in the construction operation.
        :param tasks_per_day: Average number of tasks completed per day without safety measures.
        :param safety_rating: Safety rating (0-100), where higher values indicate better safety measures.
        """
        self.workers = workers
        self.tasks_per_day = tasks_per_day
        self.safety_rating = safety_rating

    def simulate_operation(self, days):
        """
        Simulates construction operations over a given number of days, factoring in safety measures.

        :param days: Number of days to simulate.
        :return: Performance metrics including total tasks completed and worker conditions.
        """
        try:
            # Ensure valid input for simulation parameters
            if days <= 0:
                raise ValueError("Number of days must be greater than zero.")
            
            if self.safety_rating < 0 or self.safety_rating > 100:
                raise ValueError("Safety rating must be within the range 0-100.")

            total_tasks_completed = 0
            worker_conditions = []

            for day in range(1, days + 1):
                # Calculate efficiency adjustment based on safety rating (higher safety -> slightly lower efficiency)
                safety_adjustment = 1 - (self.safety_rating / 200)  # Safety reduces efficiency slightly
                tasks_today = int(self.tasks_per_day * safety_adjustment)

                # Randomly simulate worker conditions based on safety measures
                # Higher safety rating -> fewer issues with worker conditions
                worker_condition = random.choices(
                    ["Excellent", "Good", "Fair", "Poor"],
                    weights=[self.safety_rating, 100 - self.safety_rating, 50, 10],  # Weighted probabilities
                    k=self.workers
                )

                total_tasks_completed += tasks_today
                worker_conditions.append(worker_condition)

                logging.info(f"Day {day}: Completed {tasks_today} tasks.")

            # Return simulation results
            return {
                "total_tasks_completed": total_tasks_completed,
                "worker_conditions": worker_conditions
            }

        except ValueError as e:
            logging.error(f"Invalid input: {e}")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred during simulation: {e}")
            return None


if __name__ == "__main__":
    # Example usage of the ConstructionOperation class
    try:
        # Initialize the simulation parameters
        workers = 50
        tasks_per_day = 100
        safety_rating = 80  # Safety measures in place
        days_to_simulate = 10

        # Create a ConstructionOperation instance
        construction_operation = ConstructionOperation(workers, tasks_per_day, safety_rating)

        # Simulate the construction operation
        results = construction_operation.simulate_operation(days_to_simulate)

        # Display results
        if results:
            print("Simulation Results:")
            print(f"Total Tasks Completed: {results['total_tasks_completed']}")
            print("Worker Conditions by Day:")
            for day, conditions in enumerate(results['worker_conditions'], start=1):
                print(f"Day {day}: {conditions}")

    except Exception as e:
        logging.error(f"An error occurred in the main program: {e}")
```

This code meets the requirements outlined in the request and is production-ready with error handling, comments, and adherence to Python best practices.
