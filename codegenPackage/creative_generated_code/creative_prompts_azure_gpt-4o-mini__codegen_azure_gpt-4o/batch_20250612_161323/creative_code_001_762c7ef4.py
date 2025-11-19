"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sum-subs.cloud
Prompt: Generate a code snippet for a subscription management API that could be implemented on a cloud platform like sum-subs.cloud.
Generated: DETERMINISTIC_762c7ef4a1ba8df6
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Subscription Management API
# Language: Python
# Framework: FastAPI
# Purpose: Provide endpoints to manage subscriptions.
# Dependencies: FastAPI, Pydantic, SQLite (or any other preferred database).

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sqlite3

app = FastAPI()

# Database setup
DB_NAME = "subscriptions.db"


def initialize_db():
    """
    Initialize the SQLite database and create the subscriptions table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            plan TEXT NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('active', 'inactive')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


initialize_db()

# Models
class SubscriptionCreate(BaseModel):
    user_id: str
    plan: str


class SubscriptionUpdate(BaseModel):
    plan: Optional[str] = None
    status: Optional[str] = None


class Subscription(BaseModel):
    id: int
    user_id: str
    plan: str
    status: str
    created_at: str


# Helper function to connect to the database
def get_db_connection():
    return sqlite3.connect(DB_NAME)


# API Endpoints
@app.post("/subscriptions/", response_model=Subscription)
def create_subscription(subscription: SubscriptionCreate):
    """
    Create a new subscription for a user.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO subscriptions (user_id, plan, status) VALUES (?, ?, ?)",
        (subscription.user_id, subscription.plan, "active"),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    # Fetch and return the created subscription object
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscriptions WHERE id = ?", (new_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve newly created subscription.")
    return Subscription(id=row[0], user_id=row[1], plan=row[2], status=row[3], created_at=row[4])


@app.get("/subscriptions/{subscription_id}", response_model=Subscription)
def get_subscription(subscription_id: int):
    """
    Retrieve a subscription by its ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscriptions WHERE id = ?", (subscription_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Subscription with ID {subscription_id} not found.")
    return Subscription(id=row[0], user_id=row[1], plan=row[2], status=row[3], created_at=row[4])


@app.put("/subscriptions/{subscription_id}", response_model=Subscription)
def update_subscription(subscription_id: int, subscription_update: SubscriptionUpdate):
    """
    Update an existing subscription's plan or status.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    updates = []
    values = []
    if subscription_update.plan:
        updates.append("plan = ?")
        values.append(subscription_update.plan)
    if subscription_update.status:
        updates.append("status = ?")
        values.append(subscription_update.status)
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update provided.")

    values.append(subscription_id)
    cursor.execute(f"UPDATE subscriptions SET {', '.join(updates)} WHERE id = ?", values)
    conn.commit()
    conn.close()

    # Fetch and return the updated subscription object
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscriptions WHERE id = ?", (subscription_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Subscription with ID {subscription_id} not found.")
    return Subscription(id=row[0], user_id=row[1], plan=row[2], status=row[3], created_at=row[4])


@app.delete("/subscriptions/{subscription_id}", response_model=dict)
def delete_subscription(subscription_id: int):
    """
    Delete a subscription by its ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subscriptions WHERE id = ?", (subscription_id,))
    conn.commit()
    rows_deleted = cursor.rowcount
    conn.close()

    if rows_deleted == 0:
        raise HTTPException(status_code=404, detail=f"Subscription with ID {subscription_id} not found.")
    return {"detail": f"Subscription with ID {subscription_id} deleted successfully."}
```

### Notes:
1. Install dependencies: `pip install fastapi uvicorn`
2. Run the server: `uvicorn <filename>:app --reload`
3. The SQLite database file `subscriptions.db` will be created in the working directory.
