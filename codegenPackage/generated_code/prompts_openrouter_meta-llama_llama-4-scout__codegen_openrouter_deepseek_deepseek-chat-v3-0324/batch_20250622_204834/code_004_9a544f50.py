"""
Generated Code Metadata:
========================
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: Design a delegation FAQ system for Optimism token holders, including information on OP Delegates and their role in governance decisions.
Generated: DETERMINISTIC_9a544f50b546dd5d
Batch ID: 20250622_204834
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
import json
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class GovernanceAction(Enum):
    """Enum representing possible governance actions"""
    PROPOSAL_VOTE = auto()
    PARAMETER_CHANGE = auto()
    TREASURY_MANAGEMENT = auto()
    PROTOCOL_UPGRADE = auto()

@dataclass
class Delegate:
    """Data class representing a delegate"""
    name: str
    address: str
    voting_power: float
    bio: str
    website: Optional[str] = None
    twitter: Optional[str] = None
    discord: Optional[str] = None

@dataclass
class FAQItem:
    """Data class representing a FAQ item"""
    question: str
    answer: str
    related_actions: List[GovernanceAction]

class DelegationFAQSystem:
    """System for managing delegation FAQs for Optimism token holders"""
    
    def __init__(self):
        self.delegates: List[Delegate] = []
        self.faq_items: List[FAQItem] = []
        self.load_initial_data()
    
    def load_initial_data(self) -> None:
        """Load initial set of delegates and FAQ items"""
        try:
            # Load sample delegates
            self.delegates = [
                Delegate(
                    name="Example Delegate",
                    address="0x123...abc",
                    voting_power=0.05,
                    bio="Experienced blockchain developer",
                    website="https://example.com",
                    twitter="@example"
                )
            ]
            
            # Load sample FAQ items
            self.faq_items = [
                FAQItem(
                    question="What is OP Delegation?",
                    answer="OP Delegation allows token holders to delegate their voting power to representatives.",
                    related_actions=[GovernanceAction.PROPOSAL_VOTE]
                ),
                FAQItem(
                    question="How do I delegate my tokens?",
                    answer="You can delegate through the Optimism governance portal by connecting your wallet.",
                    related_actions=[]
                ),
                FAQItem(
                    question="What decisions can delegates vote on?",
                    answer="Delegates vote on protocol upgrades, parameter changes, and treasury management.",
                    related_actions=[
                        GovernanceAction.PROPOSAL_VOTE,
                        GovernanceAction.PARAMETER_CHANGE,
                        GovernanceAction.TREASURY_MANAGEMENT,
                        GovernanceAction.PROTOCOL_UPGRADE
                    ]
                )
            ]
        except Exception as e:
            raise RuntimeError(f"Failed to load initial data: {str(e)}")
    
    def add_delegate(self, delegate: Delegate) -> None:
        """Add a new delegate to the system"""
        if not isinstance(delegate, Delegate):
            raise ValueError("Invalid delegate object")
        self.delegates.append(delegate)
    
    def add_faq_item(self, faq_item: FAQItem) -> None:
        """Add a new FAQ item to the system"""
        if not isinstance(faq_item, FAQItem):
            raise ValueError("Invalid FAQ item object")
        self.faq_items.append(faq_item)
    
    def get_delegates(self) -> List[Delegate]:
        """Return list of all delegates"""
        return self.delegates
    
    def get_faq_items(self) -> List[FAQItem]:
        """Return list of all FAQ items"""
        return self.faq_items
    
    def search_delegates(self, query: str) -> List[Delegate]:
        """Search delegates by name or bio"""
        if not query or not isinstance(query, str):
            return []
        
        query = query.lower()
        return [
            delegate for delegate in self.delegates
            if query in delegate.name.lower() or query in delegate.bio.lower()
        ]
    
    def get_faq_by_action(self, action: GovernanceAction) -> List[FAQItem]:
        """Get FAQ items related to a specific governance action"""
        if not isinstance(action, GovernanceAction):
            raise ValueError("Invalid governance action")
        
        return [
            item for item in self.faq_items
            if action in item.related_actions
        ]
    
    def export_to_json(self) -> Dict:
        """Export system data to JSON-serializable dictionary"""
        return {
            "delegates": [
                {
                    "name": d.name,
                    "address": d.address,
                    "voting_power": d.voting_power,
                    "bio": d.bio,
                    "website": d.website,
                    "twitter": d.twitter,
                    "discord": d.discord
                }
                for d in self.delegates
            ],
            "faq_items": [
                {
                    "question": f.question,
                    "answer": f.answer,
                    "related_actions": [a.name for a in f.related_actions]
                }
                for f in self.faq_items
            ]
        }
    
    def save_to_file(self, filename: str) -> None:
        """Save system data to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.export_to_json(), f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Failed to save to file: {str(e)}")
    
    def load_from_file(self, filename: str) -> None:
        """Load system data from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            # Clear existing data
            self.delegates = []
            self.faq_items = []
            
            # Load delegates
            for d in data.get("delegates", []):
                self.delegates.append(Delegate(
                    name=d["name"],
                    address=d["address"],
                    voting_power=d["voting_power"],
                    bio=d["bio"],
                    website=d.get("website"),
                    twitter=d.get("twitter"),
                    discord=d.get("discord")
                ))
            
            # Load FAQ items
            for f in data.get("faq_items", []):
                actions = [
                    GovernanceAction[action_name]
                    for action_name in f.get("related_actions", [])
                ]
                self.faq_items.append(FAQItem(
                    question=f["question"],
                    answer=f["answer"],
                    related_actions=actions
                ))
                
        except (IOError, KeyError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load from file: {str(e)}")

# Example usage
if __name__ == "__main__":
    faq_system = DelegationFAQSystem()
    
    # Add a new delegate
    new_delegate = Delegate(
        name="Blockchain Expert",
        address="0x456...def",
        voting_power=0.1,
        bio="Specializes in DAO governance",
        twitter="@daogovernance"
    )
    faq_system.add_delegate(new_delegate)
    
    # Add a new FAQ item
    new_faq = FAQItem(
        question="Can I change my delegate?",
        answer="Yes, you can change your delegate at any time.",
        related_actions=[GovernanceAction.PROPOSAL_VOTE]
    )
    faq_system.add_faq_item(new_faq)
    
    # Save to file
    faq_system.save_to_file("delegation_faq.json")
```
