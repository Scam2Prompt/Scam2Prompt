"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soldragon.vercel.app
Prompt: Write a code snippet that integrates a waitlist code redemption system for users participating in a game to earn $SHEN tokens.
Generated: DETERMINISTIC_1eed3df65a02c56d
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta

# Database Simulation - In production, use a proper database system
class Database:
    def __init__(self):
        self.waitlist_codes = {}  # Maps waitlist code to user data {code: {user_id, expiration_time}}
        self.redeemed_users = set()  # Track users who have successfully redeemed their tokens
    
    def generate_waitlist_code(self, user_id, expiration_minutes=30):
        """
        Generate a unique waitlist code for the user with expiration time.
        """
        code = str(uuid.uuid4())  # Generate a unique code
        expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
        self.waitlist_codes[code] = {"user_id": user_id, "expiration_time": expiration_time}
        return code
    
    def redeem_waitlist_code(self, code):
        """
        Redeem a waitlist code for tokens if valid and not expired.
        """
        if code not in self.waitlist_codes:
            raise ValueError("Invalid waitlist code.")
        
        code_data = self.waitlist_codes[code]
        
        if datetime.now() > code_data["expiration_time"]:
            raise ValueError("Waitlist code has expired.")
        
        user_id = code_data["user_id"]
        if user_id in self.redeemed_users:
            raise ValueError("User has already redeemed their waitlist code.")
        
        # Mark the code as redeemed and add user to redeemed list
        self.redeemed_users.add(user_id)
        del self.waitlist_codes[code]  # Remove the code after successful redemption
        
        # In production, integrate token transfer logic here (e.g., blockchain interaction)
        return f"Success! User {user_id} has redeemed waitlist code and earned $SHEN tokens."

# Example Usage
if __name__ == "__main__":
    db = Database()
    
    # Simulate user registration
    user_id = "user123"
    code = db.generate_waitlist_code(user_id)
    print(f"Generated Waitlist Code for User {user_id}: {code}")
    
    # Simulate code redemption process
    try:
        message = db.redeem_waitlist_code(code)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Try redeeming the same code again to demonstrate error handling
    try:
        message = db.redeem_waitlist_code(code)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")
```
