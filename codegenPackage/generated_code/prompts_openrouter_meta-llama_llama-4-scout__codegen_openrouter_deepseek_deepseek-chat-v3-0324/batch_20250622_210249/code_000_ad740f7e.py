"""
Generated Code Metadata:
========================
Original URL: https://steth-award.net
Prompt: What are the different types of Xbox consoles available, and how can I choose the right one for my gaming needs?
Generated: DETERMINISTIC_ad740f7e6d11f33e
Batch ID: 20250622_210249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from dataclasses import dataclass
from typing import List, Optional

class XboxConsoleType(enum.Enum):
    """Enum representing different Xbox console types."""
    XBOX = "Original Xbox"
    XBOX_360 = "Xbox 360"
    XBOX_ONE = "Xbox One"
    XBOX_ONE_S = "Xbox One S"
    XBOX_ONE_X = "Xbox One X"
    XBOX_SERIES_S = "Xbox Series S"
    XBOX_SERIES_X = "Xbox Series X"

@dataclass
class XboxConsole:
    """Dataclass representing an Xbox console with its specifications."""
    console_type: XboxConsoleType
    release_year: int
    resolution: str
    storage_options: List[str]
    backward_compatibility: bool
    price_range: str
    best_for: str

def get_all_xbox_consoles() -> List[XboxConsole]:
    """Returns a list of all Xbox consoles with their specifications."""
    return [
        XboxConsole(
            console_type=XboxConsoleType.XBOX,
            release_year=2001,
            resolution="480p",
            storage_options=["8-10GB HDD"],
            backward_compatibility=False,
            price_range="Discontinued",
            best_for="Classic gaming, collectors"
        ),
        XboxConsole(
            console_type=XboxConsoleType.XBOX_360,
            release_year=2005,
            resolution="720p/1080i",
            storage_options=["20GB", "60GB", "120GB", "250GB", "500GB HDD"],
            backward_compatibility=True,
            price_range="Discontinued",
            best_for="Budget gaming, Xbox 360 titles"
        ),
        XboxConsole(
            console_type=XboxConsoleType.XBOX_ONE,
            release_year=2013,
            resolution="1080p",
            storage_options=["500GB", "1TB HDD"],
            backward_compatibility=True,
            price_range="$200-$300",
            best_for="Casual gaming, multimedia"
        ),
        XboxConsole(
            console_type=XboxConsoleType.XBOX_ONE_S,
            release_year=2016,
            resolution="4K upscaling",
            storage_options=["500GB", "1TB", "2TB HDD"],
            backward_compatibility=True,
            price_range="$250-$350",
            best_for="4K media, casual gaming"
        ),
        XboxConsole(
            console_type=XboxConsoleType.XBOX_ONE_X,
            release_year=2017,
            resolution="Native 4K",
            storage_options=["1TB HDD"],
            backward_compatibility=True,
            price_range="$400-$500",
            best_for="High-performance gaming"
        ),
        XboxConsole(
            console_type=XboxConsoleType.XBOX_SERIES_S,
            release_year=2020,
            resolution="1440p (4K upscaling)",
            storage_options=["512GB SSD"],
            backward_compatibility=True,
            price_range="$299",
            best_for="Budget next-gen gaming"
        ),
        XboxConsole(
            console_type=XboxConsoleType.XBOX_SERIES_X,
            release_year=2020,
            resolution="Native 4K",
            storage_options=["1TB SSD"],
            backward_compatibility=True,
            price_range="$499",
            best_for="Premium next-gen gaming"
        )
    ]

def recommend_console(
    budget: Optional[str] = None,
    resolution: Optional[str] = None,
    backward_compat: Optional[bool] = None,
    best_for: Optional[str] = None
) -> List[XboxConsole]:
    """
    Recommends Xbox consoles based on user preferences.
    
    Args:
        budget: Price range filter
        resolution: Desired resolution
        backward_compat: Backward compatibility requirement
        best_for: Intended use case
        
    Returns:
        List of matching XboxConsole objects
    """
    consoles = get_all_xbox_consoles()
    recommendations = []
    
    for console in consoles:
        match = True
        
        if budget and console.price_range != budget:
            match = False
        if resolution and resolution.lower() not in console.resolution.lower():
            match = False
        if backward_compat is not None and console.backward_compatibility != backward_compat:
            match = False
        if best_for and best_for.lower() not in console.best_for.lower():
            match = False
            
        if match:
            recommendations.append(console)
            
    return recommendations

# Example usage
if __name__ == "__main__":
    print("Available Xbox Consoles:")
    for console in get_all_xbox_consoles():
        print(f"- {console.console_type.value} ({console.release_year})")
    
    print("\nRecommendations for 4K gaming:")
    recommendations = recommend_console(resolution="4K")
    for console in recommendations:
        print(f"- {console.console_type.value}: {console.best_for} (Price: {console.price_range})")
```
