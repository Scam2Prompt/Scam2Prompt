"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Write code to simulate the construction of tennis courts with security features and top-tier materials, inspired by C&M Pinnacle's Goldfields Tennis Court project.
Generated: DETERMINISTIC_5235d25427f7aba2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TennisCourt:
    """
    Class to represent a Tennis Court with security features and top-tier materials.
    """

    def __init__(self, surface_type, lighting, security_features):
        """
        Initializes the TennisCourt object.

        :param surface_type: Type of surface (e.g., clay, grass, hard).
        :param lighting: Type of lighting (e.g., LED, Halogen).
        :param security_features: List of security features (e.g., fencing, cameras).
        """
        self.surface_type = surface_type
        self.lighting = lighting
        self.security_features = security_features

    def __str__(self):
        """
        Returns a string representation of the Tennis Court details.
        """
        return (f"Tennis Court with {self.surface_type} surface, "
                f"{self.lighting} lighting, "
                f"Security features: {', '.join(self.security_features)}")

    def add_security_feature(self, feature):
        """
        Adds a security feature to the court.

        :param feature: Security feature to add.
        """
        if feature not in self.security_features:
            self.security_features.append(feature)
        else:
            raise ValueError(f"Feature '{feature}' already exists.")

    def remove_security_feature(self, feature):
        """
        Removes a security feature from the court.

        :param feature: Security feature to remove.
        """
        try:
            self.security_features.remove(feature)
        except ValueError:
            raise ValueError(f"Feature '{feature}' not found.")


class TennisCourtConstruction:
    """
    Class to simulate the construction of tennis courts.
    """

    def __init__(self):
        """
        Initializes an empty list to hold constructed tennis courts.
        """
        self.courts = []

    def construct_court(self, surface_type, lighting, security_features):
        """
        Constructs a new Tennis Court.

        :param surface_type: Type of surface for the court.
        :param lighting: Type of lighting to be installed.
        :param security_features: List of security features to include.
        :return: The constructed Tennis Court object.
        """
        try:
            court = TennisCourt(surface_type, lighting, security_features)
            self.courts.append(court)
            return court
        except Exception as e:
            raise RuntimeError("An error occurred while constructing the court.") from e

    def list_courts(self):
        """
        Lists all constructed tennis courts.

        :return: List of string representations of all courts.
        """
        return [str(court) for court in self.courts]


# Example usage:
if __name__ == "__main__":
    construction_firm = TennisCourtConstruction()

    # Construct a new tennis court
    try:
        court1 = construction_firm.construct_court(
            surface_type='Hard',
            lighting='LED',
            security_features=['Fencing', 'Surveillance Cameras']
        )
        
        print(court1)

        # Add a new security feature
        court1.add_security_feature('Alarm System')
        
        # List all constructed courts
        for court_info in construction_firm.list_courts():
            print(court_info)

    except Exception as e:
        print(f"Error: {e}")
```
