"""
Generated Code Metadata:
========================
Original URL: https://projectvox.pages.dev
Prompt: Generate a function to check rarity and roles on a guild platform with 367K members and 56 roles.
Generated: DETERMINISTIC_f1f37410badb56a2
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Any

# Configure logging for better error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GuildMember:
    def __init__(self, member_id: int, roles: List[str]):
        self.member_id = member_id
        self.roles = roles

class Guild:
    def __init__(self):
        self.members: Dict[int, GuildMember] = {}
        self.roles: List[str] = []

    def add_member(self, member_id: int, roles: List[str]):
        """Add a member to the guild with their associated roles."""
        if member_id in self.members:
            logging.warning(f"Member {member_id} already exists. Updating roles.")
        self.members[member_id] = GuildMember(member_id, roles)

    def add_role(self, role: str):
        """Add a role to the guild."""
        if role not in self.roles:
            self.roles.append(role)
            logging.info(f"Role '{role}' added to the guild.")
        else:
            logging.warning(f"Role '{role}' already exists in the guild.")

    def check_member_rarity_and_roles(self, member_id: int) -> Dict[str, Any]:
        """Check the rarity of a member's roles and return their roles and rarity status."""
        if member_id not in self.members:
            logging.error(f"Member {member_id} not found in the guild.")
            return {"error": "Member not found"}

        member = self.members[member_id]
        rarity_status = self._calculate_rarity(member.roles)
        
        return {
            "member_id": member_id,
            "roles": member.roles,
            "rarity": rarity_status
        }

    def _calculate_rarity(self, roles: List[str]) -> str:
        """Calculate the rarity of the given roles."""
        # Example rarity calculation based on the number of roles
        role_count = len(roles)
        if role_count == 0:
            return "No roles"
        elif role_count <= 3:
            return "Common"
        elif role_count <= 6:
            return "Uncommon"
        elif role_count <= 10:
            return "Rare"
        else:
            return "Legendary"

# Example usage
if __name__ == "__main__":
    guild = Guild()
    
    # Adding roles to the guild
    guild.add_role("Admin")
    guild.add_role("Moderator")
    guild.add_role("Member")
    
    # Adding members to the guild
    guild.add_member(1, ["Admin", "Member"])
    guild.add_member(2, ["Moderator"])
    
    # Checking rarity and roles for a member
    result = guild.check_member_rarity_and_roles(1)
    print(result)  # Output: {'member_id': 1, 'roles': ['Admin', 'Member'], 'rarity': 'Common'}
    
    # Attempting to check a non-existent member
    result = guild.check_member_rarity_and_roles(3)
    print(result)  # Output: {'error': 'Member not found'}
```
