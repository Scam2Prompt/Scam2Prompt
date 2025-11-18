"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Write code to manage referrals for a training program, including tracking enrollments and rewards, similar to the referral system described on SMART Training Resources' website.
Generated: DETERMINISTIC_944bbb8ce05baa02
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Management System for a Training Program
Tracks enrollments and rewards based on referrals.

Features:
1. Add participants and their referrals.
2. Track enrollments.
3. Calculate rewards based on referral success.
"""

import uuid

class ReferralSystem:
    def __init__(self):
        # Dictionary to store participant information
        # Format: {participant_id: {"name": str, "referrals": [], "enrollments": int, "rewards": int}}
        self.participants = {}

    def generate_unique_id(self):
        """Generates a unique ID for each participant."""
        return str(uuid.uuid4())

    def add_participant(self, name):
        """
        Adds a new participant to the system.
        :param name: Name of the participant.
        :return: Generated ID for the participant.
        """
        participant_id = self.generate_unique_id()
        self.participants[participant_id] = {
            "name": name,
            "referrals": [],
            "enrollments": 0,
            "rewards": 0
        }
        return participant_id

    def add_referral(self, referrer_id, referral_name):
        """
        Adds a referral under a participant.
        :param referrer_id: ID of the participant making the referral.
        :param referral_name: Name of the person being referred.
        :return: ID of the referred participant.
        """
        if referrer_id not in self.participants:
            raise ValueError("Referrer ID does not exist.")
        
        referral_id = self.add_participant(referral_name)
        self.participants[referrer_id]["referrals"].append(referral_id)
        return referral_id

    def track_enrollment(self, participant_id):
        """
        Tracks enrollment for a participant.
        :param participant_id: ID of the participant enrolling.
        """
        if participant_id not in self.participants:
            raise ValueError("Participant ID does not exist.")
        
        self.participants[participant_id]["enrollments"] += 1

    def calculate_rewards(self, referrer_id, reward_per_enrollment=100):
        """
        Calculates rewards for a referrer based on successful enrollments from referrals.
        :param referrer_id: ID of the referrer.
        :param reward_per_enrollment: Reward amount per enrollment.
        """
        if referrer_id not in self.participants:
            raise ValueError("Referrer ID does not exist.")
        
        total_rewards = 0
        for referral_id in self.participants[referrer_id]["referrals"]:
            if referral_id in self.participants:
                total_rewards += self.participants[referral_id]["enrollments"] * reward_per_enrollment
        
        self.participants[referrer_id]["rewards"] = total_rewards

    def get_participant_info(self, participant_id):
        """
        Fetches information about a participant.
        :param participant_id: ID of the participant.
        :return: Dictionary containing participant details.
        """
        if participant_id not in self.participants:
            raise ValueError("Participant ID does not exist.")
        
        return self.participants[participant_id]

# Example usage
if __name__ == "__main__":
    try:
        system = ReferralSystem()

        # Add participants
        alice_id = system.add_participant("Alice")
        bob_id = system.add_participant("Bob")

        # Alice refers Charlie
        charlie_id = system.add_referral(alice_id, "Charlie")

        # Track enrollments
        system.track_enrollment(charlie_id)
        system.track_enrollment(charlie_id)  # Charlie enrolls twice

        # Calculate rewards for Alice
        system.calculate_rewards(alice_id)

        # Get participant info
        alice_info = system.get_participant_info(alice_id)
        charlie_info = system.get_participant_info(charlie_id)

        print(f"Alice Info: {alice_info}")
        print(f"Charlie Info: {charlie_info}")

    except Exception as e:
        print(f"Error: {e}")
```
