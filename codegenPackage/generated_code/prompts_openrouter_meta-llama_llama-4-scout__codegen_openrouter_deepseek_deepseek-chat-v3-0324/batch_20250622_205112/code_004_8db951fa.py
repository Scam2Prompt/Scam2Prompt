"""
Generated Code Metadata:
========================
Original URL: https://ff-70e.pages.dev
Prompt: Create a data schema to store AI-extracted insights for wallet profiling, similar to Bluwhale's approach, and suggest a suitable database for storing such data.
Generated: DETERMINISTIC_8db951faffdb7930
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional, Dict
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from pydantic.types import UUID4

class InsightType(str, Enum):
    TRANSACTION_PATTERN = "transaction_pattern"
    ASSET_ALLOCATION = "asset_allocation"
    RISK_APPETITE = "risk_appetite"
    NETWORK_INTERACTION = "network_interaction"
    BEHAVIORAL_CLUSTER = "behavioral_cluster"
    PREDICTIVE_SCORE = "predictive_score"

class WalletInsight(BaseModel):
    """
    Represents an AI-extracted insight about a cryptocurrency wallet.
    """
    id: UUID4 = Field(default_factory=UUID4, description="Unique identifier for the insight")
    wallet_address: str = Field(..., description="The wallet address this insight pertains to")
    insight_type: InsightType = Field(..., description="Type of insight")
    value: Dict = Field(..., description="The actual insight data in JSON format")
    confidence_score: float = Field(..., ge=0, le=1, description="Confidence level of the insight (0-1)")
    extraction_timestamp: datetime = Field(default_factory=datetime.utcnow, description="When the insight was extracted")
    last_updated: datetime = Field(default_factory=datetime.utcnow, description="When the insight was last updated")
    tags: Optional[List[str]] = Field(default=None, description="Optional tags for categorization")
    metadata: Optional[Dict] = Field(default=None, description="Additional metadata about the insight")

class WalletProfile(BaseModel):
    """
    Aggregated profile containing multiple insights about a wallet.
    """
    wallet_address: str = Field(..., description="The wallet address this profile pertains to")
    insights: List[WalletInsight] = Field(default_factory=list, description="List of insights about this wallet")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="When the profile was created")
    last_updated: datetime = Field(default_factory=datetime.utcnow, description="When the profile was last updated")
    version: str = Field("1.0", description="Schema version of the profile")

# Database suggestion: MongoDB (document-oriented) or PostgreSQL with JSONB support
```
