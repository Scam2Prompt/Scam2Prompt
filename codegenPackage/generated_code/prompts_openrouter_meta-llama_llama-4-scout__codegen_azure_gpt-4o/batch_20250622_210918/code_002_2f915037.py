"""
Generated Code Metadata:
========================
Original URL: https://octaviaone.pages.dev
Prompt: Generate a code example for a community moderation AI tool that provides 24/7 oversight and security, similar to Octavia's features.
Generated: DETERMINISTIC_2f91503718d8e332
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime
from typing import List, Dict

class CommunityModerationAI:
    """
    A community moderation AI tool that provides 24/7 oversight and security.
    Features include:
    - Detecting inappropriate language
    - Flagging suspicious activity
    - Logging moderation actions
    """

    def __init__(self):
        # List of banned words/phrases for moderation
        self.banned_words = ["badword1", "badword2", "offensivephrase"]
        # Log to store moderation actions
        self.moderation_log = []

    def detect_inappropriate_language(self, message: str) -> bool:
        """
        Detects if a message contains banned words or phrases.

        :param message: The message to analyze.
        :return: True if inappropriate language is detected, False otherwise.
        """
        for word in self.banned_words:
            if re.search(rf"\b{word}\b", message, re.IGNORECASE):
                return True
        return False

    def flag_suspicious_activity(self, user_activity: Dict) -> bool:
        """
        Flags suspicious activity based on predefined rules.

        :param user_activity: A dictionary containing user activity data.
                              Example: {"messages_sent": 100, "time_online": 5}
        :return: True if suspicious activity is detected, False otherwise.
        """
        # Example rule: If a user sends more than 50 messages in an hour, flag them
        if user_activity.get("messages_sent", 0) > 50:
            return True
        return False

    def log_action(self, action: str, details: Dict):
        """
        Logs moderation actions for auditing purposes.

        :param action: The action taken (e.g., "Flagged", "Muted").
        :param details: Additional details about the action.
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details
        }
        self.moderation_log.append(log_entry)

    def moderate_message(self, user_id: str, message: str):
        """
        Moderates a single message and takes appropriate action.

        :param user_id: The ID of the user who sent the message.
        :param message: The message to moderate.
        """
        if self.detect_inappropriate_language(message):
            self.log_action("Flagged", {"user_id": user_id, "message": message})
            print(f"Message flagged for inappropriate language: {message}")

    def monitor_user_activity(self, user_id: str, user_activity: Dict):
        """
        Monitors user activity and takes appropriate action if suspicious activity is detected.

        :param user_id: The ID of the user to monitor.
        :param user_activity: A dictionary containing user activity data.
        """
        if self.flag_suspicious_activity(user_activity):
            self.log_action("Suspicious Activity", {"user_id": user_id, "activity": user_activity})
            print(f"Suspicious activity detected for user {user_id}: {user_activity}")

    def get_moderation_log(self) -> List[Dict]:
        """
        Retrieves the moderation log.

        :return: A list of logged moderation actions.
        """
        return self.moderation_log


# Example usage
if __name__ == "__main__":
    moderation_tool = CommunityModerationAI()

    # Simulate a user sending a message
    moderation_tool.moderate_message(user_id="user123", message="This is a badword1 example.")

    # Simulate monitoring user activity
    user_activity_data = {"messages_sent": 60, "time_online": 2}
    moderation_tool.monitor_user_activity(user_id="user123", user_activity=user_activity_data)

    # Retrieve and print the moderation log
    log = moderation_tool.get_moderation_log()
    print("Moderation Log:", log)
```
