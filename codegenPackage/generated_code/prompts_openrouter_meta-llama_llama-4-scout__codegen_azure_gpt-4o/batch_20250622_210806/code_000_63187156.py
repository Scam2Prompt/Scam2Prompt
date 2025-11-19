"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Generate a Python program to manage membership plans for a Jiu-Jitsu school like Fusion Jiu Jitsu School, including pricing and scheduling features."
Generated: DETERMINISTIC_6318715617eadd42
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class MembershipPlan:
    """
    Class to represent a membership plan for the Jiu-Jitsu school.
    """
    def __init__(self, name, price, duration_in_months, classes_per_week):
        """
        Initialize a membership plan.

        :param name: Name of the membership plan
        :param price: Price of the membership plan (in USD)
        :param duration_in_months: Duration of the plan in months
        :param classes_per_week: Number of classes per week
        """
        self.name = name
        self.price = price
        self.duration_in_months = duration_in_months
        self.classes_per_week = classes_per_week

    def __str__(self):
        """
        String representation of the membership plan.
        """
        return (f"Plan Name: {self.name}\n"
                f"Price: ${self.price:.2f}\n"
                f"Duration: {self.duration_in_months} months\n"
                f"Classes per week: {self.classes_per_week}")


class Member:
    """
    Class to represent a member of the Jiu-Jitsu school.
    """
    def __init__(self, name, email, membership_plan):
        """
        Initialize a member.

        :param name: Name of the member
        :param email: Email of the member
        :param membership_plan: MembershipPlan object representing the member's plan
        """
        self.name = name
        self.email = email
        self.membership_plan = membership_plan
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=30 * membership_plan.duration_in_months)

    def __str__(self):
        """
        String representation of the member.
        """
        return (f"Member Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Membership Plan: {self.membership_plan.name}\n"
                f"Start Date: {self.start_date}\n"
                f"End Date: {self.end_date}")


class JiuJitsuSchool:
    """
    Class to manage the Jiu-Jitsu school membership plans and members.
    """
    def __init__(self, school_name):
        """
        Initialize the Jiu-Jitsu school.

        :param school_name: Name of the school
        """
        self.school_name = school_name
        self.membership_plans = []
        self.members = []

    def add_membership_plan(self, name, price, duration_in_months, classes_per_week):
        """
        Add a new membership plan to the school.

        :param name: Name of the membership plan
        :param price: Price of the membership plan (in USD)
        :param duration_in_months: Duration of the plan in months
        :param classes_per_week: Number of classes per week
        """
        plan = MembershipPlan(name, price, duration_in_months, classes_per_week)
        self.membership_plans.append(plan)
        print(f"Membership plan '{name}' added successfully.")

    def list_membership_plans(self):
        """
        List all available membership plans.
        """
        if not self.membership_plans:
            print("No membership plans available.")
            return
        print("Available Membership Plans:")
        for plan in self.membership_plans:
            print(plan)
            print("-" * 40)

    def register_member(self, name, email, plan_name):
        """
        Register a new member to the school.

        :param name: Name of the member
        :param email: Email of the member
        :param plan_name: Name of the membership plan the member is enrolling in
        """
        plan = next((p for p in self.membership_plans if p.name == plan_name), None)
        if not plan:
            print(f"Error: Membership plan '{plan_name}' not found.")
            return
        member = Member(name, email, plan)
        self.members.append(member)
        print(f"Member '{name}' registered successfully.")

    def list_members(self):
        """
        List all registered members.
        """
        if not self.members:
            print("No members registered.")
            return
        print("Registered Members:")
        for member in self.members:
            print(member)
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    school = JiuJitsuSchool("Fusion Jiu Jitsu School")

    # Add membership plans
    school.add_membership_plan("Basic", 100, 1, 2)
    school.add_membership_plan("Premium", 200, 3, 4)
    school.add_membership_plan("Unlimited", 300, 6, 7)

    # List membership plans
    school.list_membership_plans()

    # Register members
    school.register_member("John Doe", "john.doe@example.com", "Premium")
    school.register_member("Jane Smith", "jane.smith@example.com", "Unlimited")

    # List members
    school.list_members()
```
