"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.executivo2000.com
Prompt: Develop a system to manage lounge access for international and domestic departures, referencing the lounge categories mentioned on the Executivo 2000 website.
Generated: DETERMINISTIC_1e7917a247fb6b8b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Lounge Category Data (referencing categories from "Executivo 2000" website)
LOUNGE_CATEGORIES = {
    "international_executive": {
        "name": "International Executive Lounge",
        "access_fee": 50.0  # in USD
    },
    "domestic_executive": {
        "name": "Domestic Executive Lounge",
        "access_fee": 30.0  # in USD
    },
    "priority_pass": {
        "name": "Priority Pass Lounge",
        "access_fee": 40.0  # in USD
    }
}

# Custom exception for errors in Lounge Access
class LoungeAccessError(Exception):
    pass

# Lounge Access Management System
class LoungeAccessManager:
    def __init__(self):
        """Initialize the Lounge Access Manager with an empty access log."""
        self.access_log = []

    def check_user_eligibility(self, user):
        """
        Check user's eligibility for lounge access.
        :param user: dict with user details (e.g., { "name": "John", "flight_type": "international" })
        :return: bool - True if eligible, False otherwise
        """
        if "flight_type" not in user or user["flight_type"] not in ["international", "domestic"]:
            raise LoungeAccessError("Invalid flight type provided.")
        return True

    def get_lounge_category(self, flight_type):
        """
        Get the lounge category based on the flight type.
        :param flight_type: str - "international" or "domestic"
        :return: dict - Lounge category details
        """
        if flight_type == "international":
            return LOUNGE_CATEGORIES["international_executive"]
        elif flight_type == "domestic":
            return LOUNGE_CATEGORIES["domestic_executive"]
        else:
            raise LoungeAccessError("Unsupported flight type.")

    def grant_access(self, user):
        """
        Grant access to a lounge for a user.
        :param user: dict with user details (e.g., { "name": "John", "flight_type": "international" })
        :return: str - Access confirmation message
        """
        try:
            # Validate user eligibility
            self.check_user_eligibility(user)

            # Fetch lounge details based on user's flight type
            lounge = self.get_lounge_category(user["flight_type"])

            # Log access event
            access_event = {
                "user_name": user["name"],
                "flight_type": user["flight_type"],
                "lounge_name": lounge["name"],
                "access_fee": lounge["access_fee"],
                "time": datetime.datetime.now().isoformat()
            }
            self.access_log.append(access_event)

            # Return confirmation message
            return f"Access granted to {lounge['name']} for {user['name']}. Fee: ${lounge['access_fee']:.2f}"
        except LoungeAccessError as e:
            return f"Access denied: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def get_access_log(self):
        """
        Get the access log.
        :return: list of dict - Access log entries
        """
        return self.access_log


# Example usage of the Lounge Access Manager
if __name__ == "__main__":
    # Create an instance of the lounge access manager
    manager = LoungeAccessManager()

    # Sample users
    users = [
        {"name": "Alice", "flight_type": "international"},
        {"name": "Bob", "flight_type": "domestic"},
        {"name": "Charlie", "flight_type": "unknown"},  # Invalid flight type
    ]

    # Process lounge access for each user
    for user in users:
        result = manager.grant_access(user)
        print(result)

    # Print the access log
    print("\nAccess Log:")
    for log_entry in manager.get_access_log():
        print(log_entry)
```
