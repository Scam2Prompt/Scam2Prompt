"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molinahealthcareinc.com
Prompt: Provide an example of code to create a referral system for doctors to admit patients to a medical center, as mentioned in the "Refer a patient" section of the Molina Healthcare Inc. website.
Generated: DETERMINISTIC_5d01a7c11dd81b4e
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py
import uuid
from datetime import datetime

class ReferralSystem:
    """
    A system to manage referrals for doctors to admit patients to a medical center.
    """

    def __init__(self):
        # Initialize an empty list to store referrals
        self.referrals = []

    def create_referral(self, doctor_name, patient_name, reason_for_referral):
        """
        Create a new referral and add it to the system.
        
        :param doctor_name: Name of the referring doctor
        :param patient_name: Name of the patient being referred
        :param reason_for_referral: Reason for referral
        :return: The newly created referral ID
        """
        try:
            # Generate a unique referral ID
            referral_id = str(uuid.uuid4())
            
            # Create a referral record
            referral = {
                "referral_id": referral_id,
                "doctor_name": doctor_name,
                "patient_name": patient_name,
                "reason_for_referral": reason_for_referral,
                "timestamp": datetime.now().isoformat()
            }
            
            # Add the referral to the list of referrals
            self.referrals.append(referral)
            
            return referral_id
        except Exception as e:
            # Handle any unexpected errors during referral creation
            print(f"Error creating referral: {e}")
            return None

    def get_referral(self, referral_id):
        """
        Retrieve a referral by its ID.
        
        :param referral_id: The ID of the referral to retrieve
        :return: The referral record, or None if not found
        """
        try:
            # Search for the referral by ID
            for referral in self.referrals:
                if referral["referral_id"] == referral_id:
                    return referral
            
            # If no referral is found with the given ID
            print(f"Referral with ID {referral_id} not found.")
            return None
        except Exception as e:
            # Handle any unexpected errors during retrieval
            print(f"Error retrieving referral: {e}")
            return None

    def list_referrals(self):
        """
        List all referrals in the system.
        
        :return: A list of all referral records
        """
        try:
            return self.referrals
        except Exception as e:
            # Handle any unexpected errors during listing
            print(f"Error listing referrals: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Create an instance of the referral system
    system = ReferralSystem()

    # Create a new referral
    referral_id = system.create_referral(
        doctor_name="Dr. John Smith",
        patient_name="Jane Doe",
        reason_for_referral="Routine Checkup"
    )
    print(f"Referral created with ID: {referral_id}")

    # Retrieve the referral details
    referral = system.get_referral(referral_id)
    print(f"Retrieved Referral: {referral}")

    # List all referrals
    all_referrals = system.list_referrals()
    print("All Referrals:")
    for r in all_referrals:
        print(r)
```
