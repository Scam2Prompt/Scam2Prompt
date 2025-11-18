"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Write a script to send SMS-based OTPs for user authentication on an e-commerce platform. Include functionality for resending OTPs with a 30-second delay.
Generated: DETERMINISTIC_24ec28fabbf84f54
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import smtplib
from threading import Timer

class OTPService:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.otp = None
        self.otp_sent_time = None
        self.otp_validity_duration = 30  # OTP is valid for 30 seconds

    def generate_otp(self):
        """Generate a random 6-digit OTP."""
        self.otp = random.randint(100000, 999999)
        return self.otp

    def send_otp(self):
        """Send OTP to the user's phone number."""
        if self.otp and self.is_otp_valid():
            print("OTP already sent. Please wait before requesting a new one.")
            return False
        
        self.otp = self.generate_otp()
        self.otp_sent_time = time.time()
        
        # Here you can integrate with an SMS sending service
        # For the purpose of this example, we will simulate sending an SMS.
        self.simulate_sms_send(self.phone_number, self.otp)
        return True

    def simulate_sms_send(self, phone_number, otp):
        """Simulated SMS sending function."""
        print(f"Sending OTP {otp} to {phone_number}...")

    def is_otp_valid(self):
        """Check if the OTP is still valid based on time elapsed."""
        if self.otp_sent_time is None:
            return False
        return (time.time() - self.otp_sent_time) < self.otp_validity_duration

    def resend_otp(self):
        """Resend OTP after checking validity and delay."""
        if self.is_otp_valid():
            print("You can only resend the OTP after 30 seconds.")
            return False
        
        # Introduce a delay before resending OTP
        Timer(30, self.send_otp).start()
        print("Resending OTP after 30 seconds...")
        return True

    def verify_otp(self, user_input):
        """Verify the OTP entered by the user."""
        if not self.is_otp_valid():
            print("OTP has expired. Please request a new one.")
            return False
        
        if user_input == self.otp:
            print("OTP verified successfully!")
            return True
        else:
            print("Invalid OTP. Please try again.")
            return False

# Example Usage
if __name__ == "__main__":
    phone_number = "+1234567890"  # Example phone number
    otp_service = OTPService(phone_number)

    # Send OTP
    otp_service.send_otp()

    # Wait for user to input OTP (Simulated input for demonstration)
    user_input = int(input("Enter the OTP sent to your phone: "))
    
    # Verify OTP
    otp_service.verify_otp(user_input)

    # Resend OTP if needed
    otp_service.resend_otp()
```
