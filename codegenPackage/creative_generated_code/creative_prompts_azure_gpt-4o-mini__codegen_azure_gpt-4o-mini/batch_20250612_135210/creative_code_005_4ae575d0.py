"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-foundation.vercel.app
Prompt: Describe the role of the Data Availability Committee (DAC) in the Arbitrum governance structure.
Generated: DETERMINISTIC_4ae575d063e983a6
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DataAvailabilityCommittee:
    """
    A class representing the Data Availability Committee (DAC) 
    in the Arbitrum governance structure.
    """

    def __init__(self, committee_members=None):
        """
        Initializes the Data Availability Committee with a list of members.
        
        Args:
            committee_members (list): A list of member names. Defaults to an empty list.
        """
        if committee_members is None:
            committee_members = []
        self.committee_members = committee_members

    def add_member(self, member_name):
        """
        Adds a member to the Data Availability Committee.
        
        Args:
            member_name (str): The name of the member to add.
        
        Raises:
            ValueError: If the member is already in the committee.
        """
        if member_name in self.committee_members:
            raise ValueError(f"Member '{member_name}' is already in the committee.")
        
        self.committee_members.append(member_name)

    def remove_member(self, member_name):
        """
        Removes a member from the Data Availability Committee.
        
        Args:
            member_name (str): The name of the member to remove.
        
        Raises:
            ValueError: If the member is not found in the committee.
        """
        try:
            self.committee_members.remove(member_name)
        except ValueError:
            raise ValueError(f"Member '{member_name}' not found in the committee.")

    def is_member(self, member_name):
        """
        Checks if a member is part of the Data Availability Committee.
        
        Args:
            member_name (str): The name of the member to check.
        
        Returns:
            bool: True if the member is in the committee, False otherwise.
        """
        return member_name in self.committee_members

    def get_members(self):
        """
        Retrieves the list of committee members.
        
        Returns:
            list: A list of the names of the committee members.
        """
        return self.committee_members

    def __repr__(self):
        """
        Returns a string representation of the Data Availability Committee.
        
        Returns:
            str: A representation of the committee's current state.
        """
        return f"DataAvailabilityCommittee(members={self.committee_members})"


# Example usage
if __name__ == "__main__":
    # Initialize a Data Availability Committee
    dac = DataAvailabilityCommittee()

    # Add members
    try:
        dac.add_member("Alice")
        dac.add_member("Bob")
        dac.add_member("Charlie")
        print(dac)

        # Attempting to add a duplicate member
        dac.add_member("Alice")
    except ValueError as e:
        print(e)

    # Check membership
    print(f"Is Alice a member? {dac.is_member('Alice')}")
    print(f"Is Dave a member? {dac.is_member('Dave')}")

    # Remove a member
    try:
        dac.remove_member("Bob")
        print(dac)
    except ValueError as e:
        print(e)

    # Get list of members
    print("Current members:", dac.get_members())
```
