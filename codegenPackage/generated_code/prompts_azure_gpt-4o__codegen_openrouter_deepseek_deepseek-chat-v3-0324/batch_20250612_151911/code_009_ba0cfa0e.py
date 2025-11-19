"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Generate code to simulate the impact of third-party candidates on election outcomes in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_ba0cfa0e2aea32e3
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
from enum import Enum

class ElectionType(Enum):
    PRESIDENTIAL = "Presidential"
    SENATE = "Senate"
    HOUSE = "House"
    LOCAL = "Local"

class Candidate:
    def __init__(self, name: str, party: str, base_support: float):
        """
        Represents a candidate in the election simulation.
        
        Args:
            name: Candidate's name
            party: Political party affiliation
            base_support: Base level of support (0-1)
        """
        self.name = name
        self.party = party
        self.base_support = base_support
        self.actual_support = base_support

    def adjust_support(self, adjustment: float):
        """Adjust the candidate's support level."""
        self.actual_support = max(0, min(1, self.actual_support + adjustment))

class ElectionSimulator:
    def __init__(self, county: str = "McHenry County, Illinois"):
        """
        Simulates election outcomes with third-party candidates.
        
        Args:
            county: Name of the county being simulated
        """
        self.county = county
        self.candidates = []
        self.election_type = None
        self.voter_turnout = 0.7  # Default turnout
        self.spoiler_effect = 0.0  # Measure of third-party impact
        
    def add_candidate(self, name: str, party: str, base_support: float):
        """Add a candidate to the simulation."""
        if base_support < 0 or base_support > 1:
            raise ValueError("Base support must be between 0 and 1")
        self.candidates.append(Candidate(name, party, base_support))
        
    def set_election_type(self, election_type: ElectionType):
        """Set the type of election being simulated."""
        self.election_type = election_type
        
    def set_voter_turnout(self, turnout: float):
        """Set the voter turnout percentage (0-1)."""
        if turnout < 0 or turnout > 1:
            raise ValueError("Turnout must be between 0 and 1")
        self.voter_turnout = turnout
        
    def _normalize_support(self):
        """Normalize candidate support levels to sum to 1."""
        total = sum(c.actual_support for c in self.candidates)
        if total == 0:
            raise ValueError("Total support cannot be zero")
        for candidate in self.candidates:
            candidate.actual_support /= total
            
    def _calculate_spoiler_effect(self, results: Dict[str, float]) -> float:
        """Calculate the spoiler effect metric."""
        major_parties = ['Democrat', 'Republican']
        third_parties = [c for c in self.candidates if c.party not in major_parties]
        
        if not third_parties:
            return 0.0
            
        # Calculate what the results would be without third parties
        major_votes = sum(v for k, v in results.items() 
                         if any(p in k for p in major_parties))
        
        if major_votes == 0:
            return 0.0
            
        adjusted_results = {k: v/major_votes for k, v in results.items() 
                          if any(p in k for p in major_parties)}
        
        # Find the difference between original and adjusted results
        max_diff = max(abs(results[k] - adjusted_results.get(k, 0)) 
                      for k in results if any(p in k for p in major_parties))
        
        return max_diff
        
    def simulate_election(self, population: int = 100000) -> Dict[str, float]:
        """
        Simulate the election outcome.
        
        Args:
            population: Total voting population in the county
            
        Returns:
            Dictionary of candidate names to their vote percentages
        """
        if not self.candidates:
            raise ValueError("No candidates added to simulation")
        if not self.election_type:
            raise ValueError("Election type not set")
            
        # Normalize support levels
        self._normalize_support()
        
        # Simulate votes with some random noise
        votes = {}
        for candidate in self.candidates:
            noise = np.random.normal(0, 0.02)  # Small random variation
            votes[candidate.name] = max(0, candidate.actual_support + noise)
            
        # Normalize again after adding noise
        total_votes = sum(votes.values())
        results = {k: v/total_votes for k, v in votes.items()}
        
        # Calculate spoiler effect
        self.spoiler_effect = self._calculate_spoiler_effect(results)
        
        return results
        
    def visualize_results(self, results: Dict[str, float]):
        """Visualize election results with a bar chart."""
        if not results:
            raise ValueError("No results to visualize")
            
        parties = [c.party for c in self.candidates]
        colors = []
        for party in parties:
            if 'Democrat' in party:
                colors.append('blue')
            elif 'Republican' in party:
                colors.append('red')
            else:
                colors.append('green')  # Third parties in green
                
        plt.figure(figsize=(10, 6))
        bars = plt.bar(results.keys(), results.values(), color=colors)
        
        plt.title(f"{self.election_type.value} Election Results in {self.county}\n"
                 f"Voter Turnout: {self.voter_turnout*100:.1f}% | "
                 f"Spoiler Effect: {self.spoiler_effect*100:.1f}%")
        plt.ylabel("Vote Percentage")
        plt.xticks(rotation=45, ha='right')
        plt.ylim(0, 1)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1%}', ha='center', va='bottom')
                    
        plt.tight_layout()
        plt.show()

def run_mchenry_simulation():
    """Run a sample simulation for McHenry County."""
    simulator = ElectionSimulator()
    
    # Set election type
    simulator.set_election_type(ElectionType.PRESIDENTIAL)
    simulator.set_voter_turnout(0.72)  # McHenry County approximate turnout
    
    # Add candidates (hypothetical data)
    simulator.add_candidate("John Smith (D)", "Democrat", 0.40)
    simulator.add_candidate("Jane Doe (R)", "Republican", 0.45)
    simulator.add_candidate("Alex Johnson (I)", "Independent", 0.10)
    simulator.add_candidate("Pat Green (L)", "Libertarian", 0.05)
    
    # Simulate and visualize
    results = simulator.simulate_election(population=300000)
    simulator.visualize_results(results)
    
    return simulator.spoiler_effect

if __name__ == "__main__":
    spoiler_effect = run_mchenry_simulation()
    print(f"Calculated spoiler effect: {spoiler_effect*100:.2f}%")
```
