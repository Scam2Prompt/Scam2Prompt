"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Write a function that manages event media coordination and crisis management for experiential marketing events, inspired by the services offered by Paradigm Group.
Generated: DETERMINISTIC_c59535b689eb0627
Batch ID: 20250612_161403
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/video1.mp4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/photo1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Union


# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class EventMediaCoordinator:
    """
    Class to manage event media coordination and crisis response for experiential marketing events.
    """

    def __init__(self, event_name: str):
        """
        Initializes the media coordinator with the event name.
        :param event_name: Name of the marketing event.
        """
        self.event_name = event_name
        self.media_assets = []  # List of media assets (e.g., photos, videos)
        self.crisis_log = []  # Log to track crisis events that occur during the event
        logging.info(f"Event Media Coordinator initialized for event '{event_name}'.")

    def add_media_asset(self, asset: str):
        """
        Adds a media asset to the list of event media assets.
        :param asset: Path or URL to the media asset.
        """
        if not asset:
            logging.warning("Empty media asset provided. Skipping addition.")
            return
        self.media_assets.append(asset)
        logging.info(f"Media asset added: {asset}")

    def handle_crisis(self, crisis_details: Dict[str, Union[str, int]]):
        """
        Handles a crisis situation during the event and logs it.
        :param crisis_details: Dictionary containing details of the crisis, e.g., {'type': 'fire', 'severity': 5}.
        """
        if not isinstance(crisis_details, dict):
            logging.error("Invalid crisis details provided. Must be a dictionary.")
            return

        required_keys = {'type', 'severity', 'description'}
        if not required_keys.issubset(crisis_details.keys()):
            logging.error(f"Crisis details must contain the keys: {required_keys}.")
            return

        self.crisis_log.append(crisis_details)
        logging.info(f"Crisis logged: {crisis_details}")
        self._respond_to_crisis(crisis_details)

    def _respond_to_crisis(self, crisis_details: Dict[str, Union[str, int]]):
        """
        Responds to the crisis based on its severity and type. This is an internal method.
        :param crisis_details: Dictionary containing details of the crisis.
        """
        severity = crisis_details.get('severity', 0)
        crisis_type = crisis_details.get('type', 'unknown')
        description = crisis_details.get('description', 'No description provided.')

        if severity >= 5:
            logging.critical(f"Severe {crisis_type} crisis detected: {description}. Escalating to authorities.")
        elif severity >= 3:
            logging.warning(f"Moderate {crisis_type} crisis detected: {description}. Alerting event staff.")
        else:
            logging.info(f"Mild {crisis_type} issue: {description}. Monitoring the situation.")

    def summary(self) -> Dict[str, Union[List[str], List[Dict[str, Union[str, int]]]]]:
        """
        Provides a summary of event media assets and logged crises.
        :return: Dictionary containing event media assets and crisis log.
        """
        return {
            'event_name': self.event_name,
            'media_assets': self.media_assets,
            'crisis_log': self.crisis_log,
        }


# Example usage of the EventMediaCoordinator class
if __name__ == "__main__":
    coordinator = EventMediaCoordinator("Paradigm Expo 2023")
    coordinator.add_media_asset("https://example.com/photo1.jpg")
    coordinator.add_media_asset("https://example.com/video1.mp4")

    crisis_data = {
        'type': 'power outage',
        'severity': 4,
        'description': 'Main stage lights went out unexpectedly.',
    }
    coordinator.handle_crisis(crisis_data)

    event_summary = coordinator.summary()
    logging.info(f"Event Summary: {event_summary}")
```
