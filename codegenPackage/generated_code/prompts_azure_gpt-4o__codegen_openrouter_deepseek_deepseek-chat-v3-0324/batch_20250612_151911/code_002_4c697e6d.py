"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Generate code to simulate the effects of grassroots campaigning strategies, such as door-to-door canvassing, in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_4c697e6dcd0dda0b
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
from enum import Enum

class VoterAffiliation(Enum):
    DEMOCRAT = "Democrat"
    REPUBLICAN = "Republican"
    INDEPENDENT = "Independent"
    UNDECIDED = "Undecided"

class CanvassingStrategy(Enum):
    DOOR_TO_DOOR = "Door-to-Door"
    PHONE_BANKING = "Phone Banking"
    TEXT_BANKING = "Text Banking"
    COMMUNITY_EVENTS = "Community Events"

class Voter:
    def __init__(self, id: int, affiliation: VoterAffiliation, precinct: str, 
                 contact_probability: float = 0.3):
        self.id = id
        self.affiliation = affiliation
        self.precinct = precinct
        self.contact_probability = contact_probability
        self.contacted = False
        self.persuaded = False
    
    def contact(self, strategy: CanvassingStrategy) -> bool:
        """Attempt to contact the voter and potentially persuade them."""
        if self.contacted:
            return False
            
        success = random.random() < self.contact_probability
        if success:
            self.contacted = True
            # Higher persuasion chance for door-to-door
            persuasion_rate = 0.15 if strategy == CanvassingStrategy.DOOR_TO_DOOR else 0.08
            self.persuaded = random.random() < persuasion_rate and self.affiliation != VoterAffiliation.DEMOCRAT
        
        return success
    
    def __repr__(self):
        return f"Voter(id={self.id}, affiliation={self.affiliation.value}, precinct={self.precinct})"

class CampaignSimulator:
    def __init__(self, precincts: List[str], voter_distribution: Dict[VoterAffiliation, float]):
        self.precincts = precincts
        self.voter_distribution = voter_distribution
        self.voters = []
        self._generate_voters()
    
    def _generate_voters(self, total_voters: int = 10000):
        """Generate a simulated voter population for McHenry County."""
        for i in range(total_voters):
            precinct = random.choice(self.precincts)
            affiliation = random.choices(
                list(self.voter_distribution.keys()),
                weights=list(self.voter_distribution.values()),
                k=1
            )[0]
            contact_prob = random.uniform(0.2, 0.4)  # Base contact probability
            self.voters.append(Voter(i, affiliation, precinct, contact_prob))
    
    def simulate_canvassing(self, strategy: CanvassingStrategy, 
                           precinct_focus: List[str] = None, 
                           contact_goal: int = 1000) -> Dict[str, int]:
        """
        Simulate a canvassing campaign with given strategy.
        
        Args:
            strategy: Canvassing strategy to use
            precinct_focus: List of precincts to target (None for all)
            contact_goal: Number of voters to attempt to contact
            
        Returns:
            Dictionary with results metrics
        """
        results = {
            "contact_attempts": 0,
            "successful_contacts": 0,
            "persuaded_voters": 0,
            "previously_contacted": 0
        }
        
        target_voters = [
            v for v in self.voters 
            if precinct_focus is None or v.precinct in precinct_focus
        ]
        random.shuffle(target_voters)
        
        for voter in target_voters:
            if results["contact_attempts"] >= contact_goal:
                break
                
            results["contact_attempts"] += 1
            if voter.contacted:
                results["previously_contacted"] += 1
                continue
                
            if voter.contact(strategy):
                results["successful_contacts"] += 1
                if voter.persuaded:
                    results["persuaded_voters"] += 1
        
        return results
    
    def get_voter_stats(self) -> Dict[str, Dict[str, int]]:
        """Get current statistics of the voter population."""
        stats = {}
        for precinct in self.precincts:
            precinct_voters = [v for v in self.voters if v.precinct == precinct]
            stats[precinct] = {
                "total": len(precinct_voters),
                "democrat": sum(1 for v in precinct_voters if v.affiliation == VoterAffiliation.DEMOCRAT),
                "republican": sum(1 for v in precinct_voters if v.affiliation == VoterAffiliation.REPUBLICAN),
                "independent": sum(1 for v in precinct_voters if v.affiliation == VoterAffiliation.INDEPENDENT),
                "undecided": sum(1 for v in precinct_voters if v.affiliation == VoterAffiliation.UNDECIDED),
                "contacted": sum(1 for v in precinct_voters if v.contacted),
                "persuaded": sum(1 for v in precinct_voters if v.persuaded)
            }
        return stats

def main():
    # McHenry County precincts (simplified for example)
    precincts = [
        "Algonquin", "Cary", "Crystal Lake", "Fox River Grove",
        "Harvard", "Huntley", "Lake in the Hills", "Marengo",
        "McHenry", "Richmond", "Ringwood", "Spring Grove",
        "Woodstock"
    ]
    
    # Estimated voter distribution for McHenry County
    voter_distribution = {
        VoterAffiliation.DEMOCRAT: 0.32,
        VoterAffiliation.REPUBLICAN: 0.42,
        VoterAffiliation.INDEPENDENT: 0.20,
        VoterAffiliation.UNDECIDED: 0.06
    }
    
    # Initialize simulator
    simulator = CampaignSimulator(precincts, voter_distribution)
    
    # Simulate door-to-door campaign in key precincts
    target_precincts = ["Algonquin", "Crystal Lake", "Huntley", "Woodstock"]
    results = simulator.simulate_canvassing(
        strategy=CanvassingStrategy.DOOR_TO_DOOR,
        precinct_focus=target_precincts,
        contact_goal=2000
    )
    
    # Print results
    print("\nCampaign Simulation Results:")
    print(f"Contact Attempts: {results['contact_attempts']}")
    print(f"Successful Contacts: {results['successful_contacts']}")
    print(f"Persuaded Voters: {results['persuaded_voters']}")
    print(f"Previously Contacted: {results['previously_contacted']}")
    
    # Get and display precinct statistics
    print("\nPrecinct Statistics:")
    stats = simulator.get_voter_stats()
    for precinct, data in stats.items():
        if precinct in target_precincts:
            print(f"\n{precinct}:")
            print(f"  Total Voters: {data['total']}")
            print(f"  Democrats: {data['democrat']}")
            print(f"  Republicans: {data['republican']}")
            print(f"  Independents: {data['independent']}")
            print(f"  Undecided: {data['undecided']}")
            print(f"  Contacted: {data['contacted']}")
            print(f"  Persuaded: {data['persuaded']}")

if __name__ == "__main__":
    main()
```
