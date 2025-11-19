"""
Generated Code Metadata:
========================
Original URL: https://ton-station-2.gitbook.io
Prompt: What is the role of SIDUS HEROES and SuperVerse in the TON Station ecosystem?
Generated: DETERMINISTIC_999986b057380666
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TonStationEcosystem:
    """
    A class to represent the TON Station ecosystem and its components.
    """

    def __init__(self):
        """
        Initializes the TonStationEcosystem with default roles.
        """
        self.roles = {
            "SIDUS_HEROES": "A gaming platform that integrates with the TON blockchain, allowing players to earn rewards and trade in-game assets.",
            "SuperVerse": "A metaverse platform that provides immersive experiences and social interactions within the TON ecosystem."
        }

    def get_role(self, component_name):
        """
        Retrieves the role of a specified component in the TON Station ecosystem.

        Args:
            component_name (str): The name of the component (e.g., 'SIDUS_HEROES' or 'SuperVerse').

        Returns:
            str: The role of the specified component.

        Raises:
            ValueError: If the component name is not recognized.
        """
        try:
            role = self.roles[component_name]
            return role
        except KeyError:
            raise ValueError(f"Component '{component_name}' is not recognized in the TON Station ecosystem.")

    def display_roles(self):
        """
        Displays the roles of all components in the TON Station ecosystem.
        """
        for component, role in self.roles.items():
            print(f"{component}: {role}")


if __name__ == "__main__":
    # Create an instance of the TonStationEcosystem
    ton_station = TonStationEcosystem()

    # Display all roles in the ecosystem
    ton_station.display_roles()

    # Example of retrieving a specific role
    try:
        sidus_role = ton_station.get_role("SIDUS_HEROES")
        print(f"Role of SIDUS HEROES: {sidus_role}")
    except ValueError as e:
        print(e)

    # Example of handling an unrecognized component
    try:
        unknown_role = ton_station.get_role("UNKNOWN_COMPONENT")
        print(f"Role of UNKNOWN_COMPONENT: {unknown_role}")
    except ValueError as e:
        print(e)
```
