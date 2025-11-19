"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ofertadudia.site
Prompt: Can you provide code examples for handling access restrictions in a project that encounters XQuiz ERRO X-902?
Generated: DETERMINISTIC_0eb4e543ea785cf5
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Access Restriction Handler for XQuiz ERRO X-902

This Python module handles access restrictions based on the occurrence of the
specific error code X-902, commonly encountered in the XQuiz system.

Key Features:
- Logging of access restriction errors
- Graceful handling of unauthorized access attempts
- Custom exception for XQuiz error
"""

import logging


# Configure logging
logging.basicConfig(
    filename='access_restriction.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AccessRestrictionError(Exception):
    """
    Custom exception to handle access restriction errors for XQuiz ERRO X-902.
    """
    def __init__(self, message="Access restricted due to XQuiz ERRO X-902"):
        super().__init__(message)


def check_access(user_role: str):
    """
    Simulates checking access permissions for a user based on their role.
    
    Args:
        user_role (str): Role of the user (e.g., "admin", "user", "guest").
    
    Raises:
        AccessRestrictionError: If access is restricted due to XQuiz ERRO X-902.
    """
    restricted_roles = ["guest", "anonymous"]  # Roles that have restricted access
    if user_role in restricted_roles:
        logging.error(f"Access denied for role '{user_role}' due to XQuiz ERRO X-902.")
        raise AccessRestrictionError()


def main():
    """
    Main function to simulate access restriction handling.
    """
    users = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "guest"},
        {"name": "Charlie", "role": "user"},
        {"name": "Dave", "role": "anonymous"},
    ]

    for user in users:
        try:
            print(f"Checking access for {user['name']} with role '{user['role']}'...")
            check_access(user['role'])
            print(f"Access granted to {user['name']}.\n")
        except AccessRestrictionError as e:
            print(f"Access denied for {user['name']}: {e}\n")
        except Exception as e:
            # Catch any other unexpected errors
            logging.exception("Unexpected error occurred:")
            print(f"An unexpected error occurred for {user['name']}: {e}\n")


if __name__ == "__main__":
    main()
```
