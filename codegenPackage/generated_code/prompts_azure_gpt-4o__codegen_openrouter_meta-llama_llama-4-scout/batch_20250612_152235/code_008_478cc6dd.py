"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Write a program to generate performance reports for virtual receptionist services, including metrics like call handling efficiency and customer satisfaction, as mentioned in ProSync's ongoing support and reporting.
Generated: DETERMINISTIC_478cc6dd940a27a5
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# performance_report_generator.py

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class CallStatus(Enum):
    ANSWERED = 1
    MISSED = 2
    TRANSFERRED = 3

@dataclass
class Call:
    id: int
    status: CallStatus
    handling_time: datetime.timedelta
    customer_satisfaction: int  # 1-5 rating

@dataclass
class PerformanceReport:
    total_calls: int
    answered_calls: int
    missed_calls: int
    transferred_calls: int
    average_handling_time: datetime.timedelta
    average_customer_satisfaction: float

class VirtualReceptionist:
    def __init__(self):
        self.calls = []

    def add_call(self, call: Call):
        self.calls.append(call)

    def generate_performance_report(self) -> PerformanceReport:
        total_calls = len(self.calls)
        answered_calls = sum(1 for call in self.calls if call.status == CallStatus.ANSWERED)
        missed_calls = sum(1 for call in self.calls if call.status == CallStatus.MISSED)
        transferred_calls = sum(1 for call in self.calls if call.status == CallStatus.TRANSFERRED)

        handling_times = [call.handling_time for call in self.calls if call.status == CallStatus.ANSWERED]
        average_handling_time = self._calculate_average_handling_time(handling_times)

        customer_satisfactions = [call.customer_satisfaction for call in self.calls]
        average_customer_satisfaction = self._calculate_average_customer_satisfaction(customer_satisfactions)

        return PerformanceReport(
            total_calls,
            answered_calls,
            missed_calls,
            transferred_calls,
            average_handling_time,
            average_customer_satisfaction
        )

    @staticmethod
    def _calculate_average_handling_time(handling_times: List[datetime.timedelta]) -> datetime.timedelta:
        if not handling_times:
            return datetime.timedelta(0)

        total_seconds = sum((dt.total_seconds() for dt in handling_times))
        average_seconds = total_seconds / len(handling_times)
        return datetime.timedelta(seconds=average_seconds)

    @staticmethod
    def _calculate_average_customer_satisfaction(customer_satisfactions: List[int]) -> float:
        if not customer_satisfactions:
            return 0.0

        return sum(customer_satisfactions) / len(customer_satisfactions)

def main():
    receptionist = VirtualReceptionist()

    # Example usage:
    receptionist.add_call(Call(1, CallStatus.ANSWERED, datetime.timedelta(minutes=5), 4))
    receptionist.add_call(Call(2, CallStatus.MISSED, datetime.timedelta(0), 0))
    receptionist.add_call(Call(3, CallStatus.TRANSFERRED, datetime.timedelta(minutes=2), 3))
    receptionist.add_call(Call(4, CallStatus.ANSWERED, datetime.timedelta(minutes=10), 5))

    report = receptionist.generate_performance_report()

    print("Performance Report:")
    print(f"Total Calls: {report.total_calls}")
    print(f"Answered Calls: {report.answered_calls}")
    print(f"Missed Calls: {report.missed_calls}")
    print(f"Transferred Calls: {report.transferred_calls}")
    print(f"Average Handling Time: {report.average_handling_time}")
    print(f"Average Customer Satisfaction: {report.average_customer_satisfaction:.2f}/5")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
