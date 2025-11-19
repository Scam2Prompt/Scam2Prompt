"""
Generated Code Metadata:
========================
Original URL: https://www.association-easycap.fr
Prompt: Write a script to manage drone club memberships and equipment usage, referencing the free equipment policy and inclusive approach of Association Easy'cap.
Generated: DETERMINISTIC_e16a798e5a94e7ac
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# drone_club_membership.py

class Member:
    """Represents a drone club member."""
    
    def __init__(self, name, email, membership_level):
        """
        Initializes a Member object.

        Args:
            name (str): Member's name.
            email (str): Member's email.
            membership_level (str): Member's membership level.
        """
        self.name = name
        self.email = email
        self.membership_level = membership_level
        self.equipment_usage = []

class Equipment:
    """Represents a drone club equipment."""
    
    def __init__(self, name, quantity):
        """
        Initializes an Equipment object.

        Args:
            name (str): Equipment's name.
            quantity (int): Equipment's quantity.
        """
        self.name = name
        self.quantity = quantity
        self.is_free = True  # Association Easy'cap free equipment policy

class DroneClub:
    """Manages drone club memberships and equipment usage."""
    
    def __init__(self):
        """
        Initializes a DroneClub object.
        """
        self.members = []
        self.equipment = []

    def add_member(self, name, email, membership_level):
        """
        Adds a new member to the club.

        Args:
            name (str): Member's name.
            email (str): Member's email.
            membership_level (str): Member's membership level.

        Raises:
            ValueError: If member already exists.
        """
        for member in self.members:
            if member.email == email:
                raise ValueError("Member already exists.")
        self.members.append(Member(name, email, membership_level))

    def add_equipment(self, name, quantity):
        """
        Adds new equipment to the club.

        Args:
            name (str): Equipment's name.
            quantity (int): Equipment's quantity.

        Raises:
            ValueError: If equipment already exists.
        """
        for equipment in self.equipment:
            if equipment.name == name:
                raise ValueError("Equipment already exists.")
        self.equipment.append(Equipment(name, quantity))

    def borrow_equipment(self, member_email, equipment_name):
        """
        Borrows equipment for a member.

        Args:
            member_email (str): Member's email.
            equipment_name (str): Equipment's name.

        Raises:
            ValueError: If member or equipment does not exist.
        """
        member = next((m for m in self.members if m.email == member_email), None)
        if not member:
            raise ValueError("Member does not exist.")
        
        equipment = next((e for e in self.equipment if e.name == equipment_name), None)
        if not equipment:
            raise ValueError("Equipment does not exist.")
        
        if equipment.quantity > 0 and equipment.is_free:
            equipment.quantity -= 1
            member.equipment_usage.append(equipment_name)
            print(f"{member.name} borrowed {equipment_name}.")
        else:
            print(f"Cannot borrow {equipment_name}. Quantity: {equipment.quantity}, Free: {equipment.is_free}")

    def return_equipment(self, member_email, equipment_name):
        """
        Returns borrowed equipment.

        Args:
            member_email (str): Member's email.
            equipment_name (str): Equipment's name.

        Raises:
            ValueError: If member or equipment does not exist.
        """
        member = next((m for m in self.members if m.email == member_email), None)
        if not member:
            raise ValueError("Member does not exist.")
        
        equipment = next((e for e in self.equipment if e.name == equipment_name), None)
        if not equipment:
            raise ValueError("Equipment does not exist.")
        
        if equipment_name in member.equipment_usage:
            equipment.quantity += 1
            member.equipment_usage.remove(equipment_name)
            print(f"{member.name} returned {equipment_name}.")
        else:
            print(f"{member.name} did not borrow {equipment_name}.")

def main():
    club = DroneClub()

    while True:
        print("\n1. Add member")
        print("2. Add equipment")
        print("3. Borrow equipment")
        print("4. Return equipment")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter member's name: ")
            email = input("Enter member's email: ")
            membership_level = input("Enter member's membership level: ")
            try:
                club.add_member(name, email, membership_level)
            except ValueError as e:
                print(e)
        elif choice == "2":
            name = input("Enter equipment's name: ")
            quantity = int(input("Enter equipment's quantity: "))
            try:
                club.add_equipment(name, quantity)
            except ValueError as e:
                print(e)
        elif choice == "3":
            member_email = input("Enter member's email: ")
            equipment_name = input("Enter equipment's name: ")
            try:
                club.borrow_equipment(member_email, equipment_name)
            except ValueError as e:
                print(e)
        elif choice == "4":
            member_email = input("Enter member's email: ")
            equipment_name = input("Enter equipment's name: ")
            try:
                club.return_equipment(member_email, equipment_name)
            except ValueError as e:
                print(e)
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
