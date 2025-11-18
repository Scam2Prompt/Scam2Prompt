"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-sparkprotocol-io.ipns.dweb.link
Prompt: Create a Python script that checks the user's eligibility to access Spark Protocol services based on the Terms of Use, including location restrictions and VPN usage.
Generated: DETERMINISTIC_324f797948236cb0
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class SparkProtocolAccessChecker:
    """
    A class to check user eligibility for accessing Spark Protocol services
    based on location restrictions and VPN usage.
    """

    def __init__(self, user_location, is_using_vpn):
        """
        Initializes the access checker with user location and VPN status.

        :param user_location: str - The geographic location of the user.
        :param is_using_vpn: bool - True if the user is using a VPN, False otherwise.
        """
        self.user_location = user_location
        self.is_using_vpn = is_using_vpn
        self.restricted_locations = ['North Korea', 'Iran', 'Syria']
    
    def is_location_restricted(self):
        """
        Checks if the user's location is restricted.

        :return: bool - True if the location is restricted, False otherwise.
        """
        return self.user_location in self.restricted_locations

    def check_access(self):
        """
        Checks if the user is eligible to access Spark Protocol services.

        :return: str - Message indicating access eligibility.
        """
        try:
            if self.is_using_vpn:
                return "Access denied: VPN usage is prohibited."
            
            if self.is_location_restricted():
                return "Access denied: Your location is restricted."

            return "Access granted: You are eligible to use Spark Protocol services."
            
        except Exception as e:
            return f"An error occurred while checking access: {str(e)}"

def main():
    """
    Main function to execute the eligibility check based on user input.
    """
    # Get user input
    user_location = input("Enter your location: ").strip()
    is_using_vpn_input = input("Are you using a VPN? (yes/no): ").strip().lower()

    # Validate VPN input
    if is_using_vpn_input not in ['yes', 'no']:
        print("Invalid input for VPN usage. Please enter 'yes' or 'no'.")
        return

    is_using_vpn = is_using_vpn_input == 'yes'

    # Create an instance of the access checker
    access_checker = SparkProtocolAccessChecker(user_location, is_using_vpn)

    # Check access eligibility and print the result
    result = access_checker.check_access()
    print(result)

if __name__ == "__main__":
    main()
```
