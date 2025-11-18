"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Write code to simulate the response time of a sprinkler system in reducing heat, flames, and smoke during a fire, based on the benefits outlined by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_bbdd1c249346f0ac
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
import time
import logging

# Configure logging to capture system events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SprinklerSystem:
    def __init__(self, response_time_average: float, effectiveness: float):
        """
        Initializes the SprinklerSystem with average response time and effectiveness.

        :param response_time_average: Average time (in seconds) for the sprinkler system to activate
        :param effectiveness: Effectiveness of the system in reducing heat, flames, and smoke (0 to 1)
        """
        self.response_time_average = response_time_average
        self.effectiveness = effectiveness

    def simulate_response(self):
        """
        Simulates the response of the sprinkler system during a fire event.

        :return: A dictionary containing the response time, heat reduction, flame reduction, and smoke reduction
        """
        try:
            # Simulate the response time, which can vary around the average
            response_time = random.uniform(self.response_time_average - 2, self.response_time_average + 2)
            
            # Simulate the reduction in heat, flames, and smoke based on effectiveness
            heat_reduction = self.effectiveness * random.uniform(0.7, 1.0)  # Heat reduction percentage
            flame_reduction = self.effectiveness * random.uniform(0.6, 0.9) # Flame reduction percentage
            smoke_reduction = self.effectiveness * random.uniform(0.5, 0.8)  # Smoke reduction percentage
            
            # Log the details
            logging.info(f"Sprinkler activated after {response_time:.2f} seconds.")
            logging.info(f"Heat reduced by {heat_reduction:.2%}, flames reduced by {flame_reduction:.2%}, smoke reduced by {smoke_reduction:.2%}.")
            
            return {
                "response_time": response_time,
                "heat_reduction": heat_reduction,
                "flame_reduction": flame_reduction,
                "smoke_reduction": smoke_reduction
            }
        except Exception as e:
            logging.error(f"Error simulating sprinkler response: {e}")
            return None


def main():
    """
    Main function to run the sprinkler simulation.
    """
    # Average response time in seconds and effectiveness of the sprinkler system
    average_response_time = 10.0  # Example average response time
    effectiveness = 0.85            # Example effectiveness (85%)

    # Create a SprinklerSystem instance
    sprinkler = SprinklerSystem(response_time_average=average_response_time, effectiveness=effectiveness)

    # Simulate the sprinkler system response
    response = sprinkler.simulate_response()
    
    if response:
        # Print the simulation results
        print("Sprinkler System Response:")
        print(f"Response Time: {response['response_time']:.2f} seconds")
        print(f"Heat Reduction: {response['heat_reduction']:.2%}")
        print(f"Flame Reduction: {response['flame_reduction']:.2%}")
        print(f"Smoke Reduction: {response['smoke_reduction']:.2%}")

if __name__ == "__main__":
    main()
```
