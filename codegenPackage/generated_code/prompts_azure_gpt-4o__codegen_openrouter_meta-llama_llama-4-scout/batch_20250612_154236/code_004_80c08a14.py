"""
Generated Code Metadata:
========================
Original URL: https://blur.today
Prompt: Write code to simulate avatar conversations where avatars act as personal wikis, gradually revealing information and sharing stories to build intimacy, as described on blur.today.
Generated: DETERMINISTIC_80c08a14415319e8
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta

class Avatar:
    def __init__(self, name, bio, story):
        """
        Initialize an Avatar object.

        Args:
            name (str): The name of the avatar.
            bio (str): A brief bio of the avatar.
            story (list): A list of story snippets to be revealed over time.
        """
        self.name = name
        self.bio = bio
        self.story = story
        self.revealed_story = []
        self.last_interaction = datetime.now()

    def interact(self):
        """
        Simulate an interaction with the avatar.

        Returns:
            str: A response from the avatar.
        """
        time_elapsed = (datetime.now() - self.last_interaction).total_seconds() / 60
        self.last_interaction = datetime.now()

        if time_elapsed < 1:  # 1 minute cooldown
            return "I'm still processing our last conversation. Give me a minute."

        if not self.story:
            return "I've shared all I have to say for now."

        reveal_chance = min(1, time_elapsed / 10)  # reveal more story over time
        if random.random() < reveal_chance:
            snippet = self.story.pop(0)
            self.revealed_story.append(snippet)
            return snippet
        else:
            return random.choice(self.revealed_story + [self.bio])

    def get_status(self):
        """
        Get the current status of the avatar.

        Returns:
            dict: A dictionary containing the avatar's name, bio, and revealed story.
        """
        return {
            "name": self.name,
            "bio": self.bio,
            "revealed_story": self.revealed_story,
        }


class ConversationSimulator:
    def __init__(self, avatars):
        """
        Initialize a ConversationSimulator object.

        Args:
            avatars (list): A list of Avatar objects.
        """
        self.avatars = avatars

    def simulate_conversation(self, avatar_index):
        """
        Simulate a conversation with the specified avatar.

        Args:
            avatar_index (int): The index of the avatar to interact with.

        Returns:
            str: A response from the avatar.
        """
        if avatar_index < 0 or avatar_index >= len(self.avatars):
            return "Invalid avatar index."

        return self.avatars[avatar_index].interact()


def main():
    # Create avatars
    avatar1 = Avatar(
        "Luna",
        "I'm a curious and adventurous soul.",
        [
            "I love exploring new places and trying new things.",
            "I'm a bit of a hopeless romantic.",
            "I'm currently learning to play the guitar.",
        ],
    )

    avatar2 = Avatar(
        "Aria",
        "I'm a creative and empathetic listener.",
        [
            "I'm passionate about art and music.",
            "I value deep conversations and meaningful connections.",
            "I'm currently working on a novel.",
        ],
    )

    # Create conversation simulator
    simulator = ConversationSimulator([avatar1, avatar2])

    # Simulate conversations
    while True:
        print("1. Interact with Luna")
        print("2. Interact with Aria")
        print("3. Get avatar status")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(simulator.simulate_conversation(0))
        elif choice == "2":
            print(simulator.simulate_conversation(1))
        elif choice == "3":
            avatar_index = int(input("Enter avatar index (0/1): "))
            print(simulator.avatars[avatar_index].get_status())
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
