"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Develop a program that models the "MAGIC framework" for community building, incorporating multi-ability, multi-generational, and inclusive principles as outlined on the Kallimos website.
Generated: DETERMINISTIC_fa4b6c94220143b1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CommunityMember:
    """
    Represents a member of the community with various attributes.
    """

    def __init__(self, name: str, age: int, abilities: list):
        """
        Initializes a new community member.

        :param name: Name of the community member.
        :param age: Age of the community member.
        :param abilities: List of abilities the member possesses.
        """
        self.name = name
        self.age = age
        self.abilities = abilities

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Abilities: {', '.join(self.abilities)}"


class Community:
    """
    Represents a community that includes members of various ages and abilities.
    """

    def __init__(self):
        """
        Initializes an empty community.
        """
        self.members = []

    def add_member(self, member: CommunityMember):
        """
        Adds a new member to the community.

        :param member: An instance of CommunityMember to be added.
        """
        if not isinstance(member, CommunityMember):
            raise ValueError("Only CommunityMember instances can be added.")
        self.members.append(member)

    def get_members(self):
        """
        Returns a list of all community members.

        :return: List of community members.
        """
        return self.members

    def find_members_by_ability(self, ability: str):
        """
        Finds all members with a specific ability.

        :param ability: The ability to search for.
        :return: List of members with the specified ability.
        """
        return [member for member in self.members if ability in member.abilities]

    def __str__(self):
        return f"Community Members:\n" + "\n".join(str(member) for member in self.members)


def main():
    """
    Main function to demonstrate the MAGIC framework for community building.
    """
    # Create a community instance
    community = Community()

    # Add members to the community
    try:
        community.add_member(CommunityMember("Alice", 30, ["Teaching", "Cooking"]))
        community.add_member(CommunityMember("Bob", 65, ["Gardening", "Storytelling"]))
        community.add_member(CommunityMember("Charlie", 10, ["Drawing", "Playing"]))
    except ValueError as e:
        print(f"Error adding member: {e}")

    # Display all community members
    print(community)

    # Find members with a specific ability
    ability_to_search = "Teaching"
    members_with_ability = community.find_members_by_ability(ability_to_search)
    print(f"\nMembers with ability '{ability_to_search}':")
    for member in members_with_ability:
        print(member)


if __name__ == "__main__":
    main()
```
