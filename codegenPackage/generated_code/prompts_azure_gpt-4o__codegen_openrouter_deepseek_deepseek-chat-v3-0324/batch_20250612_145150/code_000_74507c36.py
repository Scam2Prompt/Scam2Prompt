"""
Generated Code Metadata:
========================
Original URL: https://changemypin.com.au
Prompt: Write Python code to simulate the process of changing a card PIN using a PIN Change Number, One Time Password (OTP), and new PIN as described on the Heritage Bank "Change My PIN" page.
Generated: DETERMINISTIC_74507c367962c326
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

class PinChangeSimulator:
    """
    Simulates the process of changing a card PIN using:
    - PIN Change Number (PCN)
    - One Time Password (OTP)
    - New PIN
    """
    
    def __init__(self):
        self.pin_change_number: Optional[str] = None
        self.otp: Optional[str] = None
        self.otp_expiry: Optional[float] = None
        self.otp_attempts: int = 0
        self.max_otp_attempts: int = 3
        self.otp_validity_period: int = 300  # 5 minutes in seconds
        
    def generate_pin_change_number(self) -> str:
        """Generate a 16-digit PIN Change Number (PCN)."""
        self.pin_change_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
        return self.pin_change_number
    
    def generate_otp(self) -> Tuple[str, float]:
        """Generate a 6-digit OTP and set its expiry time."""
        self.otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.otp_expiry = time.time() + self.otp_validity_period
        self.otp_attempts = 0
        return self.otp, self.otp_expiry
    
    def validate_otp(self, user_otp: str) -> bool:
        """
        Validate the provided OTP against the generated OTP.
        Returns True if valid, False otherwise.
        """
        if self.otp is None or self.otp_expiry is None:
            return False
            
        current_time = time.time()
        if current_time > self.otp_expiry:
            return False
            
        self.otp_attempts += 1
        if self.otp_attempts > self.max_otp_attempts:
            return False
            
        return user_otp == self.otp
    
    def validate_new_pin(self, new_pin: str) -> bool:
        """
        Validate the new PIN meets requirements:
        - 4 digits
        - Not sequential (e.g., 1234)
        - Not repeating (e.g., 1111)
        """
        if len(new_pin) != 4 or not new_pin.isdigit():
            return False
            
        # Check for sequential numbers
        if (all(int(new_pin[i]) + 1 == int(new_pin[i+1]) for i in range(3)) or
            all(int(new_pin[i]) - 1 == int(new_pin[i+1]) for i in range(3))):
            return False
            
        # Check for repeating numbers
        if len(set(new_pin)) == 1:
            return False
            
        return True
    
    def change_pin(
        self,
        pin_change_number: str,
        otp: str,
        new_pin: str
    ) -> Tuple[bool, str]:
        """
        Process the PIN change request.
        Returns (success: bool, message: str)
        """
        # Validate PIN Change Number
        if self.pin_change_number is None or pin_change_number != self.pin_change_number:
            return False, "Invalid PIN Change Number"
            
        # Validate OTP
        if not self.validate_otp(otp):
            return False, "Invalid or expired OTP"
            
        # Validate new PIN
        if not self.validate_new_pin(new_pin):
            return False, "Invalid PIN. Must be 4 unique, non-sequential digits"
            
        # If all validations pass, PIN change is successful
        self.pin_change_number = None
        self.otp = None
        self.otp_expiry = None
        return True, "PIN changed successfully"


# Example usage
if __name__ == "__main__":
    simulator = PinChangeSimulator()
    
    # Step 1: Generate PIN Change Number
    pcn = simulator.generate_pin_change_number()
    print(f"Generated PIN Change Number: {pcn}")
    
    # Step 2: Generate OTP
    otp, expiry = simulator.generate_otp()
    print(f"Generated OTP: {otp} (expires in 5 minutes)")
    
    # Step 3: Simulate PIN change
    # User provides PCN, OTP, and new PIN
    result, message = simulator.change_pin(
        pin_change_number=pcn,
        otp=otp,
        new_pin="2468"
    )
    
    print(f"PIN change result: {result}, Message: {message}")
```
