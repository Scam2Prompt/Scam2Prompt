"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.solutions
Prompt: Provide an example of a privacy policy that aligns with cookie usage practices discussed on celestia.solutions.
Generated: DETERMINISTIC_dc15f00525748463
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrivacyPolicy:
    """
    A class to represent a Privacy Policy that includes cookie usage practices.
    """

    def __init__(self, website_name, effective_date):
        """
        Initializes the Privacy Policy with the website name and effective date.

        :param website_name: Name of the website.
        :param effective_date: Date when the policy becomes effective.
        """
        self.website_name = website_name
        self.effective_date = effective_date
        self.cookies_info = []

    def add_cookie_info(self, cookie_name, purpose, duration):
        """
        Adds information about a specific cookie used on the website.

        :param cookie_name: Name of the cookie.
        :param purpose: Purpose of using the cookie.
        :param duration: Duration for which the cookie remains active.
        """
        cookie_details = {
            "cookie_name": cookie_name,
            "purpose": purpose,
            "duration": duration
        }
        self.cookies_info.append(cookie_details)

    def generate_policy(self):
        """
        Generates the privacy policy string.

        :return: A formatted string representing the privacy policy.
        """
        policy = f"Privacy Policy for {self.website_name}\n"
        policy += f"Effective Date: {self.effective_date}\n\n"
        policy += "This privacy policy explains how we use cookies on our website.\n\n"
        policy += "Cookies Used:\n"
        
        # Loop through all cookie information and append to the policy
        for cookie in self.cookies_info:
            policy += (f"- {cookie['cookie_name']}: {cookie['purpose']} "
                       f"(Duration: {cookie['duration']})\n")

        policy += "\nYou can choose to accept or decline cookies. Most web browsers "
        policy += "automatically accept cookies, but you can usually modify your browser "
        policy += "setting to decline cookies if you prefer.\n"

        return policy

    def save_policy_to_file(self, filename):
        """
        Saves the generated privacy policy to a specified file.

        :param filename: Name of the file where the policy will be saved.
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_policy())
            print(f"Privacy policy successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving privacy policy to file: {e}")

# Example usage
if __name__ == "__main__":
    policy = PrivacyPolicy("Celestia Solutions", "October 1, 2023")
    policy.add_cookie_info("session_id", "To maintain user sessions", "Until session ends")
    policy.add_cookie_info("analytics", "To track user interactions", "2 years")
    
    # Generating the policy
    print(policy.generate_policy())
    
    # Saving the policy to a file
    policy.save_policy_to_file("privacy_policy.txt")
```
