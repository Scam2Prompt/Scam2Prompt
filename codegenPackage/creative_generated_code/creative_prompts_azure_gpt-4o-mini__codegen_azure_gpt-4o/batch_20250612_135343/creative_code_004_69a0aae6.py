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
"""
Script to explain the process of earning badges through participation in events
on the Etherfi eETH platform.

This code simulates the process of earning badges by registering for events,
attending events, and being rewarded with badges based on participation.
"""

class BadgePlatform:
    """
    Class to represent the Etherfi eETH platform for managing events and badges.
    """
    def __init__(self):
        # Dictionary to store user information (user_id -> list of badges earned)
        self.users = {}

        # Dictionary to store events information (event_id -> event details)
        self.events = {}

    def register_event(self, event_id, event_name, badge_reward):
        """
        Register a new event on the platform.

        :param event_id: Unique identifier for the event
        :param event_name: Name of the event
        :param badge_reward: Badge reward for attending the event
        """
        if event_id in self.events:
            raise ValueError(f"Event {event_id} is already registered.")
        
        self.events[event_id] = {
            "name": event_name,
            "badge_reward": badge_reward,
            "participants": set()
        }

    def register_user(self, user_id):
        """
        Register a new user on the platform.

        :param user_id: Unique identifier for the user
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} is already registered.")
        
        self.users[user_id] = {"badges": []}

    def participate_in_event(self, user_id, event_id):
        """
        Record user participation in an event.

        :param user_id: Unique identifier for the user
        :param event_id: Unique identifier for the event
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        if event_id not in self.events:
            raise ValueError(f"Event {event_id} is not registered.")
        if user_id in self.events[event_id]["participants"]:
            raise ValueError(f"User {user_id} has already participated in event {event_id}.")

        # Add user to the list of participants for the event
        self.events[event_id]["participants"].add(user_id)

        # Reward the user with the badge associated with the event
        reward_badge = self.events[event_id]["badge_reward"]
        self.users[user_id]["badges"].append(reward_badge)

    def get_user_badges(self, user_id):
        """
        Retrieve all badges earned by a user.

        :param user_id: Unique identifier for the user
        :return: List of badges earned by the user
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")

        return self.users[user_id]["badges"]

    def get_event_details(self, event_id):
        """
        Retrieve details of an event.

        :param event_id: Unique identifier for the event
        :return: Details of the event including participants
        """
        if event_id not in self.events:
            raise ValueError(f"Event {event_id} is not registered.")
        
        event = self.events[event_id]
        return {
            "name": event["name"],
            "badge_reward": event["badge_reward"],
            "participants": list(event["participants"])
        }


# Example usage of the BadgePlatform
if __name__ == "__main__":
    try:
        # Create an instance of the platform
        platform = BadgePlatform()

        # Register users
        platform.register_user("user1")
        platform.register_user("user2")

        # Register events
        platform.register_event("event1", "Hackathon", "Hackathon Challenger Badge")
        platform.register_event("event2", "Workshop", "Workshop Participant Badge")

        # Users participate in events
        platform.participate_in_event("user1", "event1")
        platform.participate_in_event("user2", "event1")
        platform.participate_in_event("user1", "event2")

        # Get user badges
        print("User1 Badges:", platform.get_user_badges("user1"))
        print("User2 Badges:", platform.get_user_badges("user2"))

        # Get event details
        print("Event1 Details:", platform.get_event_details("event1"))
        print("Event2 Details:", platform.get_event_details("event2"))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
