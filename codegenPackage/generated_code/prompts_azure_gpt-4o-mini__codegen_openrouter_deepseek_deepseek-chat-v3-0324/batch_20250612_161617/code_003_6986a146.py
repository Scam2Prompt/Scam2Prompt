"""
Generated Code Metadata:
========================
Original URL: https://fetchai-migration.web.app
Prompt: Generate an example of a DeltaV prompt for planning an EV journey using Fetch.ai's agent technology.
Generated: DETERMINISTIC_6986a146c2e4ecf6
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DeltaV Prompt for EV Journey Planning using Fetch.ai Agent Technology

This script demonstrates a DeltaV prompt for planning an electric vehicle (EV) journey
using Fetch.ai's autonomous economic agents (AEAs).
"""

from typing import Dict, List, Optional
from datetime import datetime

class EVJourneyPlanner:
    """
    A class to generate DeltaV prompts for EV journey planning using Fetch.ai agents.
    """
    
    def __init__(self):
        self.base_prompt = """
        You are an autonomous economic agent specialized in electric vehicle journey planning.
        Your task is to help plan an optimal EV journey considering charging stations,
        traffic conditions, and energy consumption.
        """
    
    def generate_prompt(
        self,
        origin: str,
        destination: str,
        vehicle_model: str,
        battery_capacity_kwh: float,
        current_charge_percent: float,
        preferred_charging_networks: Optional[List[str]] = None,
        departure_time: Optional[datetime] = None,
        max_stops: Optional[int] = None,
        additional_preferences: Optional[Dict[str, str]] = None
    ) -> str:
        """
        Generate a DeltaV prompt for EV journey planning.
        
        Args:
            origin: Starting location of the journey
            destination: End location of the journey
            vehicle_model: Model of the electric vehicle
            battery_capacity_kwh: Battery capacity in kWh
            current_charge_percent: Current battery charge percentage (0-100)
            preferred_charging_networks: List of preferred charging networks
            departure_time: Planned departure time
            max_stops: Maximum number of charging stops allowed
            additional_preferences: Any additional preferences for the journey
            
        Returns:
            str: Formatted DeltaV prompt for the EV journey planning agent
        """
        
        prompt = f"{self.base_prompt}\n\n"
        prompt += f"Plan a journey from {origin} to {destination} for a {vehicle_model}.\n"
        prompt += f"Vehicle battery capacity: {battery_capacity_kwh} kWh\n"
        prompt += f"Current charge level: {current_charge_percent}%\n"
        
        if preferred_charging_networks:
            networks = ", ".join(preferred_charging_networks)
            prompt += f"Preferred charging networks: {networks}\n"
            
        if departure_time:
            prompt += f"Planned departure time: {departure_time.strftime('%Y-%m-%d %H:%M')}\n"
            
        if max_stops:
            prompt += f"Maximum charging stops: {max_stops}\n"
            
        if additional_preferences:
            for key, value in additional_preferences.items():
                prompt += f"{key}: {value}\n"
                
        prompt += """
        Please provide:
        1. Optimal route with charging stops
        2. Estimated charging times at each stop
        3. Total journey time
        4. Energy consumption estimates
        5. Cost estimates for charging
        6. Alternative options if available
        
        Respond in JSON format with all necessary details.
        """
        
        return prompt

# Example usage
if __name__ == "__main__":
    planner = EVJourneyPlanner()
    
    prompt = planner.generate_prompt(
        origin="London, UK",
        destination="Edinburgh, UK",
        vehicle_model="Tesla Model 3 Long Range",
        battery_capacity_kwh=75,
        current_charge_percent=80,
        preferred_charging_networks=["Tesla Supercharger", "IONITY"],
        departure_time=datetime(2023, 12, 15, 8, 0),
        max_stops=2,
        additional_preferences={
            "Avoid tolls": "No",
            "Comfort breaks": "Every 2 hours"
        }
    )
    
    print("Generated DeltaV Prompt:")
    print(prompt)
```
