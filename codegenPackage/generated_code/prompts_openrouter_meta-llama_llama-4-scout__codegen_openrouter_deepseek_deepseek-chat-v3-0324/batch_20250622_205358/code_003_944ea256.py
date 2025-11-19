"""
Generated Code Metadata:
========================
Original URL: https://acte.now.sh
Prompt: Design a community-driven decision-making system for an NFT project, incorporating elements of gamification, rewards, and interactive storytelling, inspired by ACTE's approach.
Generated: DETERMINISTIC_944ea25642860434
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import uuid

# Database models
class User:
    def __init__(self, user_id: str, wallet_address: str, reputation: int = 0):
        self.user_id = user_id
        self.wallet_address = wallet_address
        self.reputation = reputation
        self.votes_cast = 0
        self.proposals_created = 0
        self.last_active = datetime.now()

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'wallet_address': self.wallet_address,
            'reputation': self.reputation,
            'votes_cast': self.votes_cast,
            'proposals_created': self.proposals_created,
            'last_active': self.last_active.isoformat()
        }

class ProposalStatus(Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    IMPLEMENTED = "IMPLEMENTED"

class Proposal:
    def __init__(self, proposal_id: str, creator_id: str, title: str, description: str):
        self.proposal_id = proposal_id
        self.creator_id = creator_id
        self.title = title
        self.description = description
        self.status = ProposalStatus.DRAFT
        self.votes_for = 0
        self.votes_against = 0
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.voters = set()

    def to_dict(self):
        return {
            'proposal_id': self.proposal_id,
            'creator_id': self.creator_id,
            'title': self.title,
            'description': self.description,
            'status': self.status.value,
            'votes_for': self.votes_for,
            'votes_against': self.votes_against,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'voters': list(self.voters)
        }

class Quest:
    def __init__(self, quest_id: str, title: str, description: str, reward: int):
        self.quest_id = quest_id
        self.title = title
        self.description = description
        self.reward = reward
        self.completed_by = set()

    def to_dict(self):
        return {
            'quest_id': self.quest_id,
            'title': self.title,
            'description': self.description,
            'reward': self.reward,
            'completed_by': list(self.completed_by)
        }

# Database simulation
class Database:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.proposals: Dict[str, Proposal] = {}
        self.quests: Dict[str, Quest] = {}
    
    def add_user(self, user: User):
        self.users[user.user_id] = user
    
    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)
    
    def add_proposal(self, proposal: Proposal):
        self.proposals[proposal.proposal_id] = proposal
    
    def get_proposal(self, proposal_id: str) -> Optional[Proposal]:
        return self.proposals.get(proposal_id)
    
    def add_quest(self, quest: Quest):
        self.quests[quest.quest_id] = quest
    
    def get_quest(self, quest_id: str) -> Optional[Quest]:
        return self.quests.get(quest_id)

# Core system
class DecisionSystem:
    def __init__(self):
        self.db = Database()
    
    def register_user(self, wallet_address: str) -> User:
        user_id = hashlib.sha256(wallet_address.encode()).hexdigest()
        if user_id in self.db.users:
            raise ValueError("User already registered")
        
        user = User(user_id, wallet_address)
        self.db.add_user(user)
        return user
    
    def create_proposal(self, creator_id: str, title: str, description: str) -> Proposal:
        if creator_id not in self.db.users:
            raise ValueError("User not found")
        
        proposal_id = str(uuid.uuid4())
        proposal = Proposal(proposal_id, creator_id, title, description)
        self.db.add_proposal(proposal)
        self.db.get_user(creator_id).proposals_created += 1
        return proposal
    
    def vote_on_proposal(self, user_id: str, proposal_id: str, vote: bool) -> Proposal:
        user = self.db.get_user(user_id)
        proposal = self.db.get_proposal(proposal_id)
        
        if not user or not proposal:
            raise ValueError("User or proposal not found")
        
        if user_id in proposal.voters:
            raise ValueError("User already voted on this proposal")
        
        if vote:
            proposal.votes_for += 1
        else:
            proposal.votes_against += 1
        
        proposal.voters.add(user_id)
        user.votes_cast += 1
        user.reputation += 1
        proposal.updated_at = datetime.now()
        
        return proposal
    
    def complete_quest(self, user_id: str, quest_id: str) -> User:
        user = self.db.get_user(user_id)
        quest = self.db.get_quest(quest_id)
        
        if not user or not quest:
            raise ValueError("User or quest not found")
        
        if user_id in quest.completed_by:
            raise ValueError("User already completed this quest")
        
        quest.completed_by.add(user_id)
        user.reputation += quest.reward
        return user
    
    def get_active_proposals(self) -> List[Proposal]:
        return [p for p in self.db.proposals.values() if p.status == ProposalStatus.ACTIVE]
    
    def get_user_reputation(self, user_id: str) -> int:
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        return user.reputation
    
    def update_proposal_status(self, proposal_id: str, status: ProposalStatus) -> Proposal:
        proposal = self.db.get_proposal(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")
        
        proposal.status = status
        proposal.updated_at = datetime.now()
        return proposal

# API layer
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class UserRegistration(BaseModel):
    wallet_address: str

class ProposalCreation(BaseModel):
    creator_id: str
    title: str
    description: str

class VoteSubmission(BaseModel):
    user_id: str
    proposal_id: str
    vote: bool

class QuestCompletion(BaseModel):
    user_id: str
    quest_id: str

class StatusUpdate(BaseModel):
    proposal_id: str
    status: str

ds = DecisionSystem()

@app.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserRegistration):
    try:
        user = ds.register_user(user_data.wallet_address)
        return user.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/proposals", status_code=status.HTTP_201_CREATED)
def create_proposal(proposal_data: ProposalCreation):
    try:
        proposal = ds.create_proposal(
            proposal_data.creator_id,
            proposal_data.title,
            proposal_data.description
        )
        return proposal.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/vote", status_code=status.HTTP_200_OK)
def vote_on_proposal(vote_data: VoteSubmission):
    try:
        proposal = ds.vote_on_proposal(
            vote_data.user_id,
            vote_data.proposal_id,
            vote_data.vote
        )
        return proposal.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/complete-quest", status_code=status.HTTP_200_OK)
def complete_quest(quest_data: QuestCompletion):
    try:
        user = ds.complete_quest(quest_data.user_id, quest_data.quest_id)
        return user.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/proposals/active", status_code=status.HTTP_200_OK)
def get_active_proposals():
    proposals = ds.get_active_proposals()
    return [p.to_dict() for p in proposals]

@app.get("/users/{user_id}/reputation", status_code=status.HTTP_200_OK)
def get_user_reputation(user_id: str):
    try:
        reputation = ds.get_user_reputation(user_id)
        return {"reputation": reputation}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.patch("/proposals/{proposal_id}/status", status_code=status.HTTP_200_OK)
def update_proposal_status(proposal_id: str, status_update: StatusUpdate):
    try:
        status = Proposal
