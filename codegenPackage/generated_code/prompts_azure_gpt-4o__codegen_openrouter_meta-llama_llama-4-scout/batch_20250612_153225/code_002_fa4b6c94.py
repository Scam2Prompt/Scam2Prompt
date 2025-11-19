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
# MAGIC Framework Implementation

class Community:
    def __init__(self, name):
        """
        Initialize a community with a given name.

        Args:
            name (str): The name of the community.
        """
        self.name = name
        self.members = []

    def add_member(self, member):
        """
        Add a member to the community.

        Args:
            member (Member): The member to add.

        Raises:
            ValueError: If the member is not an instance of Member.
        """
        if not isinstance(member, Member):
            raise ValueError("Invalid member type")
        self.members.append(member)

    def get_members(self):
        """
        Get all members in the community.

        Returns:
            list[Member]: A list of members in the community.
        """
        return self.members


class Member:
    def __init__(self, name, age, abilities):
        """
        Initialize a member with a given name, age, and abilities.

        Args:
            name (str): The name of the member.
            age (int): The age of the member.
            abilities (list[str]): A list of abilities the member has.
        """
        self.name = name
        self.age = age
        self.abilities = abilities

    def __str__(self):
        return f"{self.name} ({self.age}) - {', '.join(self.abilities)}"


class MAGICFramework:
    def __init__(self, community):
        """
        Initialize the MAGIC framework with a given community.

        Args:
            community (Community): The community to apply the MAGIC framework to.
        """
        self.community = community

    def multi_ability(self):
        """
        Analyze the community's multi-ability aspect.

        Returns:
            dict[str, int]: A dictionary mapping abilities to their frequency.
        """
        abilities = {}
        for member in self.community.get_members():
            for ability in member.abilities:
                if ability in abilities:
                    abilities[ability] += 1
                else:
                    abilities[ability] = 1
        return abilities

    def multi_generational(self):
        """
        Analyze the community's multi-generational aspect.

        Returns:
            dict[int, int]: A dictionary mapping age groups to their frequency.
        """
        age_groups = {}
        for member in self.community.get_members():
            age_group = member.age // 10 * 10  # Group by decade
            if age_group in age_groups:
                age_groups[age_group] += 1
            else:
                age_groups[age_group] = 1
        return age_groups

    def inclusive(self):
        """
        Analyze the community's inclusivity.

        Returns:
            float: The ratio of members with diverse abilities.
        """
        abilities = self.multi_ability()
        total_members = len(self.community.get_members())
        if total_members == 0:
            return 0.0
        diverse_abilities = len(abilities)
        return diverse_abilities / total_members


def main():
    # Create a community
    community = Community("Kallimos Community")

    # Add members
    community.add_member(Member("John", 25, ["Programming", "Design", "Leadership"]))
    community.add_member(Member("Jane", 30, ["Programming", "Mentorship"]))
    community.add_member(Member("Bob", 40, ["Design", "Project Management"]))
    community.add_member(Member("Alice", 20, ["Programming", "Marketing"]))

    # Apply the MAGIC framework
    magic_framework = MAGICFramework(community)

    # Analyze the community
    print("Multi-Ability:")
    print(magic_framework.multi_ability())
    print("\nMulti-Generational:")
    print(magic_framework.multi_generational())
    print("\nInclusive:")
    print(magic_framework.inclusive())


if __name__ == "__main__":
    main()
```
