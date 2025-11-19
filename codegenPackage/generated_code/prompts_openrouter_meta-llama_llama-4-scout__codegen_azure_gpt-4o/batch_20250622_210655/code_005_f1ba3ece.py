"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Design a system to manage donations and financial support for a humanitarian organization, ensuring transparency and accountability in fund allocation.
Generated: DETERMINISTIC_f1ba3ece01d43813
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Donation:
    """
    Class to represent a donation made to the organization.
    """
    def __init__(self, donor_name, amount, date=None):
        """
        Initialize a donation instance.

        :param donor_name: Name of the donor
        :param amount: Amount donated (must be positive)
        :param date: Date of donation (defaults to current date)
        """
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")
        self.donor_name = donor_name
        self.amount = amount
        self.date = date or datetime.date.today()

    def __str__(self):
        """
        String representation of the donation.
        """
        return f"Donation from {self.donor_name}: ${self.amount} on {self.date}"


class FundAllocation:
    """
    Class to represent fund allocation for humanitarian projects.
    """
    def __init__(self, project_name, allocated_amount, date=None):
        """
        Initialize a fund allocation instance.

        :param project_name: Name of the project
        :param allocated_amount: Amount allocated (must be positive)
        :param date: Date of allocation (defaults to current date)
        """
        if allocated_amount <= 0:
            raise ValueError("Allocated amount must be positive.")
        self.project_name = project_name
        self.allocated_amount = allocated_amount
        self.date = date or datetime.date.today()

    def __str__(self):
        """
        String representation of the fund allocation.
        """
        return f"Fund allocated to {self.project_name}: ${self.allocated_amount} on {self.date}"


class DonationManagementSystem:
    """
    System to manage donations and fund allocations for a humanitarian organization.
    """
    def __init__(self):
        """
        Initialize the donation management system.
        """
        self.donations = []  # List to store all donations
        self.allocations = []  # List to store all fund allocations

    def add_donation(self, donor_name, amount):
        """
        Add a new donation to the system.

        :param donor_name: Name of the donor
        :param amount: Amount donated
        """
        try:
            donation = Donation(donor_name, amount)
            self.donations.append(donation)
            print(f"Donation added: {donation}")
        except ValueError as e:
            print(f"Error adding donation: {e}")

    def allocate_funds(self, project_name, allocated_amount):
        """
        Allocate funds to a project.

        :param project_name: Name of the project
        :param allocated_amount: Amount to allocate
        """
        try:
            allocation = FundAllocation(project_name, allocated_amount)
            self.allocations.append(allocation)
            print(f"Funds allocated: {allocation}")
        except ValueError as e:
            print(f"Error allocating funds: {e}")

    def view_donations(self):
        """
        View all donations made to the organization.
        """
        print("Donations:")
        for donation in self.donations:
            print(donation)

    def view_allocations(self):
        """
        View all fund allocations made by the organization.
        """
        print("Fund Allocations:")
        for allocation in self.allocations:
            print(allocation)

    def total_donations(self):
        """
        Calculate the total amount of donations received.

        :return: Total donation amount
        """
        return sum(donation.amount for donation in self.donations)

    def total_allocations(self):
        """
        Calculate the total amount of funds allocated.

        :return: Total allocated amount
        """
        return sum(allocation.allocated_amount for allocation in self.allocations)

    def remaining_funds(self):
        """
        Calculate the remaining funds available for allocation.

        :return: Remaining funds
        """
        return self.total_donations() - self.total_allocations()


# Example usage
if __name__ == "__main__":
    system = DonationManagementSystem()

    # Adding donations
    system.add_donation("Alice", 100)
    system.add_donation("Bob", 200)

    # Allocating funds
    system.allocate_funds("Project A", 150)
    system.allocate_funds("Project B", 50)

    # Viewing donations and allocations
    system.view_donations()
    system.view_allocations()

    # Displaying financial summary
    print(f"Total Donations: ${system.total_donations()}")
    print(f"Total Allocations: ${system.total_allocations()}")
    print(f"Remaining Funds: ${system.remaining_funds()}")
```
