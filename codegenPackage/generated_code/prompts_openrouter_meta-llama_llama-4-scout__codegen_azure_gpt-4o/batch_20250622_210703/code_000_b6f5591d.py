"""
Generated Code Metadata:
========================
Original URL: https://sherafight.nl
Prompt: Write a Python script to manage membership and pricing for a martial arts school like Shera Fight, with different rates for children, junior, and adults.
Generated: DETERMINISTIC_b6f5591df400a818
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class MartialArtsSchool:
    """
    A class to manage membership and pricing for a martial arts school.
    """

    def __init__(self):
        """
        Initialize the school with membership categories and their respective rates.
        """
        self.members = []  # List to store member information
        self.pricing = {
            "child": 50,  # Monthly rate for children (age 5-12)
            "junior": 75,  # Monthly rate for juniors (age 13-17)
            "adult": 100  # Monthly rate for adults (age 18+)
        }

    def add_member(self, name, age):
        """
        Add a new member to the school.

        :param name: Name of the member
        :param age: Age of the member
        :return: None
        """
        category = self._determine_category(age)
        if category:
            self.members.append({"name": name, "age": age, "category": category, "rate": self.pricing[category]})
            print(f"Member '{name}' added successfully as a {category} with a monthly rate of ${self.pricing[category]}.")
        else:
            print(f"Error: Age {age} is not eligible for membership.")

    def _determine_category(self, age):
        """
        Determine the membership category based on age.

        :param age: Age of the member
        :return: Category as a string ('child', 'junior', 'adult') or None if age is invalid
        """
        if 5 <= age <= 12:
            return "child"
        elif 13 <= age <= 17:
            return "junior"
        elif age >= 18:
            return "adult"
        else:
            return None

    def list_members(self):
        """
        List all members of the school.

        :return: None
        """
        if not self.members:
            print("No members found.")
            return

        print("Current Members:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Category: {member['category']}, Monthly Rate: ${member['rate']}")

    def calculate_total_revenue(self):
        """
        Calculate the total monthly revenue from all members.

        :return: Total revenue as a float
        """
        total_revenue = sum(member['rate'] for member in self.members)
        print(f"Total Monthly Revenue: ${total_revenue}")
        return total_revenue

    def remove_member(self, name):
        """
        Remove a member by name.

        :param name: Name of the member to remove
        :return: None
        """
        for member in self.members:
            if member['name'].lower() == name.lower():
                self.members.remove(member)
                print(f"Member '{name}' removed successfully.")
                return
        print(f"Error: Member '{name}' not found.")

def main():
    """
    Main function to interact with the MartialArtsSchool class.
    """
    school = MartialArtsSchool()

    while True:
        print("\nMartial Arts School Management")
        print("1. Add Member")
        print("2. List Members")
        print("3. Calculate Total Revenue")
        print("4. Remove Member")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter member name: ")
            try:
                age = int(input("Enter member age: "))
                school.add_member(name, age)
            except ValueError:
                print("Invalid age. Please enter a valid number.")
        elif choice == 2:
            school.list_members()
        elif choice == 3:
            school.calculate_total_revenue()
        elif choice == 4:
            name = input("Enter the name of the member to remove: ")
            school.remove_member(name)
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
```
