"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-thruster.pages.dev
Prompt: Implement a check in code to exclude participants from restricted countries (e.g., Bolivia, Iran, North Korea) when joining an IDO on TrustPad.
Generated: DETERMINISTIC_440a282540bda325
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class IDOParticipant:
    """
    Represents a participant trying to join an IDO (Initial DEX Offering).
    """

    RESTRICTED_COUNTRIES = {"Bolivia", "Iran", "North Korea"}

    def __init__(self, name: str, country: str):
        """
        Initializes a new IDOParticipant.

        :param name: The name of the participant.
        :param country: The country of the participant.
        """
        self.name = name
        self.country = country

    def can_join_ido(self) -> bool:
        """
        Checks if the participant is allowed to join the IDO.

        :return: True if the participant can join, False otherwise.
        """
        if self.country in self.RESTRICTED_COUNTRIES:
            return False
        return True


def main():
    """
    Main function to demonstrate the IDO registration process.
    """
    participants = [
        IDOParticipant("Alice", "USA"),
        IDOParticipant("Bob", "Bolivia"),
        IDOParticipant("Charlie", "Iran"),
        IDOParticipant("David", "Canada"),
        IDOParticipant("Eve", "North Korea"),
    ]

    for participant in participants:
        try:
            if participant.can_join_ido():
                print(f"{participant.name} from {participant.country} can join the IDO.")
            else:
                print(f"{participant.name} from {participant.country} is excluded from joining the IDO.")
        except Exception as e:
            print(f"Error processing participant {participant.name}: {e}")


if __name__ == "__main__":
    main()
```
