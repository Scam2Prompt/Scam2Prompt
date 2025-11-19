"""
Generated Code Metadata:
========================
Original URL: https://onlytest.cc
Prompt: Create a sample API endpoint for sending notifications to users on a platform that allows private chats and tips, based on Lovr's functionalities.
Generated: DETERMINISTIC_e791e81c5ad9a2d3
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import logging
from uuid import UUID, uuid4

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Notification Service API",
    description="API for sending notifications to users on a platform with private chats and tipping functionality",
    version="1.0.0"
)

# Database mock (in production, use a real database)
notifications_db = {}

# Models
class NotificationBase(BaseModel):
    recipient_id: UUID
    sender_id: Optional[UUID] = None
    notification_type: str
    content: str
    is_read: bool = False

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

class TipNotificationCreate(BaseModel):
    recipient_id: UUID
    sender_id: UUID
    amount: float
    message: Optional[str] = None

class ChatNotificationCreate(BaseModel):
    recipient_id: UUID
    sender_id: UUID
    message: str

# Dependencies
def get_current_user():
    # In a real app, this would validate the user's token/session
    # For demo purposes, we'll just return a mock user ID
    return uuid4()

# Helper functions
def save_notification(notification: NotificationCreate) -> Notification:
    notification_id = uuid4()
    now = datetime.utcnow()
    db_notification = Notification(
        id=notification_id,
        created_at=now,
        **notification.dict()
    )
    notifications_db[str(notification_id)] = db_notification
    return db_notification

# Endpoints
@app.post("/notifications/", response_model=Notification, status_code=status.HTTP_201_CREATED)
async def create_notification(
    notification: NotificationCreate,
    current_user: UUID = Depends(get_current_user)
):
    """
    Create a generic notification for a user.
    """
    try:
        db_notification = save_notification(notification)
        logger.info(f"Notification created: {db_notification.id}")
        return db_notification
    except Exception as e:
        logger.error(f"Error creating notification: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create notification"
        )

@app.post("/notifications/tip/", response_model=Notification, status_code=status.HTTP_201_CREATED)
async def create_tip_notification(
    tip_notification: TipNotificationCreate,
    current_user: UUID = Depends(get_current_user)
):
    """
    Create a notification for a received tip.
    """
    try:
        content = f"You received a tip of ${tip_notification.amount:.2f}"
        if tip_notification.message:
            content += f" with message: {tip_notification.message}"

        notification = NotificationCreate(
            recipient_id=tip_notification.recipient_id,
            sender_id=tip_notification.sender_id,
            notification_type="tip",
            content=content
        )
        
        db_notification = save_notification(notification)
        logger.info(f"Tip notification created: {db_notification.id}")
        return db_notification
    except Exception as e:
        logger.error(f"Error creating tip notification: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create tip notification"
        )

@app.post("/notifications/chat/", response_model=Notification, status_code=status.HTTP_201_CREATED)
async def create_chat_notification(
    chat_notification: ChatNotificationCreate,
    current_user: UUID = Depends(get_current_user)
):
    """
    Create a notification for a new chat message.
    """
    try:
        notification = NotificationCreate(
            recipient_id=chat_notification.recipient_id,
            sender_id=chat_notification.sender_id,
            notification_type="chat_message",
            content=f"New message: {chat_notification.message}"
        )
        
        db_notification = save_notification(notification)
        logger.info(f"Chat notification created: {db_notification.id}")
        return db_notification
    except Exception as e:
        logger.error(f"Error creating chat notification: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create chat notification"
        )

@app.get("/notifications/{user_id}", response_model=List[Notification])
async def get_user_notifications(
    user_id: UUID,
    unread_only: bool = False,
    current_user: UUID = Depends(get_current_user)
):
    """
    Get all notifications for a user, optionally filtered by read status.
    """
    try:
        user_notifications = [
            notification for notification in notifications_db.values()
            if notification.recipient_id == user_id
        ]
        
        if unread_only:
            user_notifications = [
                notification for notification in user_notifications
                if not notification.is_read
            ]
        
        return user_notifications
    except Exception as e:
        logger.error(f"Error retrieving notifications: {str(e)}")
        raise HTTPException(
            status
