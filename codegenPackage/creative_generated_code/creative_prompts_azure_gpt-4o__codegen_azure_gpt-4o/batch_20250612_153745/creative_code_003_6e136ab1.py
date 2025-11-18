"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler-automation.com
Prompt: Provide a Python script to manage client-specific content automation tasks, incorporating localization features as emphasized by Euler Automation.
Generated: DETERMINISTIC_6e136ab183cec237
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

# Constants for supported locales
SUPPORTED_LOCALES = ["en_US", "fr_FR", "es_ES", "de_DE"]

class ContentAutomationManager:
    """
    Class to manage client-specific content automation tasks.
    Includes localization features as emphasized by Euler Automation.
    """

    def __init__(self, locale="en_US"):
        """
        Initializes the ContentAutomationManager with a specified locale.

        :param locale: Language locale for content (default is "en_US").
        """
        if locale not in SUPPORTED_LOCALES:
            raise ValueError(f"Unsupported locale '{locale}'. Supported locales: {SUPPORTED_LOCALES}")
        self.locale = locale
        self.content_directory = f"./content/{locale}"  # Directory for localized content
        self.ensure_content_directory()

    def ensure_content_directory(self):
        """
        Ensures the content directory for the specified locale exists.
        If not, it creates the directory.
        """
        if not os.path.exists(self.content_directory):
            os.makedirs(self.content_directory)

    def generate_content(self, client_id, content_data):
        """
        Generates client-specific content and saves it to a file.

        :param client_id: Unique identifier for the client.
        :param content_data: Dictionary containing the content data to be saved.
        :return: Path to the created content file.
        """
        try:
            content_file = os.path.join(self.content_directory, f"{client_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
            with open(content_file, "w", encoding="utf-8") as file:
                json.dump(content_data, file, ensure_ascii=False, indent=4)
            return content_file
        except Exception as e:
            raise RuntimeError(f"Failed to generate content for client '{client_id}': {e}")

    def fetch_localized_message(self, key):
        """
        Fetches a localized message based on the provided key.

        :param key: Key for the localized message.
        :return: The localized message string.
        """
        localized_messages_file = f"./localized_messages/{self.locale}.json"
        try:
            with open(localized_messages_file, "r", encoding="utf-8") as file:
                messages = json.load(file)
            return messages.get(key, f"[Missing translation for '{key}' in locale '{self.locale}']")
        except FileNotFoundError:
            raise FileNotFoundError(f"Localized messages file '{localized_messages_file}' not found.")
        except json.JSONDecodeError:
            raise RuntimeError(f"Error decoding localized messages file '{localized_messages_file}'.")

    def log_activity(self, client_id, activity):
        """
        Logs client-specific activity.

        :param client_id: Unique identifier for the client.
        :param activity: Description of the activity to log.
        """
        try:
            log_file = f"./logs/{client_id}_activity.log"
            if not os.path.exists("./logs"):
                os.makedirs("./logs")
            with open(log_file, "a", encoding="utf-8") as file:
                file.write(f"{datetime.now()} | {activity}\n")
        except Exception as e:
            raise RuntimeError(f"Failed to log activity for client '{client_id}': {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize content automation manager with locale
        manager = ContentAutomationManager(locale="en_US")

        # Generate content for a client
        client_id = "123ABC"
        content_data = {
            "title": "Welcome to Euler Automation",
            "description": "This is a client-specific localized content example.",
        }
        content_path = manager.generate_content(client_id, content_data)
        print(f"Content generated at: {content_path}")

        # Fetch a localized message
        localized_message = manager.fetch_localized_message("welcome_message")
        print(f"Localized Message: {localized_message}")

        # Log activity
        manager.log_activity(client_id, "Generated content and fetched localized message.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
