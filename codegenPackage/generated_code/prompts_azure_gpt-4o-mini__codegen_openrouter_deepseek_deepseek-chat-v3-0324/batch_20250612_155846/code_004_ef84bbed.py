"""
Generated Code Metadata:
========================
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Explain how the community-driven venture capital model works in the context of aixCB Staking.
Generated: DETERMINISTIC_ef84bbeda616d72f
Batch ID: 20250612_155846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script simulates a community-driven venture capital model for aixCB Staking
# It includes staking, voting, and fund allocation mechanisms

from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum
import random

class ProjectStatus(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    FUNDED = 4

@dataclass
class Project:
    id: str
    name: str
    description: str
    requested_amount: float
    status: ProjectStatus = ProjectStatus.PENDING
    votes_for: int = 0
    votes_against: int = 0

@dataclass
class Staker:
    address: str
    staked_amount: float
    voting_power: float = 0.0
    voted_projects: Dict[str, bool] = None  # project_id: vote (True=for, False=against)

    def __post_init__(self):
        if self.voted_projects is None:
            self.voted_projects = {}

class CommunityVC:
    def __init__(self, staking_token: str):
        self.staking_token = staking_token
        self.total_staked = 0.0
        self.available_funds = 0.0
        self.stakers: Dict[str, Staker] = {}
        self.projects: Dict[str, Project] = {}
        self.funded_projects: List[Project] = []
        
    def stake_tokens(self, address: str, amount: float) -> bool:
        """Stake tokens to participate in the VC model"""
        if amount <= 0:
            return False
            
        if address in self.stakers:
            self.stakers[address].staked_amount += amount
        else:
            self.stakers[address] = Staker(address=address, staked_amount=amount)
            
        self.total_staked += amount
        self._update_voting_powers()
        return True
        
    def unstake_tokens(self, address: str, amount: float) -> bool:
        """Unstake tokens from the VC model"""
        if address not in self.stakers or amount <= 0:
            return False
            
        if self.stakers[address].staked_amount < amount:
            return False
            
        self.stakers[address].staked_amount -= amount
        self.total_staked -= amount
        
        if self.stakers[address].staked_amount == 0:
            del self.stakers[address]
            
        self._update_voting_powers()
        return True
        
    def _update_voting_powers(self) -> None:
        """Update voting power for all stakers based on their stake"""
        if self.total_staked == 0:
            return
            
        for staker in self.stakers.values():
            staker.voting_power = staker.staked_amount / self.total_staked
            
    def submit_project(self, project: Project) -> bool:
        """Submit a new project for community consideration"""
        if project.id in self.projects:
            return False
            
        self.projects[project.id] = project
        return True
        
    def vote_on_project(self, address: str, project_id: str, vote_for: bool) -> bool:
        """Cast a vote on a project"""
        if (address not in self.stakers or 
            project_id not in self.projects or 
            project_id in self.stakers[address].voted_projects):
            return False
            
        project = self.projects[project_id]
        if project.status != ProjectStatus.PENDING:
            return False
            
        voting_power = self.stakers[address].voting_power
        
        if vote_for:
            project.votes_for += voting_power
        else:
            project.votes_against += voting_power
            
        self.stakers[address].voted_projects[project_id] = vote_for
        return True
        
    def finalize_voting(self, project_id: str) -> bool:
        """Finalize voting and update project status"""
        if project_id not in self.projects:
            return False
            
        project = self.projects[project_id]
        if project.status != ProjectStatus.PENDING:
            return False
            
        if project.votes_for > project.votes_against:
            project.status = ProjectStatus.APPROVED
        else:
            project.status = ProjectStatus.REJECTED
            
        return True
        
    def fund_project(self, project_id: str) -> bool:
        """Allocate funds to an approved project"""
        if (project_id not in self.projects or 
            self.projects[project_id].status != ProjectStatus.APPROVED or
            self.available_funds < self.projects[project_id].requested_amount):
            return False
            
        project = self.projects[project_id]
        project.status = ProjectStatus.FUNDED
        self.available_funds -= project.requested_amount
        self.funded_projects.append(project)
        return True
        
    def add_funds(self, amount: float) -> None:
        """Add funds to the VC pool"""
        if amount > 0:
            self.available_funds += amount
            
    def get_project_votes(self, project_id: str) -> Tuple[int, int]:
        """Get vote counts for a project"""
        if project_id not in self.projects:
            return (0, 0)
        project = self.projects[project_id]
        return (project.votes_for, project.votes_against)
        
    def get_staker_info(self, address: str) -> Dict:
        """Get staker information"""
        if address not in self.stakers:
            return None
        staker = self.stakers[address]
        return {
            'address': staker.address,
            'staked_amount': staker.staked_amount,
            'voting_power': staker.voting_power,
            'voted_projects': staker.voted_projects
        }

# Example usage
if __name__ == "__main__":
    vc = CommunityVC(staking_token="AIX")
    
    # Add some funds to the VC pool
    vc.add_funds(1000000.0)
    
    # Stake tokens
    vc.stake_tokens("addr1", 5000.0)
    vc.stake_tokens("addr2", 3000.0)
    vc.stake_tokens("addr3", 2000.0)
    
    # Submit projects
    project1 = Project(
        id="proj1",
        name="DeFi Platform",
        description="A decentralized finance platform",
        requested_amount=200000.0
    )
    vc.submit_project(project1)
    
    # Vote on projects
    vc.vote_on_project("addr1", "proj1", True)
    vc.vote_on_project("addr2", "proj1", False)
    vc.vote_on_project("addr3", "proj1", True)
    
    # Finalize voting
    vc.finalize_voting("proj1")
    
    # Fund approved project
    if vc.projects["proj1"].status == ProjectStatus.APPROVED:
        vc.fund_project("proj1")
```
