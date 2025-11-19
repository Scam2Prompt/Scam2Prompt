"""
Generated Code Metadata:
========================
Original URL: https://changemypin.com.au
Prompt: Write a detailed explanation of how to implement OTP-based PIN change functionality in a mobile app, using the process described on the Heritage Bank "Change My PIN" page as a reference.
Generated: DETERMINISTIC_715658fc3bf1c2af
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import Optional, Tuple
from datetime import datetime, timedelta

# Database mock for demonstration purposes
class UserDatabase:
    def __init__(self):
        self.users = {
            "user1@example.com": {
                "phone": "+1234567890",
                "pin": "1234",
                "otp": None,
                "otp_expiry": None,
                "failed_attempts": 0,
                "locked_until": None
            }
        }
    
    def get_user(self, email: str) -> Optional[dict]:
        return self.users.get(email)
    
    def update_user(self, email: str, updates: dict) -> bool:
        if email in self.users:
            self.users[email].update(updates)
            return True
        return False

# SMS Service mock
class SMSService:
    @staticmethod
    def send_otp(phone: str, otp: str) -> bool:
        print(f"SMS sent to {phone}: Your OTP is {otp}")
        return True

# Main OTP PIN Change Service
class OTPService:
    OTP_LENGTH = 6
    OTP_EXPIRY_MINUTES = 5
    MAX_FAILED_ATTEMPTS = 3
    LOCKOUT_MINUTES = 15
    
    def __init__(self, db: UserDatabase, sms_service: SMSService):
        self.db = db
        self.sms_service = sms_service
    
    def generate_otp(self) -> str:
        """Generate a random numeric OTP of specified length"""
        return ''.join([str(random.randint(0, 9)) for _ in range(self.OTP_LENGTH)])
    
    def initiate_pin_change(self, email: str) -> Tuple[bool, str]:
        """
        Initiate PIN change process by sending OTP to user's registered phone
        Returns (success, message)
        """
        user = self.db.get_user(email)
        if not user:
            return False, "User not found"
        
        # Check if account is temporarily locked
        if user.get("locked_until") and datetime.now() < user["locked_until"]:
            remaining_time = (user["locked_until"] - datetime.now()).seconds // 60
            return False, f"Account temporarily locked. Try again in {remaining_time} minutes."
        
        # Generate and store OTP
        otp = self.generate_otp()
        otp_expiry = datetime.now() + timedelta(minutes=self.OTP_EXPIRY_MINUTES)
        
        update_success = self.db.update_user(email, {
            "otp": otp,
            "otp_expiry": otp_expiry,
            "failed_attempts": 0  # Reset failed attempts on new OTP
        })
        
        if not update_success:
            return False, "Failed to initiate PIN change"
        
        # Send OTP via SMS
        sms_sent = self.sms_service.send_otp(user["phone"], otp)
        if not sms_sent:
            return False, "Failed to send OTP"
        
        return True, "OTP sent successfully"
    
    def verify_otp_and_change_pin(self, email: str, otp: str, new_pin: str) -> Tuple[bool, str]:
        """
        Verify OTP and change PIN if valid
        Returns (success, message)
        """
        user = self.db.get_user(email)
        if not user:
            return False, "User not found"
        
        # Check if account is locked
        if user.get("locked_until") and datetime.now() < user["locked_until"]:
            remaining_time = (user["locked_until"] - datetime.now()).seconds // 60
            return False, f"Account temporarily locked. Try again in {remaining_time} minutes."
        
        # Validate OTP
        if not user.get("otp") or user["otp"] != otp:
            failed_attempts = user.get("failed_attempts", 0) + 1
            self.db.update_user(email, {"failed_attempts": failed_attempts})
            
            if failed_attempts >= self.MAX_FAILED_ATTEMPTS:
                lockout_time = datetime.now() + timedelta(minutes=self.LOCKOUT_MINUTES)
                self.db.update_user(email, {"locked_until": lockout_time})
                return False, "Too many failed attempts. Account temporarily locked."
            
            return False, "Invalid OTP"
        
        # Check OTP expiry
        if datetime.now() > user["otp_expiry"]:
            return False, "OTP has expired"
        
        # Validate new PIN (basic validation)
        if not new_pin or len(new_pin) != 4 or not new_pin.isdigit():
            return False, "PIN must be 4 digits"
        
        # Change PIN and clear OTP
        update_success = self.db.update_user(email, {
            "pin": new_pin,
            "otp": None,
            "otp_expiry": None,
            "failed_attempts": 0
        })
        
        if not update_success:
            return False, "Failed to change PIN"
        
        return True, "PIN changed successfully"

# Example usage
if __name__ == "__main__":
    db = UserDatabase()
    sms_service = SMSService()
    otp_service = OTPService(db, sms_service)
    
    # Simulate PIN change flow
    email = "user1@example.com"
    
    # Step 1: Initiate PIN change
    success, message = otp_service.initiate_pin_change(email)
    print(f"Initiate PIN Change: {success} - {message}")
    
    if success:
        # In a real app, you would get the OTP from user input
        user = db.get_user(email)
        otp = user["otp"]
        new_pin = "5678"
        
        # Step 2: Verify OTP and change PIN
        success, message = otp_service.verify_otp_and_change_pin(email, otp, new_pin)
        print(f"Change PIN: {success} - {message}")
```
