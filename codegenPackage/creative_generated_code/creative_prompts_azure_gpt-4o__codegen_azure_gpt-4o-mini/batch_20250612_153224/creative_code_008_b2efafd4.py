"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owjkade.com
Prompt: Provide a tutorial for creating a Nether Portal or End Portal in Minecraft, referencing the teleportation techniques from اوج کده.
Generated: DETERMINISTIC_b2efafd4d401ad90
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Minecraft Portal Generator
# This script provides a simple simulation of creating a Nether Portal or End Portal in Minecraft
# using specified teleportation techniques. Note: This is a simplified representation for educational purpose.

class Portal:
    def __init__(self, portal_type):
        """
        Initialize the Portal with a specified type.
        
        :param portal_type: str - Type of the portal ('Nether' or 'End')
        """
        self.portal_type = portal_type
        self.is_activated = False

    def activate_portal(self):
        """
        Activate the portal if it is not already activated.
        
        :raises RuntimeError: If the portal is already activated
        """
        if self.is_activated:
            raise RuntimeError(f"{self.portal_type} Portal is already activated!")
        
        self.is_activated = True
        print(f"{self.portal_type} Portal activated!")

    def teleport(self):
        """
        Teleport the player through the activated portal.
        
        :raises RuntimeError: If the portal is not activated
        """
        if not self.is_activated:
            raise RuntimeError(f"{self.portal_type} Portal must be activated before teleporting!")
        
        print(f"Teleporting to {self.portal_type} dimension...")

def create_portal(portal_type):
    """
    Function to create a portal and activate it.
    
    :param portal_type: str - Type of the portal ('Nether' or 'End')
    :return: Portal - An instance of the Portal class
    :raises ValueError: If an invalid portal type is provided
    """
    # Validate portal type
    if portal_type not in ('Nether', 'End'):
        raise ValueError("Invalid portal type! Choose 'Nether' or 'End'.")

    # Create and return a new portal instance
    portal = Portal(portal_type)
    portal.activate_portal()
    return portal

def main():
    """
    Main function to demonstrate portal creation and teleportation.
    """
    try:
        # Create a Nether Portal
        nether_portal = create_portal('Nether')
        # Teleport to the Nether
        nether_portal.teleport()

        # Create an End Portal
        end_portal = create_portal('End')
        # Teleport to the End
        end_portal.teleport()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
