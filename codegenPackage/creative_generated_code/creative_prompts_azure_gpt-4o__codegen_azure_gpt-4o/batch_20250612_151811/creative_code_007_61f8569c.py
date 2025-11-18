"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Create a referral tracking system for freight factoring and international factoring programs, similar to Summar Financial's referral offerings.
Generated: DETERMINISTIC_61f8569c2ea8c28c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_tracking_system.py

import uuid
import json
from datetime import datetime

class ReferralTrackingSystem:
    def __init__(self):
        """
        Initializes the Referral Tracking System.
        Stores referral data in an in-memory dictionary.
        """
        self.referrals = {}  # In-memory storage for referrals.

    def generate_referral_code(self):
        """
        Generates a unique referral code using UUID.
        :return: A unique referral code.
        """
        return str(uuid.uuid4())[:8]  # Shorten UUID for cleaner referral codes.

    def create_referral(self, referrer_name, program_type):
        """
        Creates a new referral entry.
        :param referrer_name: Name of the person referring.
        :param program_type: Type of program (e.g., "freight_factoring" or "international_factoring").
        :return: Referral code.
        """
        if program_type not in ["freight_factoring", "international_factoring"]:
            raise ValueError("Invalid program type. Use 'freight_factoring' or 'international_factoring'.")

        referral_code = self.generate_referral_code()
        self.referrals[referral_code] = {
            "referrer_name": referrer_name,
            "program_type": program_type,
            "timestamp": datetime.now().isoformat(),
            "used": False
        }
        return referral_code

    def get_referral_info(self, referral_code):
        """
        Retrieves information about a specific referral.
        :param referral_code: The referral code to search for.
        :return: Referral information dictionary.
        """
        referral = self.referrals.get(referral_code)
        if referral:
            return referral
        else:
            raise ValueError("Referral code not found.")

    def mark_referral_as_used(self, referral_code):
        """
        Marks a referral code as used.
        :param referral_code: The referral code to mark as used.
        :return: Success message.
        """
        referral = self.referrals.get(referral_code)
        if not referral:
            raise ValueError("Referral code not found.")
        if referral["used"]:
            raise ValueError("Referral code has already been used.")

        self.referrals[referral_code]["used"] = True
        return f"Referral code '{referral_code}' has been successfully marked as used."

    def export_referrals(self, file_name="referrals.json"):
        """
        Exports all referral data to a JSON file.
        :param file_name: Name of the file to save referrals (default: referrals.json).
        :return: Success message.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.referrals, file, indent=4)
            return f"Referrals successfully exported to {file_name}"
        except IOError as e:
            raise RuntimeError(f"Failed to export referrals: {str(e)}")


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize referral system
        system = ReferralTrackingSystem()
        
        # Create referrals
        code1 = system.create_referral("Alice", "freight_factoring")
        code2 = system.create_referral("Bob", "international_factoring")
        
        print(f"Referral Code for Alice: {code1}")
        print(f"Referral Code for Bob: {code2}")
        
        # Retrieve referral information
        print("Referral Info for Alice's Code:", system.get_referral_info(code1))
        
        # Mark a referral code as used
        print(system.mark_referral_as_used(code1))
        
        # Attempt to mark the same referral code as used again
        try:
            system.mark_referral_as_used(code1)
        except ValueError as e:
            print(f"Error: {e}")
        
        # Export referrals to a JSON file
        print(system.export_referrals())
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
