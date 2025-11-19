"""
Generated Code Metadata:
========================
Original URL: https://usdcprinter.xyz
Prompt: Design a basic roadmap for a cryptocurrency project like $UPRINT, including phases for launch, community building, and exchange listings.
Generated: DETERMINISTIC_706b678afb699afc
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roadmap.py

class RoadmapPhase:
    """Represents a phase in the cryptocurrency project roadmap."""

    def __init__(self, name, description, start_date, end_date):
        """
        Initializes a RoadmapPhase.

        Args:
            name (str): Phase name.
            description (str): Phase description.
            start_date (str): Phase start date (YYYY-MM-DD).
            end_date (str): Phase end date (YYYY-MM-DD).
        """
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date}): {self.description}"


class CryptoRoadmap:
    """Represents a cryptocurrency project roadmap."""

    def __init__(self):
        self.phases = []

    def add_phase(self, phase):
        """
        Adds a phase to the roadmap.

        Args:
            phase (RoadmapPhase): Phase to add.
        """
        self.phases.append(phase)

    def __str__(self):
        roadmap_str = "Roadmap:\n"
        for i, phase in enumerate(self.phases, 1):
            roadmap_str += f"{i}. {phase}\n"
        return roadmap_str


def main():
    try:
        # Create roadmap
        roadmap = CryptoRoadmap()

        # Phase 1: Launch
        launch_phase = RoadmapPhase(
            "Launch",
            "Token creation, website launch, and initial community building.",
            "2024-09-01",
            "2024-09-30"
        )
        roadmap.add_phase(launch_phase)

        # Phase 2: Community Building
        community_phase = RoadmapPhase(
            "Community Building",
            "Social media campaigns, AMA sessions, and community engagement.",
            "2024-10-01",
            "2024-11-30"
        )
        roadmap.add_phase(community_phase)

        # Phase 3: Exchange Listings
        exchange_phase = RoadmapPhase(
            "Exchange Listings",
            "Listing on major cryptocurrency exchanges.",
            "2024-12-01",
            "2025-01-31"
        )
        roadmap.add_phase(exchange_phase)

        # Print roadmap
        print(roadmap)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
