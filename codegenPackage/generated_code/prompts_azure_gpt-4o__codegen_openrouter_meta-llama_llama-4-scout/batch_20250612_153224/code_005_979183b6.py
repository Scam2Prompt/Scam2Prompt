"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Develop a payroll system for school staff, including pay slip generation and salary calculations, inspired by Him Saral's Payroll module.
Generated: DETERMINISTIC_979183b682e8791d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payroll_system.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class PayFrequency(Enum):
    """Pay frequency enum"""
    MONTHLY = 1
    BI_WEEKLY = 2
    WEEKLY = 3

class StaffMember:
    """Staff member class"""
    def __init__(self, staff_id: int, name: str, pay_frequency: PayFrequency, 
                 basic_salary: float, allowances: Dict[str, float] = {}, 
                 deductions: Dict[str, float] = {}):
        self.staff_id = staff_id
        self.name = name
        self.pay_frequency = pay_frequency
        self.basic_salary = basic_salary
        self.allowances = allowances
        self.deductions = deductions

    def calculate_gross_salary(self) -> float:
        """Calculate gross salary"""
        gross_salary = self.basic_salary
        for allowance in self.allowances.values():
            gross_salary += allowance
        return gross_salary

    def calculate_net_salary(self) -> float:
        """Calculate net salary"""
        net_salary = self.calculate_gross_salary()
        for deduction in self.deductions.values():
            net_salary -= deduction
        return net_salary

class PaySlip:
    """Pay slip class"""
    def __init__(self, staff_member: StaffMember, pay_period: str, 
                 gross_salary: float, net_salary: float):
        self.staff_member = staff_member
        self.pay_period = pay_period
        self.gross_salary = gross_salary
        self.net_salary = net_salary

    def generate_pay_slip(self) -> str:
        """Generate pay slip"""
        pay_slip = f"Pay Slip for {self.staff_member.name}\n"
        pay_slip += f"Pay Period: {self.pay_period}\n"
        pay_slip += f"Gross Salary: ${self.gross_salary:.2f}\n"
        pay_slip += f"Net Salary: ${self.net_salary:.2f}\n"
        pay_slip += "Allowances:\n"
        for allowance, amount in self.staff_member.allowances.items():
            pay_slip += f"- {allowance}: ${amount:.2f}\n"
        pay_slip += "Deductions:\n"
        for deduction, amount in self.staff_member.deductions.items():
            pay_slip += f"- {deduction}: ${amount:.2f}\n"
        return pay_slip

class PayrollSystem:
    """Payroll system class"""
    def __init__(self):
        self.staff_members = []

    def add_staff_member(self, staff_member: StaffMember):
        """Add staff member"""
        self.staff_members.append(staff_member)

    def generate_pay_slips(self, pay_period: str) -> List[PaySlip]:
        """Generate pay slips"""
        pay_slips = []
        for staff_member in self.staff_members:
            gross_salary = staff_member.calculate_gross_salary()
            net_salary = staff_member.calculate_net_salary()
            pay_slip = PaySlip(staff_member, pay_period, gross_salary, net_salary)
            pay_slips.append(pay_slip)
        return pay_slips

def main():
    try:
        payroll_system = PayrollSystem()

        staff_member1 = StaffMember(
            1, 
            "John Doe", 
            PayFrequency.MONTHLY, 
            5000.0, 
            allowances={"Housing Allowance": 1000.0, "Transportation Allowance": 500.0}, 
            deductions={"Tax": 1000.0, "Health Insurance": 200.0}
        )

        staff_member2 = StaffMember(
            2, 
            "Jane Doe", 
            PayFrequency.BI_WEEKLY, 
            3000.0, 
            allowances={"Housing Allowance": 800.0, "Transportation Allowance": 300.0}, 
            deductions={"Tax": 800.0, "Health Insurance": 150.0}
        )

        payroll_system.add_staff_member(staff_member1)
        payroll_system.add_staff_member(staff_member2)

        pay_period = f"{datetime.now().strftime('%B %Y')}"
        pay_slips = payroll_system.generate_pay_slips(pay_period)

        for pay_slip in pay_slips:
            print(pay_slip.generate_pay_slip())
            print("------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
