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
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class ConferenceFormat(Enum):
    """Enum representing different conference formats."""
    DYNAMIC_PANEL = auto()
    IMMERSIVE_WORKSHOP = auto()
    VIRTUAL_CONFERENCE = auto()

@dataclass
class ConferenceFeature:
    """Represents a feature of a conference format."""
    name: str
    description: str

@dataclass
class ConferenceFormatDetails:
    """Represents details of a conference format."""
    format_type: ConferenceFormat
    features: List[ConferenceFeature]
    duration_hours: int
    max_participants: Optional[int] = None
    is_virtual: bool = False

class ConferenceComparator:
    """Compares and contrasts different conference formats."""
    
    def __init__(self):
        self.formats = {
            ConferenceFormat.DYNAMIC_PANEL: ConferenceFormatDetails(
                format_type=ConferenceFormat.DYNAMIC_PANEL,
                features=[
                    ConferenceFeature(
                        name="Expert Panels",
                        description="Interactive discussions with industry experts"
                    ),
                    ConferenceFeature(
                        name="Audience Q&A",
                        description="Real-time audience participation"
                    )
                ],
                duration_hours=2,
                max_participants=500
            ),
            ConferenceFormat.IMMERSIVE_WORKSHOP: ConferenceFormatDetails(
                format_type=ConferenceFormat.IMMERSIVE_WORKSHOP,
                features=[
                    ConferenceFeature(
                        name="Hands-on Activities",
                        description="Practical, skill-building exercises"
                    ),
                    ConferenceFeature(
                        name="Small Group Collaboration",
                        description="Deep dives into topics with peers"
                    )
                ],
                duration_hours=4,
                max_participants=50
            ),
            ConferenceFormat.VIRTUAL_CONFERENCE: ConferenceFormatDetails(
                format_type=ConferenceFormat.VIRTUAL_CONFERENCE,
                features=[
                    ConferenceFeature(
                        name="Global Accessibility",
                        description="Accessible from anywhere with internet"
                    ),
                    ConferenceFeature(
                        name="On-Demand Content",
                        description="Recorded sessions available post-event"
                    )
                ],
                duration_hours=8,
                is_virtual=True
            )
        }

    def compare_formats(self) -> List[ConferenceFormatDetails]:
        """Returns a list of all conference formats with their details."""
        return list(self.formats.values())

    def get_format_details(self, format_type: ConferenceFormat) -> ConferenceFormatDetails:
        """Returns details for a specific conference format.
        
        Args:
            format_type: The conference format to get details for.
            
        Returns:
            ConferenceFormatDetails for the specified format.
            
        Raises:
            ValueError: If the format type is not recognized.
        """
        if format_type not in self.formats:
            raise ValueError(f"Unknown conference format: {format_type}")
        return self.formats[format_type]

    def compare_features(self) -> dict:
        """Compares features across all conference formats.
        
        Returns:
            A dictionary mapping each feature to the formats that offer it.
        """
        feature_map = {}
        for format_type, details in self.formats.items():
            for feature in details.features:
                if feature.name not in feature_map:
                    feature_map[feature.name] = []
                feature_map[feature.name].append(format_type)
        return feature_map

# Example usage
if __name__ == "__main__":
    comparator = ConferenceComparator()
    
    # Get all formats
    all_formats = comparator.compare_formats()
    print("All conference formats:")
    for fmt in all_formats:
        print(f"- {fmt.format_type.name}")
    
    # Compare features
    feature_comparison = comparator.compare_features()
    print("\nFeature comparison:")
    for feature, formats in feature_comparison.items():
        format_names = [f.name for f in formats]
        print(f"{feature}: Available in {', '.join(format_names)}")
```
