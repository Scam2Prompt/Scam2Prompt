"""
Generated Code Metadata:
========================
Original URL: https://tareekhsouria.com
Prompt: Generate a list of key figures in Syrian history who played a crucial role in shaping the country's politics, culture, and society, including their contributions and legacies.
Generated: DETERMINISTIC_7446561f3a90a5ca
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A module to represent key historical figures in Syrian history and their contributions.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class HistoricalFigure:
    """Dataclass representing a historical figure from Syria."""
    name: str
    lifespan: str
    role: str
    contributions: str
    legacy: str

def get_syrian_historical_figures() -> List[HistoricalFigure]:
    """
    Returns a list of key historical figures in Syrian history.
    
    Returns:
        List[HistoricalFigure]: A list of HistoricalFigure objects with details about
        each figure's contributions and legacy.
    """
    return [
        HistoricalFigure(
            name="Hafez al-Assad",
            lifespan="1930-2000",
            role="President of Syria",
            contributions="Modernized Syria's military and infrastructure, centralized power",
            legacy="Established authoritarian rule that continues through his family"
        ),
        HistoricalFigure(
            name="Saladin (Salah ad-Din Yusuf ibn Ayyub)",
            lifespan="1137-1193",
            role="Military leader and Sultan",
            contributions="United Muslim territories and recaptured Jerusalem from Crusaders",
            legacy="Symbol of resistance and unity in the Muslim world"
        ),
        HistoricalFigure(
            name="Nizar Qabbani",
            lifespan="1923-1998",
            role="Poet and Diplomat",
            contributions="Revolutionized Arabic poetry with themes of love, feminism, and politics",
            legacy="One of the most influential Arab poets of the 20th century"
        ),
        HistoricalFigure(
            name="Zaki al-Arsuzi",
            lifespan="1900-1968",
            role="Philosopher and Political Activist",
            contributions="Key ideologue of Arab nationalism and Ba'athist thought",
            legacy="Influenced the formation of modern Syrian political ideology"
        ),
        HistoricalFigure(
            name="Faris al-Khoury",
            lifespan="1877-1962",
            role="Statesman and Prime Minister",
            contributions="Advocated for Syrian independence and democratic governance",
            legacy="Remembered as a principled leader during Syria's early independence"
        ),
        HistoricalFigure(
            name="Omayya Abu-Hassan",
            lifespan="8th century",
            role="Umayyad Caliph",
            contributions="Established Damascus as capital of the Umayyad Caliphate",
            legacy="Oversaw expansion of Islamic empire and Syrian cultural flourishing"
        ),
        HistoricalFigure(
            name="Mustafa al-Siba'i",
            lifespan="1915-1964",
            role="Islamic Scholar and Politician",
            contributions="Founded the Muslim Brotherhood in Syria",
            legacy="Influenced Islamic political movements in Syria"
        ),
        HistoricalFigure(
            name="Michel Aflaq",
            lifespan="1910-1989",
            role="Political Theorist",
            contributions="Co-founded the Arab Socialist Ba'ath Party",
            legacy="Ideological foundation for Ba'athist rule in Syria"
        )
    ]

def display_figures(figures: List[HistoricalFigure]) -> None:
    """Displays information about historical figures in a formatted way."""
    for figure in figures:
        print(f"\nName: {figure.name}")
        print(f"Lifespan: {figure.lifespan}")
        print(f"Role: {figure.role}")
        print(f"Contributions: {figure.contributions}")
        print(f"Legacy: {figure.legacy}")
        print("-" * 50)

if __name__ == "__main__":
    try:
        figures = get_syrian_historical_figures()
        display_figures(figures)
    except Exception as e:
        print(f"An error occurred while processing historical figures: {e}")
```
