"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalflightguide.com
Prompt: Write code to implement a referral system that connects users to flight booking services, ensuring compliance with TCPA disclosure requirements as outlined on globalflightguide.com.
Generated: DETERMINISTIC_d83c86f1acf83fe5
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

# Referral system implementation for flight booking services
class ReferralSystem:
    def __init__(self):
        # Stores user data and their referrals
        self.users = {}
        self.referrals = {}
    
    def create_user(self, name, email, phone_number):
        """
        Create a new user in the system.

        Args:
            name (str): Name of the user.
            email (str): Email of the user.
            phone_number (str): Phone number of the user.

        Returns:
            dict: A dictionary containing the user's details.
        """
        try:
            # Generate a unique user ID
            user_id = str(uuid.uuid4())
            
            # Validate input
            if not name or not email or not phone_number:
                raise ValueError("All fields (name, email, phone_number) are required.")
            
            # Ensure email isn't already registered
            if any(user['email'] == email for user in self.users.values()):
                raise ValueError("Email already registered.")
            
            # Ensure phone number isn't already registered
            if any(user['phone_number'] == phone_number for user in self.users.values()):
                raise ValueError("Phone number already registered.")
            
            # Create a user record
            user = {
                "user_id": user_id,
                "name": name,
                "email": email,
                "phone_number": phone_number,
                "created_at": datetime.now(),
                "referral_code": str(uuid.uuid4())[:8],  # Generate a short referral code
                "referred_by": None  # Initially, no one referred this user
            }
            
            self.users[user_id] = user
            
            return user
        except Exception as e:
            raise ValueError(f"Error creating user: {str(e)}")

    def refer_user(self, referrer_code, name, email, phone_number):
        """
        Refer a new user to the system using a referral code.

        Args:
            referrer_code (str): The referral code of the user making the referral.
            name (str): Name of the new user.
            email (str): Email of the new user.
            phone_number (str): Phone number of the new user.

        Returns:
            dict: A dictionary containing the new user's details and referral information.
        """
        try:
            # Find referrer by referral code
            referrer = next(
                (user for user in self.users.values() if user['referral_code'] == referrer_code), 
                None
            )
            if not referrer:
                raise ValueError("Invalid referral code.")
            
            # Create the new user
            new_user = self.create_user(name, email, phone_number)
            
            # Link referrer and new user
            new_user["referred_by"] = referrer["user_id"]
            referrer_id = referrer["user_id"]
            
            # Store referral information
            if referrer_id not in self.referrals:
                self.referrals[referrer_id] = []
            self.referrals[referrer_id].append(new_user["user_id"])
            
            return new_user
        except Exception as e:
            raise ValueError(f"Error referring user: {str(e)}")

    def get_user_referrals(self, user_id):
        """
        Retrieve a list of users referred by the given user.

        Args:
            user_id (str): The ID of the user whose referrals are to be retrieved.

        Returns:
            list: A list of user details referred by the given user.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        
        referred_user_ids = self.referrals.get(user_id, [])
        return [self.users[uid] for uid in referred_user_ids]

    def ensure_tcpa_compliance(self):
        """
        Display TCPA disclosure to ensure compliance.

        This function should be called before sending any communications
        to ensure users are aware of terms and conditions.
        """
        return (
            "By using this service, you agree to receive communications "
            "regarding your referrals and bookings. For more details, visit "
            "globalflightguide.com/tcpa-disclosure."
        )


# Example usage
if __name__ == "__main__":
    try:
        system = ReferralSystem()
        
        # Display TCPA disclosure
        print(system.ensure_tcpa_compliance())
        
        # Create a new user
        user1 = system.create_user("John Doe", "john@example.com", "1234567890")
        print(f"User created: {user1}")
        
        # Refer a new user
        referred_user = system.refer_user(user1["referral_code"], "Jane Smith", "jane@example.com", "0987654321")
        print(f"Referred user: {referred_user}")
        
        # Get referrals for a user
        user1_referrals = system.get_user_referrals(user1["user_id"])
        print(f"Referrals for {user1['name']}: {user1_referrals}")
    except Exception as e:
        print(f"Error: {e}")
```
