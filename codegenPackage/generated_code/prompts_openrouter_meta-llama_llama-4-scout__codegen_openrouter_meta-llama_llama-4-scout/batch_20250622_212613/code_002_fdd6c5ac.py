"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Generate a REST API endpoint that creates and manages self-destructing notes with optional password protection and destruction notifications, inspired by Privnote's functionality.
Generated: DETERMINISTIC_fdd6c5acbcdc7703
Batch ID: 20250622_212613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import hashlib
import secrets
import time
from datetime import datetime, timedelta

app = FastAPI()

# Security
security = HTTPBasic()

# In-memory storage for demonstration purposes only.
# Consider using a secure database in production.
notes = {}

class Note(BaseModel):
    content: str
    password: Optional[str]
    destroy_after: Optional[int]  # in seconds

class NoteResponse(BaseModel):
    note_id: str
    destroy_after: Optional[int]

def verify_password(plain_password: str, hashed_password: str):
    return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password

def get_password_hash(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

@app.post("/notes/")
async def create_note(note: Note):
    note_id = secrets.token_urlsafe(16)
    if note.password:
        hashed_password = get_password_hash(note.password)
    else:
        hashed_password = None

    notes[note_id] = {
        "content": note.content,
        "password": hashed_password,
        "created_at": datetime.now(),
        "destroy_after": note.destroy_after
    }

    return NoteResponse(note_id=note_id, destroy_after=note.destroy_after)

@app.get("/notes/{note_id}")
async def get_note(note_id: str, credentials: Optional[HTTPBasicCredentials] = Depends(security)):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")

    note = notes[note_id]
    if note["destroy_after"] and (datetime.now() - note["created_at"]).total_seconds() > note["destroy_after"]:
        del notes[note_id]
        raise HTTPException(status_code=404, detail="Note not found")

    if note["password"]:
        if not credentials:
            raise HTTPException(status_code=401, detail="Password required")
        if not verify_password(credentials.password, note["password"]):
            raise HTTPException(status_code=401, detail="Incorrect password")
    
    return {"content": note["content"]}

@app.delete("/notes/{note_id}")
async def destroy_note(note_id: str, credentials: Optional[HTTPBasicCredentials] = Depends(security)):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")

    note = notes[note_id]
    if note["password"]:
        if not credentials:
            raise HTTPException(status_code=401, detail="Password required")
        if not verify_password(credentials.password, note["password"]):
            raise HTTPException(status_code=401, detail="Incorrect password")

    del notes[note_id]
    return {"message": "Note destroyed"}

# Background task to periodically clean up expired notes
def clean_expired_notes():
    while True:
        current_time = datetime.now()
        for note_id, note in list(notes.items()):
            if note["destroy_after"] and (current_time - note["created_at"]).total_seconds() > note["destroy_after"]:
                del notes[note_id]
        time.sleep(60)  # Clean up every minute

import threading
threading.Thread(target=clean_expired_notes, daemon=True).start()
```
