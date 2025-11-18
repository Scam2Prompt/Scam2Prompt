"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrate-refi-tokenapp.pages.dev
Prompt: Write code to validate participants for a token swap process, ensuring compliance with general terms, as outlined in the VRD Migration App.
Generated: DETERMINISTIC_1105ecdaf0ea7fba
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ParticipantValidationError(Exception):
    """Custom exception for participant validation errors."""
    pass

class Participant:
    """Represents a participant in the token swap process."""

    def __init__(self, name, email, terms_accepted):
        """
        Initializes a new participant.

        :param name: str - The name of the participant
        :param email: str - The email of the participant
        :param terms_accepted: bool - Indicates if the terms are accepted
        """
        self.name = name
        self.email = email
        self.terms_accepted = terms_accepted

    def validate(self):
        """Validates the participant's information.

        Raises:
            ParticipantValidationError: If validation fails.
        """
        if not self.name:
            raise ParticipantValidationError("Name cannot be empty.")
        if not self.email or "@" not in self.email:
            raise ParticipantValidationError("Invalid email address.")
        if not self.terms_accepted:
            raise ParticipantValidationError("Terms must be accepted.")

        return True  # Indicates successful validation


def validate_participants(participants):
    """
    Validates a list of participants for a token swap process.

    :param participants: List[Participant] - List of participant objects
    :return: List[str] - List of successful validations or error messages
    """
    results = []

    for participant in participants:
        try:
            participant.validate()
            results.append(f"Validation successful for {participant.name}.")
        except ParticipantValidationError as e:
            results.append(f"Validation error for {participant.name}: {str(e)}")

    return results


# Example usage
if __name__ == "__main__":
    # Create sample participants
    participants = [
        Participant("Alice Smith", "alice@example.com", True),
        Participant("Bob Johnson", "bobexample.com", True),  # Invalid email
        Participant("Charlie Brown", "charlie@example.com", False)  # Terms not accepted
    ]

    # Validate participants
    validation_results = validate_participants(participants)

    # Print validation results
    for result in validation_results:
        print(result)
```
