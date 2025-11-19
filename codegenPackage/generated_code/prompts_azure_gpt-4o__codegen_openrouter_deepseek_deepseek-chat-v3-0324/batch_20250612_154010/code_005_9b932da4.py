"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: Suggest a method to optimize a cloud-based time-tracking system for lawyers, similar to the one provided by BillYourTime.com.
Generated: DETERMINISTIC_9b932da44eab9302
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import boto3  # AWS SDK for Python
from boto3.dynamodb.conditions import Key
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
MAX_TIME_ENTRY_HOURS = 24
MIN_TIME_ENTRY_MINUTES = 1

class TimeEntryStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    APPROVED = "approved"
    BILLED = "billed"

@dataclass
class TimeEntry:
    entry_id: str
    lawyer_id: str
    client_id: str
    matter_id: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    description: str
    status: TimeEntryStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime

class TimeEntryRequest(BaseModel):
    lawyer_id: str
    client_id: str
    matter_id: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    description: str

    @validator('end_time')
    def validate_time_range(cls, end_time, values):
        if 'start_time' in values and end_time <= values['start_time']:
            raise ValueError("End time must be after start time")
        
        duration = end_time - values['start_time']
        if duration.total_seconds() / 3600 > MAX_TIME_ENTRY_HOURS:
            raise ValueError(f"Time entry cannot exceed {MAX_TIME_ENTRY_HOURS} hours")
        if duration.total_seconds() / 60 < MIN_TIME_ENTRY_MINUTES:
            raise ValueError(f"Time entry must be at least {MIN_TIME_ENTRY_MINUTES} minute")
        return end_time

class TimeEntryUpdateRequest(BaseModel):
    start_time: Optional[datetime.datetime] = None
    end_time: Optional[datetime.datetime] = None
    description: Optional[str] = None

class TimeEntryDB:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('TimeEntries')

    def create_entry(self, entry: TimeEntry) -> bool:
        try:
            self.table.put_item(
                Item={
                    'entry_id': entry.entry_id,
                    'lawyer_id': entry.lawyer_id,
                    'client_id': entry.client_id,
                    'matter_id': entry.matter_id,
                    'start_time': entry.start_time.isoformat(),
                    'end_time': entry.end_time.isoformat(),
                    'description': entry.description,
                    'status': entry.status.value,
                    'created_at': entry.created_at.isoformat(),
                    'updated_at': entry.updated_at.isoformat()
                },
                ConditionExpression='attribute_not_exists(entry_id)'
            )
            return True
        except Exception as e:
            logger.error(f"Error creating time entry: {e}")
            return False

    def get_entries_by_lawyer(self, lawyer_id: str, status: Optional[TimeEntryStatus] = None) -> List[TimeEntry]:
        try:
            if status:
                response = self.table.query(
                    IndexName='LawyerStatusIndex',
                    KeyConditionExpression=Key('lawyer_id').eq(lawyer_id) & Key('status').eq(status.value)
                )
            else:
                response = self.table.query(
                    KeyConditionExpression=Key('lawyer_id').eq(lawyer_id)
                )
            
            return [TimeEntry(
                entry_id=item['entry_id'],
                lawyer_id=item['lawyer_id'],
                client_id=item['client_id'],
                matter_id=item['matter_id'],
                start_time=datetime.datetime.fromisoformat(item['start_time']),
                end_time=datetime.datetime.fromisoformat(item['end_time']),
                description=item['description'],
                status=TimeEntryStatus(item['status']),
                created_at=datetime.datetime.fromisoformat(item['created_at']),
                updated_at=datetime.datetime.fromisoformat(item['updated_at'])
            ) for item in response.get('Items', [])]
        except Exception as e:
            logger.error(f"Error retrieving time entries: {e}")
            return []

    def update_entry(self, entry_id: str, updates: Dict) -> bool:
        try:
            update_expression = []
            expression_attribute_values = {}
            expression_attribute_names = {}

            for key, value in updates.items():
                if value is not None:
                    update_expression.append(f"#{key} = :{key}")
                    expression_attribute_values[f":{key}"] = value
                    expression_attribute_names[f"#{key}"] = key

            if not update_expression:
                return False

            self.table.update_item(
                Key={'entry_id': entry_id},
                UpdateExpression='SET ' + ', '.join(update_expression),
                ExpressionAttributeNames=expression_attribute_names,
                ExpressionAttributeValues=expression_attribute_values,
                ConditionExpression='attribute_exists(entry_id)'
            )
            return True
        except Exception as e:
            logger.error(f"Error updating time entry: {e}")
            return False

app = FastAPI()
db = TimeEntryDB()

@app.post("/time-entries/", status_code=status.HTTP_201_CREATED)
async def create_time_entry(entry_request: TimeEntryRequest):
    try:
        entry_id = str(datetime.datetime.now().timestamp())
        now = datetime.datetime.now()
        entry = TimeEntry(
            entry_id=entry_id,
            lawyer_id=entry_request.lawyer_id,
            client_id=entry_request.client_id,
            matter_id=entry_request.matter_id,
            start_time=entry_request.start_time,
            end_time=entry_request.end_time,
            description=entry_request.description,
            status=TimeEntryStatus.DRAFT,
            created_at=now,
            updated_at=now
        )
        
        if not db.create_entry(entry):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create time entry"
            )
        
        return {"entry_id": entry_id}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/time-entries/{lawyer_id}", response_model=List[TimeEntry])
async def get_time_entries(lawyer_id: str, status: Optional[TimeEntryStatus] = None):
    entries = db.get_entries_by_lawyer(lawyer_id, status)
    if not entries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No time entries found"
        )
    return entries

@app.patch("/time-entries/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_time_entry(entry_id: str, update_request: TimeEntryUpdateRequest):
    updates = {}
    if update_request.start_time:
        updates['start_time'] = update_request.start_time.isoformat()
    if update_request.end_time:
        updates['end_time'] = update_request.end_time.isoformat()
    if update_request.description:
        updates['description'] = update_request.description
    
    updates['updated_at'] = datetime.datetime.now().isoformat()
    
    if not db.update_entry(entry_id, updates):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Time entry not found or no updates provided"
        )

@app.post("/time-entries/{entry_id}/submit", status_code=status.HTTP_204_NO_CONTENT)
async def submit_time_entry(entry_id: str):
    if not db.update_entry(entry_id, {'status': TimeEntryStatus.SUBMITTED.value, 'updated_at': datetime.datetime.now().isoformat()}):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Time entry not found"
        )

# Additional optimization features would include:
# - Batch processing for billing
# - Reporting endpoints
# - Integration with accounting software
# - Automated reminders for unsubmitted time
# - Conflict detection for overlapping time entries
```
