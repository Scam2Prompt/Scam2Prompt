"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-redstone.com
Prompt: What are the special roles in the RedStone Expedition, and how do they impact participation in the airdrop?
Generated: DETERMINISTIC_0baf56aa75cc6944
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RedStoneExpedition:
    """
    Class to represent the RedStone Expedition and its special roles.
    """

    def __init__(self):
        # Initialize a dictionary to hold the roles and their impacts on airdrop participation
        self.roles = {
            "Explorer": {
                "description": "Explorers are responsible for mapping out uncharted territories.",
                "airdrop_impact": "High - They have a greater chance of receiving airdrops due to their exploratory nature."
            },
            "Guardian": {
                "description": "Guardians protect the expedition from external threats.",
                "airdrop_impact": "Medium - They receive a moderate chance of airdrops for their protective roles."
            },
            "Innovator": {
                "description": "Innovators create new technologies to improve the expedition's efficiency.",
                "airdrop_impact": "High - Their innovations are rewarded with airdrops to encourage creativity."
            },
            "Support": {
                "description": "Support members assist in logistical and medical needs.",
                "airdrop_impact": "Low - They have a lower chance of receiving airdrops but are essential for the team's wellbeing."
            }
        }

    def get_role_information(self, role_name):
        """
        Retrieve information about a specific role.

        Args:
            role_name (str): The name of the role to retrieve information for.

        Returns:
            dict: A dictionary containing the role's description and airdrop impact.
        """
        # Error handling for invalid role names
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' not found in expedition roles.")
        
        return self.roles[role_name]

    def list_all_roles(self):
        """
        List all roles in the RedStone Expedition.

        Returns:
            dict: A dictionary of all roles with their descriptions and airdrop impacts.
        """
        return self.roles

def main():
    """
    Main function to demonstrate the RedStone Expedition functionality.
    """
    expedition = RedStoneExpedition()

    # Example: Get information about a specific role
    try:
        role_name = "Explorer"
        role_info = expedition.get_role_information(role_name)
        print(f"Role: {role_name}\nDescription: {role_info['description']}\nAirdrop Impact: {role_info['airdrop_impact']}\n")
    except ValueError as e:
        print(e)

    # Example: List all roles
    print("All Roles in the RedStone Expedition:")
    all_roles = expedition.list_all_roles()
    for role, info in all_roles.items():
        print(f"Role: {role}\nDescription: {info['description']}\nAirdrop Impact: {info['airdrop_impact']}\n")

if __name__ == "__main__":
    main()
```
