"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Write code to implement a role-based access control system for healthcare professionals in a SUS-inspired system, ensuring that general practitioners, nurses, and community health agents have access to relevant patient data.
Generated: DETERMINISTIC_88181a014dd5f0a6
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """Represents a user in the healthcare system."""
    
    def __init__(self, username, role):
        """
        Initializes a new user with a username and role.
        
        Args:
            username (str): The username of the user.
            role (str): The role of the user (e.g., 'general_practitioner', 'nurse', 'community_health_agent').
        """
        self.username = username
        self.role = role


class Patient:
    """Represents a patient in the healthcare system."""
    
    def __init__(self, patient_id, name, medical_history):
        """
        Initializes a new patient with an ID, name, and medical history.
        
        Args:
            patient_id (str): The unique identifier for the patient.
            name (str): The name of the patient.
            medical_history (dict): The medical history of the patient.
        """
        self.patient_id = patient_id
        self.name = name
        self.medical_history = medical_history


class AccessControl:
    """Handles role-based access control for healthcare professionals."""
    
    def __init__(self):
        """Initializes the access control system with role permissions."""
        self.role_permissions = {
            'general_practitioner': ['view_patient_data', 'update_patient_data'],
            'nurse': ['view_patient_data'],
            'community_health_agent': ['view_patient_data']
        }

    def has_permission(self, user, action):
        """
        Checks if a user has permission to perform a specific action.
        
        Args:
            user (User): The user to check permissions for.
            action (str): The action to check permissions against.
        
        Returns:
            bool: True if the user has permission, False otherwise.
        """
        return action in self.role_permissions.get(user.role, [])

    def access_patient_data(self, user, patient):
        """
        Allows a user to access patient data based on their role.
        
        Args:
            user (User): The user attempting to access the data.
            patient (Patient): The patient whose data is being accessed.
        
        Returns:
            dict: The patient's data if access is granted, otherwise raises an exception.
        
        Raises:
            PermissionError: If the user does not have permission to access the data.
        """
        action = 'view_patient_data'
        if self.has_permission(user, action):
            return {
                'patient_id': patient.patient_id,
                'name': patient.name,
                'medical_history': patient.medical_history
            }
        else:
            raise PermissionError(f"{user.username} does not have permission to access patient data.")


# Example usage
if __name__ == "__main__":
    # Create users
    gp = User("dr_smith", "general_practitioner")
    nurse = User("nurse_jane", "nurse")
    cha = User("agent_bob", "community_health_agent")

    # Create a patient
    patient = Patient("12345", "John Doe", {"allergies": ["penicillin"], "conditions": ["hypertension"]})

    # Initialize access control
    access_control = AccessControl()

    # Attempt to access patient data
    try:
        print(access_control.access_patient_data(gp, patient))  # Should succeed
        print(access_control.access_patient_data(nurse, patient))  # Should succeed
        print(access_control.access_patient_data(cha, patient))  # Should succeed
    except PermissionError as e:
        print(e)
```
