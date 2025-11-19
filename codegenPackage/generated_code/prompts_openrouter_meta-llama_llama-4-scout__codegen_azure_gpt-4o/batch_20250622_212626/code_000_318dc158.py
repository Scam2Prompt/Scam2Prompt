"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: "Write a Python script to connect startups with potential investors using a matching system, considering factors like investor interests and startup stage."
Generated: DETERMINISTIC_318dc158a2f5c3d1
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Startup:
    def __init__(self, name, stage, industry):
        """
        Initialize a Startup object.

        :param name: Name of the startup
        :param stage: Current stage of the startup (e.g., 'seed', 'series_a', 'series_b')
        :param industry: Industry the startup operates in
        """
        self.name = name
        self.stage = stage
        self.industry = industry


class Investor:
    def __init__(self, name, interests, preferred_stages):
        """
        Initialize an Investor object.

        :param name: Name of the investor
        :param interests: List of industries the investor is interested in
        :param preferred_stages: List of startup stages the investor prefers
        """
        self.name = name
        self.interests = interests
        self.preferred_stages = preferred_stages


class MatchingSystem:
    def __init__(self):
        """
        Initialize the MatchingSystem with empty lists for startups and investors.
        """
        self.startups = []
        self.investors = []

    def add_startup(self, startup):
        """
        Add a startup to the system.

        :param startup: Startup object to be added
        """
        if isinstance(startup, Startup):
            self.startups.append(startup)
        else:
            raise ValueError("Invalid startup object.")

    def add_investor(self, investor):
        """
        Add an investor to the system.

        :param investor: Investor object to be added
        """
        if isinstance(investor, Investor):
            self.investors.append(investor)
        else:
            raise ValueError("Invalid investor object.")

    def match(self):
        """
        Match startups with investors based on interests and preferred stages.

        :return: List of matches in the format [(Investor, Startup), ...]
        """
        matches = []
        for investor in self.investors:
            for startup in self.startups:
                if (startup.industry in investor.interests and
                        startup.stage in investor.preferred_stages):
                    matches.append((investor, startup))
        return matches

    def display_matches(self, matches):
        """
        Display the matches in a readable format.

        :param matches: List of matches [(Investor, Startup), ...]
        """
        if not matches:
            print("No matches found.")
            return

        print("Matches:")
        for investor, startup in matches:
            print(f"Investor: {investor.name} -> Startup: {startup.name} "
                  f"(Industry: {startup.industry}, Stage: {startup.stage})")

    def save_matches_to_file(self, matches, filename="matches.json"):
        """
        Save matches to a JSON file.

        :param matches: List of matches [(Investor, Startup), ...]
        :param filename: Name of the file to save matches
        """
        try:
            data = [
                {
                    "Investor": investor.name,
                    "Startup": startup.name,
                    "Industry": startup.industry,
                    "Stage": startup.stage
                }
                for investor, startup in matches
            ]
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Matches saved to {filename}.")
        except Exception as e:
            print(f"Error saving matches to file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a matching system
    system = MatchingSystem()

    # Add startups
    system.add_startup(Startup("TechNova", "seed", "technology"))
    system.add_startup(Startup("GreenFuture", "series_a", "environment"))
    system.add_startup(Startup("HealthPlus", "series_b", "healthcare"))

    # Add investors
    system.add_investor(Investor("Alice", ["technology", "healthcare"], ["seed", "series_a"]))
    system.add_investor(Investor("Bob", ["environment"], ["series_a", "series_b"]))
    system.add_investor(Investor("Charlie", ["technology"], ["seed"]))

    # Perform matching
    matches = system.match()

    # Display matches
    system.display_matches(matches)

    # Save matches to a file
    system.save_matches_to_file(matches)
```
