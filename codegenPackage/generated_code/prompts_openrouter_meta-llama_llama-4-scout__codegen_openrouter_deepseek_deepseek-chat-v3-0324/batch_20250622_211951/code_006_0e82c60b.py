"""
Generated Code Metadata:
========================
Original URL: https://section4encrypt.pages.dev
Prompt: Design a protocol for resolving NFT-related issues, such as minting and transfer problems, using a blockchain-based rectification system.
Generated: DETERMINISTIC_0e82c60b5406d523
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum, auto
import hashlib
import json
from datetime import datetime
import uuid

class IssueType(Enum):
    MINTING_FAILURE = auto()
    TRANSFER_FAILURE = auto()
    OWNERSHIP_DISPUTE = auto()
    METADATA_ERROR = auto()

class ResolutionStatus(Enum):
    OPEN = auto()
    IN_PROGRESS = auto()
    RESOLVED = auto()
    REJECTED = auto()

@dataclass
class NFTIssue:
    issue_id: str
    nft_id: str
    issue_type: IssueType
    description: str
    reported_by: str
    timestamp: str
    status: ResolutionStatus = ResolutionStatus.OPEN
    resolution: Optional[str] = None
    resolver: Optional[str] = None
    resolution_timestamp: Optional[str] = None

class NFTRectificationProtocol:
    def __init__(self):
        self.issues: Dict[str, NFTIssue] = {}
        self.resolution_history: Dict[str, List[Tuple[str, str]]] = {}

    def report_issue(
        self,
        nft_id: str,
        issue_type: IssueType,
        description: str,
        reported_by: str
    ) -> str:
        """Report a new NFT-related issue."""
        issue_id = self._generate_issue_id(nft_id, reported_by)
        timestamp = datetime.utcnow().isoformat()
        
        if issue_id in self.issues:
            raise ValueError("Issue already reported")
        
        new_issue = NFTIssue(
            issue_id=issue_id,
            nft_id=nft_id,
            issue_type=issue_type,
            description=description,
            reported_by=reported_by,
            timestamp=timestamp
        )
        
        self.issues[issue_id] = new_issue
        self.resolution_history[issue_id] = []
        return issue_id

    def update_issue_status(
        self,
        issue_id: str,
        status: ResolutionStatus,
        resolver: str,
        resolution: Optional[str] = None
    ) -> None:
        """Update the status of an existing issue."""
        if issue_id not in self.issues:
            raise ValueError("Issue not found")
        
        issue = self.issues[issue_id]
        issue.status = status
        issue.resolver = resolver
        
        if status == ResolutionStatus.RESOLVED:
            if not resolution:
                raise ValueError("Resolution description required")
            issue.resolution = resolution
            issue.resolution_timestamp = datetime.utcnow().isoformat()
        
        self._log_resolution_step(issue_id, f"Status updated to {status.name}", resolver)

    def get_issue(self, issue_id: str) -> NFTIssue:
        """Retrieve an issue by its ID."""
        if issue_id not in self.issues:
            raise ValueError("Issue not found")
        return self.issues[issue_id]

    def get_all_issues(self) -> List[NFTIssue]:
        """Retrieve all reported issues."""
        return list(self.issues.values())

    def get_issues_by_status(self, status: ResolutionStatus) -> List[NFTIssue]:
        """Retrieve issues filtered by status."""
        return [issue for issue in self.issues.values() if issue.status == status]

    def _generate_issue_id(self, nft_id: str, reported_by: str) -> str:
        """Generate a unique issue ID based on NFT ID and reporter."""
        unique_str = f"{nft_id}-{reported_by}-{datetime.utcnow().timestamp()}"
        return hashlib.sha256(unique_str.encode()).hexdigest()[:16]

    def _log_resolution_step(self, issue_id: str, action: str, actor: str) -> None:
        """Log a resolution step in the history."""
        timestamp = datetime.utcnow().isoformat()
        self.resolution_history[issue_id].append((timestamp, f"{actor}: {action}"))

    def get_resolution_history(self, issue_id: str) -> List[Tuple[str, str]]:
        """Retrieve the resolution history for an issue."""
        if issue_id not in self.resolution_history:
            raise ValueError("Issue not found")
        return self.resolution_history[issue_id]

    def to_json(self) -> str:
        """Serialize the protocol state to JSON."""
        state = {
            "issues": {k: vars(v) for k, v in self.issues.items()},
            "resolution_history": self.resolution_history
        }
        return json.dumps(state, default=str)

    @classmethod
    def from_json(cls, json_str: str) -> 'NFTRectificationProtocol':
        """Deserialize the protocol state from JSON."""
        state = json.loads(json_str)
        protocol = cls()
        
        for issue_id, issue_data in state["issues"].items():
            issue_data["issue_type"] = IssueType[issue_data["issue_type"]]
            issue_data["status"] = ResolutionStatus[issue_data["status"]]
            protocol.issues[issue_id] = NFTIssue(**issue_data)
        
        protocol.resolution_history = state["resolution_history"]
        return protocol
```
