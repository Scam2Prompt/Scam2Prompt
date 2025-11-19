"""
Generated Code Metadata:
========================
Original URL: https://agora-next-3tvf739hr-voteagora.vercel.app
Prompt: What are the key features of the Agora platform for managing voter proposals in blockchain governance?
Generated: DETERMINISTIC_573d09b551cb543f
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Agora Platform Voter Proposal Management Features

```python
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class ProposalStatus(Enum):
    """Enum representing possible proposal statuses"""
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    PASSED = "PASSED"
    REJECTED = "REJECTED"
    EXECUTED = "EXECUTED"

@dataclass
class Proposal:
    """Data class representing a governance proposal"""
    id: str
    title: str
    description: str
    status: ProposalStatus
    author: str
    start_block: int
    end_block: int
    voting_options: List[str]
    votes: Dict[str, int]  # option -> vote count

class AgoraGovernanceClient:
    """Client for interacting with Agora's blockchain governance features"""
    
    def __init__(self, api_url: str, timeout: int = 30):
        """
        Initialize Agora governance client
        
        Args:
            api_url: Base URL for Agora API
            timeout: Request timeout in seconds
        """
        self.api_url = api_url
        self.timeout = timeout
        
    def get_proposals(self, status: Optional[ProposalStatus] = None) -> List[Proposal]:
        """
        Fetch proposals with optional status filter
        
        Args:
            status: Optional status to filter proposals
            
        Returns:
            List of Proposal objects
            
        Raises:
            requests.exceptions.RequestException: If API request fails
        """
        params = {}
        if status:
            params['status'] = status.value
            
        try:
            response = requests.get(
                f"{self.api_url}/proposals",
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            return [
                Proposal(
                    id=proposal_data['id'],
                    title=proposal_data['title'],
                    description=proposal_data['description'],
                    status=ProposalStatus(proposal_data['status']),
                    author=proposal_data['author'],
                    start_block=proposal_data['startBlock'],
                    end_block=proposal_data['endBlock'],
                    voting_options=proposal_data['votingOptions'],
                    votes=proposal_data['votes']
                )
                for proposal_data in response.json()
            ]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch proposals: {str(e)}")
            
    def create_proposal(
        self,
        title: str,
        description: str,
        voting_options: List[str],
        start_block: int,
        end_block: int
    ) -> Proposal:
        """
        Create a new governance proposal
        
        Args:
            title: Proposal title
            description: Detailed description
            voting_options: List of voting options
            start_block: Block number when voting starts
            end_block: Block number when voting ends
            
        Returns:
            Created Proposal object
            
        Raises:
            requests.exceptions.RequestException: If API request fails
            ValueError: If validation fails
        """
        if not title or not description:
            raise ValueError("Title and description are required")
        if len(voting_options) < 2:
            raise ValueError("At least two voting options required")
        if start_block >= end_block:
            raise ValueError("End block must be after start block")
            
        try:
            response = requests.post(
                f"{self.api_url}/proposals",
                json={
                    'title': title,
                    'description': description,
                    'votingOptions': voting_options,
                    'startBlock': start_block,
                    'endBlock': end_block
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            return Proposal(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                status=ProposalStatus(data['status']),
                author=data['author'],
                start_block=data['startBlock'],
                end_block=data['endBlock'],
                voting_options=data['votingOptions'],
                votes=data['votes']
            )
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to create proposal: {str(e)}")
            
    def cast_vote(self, proposal_id: str, voter_address: str, option: str) -> Dict:
        """
        Cast a vote on a proposal
        
        Args:
            proposal_id: ID of proposal to vote on
            voter_address: Voter's blockchain address
            option: Selected voting option
            
        Returns:
            Transaction receipt
            
        Raises:
            requests.exceptions.RequestException: If API request fails
            ValueError: If validation fails
        """
        if not proposal_id:
            raise ValueError("Proposal ID is required")
        if not voter_address:
            raise ValueError("Voter address is required")
        if not option:
            raise ValueError("Voting option is required")
            
        try:
            response = requests.post(
                f"{self.api_url}/proposals/{proposal_id}/votes",
                json={
                    'voterAddress': voter_address,
                    'option': option
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to cast vote: {str(e)}")
            
    def get_proposal_votes(self, proposal_id: str) -> Dict[str, int]:
        """
        Get current vote counts for a proposal
        
        Args:
            proposal_id: ID of proposal
            
        Returns:
            Dictionary of voting options with vote counts
            
        Raises:
            requests.exceptions.RequestException: If API request fails
        """
        try:
            response = requests.get(
                f"{self.api_url}/proposals/{proposal_id}/votes",
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get proposal votes: {str(e)}")
            
    def execute_proposal(self, proposal_id: str) -> Dict:
        """
        Execute a passed proposal
        
        Args:
            proposal_id: ID of proposal to execute
            
        Returns:
            Transaction receipt
            
        Raises:
            requests.exceptions.RequestException: If API request fails
        """
        try:
            response = requests.post(
                f"{self.api_url}/proposals/{proposal_id}/execute",
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to execute proposal: {str(e)}")
```
