"""
Generated Code Metadata:
========================
Original URL: https://ktx.typeform.com
Prompt: Explain how to use Typeform's quiz maker to create a trivia quiz and write code to collect and store user responses in a database.
Generated: DETERMINISTIC_1daf66b111d13977
Batch ID: 20250612_151847
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com": {
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
import requests
from typing import Dict, Any
import sqlite3
from datetime import datetime

# Configuration for Typeform API
TYPEFORM_API_KEY = "your_typeform_api_key"
TYPEFORM_FORM_ID = "your_form_id"
TYPEFORM_API_BASE_URL = "https://api.typeform.com"

# Database configuration
DATABASE_NAME = "trivia_quiz_responses.db"

def create_database() -> None:
    """Create SQLite database and tables for storing quiz responses."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        response_id TEXT NOT NULL UNIQUE,
        form_id TEXT NOT NULL,
        user_id TEXT,
        submitted_at DATETIME NOT NULL,
        score INTEGER,
        raw_response TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        response_id TEXT NOT NULL,
        question_id TEXT NOT NULL,
        question_text TEXT NOT NULL,
        answer_text TEXT NOT NULL,
        is_correct BOOLEAN,
        FOREIGN KEY (response_id) REFERENCES responses (response_id)
    )
    """)
    
    conn.commit()
    conn.close()

def fetch_typeform_responses() -> Dict[str, Any]:
    """Fetch responses from Typeform API."""
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}",
        "Content-Type": "application/json"
    }
    
    url = f"{TYPEFORM_API_BASE_URL}/forms/{TYPEFORM_FORM_ID}/responses"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching responses from Typeform: {e}")
        return {}

def process_response(response_data: Dict[str, Any]) -> None:
    """Process and store a single Typeform response."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    try:
        response_id = response_data.get("response_id")
        submitted_at = response_data.get("submitted_at")
        answers = response_data.get("answers", [])
        
        # Calculate score
        score = sum(1 for answer in answers if answer.get("is_correct", False))
        
        # Insert main response
        cursor.execute("""
        INSERT OR IGNORE INTO responses (
            response_id, form_id, user_id, submitted_at, score, raw_response
        ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            response_id,
            TYPEFORM_FORM_ID,
            response_data.get("hidden", {}).get("user_id"),
            datetime.strptime(submitted_at, "%Y-%m-%dT%H:%M:%SZ"),
            score,
            str(response_data)
        ))
        
        # Insert answers
        for answer in answers:
            cursor.execute("""
            INSERT INTO answers (
                response_id, question_id, question_text, answer_text, is_correct
            ) VALUES (?, ?, ?, ?, ?)
            """, (
                response_id,
                answer.get("field", {}).get("id"),
                answer.get("field", {}).get("title"),
                answer.get("text") or str(answer.get("choice", {}).get("label")),
                answer.get("is_correct", False)
            ))
        
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error processing response {response_id}: {e}")
    finally:
        conn.close()

def sync_responses() -> None:
    """Sync all responses from Typeform to local database."""
    print("Starting response sync...")
    create_database()
    
    responses_data = fetch_typeform_responses()
    if not responses_data:
        print("No responses found or error occurred.")
        return
    
    items = responses_data.get("items", [])
    print(f"Found {len(items)} responses to process.")
    
    for response in items:
        process_response(response)
    
    print("Sync completed successfully.")

if __name__ == "__main__":
    sync_responses()
```
