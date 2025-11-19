"""
Generated Code Metadata:
========================
Original URL: https://opensea.org.cn
Prompt: Create a step-by-step guide for verifying an OpenSea account and resolving common verification issues, as outlined in the site's troubleshooting section.
Generated: DETERMINISTIC_a97280cb9ca99be1
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# verification_guide.py

class OpenSeaVerificationGuide:
    def __init__(self):
        self.steps = [
            self.connect_wallet,
            self.verify_email,
            self.add_social_profiles,
            self.apply_for_verification
        ]

    def connect_wallet(self):
        """
        Connects user's wallet to OpenSea.

        Raises:
            Exception: If wallet connection fails.
        """
        try:
            # Simulating wallet connection (replace with actual implementation)
            print("Connecting wallet...")
            # wallet.connect()
            print("Wallet connected successfully.")
        except Exception as e:
            print(f"Error connecting wallet: {str(e)}")
            raise

    def verify_email(self):
        """
        Verifies user's email address.

        Raises:
            Exception: If email verification fails.
        """
        try:
            # Simulating email verification (replace with actual implementation)
            print("Verifying email...")
            # email.verify()
            print("Email verified successfully.")
        except Exception as e:
            print(f"Error verifying email: {str(e)}")
            raise

    def add_social_profiles(self):
        """
        Adds user's social profiles.

        Raises:
            Exception: If social profile addition fails.
        """
        try:
            # Simulating social profile addition (replace with actual implementation)
            print("Adding social profiles...")
            # social_profiles.add()
            print("Social profiles added successfully.")
        except Exception as e:
            print(f"Error adding social profiles: {str(e)}")
            raise

    def apply_for_verification(self):
        """
        Applies for OpenSea account verification.

        Raises:
            Exception: If verification application fails.
        """
        try:
            # Simulating verification application (replace with actual implementation)
            print("Applying for verification...")
            # verification.apply()
            print("Verification application submitted successfully.")
        except Exception as e:
            print(f"Error applying for verification: {str(e)}")
            raise

    def troubleshoot_verification_issues(self, issue):
        """
        Troubleshoots common verification issues.

        Args:
            issue (str): The verification issue.

        Returns:
            str: The solution to the issue.
        """
        solutions = {
            "wallet_connection": "Check wallet connection and try again.",
            "email_verification": "Check email for verification link and try again.",
            "social_profile_addition": "Check social profile information and try again.",
            "verification_application": "Check verification application and try again."
        }

        return solutions.get(issue, "Unknown issue. Please contact support.")

def main():
    guide = OpenSeaVerificationGuide()

    print("Step-by-Step Verification Guide:")
    for i, step in enumerate(guide.steps):
        print(f"\nStep {i+1}:")
        step()

    print("\nTroubleshooting Common Verification Issues:")
    issue = input("Enter the issue (wallet_connection, email_verification, social_profile_addition, verification_application): ")
    solution = guide.troubleshoot_verification_issues(issue)
    print(solution)

if __name__ == "__main__":
    main()
```
