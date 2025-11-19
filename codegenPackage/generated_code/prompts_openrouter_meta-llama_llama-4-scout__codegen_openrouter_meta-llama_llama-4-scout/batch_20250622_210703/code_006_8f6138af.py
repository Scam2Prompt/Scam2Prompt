"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Write a code snippet to track and manage therapy referrals for children, including progress monitoring and communication with parents and therapists.
Generated: DETERMINISTIC_8f6138aff1855e2d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# therapy_referral_tracker.py

import datetime
from enum import Enum

class TherapyStatus(Enum):
    """Enum for therapy status"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class Referral:
    """Class to represent a therapy referral"""
    def __init__(self, child_name, therapist_name, parent_contact):
        self.child_name = child_name
        self.therapist_name = therapist_name
        self.parent_contact = parent_contact
        self.status = TherapyStatus.PENDING
        self.progress_notes = []

    def update_status(self, status):
        """Update the status of the referral"""
        if not isinstance(status, TherapyStatus):
            raise ValueError("Invalid therapy status")
        self.status = status

    def add_progress_note(self, note):
        """Add a progress note to the referral"""
        self.progress_notes.append((datetime.datetime.now(), note))

    def __str__(self):
        return f"Child: {self.child_name}, Therapist: {self.therapist_name}, Status: {self.status.name}"

class TherapyReferralTracker:
    """Class to track and manage therapy referrals"""
    def __init__(self):
        self.referrals = {}

    def create_referral(self, child_name, therapist_name, parent_contact):
        """Create a new referral"""
        referral = Referral(child_name, therapist_name, parent_contact)
        self.referrals[child_name] = referral
        return referral

    def get_referral(self, child_name):
        """Get a referral by child name"""
        return self.referrals.get(child_name)

    def update_referral_status(self, child_name, status):
        """Update the status of a referral"""
        referral = self.get_referral(child_name)
        if referral:
            referral.update_status(status)
        else:
            raise ValueError("Referral not found")

    def add_progress_note(self, child_name, note):
        """Add a progress note to a referral"""
        referral = self.get_referral(child_name)
        if referral:
            referral.add_progress_note(note)
        else:
            raise ValueError("Referral not found")

    def send_communication(self, child_name, message, recipient):
        """Send communication to a parent or therapist"""
        referral = self.get_referral(child_name)
        if referral:
            if recipient == "parent":
                print(f"Sending to parent: {referral.parent_contact} - {message}")
            elif recipient == "therapist":
                print(f"Sending to therapist: {referral.therapist_name} - {message}")
            else:
                raise ValueError("Invalid recipient")
        else:
            raise ValueError("Referral not found")

def main():
    tracker = TherapyReferralTracker()

    # Create a referral
    referral = tracker.create_referral("John Doe", "Jane Smith", "123-456-7890")
    print(referral)

    # Update referral status
    tracker.update_referral_status("John Doe", TherapyStatus.IN_PROGRESS)
    print(tracker.get_referral("John Doe"))

    # Add progress note
    tracker.add_progress_note("John Doe", "Progress note 1")
    print("Progress Notes:")
    for note in tracker.get_referral("John Doe").progress_notes:
        print(note)

    # Send communication
    tracker.send_communication("John Doe", "Hello, this is a test message", "parent")

if __name__ == "__main__":
    main()
```
