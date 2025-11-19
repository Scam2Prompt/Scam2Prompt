"""
Generated Code Metadata:
========================
Original URL: https://conferencesglobal.org
Prompt: Compare and contrast the conference formats offered by Conferences Global, including dynamic panel discussions, immersive workshops, and virtual conferences.
Generated: DETERMINISTIC_ce575e7d6748615b
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# conference_formats.py

from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class ConferenceFormatType(str, Enum):
    """Enum for conference format types."""
    DYNAMIC_PANEL_DISCUSSION = "dynamic_panel_discussion"
    IMMERSIVE_WORKSHOP = "immersive_workshop"
    VIRTUAL_CONFERENCE = "virtual_conference"

class ConferenceFormat(ABC):
    """Abstract base class for conference formats."""

    def __init__(self, name: str, description: str, format_type: ConferenceFormatType):
        """
        Initialize a conference format.

        Args:
        - name (str): The name of the conference format.
        - description (str): A brief description of the conference format.
        - format_type (ConferenceFormatType): The type of the conference format.
        """
        self.name = name
        self.description = description
        self.format_type = format_type

    @abstractmethod
    def get_details(self) -> str:
        """Get details about the conference format."""
        pass

class DynamicPanelDiscussion(ConferenceFormat):
    """Class for dynamic panel discussions."""

    def __init__(self, name: str, description: str, panelists: List[str]):
        """
        Initialize a dynamic panel discussion.

        Args:
        - name (str): The name of the dynamic panel discussion.
        - description (str): A brief description of the dynamic panel discussion.
        - panelists (List[str]): A list of panelists participating in the discussion.
        """
        super().__init__(name, description, ConferenceFormatType.DYNAMIC_PANEL_DISCUSSION)
        self.panelists = panelists

    def get_details(self) -> str:
        """Get details about the dynamic panel discussion."""
        return f"{self.name}: A dynamic panel discussion with {', '.join(self.panelists)}"

class ImmersiveWorkshop(ConferenceFormat):
    """Class for immersive workshops."""

    def __init__(self, name: str, description: str, facilitator: str, duration: str):
        """
        Initialize an immersive workshop.

        Args:
        - name (str): The name of the immersive workshop.
        - description (str): A brief description of the immersive workshop.
        - facilitator (str): The facilitator of the workshop.
        - duration (str): The duration of the workshop.
        """
        super().__init__(name, description, ConferenceFormatType.IMMERSIVE_WORKSHOP)
        self.facilitator = facilitator
        self.duration = duration

    def get_details(self) -> str:
        """Get details about the immersive workshop."""
        return f"{self.name}: An immersive workshop led by {self.facilitator}, lasting {self.duration}"

class VirtualConference(ConferenceFormat):
    """Class for virtual conferences."""

    def __init__(self, name: str, description: str, date: str, time: str):
        """
        Initialize a virtual conference.

        Args:
        - name (str): The name of the virtual conference.
        - description (str): A brief description of the virtual conference.
        - date (str): The date of the virtual conference.
        - time (str): The time of the virtual conference.
        """
        super().__init__(name, description, ConferenceFormatType.VIRTUAL_CONFERENCE)
        self.date = date
        self.time = time

    def get_details(self) -> str:
        """Get details about the virtual conference."""
        return f"{self.name}: A virtual conference on {self.date} at {self.time}"

def compare_conference_formats(formats: List[ConferenceFormat]) -> None:
    """
    Compare and contrast conference formats.

    Args:
    - formats (List[ConferenceFormat]): A list of conference formats to compare.
    """
    for format in formats:
        print(f"Format Type: {format.format_type.value}")
        print(f"Name: {format.name}")
        print(f"Description: {format.description}")
        print(f"Details: {format.get_details()}")
        print("------------------------")

def main() -> None:
    try:
        # Create conference formats
        dynamic_panel_discussion = DynamicPanelDiscussion(
            "Future of Tech",
            "A discussion on the future of technology",
            ["John Doe", "Jane Smith", "Bob Johnson"]
        )

        immersive_workshop = ImmersiveWorkshop(
            "Design Thinking",
            "A hands-on workshop on design thinking",
            "Alice Brown",
            "2 hours"
        )

        virtual_conference = VirtualConference(
            "Global Summit",
            "A virtual conference for global leaders",
            "2024-03-15",
            "10:00 AM EST"
        )

        # Compare conference formats
        compare_conference_formats([dynamic_panel_discussion, immersive_workshop, virtual_conference])

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
