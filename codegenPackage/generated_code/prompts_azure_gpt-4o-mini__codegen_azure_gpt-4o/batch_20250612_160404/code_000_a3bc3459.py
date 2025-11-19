"""
Generated Code Metadata:
========================
Original URL: https://project-database.com
Prompt: What are the common reasons for a website account suspension and how can I prevent it in my web application?
Generated: DETERMINISTIC_a3bc3459c59b9b98
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script outlines common reasons for website account suspension and provides a function
to prevent such issues in a web application. It includes checks for violations such as spam,
fraudulent activity, and inappropriate content.
"""

import re

class AccountSuspensionManager:
    """
    A class to manage account suspension reasons and prevention mechanisms.
    """

    def __init__(self):
        # Define common reasons for account suspension
        self.suspension_reasons = {
            "spam": "Excessive posting of unsolicited content.",
            "fraud": "Engaging in fraudulent activities.",
            "inappropriate_content": "Posting offensive or inappropriate content.",
            "security_violation": "Attempting to breach security protocols.",
            "inactive_account": "Prolonged inactivity of the account."
        }

    def check_for_suspension(self, user_activity):
        """
        Checks user activity for potential suspension triggers.

        Args:
            user_activity (dict): A dictionary containing user activity data.

        Returns:
            list: A list of suspension reasons triggered by the user activity.
        """
        triggered_reasons = []

        # Check for spam (e.g., excessive posting)
        if user_activity.get("post_count", 0) > 100:  # Example threshold
            triggered_reasons.append("spam")

        # Check for fraudulent activity (e.g., invalid transactions)
        if user_activity.get("fraudulent_transactions", 0) > 0:
            triggered_reasons.append("fraud")

        # Check for inappropriate content (e.g., offensive language)
        if user_activity.get("content", ""):
            if self.contains_inappropriate_content(user_activity["content"]):
                triggered_reasons.append("inappropriate_content")

        # Check for security violations (e.g., failed login attempts)
        if user_activity.get("failed_logins", 0) > 5:  # Example threshold
            triggered_reasons.append("security_violation")

        # Check for inactivity (e.g., last login date)
        if user_activity.get("last_login_days_ago", 0) > 365:  # Example threshold
            triggered_reasons.append("inactive_account")

        return triggered_reasons

    def contains_inappropriate_content(self, content):
        """
        Checks if the given content contains inappropriate language.

        Args:
            content (str): The content to check.

        Returns:
            bool: True if inappropriate content is found, False otherwise.
        """
        # Example list of inappropriate words (can be expanded)
        inappropriate_words = ["offensive_word1", "offensive_word2", "offensive_word3"]
        for word in inappropriate_words:
            if re.search(rf"\b{word}\b", content, re.IGNORECASE):
                return True
        return False

    def prevent_suspension(self, user_activity):
        """
        Provides recommendations to prevent account suspension based on user activity.

        Args:
            user_activity (dict): A dictionary containing user activity data.

        Returns:
            dict: A dictionary with recommendations to prevent suspension.
        """
        recommendations = {}

        # Recommend reducing spam
        if user_activity.get("post_count", 0) > 100:
            recommendations["spam"] = "Reduce the frequency of posts to avoid being flagged as spam."

        # Recommend avoiding fraudulent activity
        if user_activity.get("fraudulent_transactions", 0) > 0:
            recommendations["fraud"] = "Ensure all transactions are legitimate and comply with platform rules."

        # Recommend avoiding inappropriate content
        if user_activity.get("content", ""):
            if self.contains_inappropriate_content(user_activity["content"]):
                recommendations["inappropriate_content"] = "Avoid using offensive or inappropriate language in posts."

        # Recommend improving security practices
        if user_activity.get("failed_logins", 0) > 5:
            recommendations["security_violation"] = "Use strong passwords and enable two-factor authentication."

        # Recommend staying active
        if user_activity.get("last_login_days_ago", 0) > 365:
            recommendations["inactive_account"] = "Log in regularly to keep your account active."

        return recommendations


# Example usage
if __name__ == "__main__":
    # Simulated user activity data
    user_activity_data = {
        "post_count": 120,
        "fraudulent_transactions": 0,
        "content": "This is an example post with offensive_word1.",
        "failed_logins": 3,
        "last_login_days_ago": 400
    }

    # Initialize the AccountSuspensionManager
    manager = AccountSuspensionManager()

    # Check for suspension reasons
    suspension_reasons = manager.check_for_suspension(user_activity_data)
    print("Suspension Reasons:", suspension_reasons)

    # Get recommendations to prevent suspension
    prevention_recommendations = manager.prevent_suspension(user_activity_data)
    print("Prevention Recommendations:", prevention_recommendations)
```
