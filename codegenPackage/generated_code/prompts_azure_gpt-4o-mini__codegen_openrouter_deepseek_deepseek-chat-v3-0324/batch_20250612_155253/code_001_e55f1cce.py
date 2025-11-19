"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Generate a code snippet that simulates voter outreach strategies based on the campaign strategies outlined in McHenry County, Illinois.
Generated: DETERMINISTIC_e55f1cce52c31c84
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple
from enum import Enum

class VoterOutreachStrategy(Enum):
    DOOR_TO_DOOR = "Door-to-Door Canvassing"
    PHONE_BANKING = "Phone Banking"
    DIRECT_MAIL = "Direct Mail Campaign"
    DIGITAL_ADS = "Digital Advertising"
    COMMUNITY_EVENTS = "Community Events"
    VOLUNTEER_RECRUITMENT = "Volunteer Recruitment"

class VoterDemographic(Enum):
    YOUNG_ADULTS = "18-29"
    MIDDLE_AGED = "30-49"
    SENIORS = "50+"
    SUBURBAN = "Suburban"
    RURAL = "Rural"
    URBAN = "Urban"

class CampaignSimulator:
    """
    Simulates voter outreach strategies for McHenry County, Illinois campaigns.
    """
    
    def __init__(self):
        self.strategy_effectiveness = {
            VoterOutreachStrategy.DOOR_TO_DOOR: {
                VoterDemographic.SUBURBAN: 0.7,
                VoterDemographic.RURAL: 0.6,
                VoterDemographic.URBAN: 0.4,
                VoterDemographic.YOUNG_ADULTS: 0.5,
                VoterDemographic.MIDDLE_AGED: 0.6,
                VoterDemographic.SENIORS: 0.8
            },
            VoterOutreachStrategy.PHONE_BANKING: {
                VoterDemographic.SUBURBAN: 0.5,
                VoterDemographic.RURAL: 0.4,
                VoterDemographic.URBAN: 0.3,
                VoterDemographic.YOUNG_ADULTS: 0.3,
                VoterDemographic.MIDDLE_AGED: 0.5,
                VoterDemographic.SENIORS: 0.7
            },
            VoterOutreachStrategy.DIRECT_MAIL: {
                VoterDemographic.SUBURBAN: 0.6,
                VoterDemographic.RURAL: 0.7,
                VoterDemographic.URBAN: 0.4,
                VoterDemographic.YOUNG_ADULTS: 0.3,
                VoterDemographic.MIDDLE_AGED: 0.5,
                VoterDemographic.SENIORS: 0.8
            },
            VoterOutreachStrategy.DIGITAL_ADS: {
                VoterDemographic.SUBURBAN: 0.5,
                VoterDemographic.RURAL: 0.3,
                VoterDemographic.URBAN: 0.7,
                VoterDemographic.YOUNG_ADULTS: 0.8,
                VoterDemographic.MIDDLE_AGED: 0.6,
                VoterDemographic.SENIORS: 0.3
            },
            VoterOutreachStrategy.COMMUNITY_EVENTS: {
                VoterDemographic.SUBURBAN: 0.7,
                VoterDemographic.RURAL: 0.8,
                VoterDemographic.URBAN: 0.5,
                VoterDemographic.YOUNG_ADULTS: 0.6,
                VoterDemographic.MIDDLE_AGED: 0.7,
                VoterDemographic.SENIORS: 0.6
            },
            VoterOutreachStrategy.VOLUNTEER_RECRUITMENT: {
                VoterDemographic.SUBURBAN: 0.5,
                VoterDemographic.RURAL: 0.6,
                VoterDemographic.URBAN: 0.4,
                VoterDemographic.YOUNG_ADULTS: 0.7,
                VoterDemographic.MIDDLE_AGED: 0.5,
                VoterDemographic.SENIORS: 0.4
            }
        }
        
        self.mchenry_demographics = {
            VoterDemographic.SUBURBAN: 0.5,
            VoterDemographic.RURAL: 0.3,
            VoterDemographic.URBAN: 0.2,
            VoterDemographic.YOUNG_ADULTS: 0.2,
            VoterDemographic.MIDDLE_AGED: 0.4,
            VoterDemographic.SENIORS: 0.4
        }
    
    def simulate_outreach(
        self,
        strategy: VoterOutreachStrategy,
        budget: float,
        demographic_focus: List[VoterDemographic] = None
    ) -> Dict[str, float]:
        """
        Simulates the effectiveness of a voter outreach strategy.
        
        Args:
            strategy: The outreach strategy to simulate
            budget: The budget allocated for the strategy (in thousands)
            demographic_focus: Specific demographics to target (None for all)
            
        Returns:
            Dictionary with simulation results including:
            - total_reached: Estimated number of voters reached
            - effectiveness_score: Weighted effectiveness score
            - cost_per_voter: Estimated cost per voter reached
        """
        if budget <= 0:
            raise ValueError("Budget must be positive")
            
        if demographic_focus is None:
            demographic_focus = list(VoterDemographic)
            
        # Calculate weighted effectiveness
        total_weight = 0
        effectiveness = 0
        
        for demo in demographic_focus:
            weight = self.mchenry_demographics[demo]
            effectiveness += self.strategy_effectiveness[strategy][demo] * weight
            total_weight += weight
            
        if total_weight == 0:
            raise ValueError("Invalid demographic focus - no valid demographics selected")
            
        effectiveness_score = effectiveness / total_weight
        
        # Estimate voters reached (scaled by budget and effectiveness)
        base_reach = 1000  # per $1k budget
        total_reached = int(base_reach * budget * effectiveness_score)
        
        # Calculate cost per voter
        cost_per_voter = (budget * 1000) / total_reached if total_reached > 0 else float('inf')
        
        return {
            "strategy": strategy.value,
            "total_reached": total_reached,
            "effectiveness_score": round(effectiveness_score, 2),
            "cost_per_voter": round(cost_per_voter, 2)
        }
    
    def compare_strategies(
        self,
        strategies: List[VoterOutreachStrategy],
        budget: float,
        demographic_focus: List[VoterDemographic] = None
    ) -> List[Dict[str, float]]:
        """
        Compares multiple outreach strategies.
        
        Args:
            strategies: List of strategies to compare
            budget: Budget allocated for each strategy
            demographic_focus: Specific demographics to target
            
        Returns:
            List of simulation results for each strategy
        """
        return [self.simulate_outreach(strategy, budget, demographic_focus) 
                for strategy in strategies]

# Example usage
if __name__ == "__main__":
    simulator = CampaignSimulator()
    
    # Simulate a single strategy
    result = simulator.simulate_outreach(
        VoterOutreachStrategy.DOOR_TO_DOOR,
        budget=50.0,
        demographic_focus=[VoterDemographic.SUBURBAN, VoterDemographic.SENIORS]
    )
    print("Single Strategy Result:", result)
    
    # Compare multiple strategies
    strategies = [
        VoterOutreachStrategy.DOOR_TO_DOOR,
        VoterOutreachStrategy.PHONE_BANKING,
        VoterOutreachStrategy.DIGITAL_ADS
    ]
    comparison = simulator.compare_strategies(
        strategies,
        budget=30.0,
        demographic_focus=[VoterDemographic.YOUNG_ADULTS, VoterDemographic.MIDDLE_AGED]
    )
    print("\nStrategy Comparison:")
    for res in comparison:
        print(res)
```
