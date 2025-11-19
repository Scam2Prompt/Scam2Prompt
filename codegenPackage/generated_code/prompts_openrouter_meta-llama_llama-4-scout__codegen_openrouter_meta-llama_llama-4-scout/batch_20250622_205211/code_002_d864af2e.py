"""
Generated Code Metadata:
========================
Original URL: https://www.predaiaarteenatura.eu
Prompt: Generate a JSON file that catalogues the art exhibitions held at the Predaia Arte e Natura project, including the artist names, exhibition titles, and years.
Generated: DETERMINISTIC_d864af2e03329e36
Batch ID: 20250622_205211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List

@dataclass
class Exhibition:
    """Represents an art exhibition."""
    artist_name: str
    exhibition_title: str
    year: int

class ExhibitionCatalogue:
    """Catalogues art exhibitions held at the Predaia Arte e Natura project."""

    def __init__(self):
        self.exhibitions = []

    def add_exhibition(self, exhibition: Exhibition):
        """Adds an exhibition to the catalogue."""
        self.exhibitions.append(exhibition)

    def to_json(self, filename: str):
        """Generates a JSON file representing the exhibition catalogue."""
        data = [
            {
                "artist_name": exhibition.artist_name,
                "exhibition_title": exhibition.exhibition_title,
                "year": exhibition.year
            } for exhibition in self.exhibitions
        ]

        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error writing to file: {e}")

def main():
    catalogue = ExhibitionCatalogue()

    # Example exhibitions
    exhibitions: List[Exhibition] = [
        Exhibition("Artist 1", "Exhibition 1", 2020),
        Exhibition("Artist 2", "Exhibition 2", 2021),
        Exhibition("Artist 3", "Exhibition 3", 2022),
    ]

    for exhibition in exhibitions:
        catalogue.add_exhibition(exhibition)

    filename = "exhibition_catalogue.json"
    catalogue.to_json(filename)
    print(f"Exhibition catalogue saved to {filename}")

if __name__ == "__main__":
    main()
```
