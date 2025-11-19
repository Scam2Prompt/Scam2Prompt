"""
Generated Code Metadata:
========================
Original URL: https://bankless.pages.dev
Prompt: Explain the differences between the three redemption phases for $BASED tokens and how the token allocation varies depending on the phase.
Generated: DETERMINISTIC_ce65deada9478b40
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Token Redemption Phases
class BasedTokenRedemption:
    def __init__(self):
        # Define token allocation for each phase
        self.phases = {
            "phase_1": {"name": "Early Redemption", "allocation": 0.3},
            "phase_2": {"name": "Standard Redemption", "allocation": 0.4},
            "phase_3": {"name": "Late Redemption", "allocation": 0.3},
        }

    def get_phase_details(self, phase):
        """
        Retrieves details for a specific redemption phase.

        Args:
            phase (str): The phase to retrieve details for (phase_1, phase_2, phase_3).

        Returns:
            dict: Details for the specified phase.

        Raises:
            ValueError: If the phase is not recognized.
        """
        try:
            return self.phases[phase]
        except KeyError:
            raise ValueError("Invalid phase. Please choose from: {}".format(list(self.phases.keys())))

    def compare_token_allocation(self):
        """
        Compares token allocation across all redemption phases.

        Returns:
            dict: A dictionary summarizing token allocation for each phase.
        """
        allocation_summary = {}
        for phase, details in self.phases.items():
            allocation_summary[phase] = details["allocation"]
        return allocation_summary

    def calculate_token_distribution(self, total_tokens):
        """
        Calculates token distribution for each redemption phase.

        Args:
            total_tokens (int): The total number of $BASED tokens.

        Returns:
            dict: A dictionary with token distribution for each phase.

        Raises:
            ValueError: If total_tokens is not a positive number.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be a positive number.")

        token_distribution = {}
        for phase, details in self.phases.items():
            tokens_in_phase = total_tokens * details["allocation"]
            token_distribution[phase] = tokens_in_phase
        return token_distribution


def main():
    redemption = BasedTokenRedemption()

    # Get details for a specific phase
    print(redemption.get_phase_details("phase_1"))

    # Compare token allocation across phases
    print(redemption.compare_token_allocation())

    # Calculate token distribution for 1 million tokens
    total_tokens = 1_000_000
    print(redemption.calculate_token_distribution(total_tokens))


if __name__ == "__main__":
    main()
```
