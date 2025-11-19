"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fi-dapp-owmargzh9-etherfi.vercel.app
Prompt: Explain the process of earning badges through participation in events on the etherfi eETH platform.
Generated: DETERMINISTIC_69a0aae6034d7f66
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Badge:
    """Class representing a badge earned through event participation."""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.earned = False

    def earn_badge(self):
        """Mark the badge as earned."""
        self.earned = True
        print(f"Badge '{self.name}' earned!")

class Event:
    """Class representing an event on the etherfi eETH platform."""
    
    def __init__(self, title, date, participants_limit):
        self.title = title
        self.date = date
        self.participants_limit = participants_limit
        self.participants = []

    def add_participant(self, user):
        """Add a user to the event participants list if there's space."""
        if len(self.participants) < self.participants_limit:
            self.participants.append(user)
            print(f"{user} has been added to the event '{self.title}'.")
        else:
            print(f"Event '{self.title}' is full. Cannot add {user}.")

class User:
    """Class representing a user on the etherfi eETH platform."""
    
    def __init__(self, username):
        self.username = username
        self.badges = []

    def participate_in_event(self, event):
        """Participate in the specified event, earning a badge if successful."""
        try:
            event.add_participant(self.username)
            badge = Badge(name=event.title, description=f"Participation in {event.title}")
            badge.earn_badge()
            self.badges.append(badge)
        except Exception as e:
            print(f"Error participating in event: {e}")

def main():
    """Main function to demonstrate event participation and badge earning."""
    # Create an event
    event = Event(title="eETH Summit 2023", date="2023-11-01", participants_limit=2)

    # Create users
    user1 = User(username="Alice")
    user2 = User(username="Bob")
    user3 = User(username="Charlie")

    # Users participate in the event
    user1.participate_in_event(event)
    user2.participate_in_event(event)
    user3.participate_in_event(event)  # This should trigger the full event message

if __name__ == "__main__":
    main()
```
