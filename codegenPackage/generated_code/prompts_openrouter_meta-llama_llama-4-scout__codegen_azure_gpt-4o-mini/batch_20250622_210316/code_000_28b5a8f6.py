"""
Generated Code Metadata:
========================
Original URL: https://gradkosarke.org
Prompt: What is the purpose of the Grad Košarke association and how does it support KK Zadar, the basketball club in Zadar, Croatia?
Generated: DETERMINISTIC_28b5a8f6d8c150c6
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GradKosarke:
    """
    A class to represent the Grad Košarke association and its support for KK Zadar.
    """

    def __init__(self, name, location):
        """
        Initializes the Grad Košarke association with a name and location.

        :param name: Name of the association
        :param location: Location of the association
        """
        self.name = name
        self.location = location
        self.supported_clubs = []

    def add_supported_club(self, club_name):
        """
        Adds a basketball club to the list of supported clubs.

        :param club_name: Name of the basketball club to support
        """
        if club_name not in self.supported_clubs:
            self.supported_clubs.append(club_name)
        else:
            raise ValueError(f"{club_name} is already supported.")

    def get_supported_clubs(self):
        """
        Returns a list of supported basketball clubs.

        :return: List of supported clubs
        """
        return self.supported_clubs

    def provide_support(self, club_name, support_type):
        """
        Provides support to a specific basketball club.

        :param club_name: Name of the basketball club
        :param support_type: Type of support (e.g., financial, logistical)
        :raises ValueError: If the club is not supported
        """
        if club_name not in self.supported_clubs:
            raise ValueError(f"{club_name} is not supported by {self.name}.")
        
        # Simulate providing support
        print(f"Providing {support_type} to {club_name}.")

# Example usage
if __name__ == "__main__":
    try:
        grad_kosarke = GradKosarke("Grad Košarke", "Zadar, Croatia")
        grad_kosarke.add_supported_club("KK Zadar")
        grad_kosarke.provide_support("KK Zadar", "financial support")
        
        # Display supported clubs
        print("Supported clubs:", grad_kosarke.get_supported_clubs())
    except Exception as e:
        print(f"An error occurred: {e}")
```
