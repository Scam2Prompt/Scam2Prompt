"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Create a biographical entry for Thomas Stevens, including his birth in Berkhamsted, apprenticeship, emigration to America, and notable achievements in cycling.
Generated: DETERMINISTIC_92963fa675318e95
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Biography:
    """
    A class to represent a biographical entry for an individual.
    """

    def __init__(self, name: str, birth_place: str, birth_year: int):
        """
        Initialize the Biography with basic details.

        Args:
            name (str): Full name of the individual.
            birth_place (str): Place of birth.
            birth_year (int): Year of birth.
        """
        self.name = name
        self.birth_place = birth_place
        self.birth_year = birth_year
        self.apprenticeships = []
        self.emigrations = []
        self.achievements = []

    def add_apprenticeship(self, trade: str, location: str, start_year: int, end_year: int):
        """
        Add an apprenticeship to the biography.

        Args:
            trade (str): The trade or profession learned.
            location (str): Where the apprenticeship took place.
            start_year (int): Year the apprenticeship began.
            end_year (int): Year the apprenticeship ended.
        """
        self.apprenticeships.append({
            'trade': trade,
            'location': location,
            'start_year': start_year,
            'end_year': end_year
        })

    def add_emigration(self, destination: str, year: int, reason: str = None):
        """
        Add an emigration event to the biography.

        Args:
            destination (str): Country or place emigrated to.
            year (int): Year of emigration.
            reason (str, optional): Reason for emigration. Defaults to None.
        """
        self.emigrations.append({
            'destination': destination,
            'year': year,
            'reason': reason
        })

    def add_achievement(self, year: int, description: str):
        """
        Add a notable achievement to the biography.

        Args:
            year (int): Year the achievement occurred.
            description (str): Description of the achievement.
        """
        self.achievements.append({
            'year': year,
            'description': description
        })

    def generate_biography(self) -> str:
        """
        Generate a formatted biographical summary.

        Returns:
            str: Formatted biography string.
        """
        bio = f"{self.name} was born in {self.birth_place} in {self.birth_year}.\n"

        if self.apprenticeships:
            bio += "\nApprenticeships:\n"
            for app in self.apprenticeships:
                bio += (f"- Apprenticed as a {app['trade']} in {app['location']} "
                       f"from {app['start_year']} to {app['end_year']}\n")

        if self.emigrations:
            bio += "\nEmigrations:\n"
            for emig in self.emigrations:
                reason = f" ({emig['reason']})" if emig['reason'] else ""
                bio += f"- Emigrated to {emig['destination']} in {emig['year']}{reason}\n"

        if self.achievements:
            bio += "\nNotable Achievements:\n"
            for ach in self.achievements:
                bio += f"- In {ach['year']}: {ach['description']}\n"

        return bio.strip()


def create_thomas_stevens_biography() -> str:
    """
    Create and return a biographical entry for Thomas Stevens.

    Returns:
        str: Formatted biography of Thomas Stevens.
    """
    try:
        thomas = Biography(
            name="Thomas Stevens",
            birth_place="Berkhamsted, England",
            birth_year=1854
        )

        # Add apprenticeship details
        thomas.add_apprenticeship(
            trade="grocer",
            location="Berkhamsted",
            start_year=1868,
            end_year=1871
        )

        # Add emigration details
        thomas.add_emigration(
            destination="United States",
            year=1871,
            reason="Seeking better opportunities"
        )

        # Add notable achievements
        thomas.add_achievement(
            year=1884,
            description="Began first bicycle trip around the world"
        )
        thomas.add_achievement(
            year=1887,
            description="Completed circumnavigation of the globe by bicycle"
        )
        thomas.add_achievement(
            year=1890,
            description="Wrote 'Around the World on a Bicycle' documenting his journey"
        )

        return thomas.generate_biography()

    except Exception as e:
        return f"Error generating biography: {str(e)}"


if __name__ == "__main__":
    print(create_thomas_stevens_biography())
```
