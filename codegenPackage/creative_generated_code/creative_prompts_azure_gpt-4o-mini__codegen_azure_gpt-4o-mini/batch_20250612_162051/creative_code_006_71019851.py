"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: What code can I use to facilitate simultaneous mini-sessions for up to 300 participants in a virtual event using VME's technology?
Generated: DETERMINISTIC_71019851fe8074e2
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vme.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)

class VMEEvent:
    def __init__(self, api_url: str, event_id: str):
        """
        Initializes the VMEEvent with the API URL and event ID.
        
        :param api_url: The URL of the VME API
        :param event_id: The unique ID of the event to be managed
        """
        self.api_url = api_url
        self.event_id = event_id

    def create_mini_session(self, session_id: str, participant_ids: list):
        """
        Creates a mini session for a group of participants.
        
        :param session_id: The unique ID for the mini session
        :param participant_ids: List of participant IDs to be included in this session
        :return: Response from the VME API
        """
        payload = {
            "session_id": session_id,
            "event_id": self.event_id,
            "participants": participant_ids
        }
        try:
            response = requests.post(f"{self.api_url}/create_mini_session", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info(f"Mini session {session_id} created successfully.")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error creating mini session {session_id}: {e}")
            return None

    def facilitate_sessions(self, num_sessions: int, participants: list):
        """
        Facilitates the creation of multiple mini sessions simultaneously.

        :param num_sessions: Number of mini sessions to create
        :param participants: List of participant IDs
        """
        # Split participants into equal groups for mini sessions
        participant_groups = [participants[i::num_sessions] for i in range(num_sessions)]

        with ThreadPoolExecutor(max_workers=num_sessions) as executor:
            future_to_session = {
                executor.submit(self.create_mini_session, f"session_{i + 1}", group): i + 1
                for i, group in enumerate(participant_groups)
            }
            for future in as_completed(future_to_session):
                session_num = future_to_session[future]
                try:
                    result = future.result()
                    if result is not None:
                        logging.info(f"Session {session_num} created with response: {result}")
                except Exception as e:
                    logging.error(f"Session {session_num} generated an exception: {e}")

if __name__ == "__main__":
    # Example usage: 
    API_URL = "https://api.vme.com"
    EVENT_ID = "event_12345"
    
    # Initialize the VME Event
    vme_event = VMEEvent(API_URL, EVENT_ID)
    
    # Define participants (example participant IDs)
    participant_ids = [f"participant_{i}" for i in range(300)]
    
    # Facilitate mini sessions for up to 300 participants
    vme_event.facilitate_sessions(num_sessions=10, participants=participant_ids)  # 10 sessions with 30 participants each
```

Make sure to replace the `API_URL` and `EVENT_ID` with the actual values for your VME event integration. This code assumes that the VME API has an endpoint for creating mini sessions and that it accepts a JSON payload with the specified structure.
