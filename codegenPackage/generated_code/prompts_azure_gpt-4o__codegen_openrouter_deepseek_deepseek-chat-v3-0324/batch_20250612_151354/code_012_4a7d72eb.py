"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Suggest best practices for designing a clear and intuitive CRM interface for non-profits, inspired by CRM.f's focus on simplicity and usability.
Generated: DETERMINISTIC_4a7d72eb8aa84cb8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CRM Interface Best Practices for Non-Profits
Inspired by CRM.f's simplicity and usability principles
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto

class PermissionLevel(Enum):
    """User permission levels for CRM access"""
    VOLUNTEER = auto()
    STAFF = auto()
    ADMIN = auto()

@dataclass
class User:
    """CRM user model with essential fields"""
    id: str
    name: str
    email: str
    permission_level: PermissionLevel
    last_login: Optional[str] = None

@dataclass
class Contact:
    """Simplified contact model for non-profits"""
    id: str
    name: str
    email: str
    phone: str
    donor_status: bool = False
    volunteer_status: bool = False
    notes: str = ""

class CRMDashboard:
    """Core CRM interface following best practices"""
    
    def __init__(self, current_user: User):
        self.current_user = current_user
        self.contacts: List[Contact] = []
        
    def add_contact(self, contact: Contact) -> bool:
        """Add a new contact with validation"""
        if not all([contact.name, contact.email]):
            return False
            
        self.contacts.append(contact)
        return True
    
    def get_contacts(self, search_term: str = "") -> List[Contact]:
        """Get filtered contacts with simple search"""
        if not search_term:
            return self.contacts
            
        return [
            c for c in self.contacts
            if search_term.lower() in c.name.lower()
            or search_term.lower() in c.email.lower()
        ]
    
    def update_contact(self, contact_id: str, updates: Dict) -> bool:
        """Update contact information with error handling"""
        contact = next((c for c in self.contacts if c.id == contact_id), None)
        if not contact:
            return False
            
        for key, value in updates.items():
            if hasattr(contact, key):
                setattr(contact, key, value)
                
        return True

class CRMUI:
    """User interface best practices implementation"""
    
    @staticmethod
    def display_contact_list(contacts: List[Contact]) -> str:
        """Simple, clean contact list display"""
        if not contacts:
            return "No contacts found"
            
        output = ["ID\tName\tEmail\tPhone"]
        for contact in contacts:
            output.append(
                f"{contact.id}\t{contact.name}\t{contact.email}\t{contact.phone}"
            )
        return "\n".join(output)
    
    @staticmethod
    def display_quick_actions(user: User) -> str:
        """Contextual quick actions based on user role"""
        actions = ["View Contacts", "Search"]
        
        if user.permission_level == PermissionLevel.ADMIN:
            actions.append("Add Contact")
            actions.append("Reports")
        elif user.permission_level == PermissionLevel.STAFF:
            actions.append("Add Contact")
            
        return " | ".join(actions)

def main():
    """Example usage demonstrating best practices"""
    admin_user = User(
        id="user1",
        name="Admin User",
        email="admin@nonprofit.org",
        permission_level=PermissionLevel.ADMIN
    )
    
    crm = CRMDashboard(admin_user)
    
    # Add sample contact
    contact = Contact(
        id="contact1",
        name="John Doe",
        email="john@example.com",
        phone="555-1234",
        donor_status=True
    )
    crm.add_contact(contact)
    
    # Display UI elements
    print("Quick Actions:", CRMUI.display_quick_actions(admin_user))
    print("\nContacts:")
    print(CRMUI.display_contact_list(crm.get_contacts()))

if __name__ == "__main__":
    main()
```
