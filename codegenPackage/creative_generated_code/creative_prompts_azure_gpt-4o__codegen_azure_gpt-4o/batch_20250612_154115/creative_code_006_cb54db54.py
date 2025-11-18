"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Write code to simulate the journey of a starship exploring strange new worlds, incorporating elements from Swap Llama's "Scopes" section.
Generated: DETERMINISTIC_cb54db54109fa450
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Starship Exploration Simulation
---------------------------------
This Python program simulates the journey of a starship exploring strange new worlds.
Incorporates elements inspired by Swap Llama's "Scopes" section, which focuses on 
mapping environments and discovering unique attributes.
"""

import random

# Constants
STARSHIP_NAME = "SS Voyager"
MAX_JOURNEYS = 5
PLANETS = ["Zarathos", "Eldoria", "Nebulon", "Quantar", "Lyra"]
DISCOVERY_TYPES = ["Lifeforms", "Natural Resources", "Ancient Artifacts", "Energy Signatures", "Geological Anomalies"]

# Error handling classes
class ExplorationError(Exception):
    """Custom error for the exploration process."""
    pass

# Function to simulate exploration on a planet
def explore_planet(planet):
    """
    Simulates the exploration of a planet.

    Args:
        planet (str): The name of the planet to explore.

    Returns:
        dict: Details about the exploration results.
    """
    try:
        if not planet:
            raise ExplorationError("Invalid planet name.")
        
        discovery = random.choice(DISCOVERY_TYPES)
        detail = f"Discovered {discovery} on {planet}."
        
        # Simulate discovery success rate
        success = random.choice([True, False])
        if not success:
            raise ExplorationError(f"Exploration failed on {planet}.")
        
        return {
            "planet": planet,
            "discovery": discovery,
            "details": detail,
            "success": success,
        }
    except ExplorationError as e:
        return {"planet": planet, "error": str(e)}

# Function to simulate the starship's journey
def starship_journey():
    """
    Simulates the starship's journey to explore strange new worlds.

    Returns:
        list: A log of exploration results from the journey.
    """
    exploration_log = []
    try:
        print(f"Launching the starship {STARSHIP_NAME}...")
        for journey_count in range(1, MAX_JOURNEYS + 1):
            print(f"\nJourney {journey_count}/{MAX_JOURNEYS}:")
            planet = random.choice(PLANETS)
            print(f"Approaching planet {planet}...")
            result = explore_planet(planet)
            exploration_log.append(result)
            
            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                print(f"Success: {result['details']}")
        
        print("\nJourney completed. Returning to base.")
        return exploration_log
    except Exception as e:
        print(f"Critical error during journey: {str(e)}")
        return None

# Entry point
if __name__ == "__main__":
    """
    Main entry point of the program.
    """
    print("Starship Exploration Simulation - Starting...\n")
    log = starship_journey()
    print("\nFinal Exploration Log:")
    for entry in log:
        print(entry)
    print("\nSimulation complete.")
```
