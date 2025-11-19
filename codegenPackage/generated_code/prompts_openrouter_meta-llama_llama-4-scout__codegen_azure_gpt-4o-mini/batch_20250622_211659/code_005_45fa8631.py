"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: What are the advantages of becoming a Comfort Club Member with RJW Mechanical, and how can this membership affect the cost of HVAC repairs and maintenance?
Generated: DETERMINISTIC_45fa8631187dde9d
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ComfortClubMember:
    """
    A class to represent a Comfort Club Membership with RJW Mechanical.
    This membership provides various benefits related to HVAC repairs and maintenance.
    """

    def __init__(self, member_name, membership_level):
        """
        Initializes a new Comfort Club Member.

        :param member_name: str - The name of the member
        :param membership_level: str - The level of membership (e.g., 'Basic', 'Premium')
        """
        self.member_name = member_name
        self.membership_level = membership_level
        self.benefits = self.get_benefits()
        self.discount_rate = self.get_discount_rate()

    def get_benefits(self):
        """
        Returns the benefits associated with the membership level.

        :return: list - A list of benefits
        """
        benefits_dict = {
            'Basic': [
                '10% discount on all repairs',
                'Priority scheduling for service calls',
                'Annual system check-up'
            ],
            'Premium': [
                '15% discount on all repairs',
                'Priority scheduling for service calls',
                'Annual system check-up',
                'Free filter replacements'
            ]
        }
        return benefits_dict.get(self.membership_level, [])

    def get_discount_rate(self):
        """
        Returns the discount rate based on the membership level.

        :return: float - The discount rate as a percentage
        """
        discount_dict = {
            'Basic': 0.10,
            'Premium': 0.15
        }
        return discount_dict.get(self.membership_level, 0.0)

    def calculate_repair_cost(self, original_cost):
        """
        Calculates the cost of repairs after applying the membership discount.

        :param original_cost: float - The original cost of the repair
        :return: float - The discounted cost
        """
        if original_cost < 0:
            raise ValueError("Original cost must be a non-negative value.")
        discount = original_cost * self.discount_rate
        return original_cost - discount

    def display_member_info(self):
        """
        Displays the member's information and benefits.
        """
        print(f"Member Name: {self.member_name}")
        print(f"Membership Level: {self.membership_level}")
        print("Benefits:")
        for benefit in self.benefits:
            print(f"- {benefit}")
        print(f"Discount Rate: {self.discount_rate * 100}%")

# Example usage
if __name__ == "__main__":
    try:
        member = ComfortClubMember("John Doe", "Premium")
        member.display_member_info()
        original_cost = 500.0  # Example repair cost
        discounted_cost = member.calculate_repair_cost(original_cost)
        print(f"Original Repair Cost: ${original_cost:.2f}")
        print(f"Discounted Repair Cost: ${discounted_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
