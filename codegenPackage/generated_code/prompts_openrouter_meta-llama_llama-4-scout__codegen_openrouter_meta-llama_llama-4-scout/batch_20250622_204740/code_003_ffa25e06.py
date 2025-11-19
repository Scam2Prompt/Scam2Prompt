"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Develop a code snippet to track and analyze hotel staff performance and management metrics, focusing on effective hotel management practices.
Generated: DETERMINISTIC_ffa25e0690fe206c
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hotel_performance_tracker.py

from datetime import datetime
from typing import Dict, List

class StaffMember:
    """Represents a hotel staff member."""

    def __init__(self, staff_id: int, name: str, role: str):
        """
        Initializes a StaffMember object.

        Args:
        staff_id (int): Unique staff ID.
        name (str): Staff member name.
        role (str): Staff member role.
        """
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.check_in_count = 0
        self.check_out_count = 0
        self.customer_feedback = []

    def check_in(self):
        """Increments the check-in count."""
        self.check_in_count += 1

    def check_out(self):
        """Increments the check-out count."""
        self.check_out_count += 1

    def add_feedback(self, feedback: str):
        """
        Adds customer feedback.

        Args:
        feedback (str): Customer feedback.
        """
        self.customer_feedback.append(feedback)


class HotelPerformanceTracker:
    """Tracks and analyzes hotel staff performance and management metrics."""

    def __init__(self):
        """Initializes a HotelPerformanceTracker object."""
        self.staff_members: Dict[int, StaffMember] = {}
        self.total_revenue = 0.0

    def add_staff_member(self, staff_id: int, name: str, role: str):
        """
        Adds a staff member.

        Args:
        staff_id (int): Unique staff ID.
        name (str): Staff member name.
        role (str): Staff member role.
        """
        if staff_id in self.staff_members:
            raise ValueError("Staff ID already exists.")
        self.staff_members[staff_id] = StaffMember(staff_id, name, role)

    def remove_staff_member(self, staff_id: int):
        """
        Removes a staff member.

        Args:
        staff_id (int): Unique staff ID.
        """
        if staff_id not in self.staff_members:
            raise ValueError("Staff ID does not exist.")
        del self.staff_members[staff_id]

    def log_check_in(self, staff_id: int):
        """
        Logs a staff member check-in.

        Args:
        staff_id (int): Unique staff ID.
        """
        if staff_id not in self.staff_members:
            raise ValueError("Staff ID does not exist.")
        self.staff_members[staff_id].check_in()

    def log_check_out(self, staff_id: int):
        """
        Logs a staff member check-out.

        Args:
        staff_id (int): Unique staff ID.
        """
        if staff_id not in self.staff_members:
            raise ValueError("Staff ID does not exist.")
        self.staff_members[staff_id].check_out()

    def add_customer_feedback(self, staff_id: int, feedback: str):
        """
        Adds customer feedback for a staff member.

        Args:
        staff_id (int): Unique staff ID.
        feedback (str): Customer feedback.
        """
        if staff_id not in self.staff_members:
            raise ValueError("Staff ID does not exist.")
        self.staff_members[staff_id].add_feedback(feedback)

    def log_revenue(self, amount: float):
        """
        Logs hotel revenue.

        Args:
        amount (float): Revenue amount.
        """
        self.total_revenue += amount

    def get_staff_performance(self, staff_id: int) -> Dict[str, object]:
        """
        Retrieves staff performance metrics.

        Args:
        staff_id (int): Unique staff ID.

        Returns:
        Dict[str, object]: Staff performance metrics.
        """
        if staff_id not in self.staff_members:
            raise ValueError("Staff ID does not exist.")
        staff_member = self.staff_members[staff_id]
        return {
            "name": staff_member.name,
            "role": staff_member.role,
            "check_in_count": staff_member.check_in_count,
            "check_out_count": staff_member.check_out_count,
            "customer_feedback": staff_member.customer_feedback,
        }

    def get_hotel_performance(self) -> Dict[str, object]:
        """
        Retrieves hotel performance metrics.

        Returns:
        Dict[str, object]: Hotel performance metrics.
        """
        staff_performance = {
            staff_id: {
                "name": staff_member.name,
                "role": staff_member.role,
                "check_in_count": staff_member.check_in_count,
                "check_out_count": staff_member.check_out_count,
            }
            for staff_id, staff_member in self.staff_members.items()
        }
        return {
            "total_revenue": self.total_revenue,
            "staff_performance": staff_performance,
        }


def main():
    tracker = HotelPerformanceTracker()

    # Add staff members
    tracker.add_staff_member(1, "John Doe", "Front Desk")
    tracker.add_staff_member(2, "Jane Smith", "Housekeeping")

    # Log staff check-ins and check-outs
    tracker.log_check_in(1)
    tracker.log_check_in(2)
    tracker.log_check_out(1)
    tracker.log_check_out(2)

    # Add customer feedback
    tracker.add_customer_feedback(1, "Excellent service!")
    tracker.add_customer_feedback(2, "Good job!")

    # Log revenue
    tracker.log_revenue(1000.0)
    tracker.log_revenue(500.0)

    # Retrieve staff performance metrics
    print(tracker.get_staff_performance(1))

    # Retrieve hotel performance metrics
    print(tracker.get_hotel_performance())


if __name__ == "__main__":
    main()
```
