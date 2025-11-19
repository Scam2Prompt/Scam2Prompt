"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Recommend a suitable software solution for a cooperative society in Pune, including features such as member management, billing, and accounting, based on MDA Tech Sys's software development services."
Generated: DETERMINISTIC_ec0f88c00fd2bba8
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cooperative_society.py

class Member:
    """Represents a member of the cooperative society."""
    
    def __init__(self, member_id, name, email, phone):
        """
        Initializes a Member object.

        Args:
            member_id (int): Unique identifier for the member.
            name (str): Name of the member.
            email (str): Email address of the member.
            phone (str): Phone number of the member.
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

class CooperativeSociety:
    """Represents a cooperative society with member management, billing, and accounting features."""
    
    def __init__(self):
        """Initializes a CooperativeSociety object."""
        self.members = {}
        self.bills = {}

    def add_member(self, member):
        """
        Adds a member to the cooperative society.

        Args:
            member (Member): Member object to be added.

        Raises:
            ValueError: If a member with the same ID already exists.
        """
        if member.member_id in self.members:
            raise ValueError("Member with ID {} already exists.".format(member.member_id))
        self.members[member.member_id] = member

    def remove_member(self, member_id):
        """
        Removes a member from the cooperative society.

        Args:
            member_id (int): ID of the member to be removed.

        Raises:
            ValueError: If the member does not exist.
        """
        if member_id not in self.members:
            raise ValueError("Member with ID {} does not exist.".format(member_id))
        del self.members[member_id]

    def add_bill(self, member_id, bill_amount):
        """
        Adds a bill for a member.

        Args:
            member_id (int): ID of the member.
            bill_amount (float): Amount of the bill.

        Raises:
            ValueError: If the member does not exist.
        """
        if member_id not in self.members:
            raise ValueError("Member with ID {} does not exist.".format(member_id))
        if member_id not in self.bills:
            self.bills[member_id] = []
        self.bills[member_id].append(bill_amount)

    def get_member_bills(self, member_id):
        """
        Retrieves the bills for a member.

        Args:
            member_id (int): ID of the member.

        Returns:
            list: List of bill amounts for the member.

        Raises:
            ValueError: If the member does not exist.
        """
        if member_id not in self.members:
            raise ValueError("Member with ID {} does not exist.".format(member_id))
        return self.bills.get(member_id, [])

    def calculate_member_balance(self, member_id):
        """
        Calculates the balance for a member.

        Args:
            member_id (int): ID of the member.

        Returns:
            float: Balance for the member.

        Raises:
            ValueError: If the member does not exist.
        """
        if member_id not in self.members:
            raise ValueError("Member with ID {} does not exist.".format(member_id))
        bills = self.get_member_bills(member_id)
        return sum(bills)

def main():
    try:
        society = CooperativeSociety()

        # Create members
        member1 = Member(1, "John Doe", "john@example.com", "1234567890")
        member2 = Member(2, "Jane Doe", "jane@example.com", "9876543210")

        # Add members to the society
        society.add_member(member1)
        society.add_member(member2)

        # Add bills for members
        society.add_bill(1, 1000.0)
        society.add_bill(1, 500.0)
        society.add_bill(2, 2000.0)

        # Retrieve member bills
        print("Member 1 bills:", society.get_member_bills(1))
        print("Member 2 bills:", society.get_member_bills(2))

        # Calculate member balances
        print("Member 1 balance:", society.calculate_member_balance(1))
        print("Member 2 balance:", society.calculate_member_balance(2))

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
```
