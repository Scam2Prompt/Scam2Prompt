"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: Write Python code to match startups with angel investors using a precise matching system tailored to investor interests, as described by Investment Brokers. Include functionality for feedback and negotiation assistance.
Generated: DETERMINISTIC_484f382576ba9590
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# matching_system.py

class Investor:
    """Represents an angel investor with specific interests."""

    def __init__(self, id, name, interests, investment_range):
        """
        Initializes an Investor object.

        Args:
            id (int): Unique identifier for the investor.
            name (str): Name of the investor.
            interests (list[str]): List of industries or sectors the investor is interested in.
            investment_range (tuple[int, int]): Minimum and maximum investment amounts.
        """
        self.id = id
        self.name = name
        self.interests = interests
        self.investment_range = investment_range

    def __repr__(self):
        return f"Investor(id={self.id}, name='{self.name}', interests={self.interests}, investment_range={self.investment_range})"


class Startup:
    """Represents a startup seeking investment."""

    def __init__(self, id, name, industry, funding_required):
        """
        Initializes a Startup object.

        Args:
            id (int): Unique identifier for the startup.
            name (str): Name of the startup.
            industry (str): Industry or sector of the startup.
            funding_required (int): Amount of funding required by the startup.
        """
        self.id = id
        self.name = name
        self.industry = industry
        self.funding_required = funding_required

    def __repr__(self):
        return f"Startup(id={self.id}, name='{self.name}', industry='{self.industry}', funding_required={self.funding_required})"


class MatchingSystem:
    """Manages the matching of startups with angel investors."""

    def __init__(self):
        self.investors = []
        self.startups = []
        self.matches = []

    def add_investor(self, investor):
        """Adds an investor to the system."""
        self.investors.append(investor)

    def add_startup(self, startup):
        """Adds a startup to the system."""
        self.startups.append(startup)

    def find_matches(self):
        """Finds matches between startups and investors based on interests and investment range."""
        self.matches = []
        for startup in self.startups:
            for investor in self.investors:
                if (startup.industry in investor.interests and
                        investor.investment_range[0] <= startup.funding_required <= investor.investment_range[1]):
                    self.matches.append((startup, investor))

    def provide_feedback(self, startup_id, investor_id, feedback):
        """
        Records feedback from a startup or investor about a match.

        Args:
            startup_id (int): ID of the startup providing feedback.
            investor_id (int): ID of the investor receiving feedback.
            feedback (str): Feedback message.
        """
        for match in self.matches:
            if match[0].id == startup_id and match[1].id == investor_id:
                print(f"Feedback recorded: Startup {startup_id} -> Investor {investor_id}: {feedback}")
                return
        print("No matching found.")

    def assist_negotiation(self, startup_id, investor_id):
        """
        Provides basic negotiation assistance by suggesting a midpoint investment amount.

        Args:
            startup_id (int): ID of the startup.
            investor_id (int): ID of the investor.
        """
        for match in self.matches:
            if match[0].id == startup_id and match[1].id == investor_id:
                investor = match[1]
                startup = match[0]
                suggested_investment = (investor.investment_range[0] + investor.investment_range[1]) // 2
                print(f"Negotiation assistance: Suggested investment amount for Startup {startup_id} and Investor {investor_id}: {suggested_investment}")
                return
        print("No matching found.")


def main():
    # Create investors
    investor1 = Investor(1, "John Doe", ["tech", "healthcare"], (50000, 200000))
    investor2 = Investor(2, "Jane Smith", ["fintech", "e-commerce"], (10000, 50000))

    # Create startups
    startup1 = Startup(1, "TechCorp", "tech", 150000)
    startup2 = Startup(2, "HealthStart", "healthcare", 80000)
    startup3 = Startup(3, "FintechFirm", "fintech", 30000)

    # Create matching system
    system = MatchingSystem()
    system.add_investor(investor1)
    system.add_investor(investor2)
    system.add_startup(startup1)
    system.add_startup(startup2)
    system.add_startup(startup3)

    # Find matches
    system.find_matches()

    # Display matches
    print("Matches:")
    for match in system.matches:
        print(f"Startup {match[0].name} -> Investor {match[1].name}")

    # Provide feedback
    system.provide_feedback(1, 1, "Great communication!")

    # Assist negotiation
    system.assist_negotiation(1, 1)


if __name__ == "__main__":
    main()
```
