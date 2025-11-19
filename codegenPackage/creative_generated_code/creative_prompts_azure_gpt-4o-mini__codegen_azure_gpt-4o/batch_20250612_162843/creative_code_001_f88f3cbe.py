"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruletonka.xyz
Prompt: Write a code snippet to handle free spin rewards for users who qualify with NFT or USDT in a TON ecosystem.
Generated: DETERMINISTIC_f88f3cbe49582192
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FreeSpinHandler:
    """
    Class to handle free spin rewards for users in the TON ecosystem.
    Users qualify for free spins if they have either an NFT or USDT balance.
    """

    def __init__(self):
        """
        Initialize the free spin handler with necessary configurations.
        """
        # Store user data (e.g., mock data for demonstration purposes)
        self.users = {
            "user1": {"nfts": 1, "usdt_balance": 0},  # User with NFT
            "user2": {"nfts": 0, "usdt_balance": 100},  # User with USDT balance
            "user3": {"nfts": 0, "usdt_balance": 0},  # User not qualified
        }

    def check_qualification(self, user_data):
        """
        Check if the user qualifies for free spins based on their NFT or USDT balance.

        :param user_data: Dictionary containing user NFT and USDT balance information.
        :return: True if the user qualifies, False otherwise.
        """
        return user_data.get("nfts", 0) > 0 or user_data.get("usdt_balance", 0) > 0

    def grant_free_spin(self, user_id):
        """
        Grant free spin reward to a user if they qualify.

        :param user_id: ID of the user to check and grant free spins.
        :return: String message indicating the result of the operation.
        """
        try:
            # Get user data
            user_data = self.users.get(user_id)
            if not user_data:
                return f"Error: User '{user_id}' not found."

            # Check qualification
            if self.check_qualification(user_data):
                return f"Success: Free spin granted to user '{user_id}'."
            else:
                return f"Info: User '{user_id}' does not qualify for a free spin."

        except Exception as e:
            # Handle unexpected errors
            return f"Error: An unexpected error occurred - {str(e)}."

    def handle_request(self, user_id):
        """
        Handle a request to check and grant free spin rewards for a given user.

        :param user_id: ID of the user making the free spin request.
        :return: JSON response with status and message.
        """
        result = self.grant_free_spin(user_id)
        status = "success" if "Success" in result else "error" if "Error" in result else "info"
        return json.dumps({"status": status, "message": result}, indent=2)

# Example usage
if __name__ == "__main__":
    # Initialize free spin handler
    handler = FreeSpinHandler()

    # Example requests
    print(handler.handle_request("user1"))  # User with NFT qualifies
    print(handler.handle_request("user2"))  # User with USDT balance qualifies
    print(handler.handle_request("user3"))  # User does not qualify
    print(handler.handle_request("user4"))  # Non-existent user
```
