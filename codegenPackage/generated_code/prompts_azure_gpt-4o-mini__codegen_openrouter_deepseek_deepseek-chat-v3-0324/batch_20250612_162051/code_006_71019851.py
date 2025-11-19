"""
Generated Code Metadata:
========================
Original URL: https://www.virtualmediaevents.com
Prompt: What code can I use to facilitate simultaneous mini-sessions for up to 300 participants in a virtual event using VME's technology?
Generated: DETERMINISTIC_71019851fe8074e2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import logging
from typing import List, Dict, Optional
from uuid import uuid4

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MiniSession:
    def __init__(self, session_id: str, max_participants: int = 20):
        self.session_id = session_id
        self.max_participants = max_participants
        self.participants: List[str] = []
        self.is_active = False

    def add_participant(self, participant_id: str) -> bool:
        """Add participant to session if there's space"""
        if len(self.participants) < self.max_participants:
            self.participants.append(participant_id)
            return True
        return False

    def remove_participant(self, participant_id: str) -> bool:
        """Remove participant from session"""
        try:
            self.participants.remove(participant_id)
            return True
        except ValueError:
            return False

    def start_session(self) -> None:
        """Mark session as active"""
        self.is_active = True

    def end_session(self) -> None:
        """Mark session as inactive"""
        self.is_active = False

class SessionManager:
    def __init__(self, max_sessions: int = 15):  # 15 sessions * 20 participants = 300
        self.sessions: Dict[str, MiniSession] = {}
        self.max_sessions = max_sessions

    def create_session(self) -> Optional[str]:
        """Create a new mini-session if under max capacity"""
        if len(self.sessions) >= self.max_sessions:
            return None

        session_id = str(uuid4())
        self.sessions[session_id] = MiniSession(session_id)
        return session_id

    def get_available_session(self) -> Optional[str]:
        """Find a session with available space"""
        for session_id, session in self.sessions.items():
            if len(session.participants) < session.max_participants and session.is_active:
                return session_id
        return None

    def add_participant_to_session(self, participant_id: str) -> Optional[str]:
        """Add participant to an available session"""
        session_id = self.get_available_session()
        if session_id is None:
            session_id = self.create_session()
            if session_id is None:
                return None
            self.sessions[session_id].start_session()

        if self.sessions[session_id].add_participant(participant_id):
            return session_id
        return None

    def remove_participant(self, participant_id: str, session_id: str) -> bool:
        """Remove participant from a session"""
        if session_id not in self.sessions:
            return False
        return self.sessions[session_id].remove_participant(participant_id)

    def end_session(self, session_id: str) -> bool:
        """End a specific session"""
        if session_id not in self.sessions:
            return False
        self.sessions[session_id].end_session()
        return True

async def handle_participant(participant_id: str, manager: SessionManager) -> None:
    """Simulate participant joining a session"""
    try:
        session_id = manager.add_participant_to_session(participant_id)
        if session_id is None:
            logger.error(f"No available sessions for participant {participant_id}")
            return

        logger.info(f"Participant {participant_id} joined session {session_id}")
        
        # Simulate participant staying in session
        await asyncio.sleep(30)
        
        # Remove participant when done
        manager.remove_participant(participant_id, session_id)
        logger.info(f"Participant {participant_id} left session {session_id}")
        
    except Exception as e:
        logger.error(f"Error handling participant {participant_id}: {str(e)}")

async def main():
    manager = SessionManager()
    
    # Simulate 300 participants joining
    participants = [str(uuid4()) for _ in range(300)]
    tasks = [handle_participant(pid, manager) for pid in participants]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```
