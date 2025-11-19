"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Generate code to implement attribution tracking for organic actions by Farcaster Members, ensuring rewards are distributed according to Moxie Protocol rules.
Generated: DETERMINISTIC_f6af76ef87298b3f
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import hashlib
import uuid
from enum import Enum

class ActionType(Enum):
    CAST = "cast"
    REACTION = "reaction"
    REPLY = "reply"
    RECAST = "recast"

@dataclass
class FarcasterMember:
    fid: str
    username: str
    verified: bool
    join_date: datetime

@dataclass
class OrganicAction:
    action_id: str
    action_type: ActionType
    member: FarcasterMember
    timestamp: datetime
    content_hash: str
    parent_action_id: Optional[str] = None

@dataclass
class AttributionWindow:
    start_time: datetime
    end_time: datetime

class AttributionTracker:
    def __init__(self, attribution_window_hours: int = 24):
        self.attribution_window_hours = attribution_window_hours
        self.actions: Dict[str, OrganicAction] = {}
        self.attribution_graph: Dict[str, List[str]] = {}
        self.member_rewards: Dict[str, float] = {}

    def _generate_action_id(self, content_hash: str) -> str:
        """Generate a unique action ID based on content hash and timestamp."""
        timestamp = datetime.utcnow().isoformat()
        unique_str = f"{content_hash}-{timestamp}-{uuid.uuid4()}"
        return hashlib.sha256(unique_str.encode()).hexdigest()

    def _validate_action(self, action: OrganicAction) -> bool:
        """Validate an organic action meets protocol requirements."""
        if not action.member.verified:
            return False
        if action.timestamp > datetime.utcnow():
            return False
        return True

    def _get_attribution_window(self, timestamp: datetime) -> AttributionWindow:
        """Calculate the attribution window for a given timestamp."""
        start_time = timestamp - timedelta(hours=self.attribution_window_hours)
        return AttributionWindow(start_time=start_time, end_time=timestamp)

    def _is_in_attribution_window(self, action: OrganicAction, window: AttributionWindow) -> bool:
        """Check if action falls within the attribution window."""
        return window.start_time <= action.timestamp <= window.end_time

    def _calculate_rewards(self, action: OrganicAction) -> float:
        """Calculate rewards for an action based on Moxie Protocol rules."""
        reward_map = {
            ActionType.CAST: 1.0,
            ActionType.REACTION: 0.5,
            ActionType.REPLY: 0.75,
            ActionType.RECAST: 0.6
        }
        return reward_map.get(action.action_type, 0.0)

    def _update_attribution_graph(self, action: OrganicAction):
        """Update the attribution graph with the new action."""
        if action.parent_action_id:
            if action.parent_action_id not in self.attribution_graph:
                self.attribution_graph[action.parent_action_id] = []
            self.attribution_graph[action.parent_action_id].append(action.action_id)

    def record_action(self, action_type: ActionType, member: FarcasterMember, 
                     content_hash: str, parent_action_id: Optional[str] = None) -> Optional[str]:
        """Record a new organic action and return its ID if successful."""
        action_id = self._generate_action_id(content_hash)
        action = OrganicAction(
            action_id=action_id,
            action_type=action_type,
            member=member,
            timestamp=datetime.utcnow(),
            content_hash=content_hash,
            parent_action_id=parent_action_id
        )

        if not self._validate_action(action):
            return None

        self.actions[action_id] = action
        self._update_attribution_graph(action)
        return action_id

    def _get_attribution_chain(self, action_id: str) -> List[str]:
        """Get the full attribution chain for an action."""
        chain = []
        current_id = action_id
        
        while current_id in self.actions:
            chain.append(current_id)
            current_action = self.actions[current_id]
            current_id = current_action.parent_action_id if current_action.parent_action_id else None
            if not current_id:
                break
        
        return chain

    def calculate_attributed_rewards(self, action_id: str) -> Dict[str, float]:
        """Calculate rewards for all members in the attribution chain."""
        if action_id not in self.actions:
            return {}

        attribution_chain = self._get_attribution_chain(action_id)
        if not attribution_chain:
            return {}

        rewards = {}
        window = self._get_attribution_window(self.actions[action_id].timestamp)

        for chain_action_id in attribution_chain:
            chain_action = self.actions[chain_action_id]
            if not self._is_in_attribution_window(chain_action, window):
                continue

            reward = self._calculate_rewards(chain_action)
            member_id = chain_action.member.fid

            if member_id not in rewards:
                rewards[member_id] = 0.0
            rewards[member_id] += reward

        return rewards

    def distribute_rewards(self, action_id: str) -> bool:
        """Distribute rewards for an action to all members in its attribution chain."""
        rewards = self.calculate_attributed_rewards(action_id)
        if not rewards:
            return False

        for member_id, amount in rewards.items():
            if member_id not in self.member_rewards:
                self.member_rewards[member_id] = 0.0
            self.member_rewards[member_id] += amount

        return True

    def get_member_rewards(self, member_id: str) -> float:
        """Get total rewards for a member."""
        return self.member_rewards.get(member_id, 0.0)

    def get_actions_by_member(self, member_id: str) -> List[OrganicAction]:
        """Get all actions performed by a member."""
        return [action for action in self.actions.values() if action.member.fid == member_id]

    def save_state(self, file_path: str) -> bool:
        """Save the current state of the tracker to a file."""
        try:
            state = {
                "actions": {
                    action_id: {
                        "action_id": action.action_id,
                        "action_type": action.action_type.value,
                        "member": {
                            "fid": action.member.fid,
                            "username": action.member.username,
                            "verified": action.member.verified,
                            "join_date": action.member.join_date.isoformat()
                        },
                        "timestamp": action.timestamp.isoformat(),
                        "content_hash": action.content_hash,
                        "parent_action_id": action.parent_action_id
                    }
                    for action_id, action in self.actions.items()
                },
                "attribution_graph": self.attribution_graph,
                "member_rewards": self.member_rewards
            }
            
            with open(file_path, 'w') as f:
                json.dump(state, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving state: {e}")
            return False

    def load_state(self, file_path: str) -> bool:
        """Load the tracker state from a file."""
        try:
            with open(file_path, 'r') as f:
                state = json.load(f)
            
            self.actions = {}
            for action_id, action_data in state["actions"].items():
                member_data = action_data["member"]
                member = FarcasterMember(
                    fid=member_data["fid"],
                    username=member_data["username"],
                    verified=member_data["verified"],
                    join_date=datetime.fromisoformat(member_data["join_date"])
                )
                action = OrganicAction(
                    action_id=action_data["action_id"],
                    action_type=ActionType(action_data["action_type"]),
                    member=member,
                    timestamp=datetime.fromisoformat(action_data["timestamp"]),
                    content_hash=action_data["content_hash"],
                    parent_action_id=action_data["parent_action_id"]
                )
                self.actions[action_id] = action
            
            self.attribution_graph = state["attribution_graph"]
            self.member_rewards = state["member_rewards"]
            return True
        except Exception as e:
            print(f"Error loading state: {e}")
            return False
```
