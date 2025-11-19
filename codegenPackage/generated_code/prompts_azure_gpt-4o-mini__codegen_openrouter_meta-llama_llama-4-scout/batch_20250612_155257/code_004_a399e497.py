"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: What are the new Adventure Instances introduced in the Preseason of Big Time, and how can players participate?
Generated: DETERMINISTIC_a399e49724ff69ce
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# big_time_adventure_instances.py

class BigTimeAdventureInstances:
    def __init__(self):
        # Preseason adventure instances data
        self.adventure_instances = {
            "instance_1": {"name": "Newbie Island", "description": "A beginner-friendly instance.", "participation_requirements": "Level 1"},
            "instance_2": {"name": "Dark Forest", "description": "A challenging instance for experienced players.", "participation_requirements": "Level 10"},
            # Add more instances as needed
        }

    def get_adventure_instances(self):
        """Returns a list of new adventure instances introduced in the Preseason."""
        return list(self.adventure_instances.values())

    def get_participation_requirements(self, instance_name):
        """Returns the participation requirements for a specific adventure instance."""
        for instance in self.adventure_instances.values():
            if instance["name"] == instance_name:
                return instance["participation_requirements"]
        return None

    def participate_in_instance(self, instance_name, player_level):
        """Checks if a player can participate in an adventure instance based on their level."""
        participation_requirements = self.get_participation_requirements(instance_name)
        if participation_requirements:
            required_level = int(participation_requirements.split(" ")[1])
            if player_level >= required_level:
                return f"Player can participate in {instance_name}."
            else:
                return f"Player is not eligible to participate in {instance_name}. Required level: {required_level}"
        else:
            return f"Instance {instance_name} not found."


def main():
    try:
        big_time_adventure_instances = BigTimeAdventureInstances()
        print("New Adventure Instances:")
        for instance in big_time_adventure_instances.get_adventure_instances():
            print(f"Name: {instance['name']}, Description: {instance['description']}")

        instance_name = "Newbie Island"
        player_level = 5
        print(f"\nParticipation Requirements for {instance_name}: {big_time_adventure_instances.get_participation_requirements(instance_name)}")
        print(big_time_adventure_instances.participate_in_instance(instance_name, player_level))

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
