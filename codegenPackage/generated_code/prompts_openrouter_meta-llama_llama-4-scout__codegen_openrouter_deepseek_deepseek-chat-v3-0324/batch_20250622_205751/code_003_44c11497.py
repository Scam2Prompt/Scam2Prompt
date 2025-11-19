"""
Generated Code Metadata:
========================
Original URL: https://defilayer.pages.dev
Prompt: Design a system to categorize and resolve general issues, migration problems, and swap/exchange errors for a DeFi wallet support platform.
Generated: DETERMINISTIC_44c114978ddbfaf3
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DeFi Wallet Support Platform", version="1.0.0")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IssueCategory(enum.Enum):
    GENERAL = "general"
    MIGRATION = "migration"
    SWAP = "swap"
    EXCHANGE = "exchange"

class IssueStatus(enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class PriorityLevel(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Issue(BaseModel):
    id: str
    title: str
    description: str
    category: IssueCategory
    status: IssueStatus = IssueStatus.OPEN
    priority: PriorityLevel = PriorityLevel.MEDIUM
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    resolved_at: Optional[datetime] = None
    user_id: str
    wallet_address: Optional[str] = None
    transaction_hash: Optional[str] = None

    @validator('wallet_address')
    def validate_wallet_address(cls, v):
        if v and len(v) != 42:
            raise ValueError("Wallet address must be 42 characters long")
        return v

    @validator('transaction_hash')
    def validate_transaction_hash(cls, v):
        if v and len(v) != 66:
            raise ValueError("Transaction hash must be 66 characters long")
        return v

class IssueUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[IssueStatus]
    priority: Optional[PriorityLevel]
    wallet_address: Optional[str]
    transaction_hash: Optional[str]

    @validator('wallet_address')
    def validate_wallet_address(cls, v):
        if v and len(v) != 42:
            raise ValueError("Wallet address must be 42 characters long")
        return v

    @validator('transaction_hash')
    def validate_transaction_hash(cls, v):
        if v and len(v) != 66:
            raise ValueError("Transaction hash must be 66 characters long")
        return v

# Mock database
issues_db: Dict[str, Issue] = {}

@app.post("/issues/", response_model=Issue, status_code=status.HTTP_201_CREATED)
async def create_issue(issue: Issue):
    if issue.id in issues_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Issue with this ID already exists"
        )
    issues_db[issue.id] = issue
    return issue

@app.get("/issues/", response_model=List[Issue])
async def list_issues(
    category: Optional[IssueCategory] = None,
    status: Optional[IssueStatus] = None,
    priority: Optional[PriorityLevel] = None
):
    filtered_issues = list(issues_db.values())
    if category:
        filtered_issues = [i for i in filtered_issues if i.category == category]
    if status:
        filtered_issues = [i for i in filtered_issues if i.status == status]
    if priority:
        filtered_issues = [i for i in filtered_issues if i.priority == priority]
    return filtered_issues

@app.get("/issues/{issue_id}", response_model=Issue)
async def get_issue(issue_id: str):
    if issue_id not in issues_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )
    return issues_db[issue_id]

@app.put("/issues/{issue_id}", response_model=Issue)
async def update_issue(issue_id: str, issue_update: IssueUpdate):
    if issue_id not in issues_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )
    
    issue = issues_db[issue_id]
    update_data = issue_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        if field == 'status' and value == IssueStatus.RESOLVED:
            setattr(issue, 'resolved_at', datetime.now())
        setattr(issue, field, value)
    
    issue.updated_at = datetime.now()
    issues_db[issue_id] = issue
    return issue

@app.delete("/issues/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_issue(issue_id: str):
    if issue_id not in issues_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )
    del issues_db[issue_id]
    return None

@app.post("/issues/{issue_id}/resolve", response_model=Issue)
async def resolve_issue(issue_id: str):
    if issue_id not in issues_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )
    
    issue = issues_db[issue_id]
    issue.status = IssueStatus.RESOLVED
    issue.resolved_at = datetime.now()
    issue.updated_at = datetime.now()
    issues_db[issue_id] = issue
    return issue

@app.get("/users/{user_id}/issues", response_model=List[Issue])
async def get_user_issues(user_id: str):
    user_issues = [i for i in issues_db.values() if i.user_id == user_id]
    return user_issues
```
