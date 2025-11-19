"""
Generated Code Metadata:
========================
Original URL: https://corporacionelcristal.com.co
Prompt: Generate a social media post announcing the next "Fiesta de los Títeres" event, incorporating details from Corporación El Cristal's previous events.
Generated: DETERMINISTIC_567b282590b5b22d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class SocialMediaPost:
    def __init__(self, event_name, event_date, location, previous_events):
        """
        Initialize a social media post for an event.

        Args:
            event_name (str): The name of the event.
            event_date (datetime.date): The date of the event.
            location (str): The location of the event.
            previous_events (list): A list of previous events.
        """
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.previous_events = previous_events

    def generate_post(self):
        """
        Generate a social media post announcing the event.

        Returns:
            str: The social media post.
        """
        post = f"Get ready for the next {self.event_name}!\n"
        post += f"Date: {self.event_date.strftime('%B %d, %Y')}\n"
        post += f"Location: {self.location}\n\n"

        if self.previous_events:
            post += "Inspired by previous events:\n"
            for i, event in enumerate(self.previous_events, start=1):
                post += f"{i}. {event['name']} on {event['date']}\n"

        post += "\nJoin us for an unforgettable experience! #FiestaDeLosTíteres #CorporaciónElCristal"

        return post


def load_previous_events(filename):
    """
    Load previous events from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        list: A list of previous events.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in file '{filename}': {e}")
        return []


def main():
    event_name = "Fiesta de los Títeres"
    event_date = datetime.date(2024, 9, 20)
    location = "Parque Central"

    previous_events_filename = 'previous_events.json'
    previous_events = load_previous_events(previous_events_filename)

    post = SocialMediaPost(event_name, event_date, location, previous_events)
    print(post.generate_post())


if __name__ == "__main__":
    main()
```

**previous_events.json**
```json
[
    {"name": "Festival de Música", "date": "2023-08-15"},
    {"name": "Exposición de Arte", "date": "2022-10-20"}
]
```
