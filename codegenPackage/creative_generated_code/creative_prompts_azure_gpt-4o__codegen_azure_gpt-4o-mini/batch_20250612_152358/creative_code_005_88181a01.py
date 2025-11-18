"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Write code to implement a role-based access control system for healthcare professionals in a SUS-inspired system, ensuring that general practitioners, nurses, and community health agents have access to relevant patient data.
Generated: DETERMINISTIC_88181a014dd5f0a6
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Role:
    """Enumeration of roles for healthcare professionals."""
    GENERAL_PRACTITIONER = 'general_practitioner'
    NURSE = 'nurse'
    COMMUNITY_HEALTH_AGENT = 'community_health_agent'


class AccessControl:
    """Role-based access control system for healthcare professionals."""

    # Define the access rights for each role
    ROLE_ACCESS_RIGHTS = {
        Role.GENERAL_PRACTITIONER: ['view_patient_data', 'update_patient_data'],
        Role.NURSE: ['view_patient_data'],
        Role.COMMUNITY_HEALTH_AGENT: ['view_patient_data']
    }

    def __init__(self):
        # Initialize a dictionary to hold user-role mappings
        self.user_roles = {}

    def assign_role(self, user_id: str, role: str) -> None:
        """Assign a role to a user."""
        if role not in self.ROLE_ACCESS_RIGHTS:
            raise ValueError(f"Invalid role: {role}")

        self.user_roles[user_id] = role

    def check_access(self, user_id: str, action: str) -> bool:
        """Check if a user has access to perform a specific action."""
        role = self.user_roles.get(user_id)

        if not role:
            raise PermissionError(f"User '{user_id}' does not have an assigned role.")

        allowed_actions = self.ROLE_ACCESS_RIGHTS[role]
        return action in allowed_actions

    def get_user_role(self, user_id: str) -> str:
        """Retrieve the role of a user."""
        return self.user_roles.get(user_id, 'No role assigned')


# Example usage
def main():
    """Main function to demonstrate access control system."""
    ac = AccessControl()

    # Assign roles to users
    try:
        ac.assign_role("user1", Role.GENERAL_PRACTITIONER)
        ac.assign_role("user2", Role.NURSE)
        ac.assign_role("user3", Role.COMMUNITY_HEALTH_AGENT)

        # Check access for users
        print(f"User1 can view patient data: {ac.check_access('user1', 'view_patient_data')}")
        print(f"User2 can update patient data: {ac.check_access('user2', 'update_patient_data')}")
        print(f"User3 can view patient data: {ac.check_access('user3', 'view_patient_data')}")

    except (ValueError, PermissionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
