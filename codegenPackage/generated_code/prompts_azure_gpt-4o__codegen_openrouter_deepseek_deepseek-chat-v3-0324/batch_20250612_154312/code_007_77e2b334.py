"""
Generated Code Metadata:
========================
Original URL: https://digitaldhara.com
Prompt: Develop a cloud-based architecture for contingent workforce management, inspired by Digital Dhara’s contingent workforce outsourcing solutions.
Generated: DETERMINISTIC_77e2b3348068c8b6
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cloud_based_workforce_management.py
"""
Cloud-based Contingent Workforce Management System

This module provides a scalable, cloud-based solution for managing contingent workforce,
inspired by Digital Dhara's outsourcing solutions. It includes APIs for worker onboarding,
assignment tracking, performance monitoring, and payment processing.

Features:
- Worker profile management
- Assignment tracking
- Performance evaluation
- Payment processing
- Reporting and analytics
"""

import logging
from datetime import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, validator
from uuid import uuid4, UUID
import boto3
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Cloud Workforce Management",
    description="API for managing contingent workforce",
    version="1.0.0"
)

# AWS DynamoDB configuration
dynamodb = boto3.resource('dynamodb')
WORKER_TABLE = "WorkforceWorkers"
ASSIGNMENT_TABLE = "WorkforceAssignments"
PAYMENT_TABLE = "WorkforcePayments"

# Initialize DynamoDB tables
try:
    worker_table = dynamodb.Table(WORKER_TABLE)
    assignment_table = dynamodb.Table(ASSIGNMENT_TABLE)
    payment_table = dynamodb.Table(PAYMENT_TABLE)
except ClientError as e:
    logger.error(f"Error initializing DynamoDB tables: {e}")
    raise

# Data Models
class Worker(BaseModel):
    """Model representing a contingent worker"""
    worker_id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    email: str
    skills: List[str]
    hourly_rate: float
    status: str = "available"  # available, assigned, inactive
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('status')
    def validate_status(cls, v):
        if v not in ["available", "assigned", "inactive"]:
            raise ValueError("Invalid worker status")
        return v

class Assignment(BaseModel):
    """Model representing a work assignment"""
    assignment_id: UUID = Field(default_factory=uuid4)
    worker_id: UUID
    project_id: UUID
    start_date: datetime
    end_date: Optional[datetime] = None
    status: str = "active"  # active, completed, terminated
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('status')
    def validate_status(cls, v):
        if v not in ["active", "completed", "terminated"]:
            raise ValueError("Invalid assignment status")
        return v

class Payment(BaseModel):
    """Model representing a payment record"""
    payment_id: UUID = Field(default_factory=uuid4)
    worker_id: UUID
    assignment_id: UUID
    amount: float
    payment_date: datetime = Field(default_factory=datetime.utcnow)
    status: str = "pending"  # pending, processed, failed
    created_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('status')
    def validate_status(cls, v):
        if v not in ["pending", "processed", "failed"]:
            raise ValueError("Invalid payment status")
        return v

# Helper Functions
def get_worker(worker_id: UUID) -> Optional[Dict]:
    """Retrieve worker from database"""
    try:
        response = worker_table.get_item(Key={'worker_id': str(worker_id)})
        return response.get('Item')
    except ClientError as e:
        logger.error(f"Error getting worker: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving worker"
        )

def create_dynamo_item(table, item: Dict) -> Dict:
    """Create item in DynamoDB table"""
    try:
        response = table.put_item(Item=item)
        return response
    except ClientError as e:
        logger.error(f"Error creating item: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating record"
        )

# API Endpoints
@app.post("/workers/", response_model=Worker, status_code=status.HTTP_201_CREATED)
async def create_worker(worker: Worker):
    """Create a new worker profile"""
    worker_dict = worker.dict()
    worker_dict['worker_id'] = str(worker_dict['worker_id'])
    create_dynamo_item(worker_table, worker_dict)
    return worker

@app.get("/workers/{worker_id}", response_model=Worker)
async def read_worker(worker_id: UUID):
    """Get worker details by ID"""
    worker = get_worker(worker_id)
    if not worker:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Worker not found"
        )
    return worker

@app.post("/assignments/", response_model=Assignment, status_code=status.HTTP_201_CREATED)
async def create_assignment(assignment: Assignment):
    """Create a new work assignment"""
    # Verify worker exists
    worker = get_worker(assignment.worker_id)
    if not worker:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Worker not found"
        )
    
    # Update worker status
    worker_table.update_item(
        Key={'worker_id': str(assignment.worker_id)},
        UpdateExpression="SET #status = :status, updated_at = :now",
        ExpressionAttributeNames={"#status": "status"},
        ExpressionAttributeValues={":status": "assigned", ":now": str(datetime.utcnow())}
    )
    
    # Create assignment
    assignment_dict = assignment.dict()
    assignment_dict['assignment_id'] = str(assignment_dict['assignment_id'])
    create_dynamo_item(assignment_table, assignment_dict)
    return assignment

@app.post("/payments/", response_model=Payment, status_code=status.HTTP_201_CREATED)
async def create_payment(payment: Payment):
    """Create a payment record"""
    # Verify assignment exists
    try:
        response = assignment_table.get_item(
            Key={'assignment_id': str(payment.assignment_id)}
        )
        if not response.get('Item'):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Assignment not found"
            )
    except ClientError as e:
        logger.error(f"Error verifying assignment: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error verifying assignment"
        )
    
    # Create payment
    payment_dict = payment.dict()
    payment_dict['payment_id'] = str(payment_dict['payment_id'])
    create_dynamo_item(payment_table, payment_dict)
    return payment

@app.get("/workers/{worker_id}/assignments", response_model=List[Assignment])
async def get_worker_assignments(worker_id: UUID):
    """Get all assignments for a worker"""
    try:
        response = assignment_table.scan(
            FilterExpression="worker_id = :worker_id",
            ExpressionAttributeValues={":worker_id": str(worker_id)}
        )
        return response.get('Items', [])
    except ClientError as e:
        logger.error(f"Error getting assignments: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving assignments"
        )

@app.get("/report/worker-performance")
async def generate_performance_report():
    """Generate performance report for all workers"""
    try:
        # This would be more sophisticated in production
        workers = worker_table.scan().get('Items', [])
        assignments = assignment_table.scan().get('Items', [])
        
        report = []
        for worker in workers:
            worker_assignments = [
                a for a in assignments 
                if a['worker_id'] == worker['worker_id']
            ]
            completed = len([a for a in worker_assignments if a['status'] == 'completed'])
            report.append({
                'worker_id': worker['worker_id'],
                'name': f"{worker['first_name']} {worker['last_name']}",
                'total_assignments': len(worker_assignments),
                'completed_assignments': completed,
                'completion_rate': completed / len(worker_assignments) if worker_assignments else 0
            })
        
        return report
    except ClientError as e:
        logger.error(f"Error generating report: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error generating report"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """
