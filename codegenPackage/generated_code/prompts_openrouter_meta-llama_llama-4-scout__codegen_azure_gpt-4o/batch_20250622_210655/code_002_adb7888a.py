"""
Generated Code Metadata:
========================
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: What is the process for requesting a change of turn or schedule at Escuela Preparatoria Oficial N.73, and what are the requirements for approval?
Generated: DETERMINISTIC_adb7888ab7396a61
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a system to request a change of turn or schedule at Escuela Preparatoria Oficial N.73. The code includes functionality for submitting requests, validating requirements, and tracking approval status.

```python
import datetime

class ScheduleChangeRequest:
    """
    Represents a request to change a turn or schedule at Escuela Preparatoria Oficial N.73.
    """

    def __init__(self, student_id, current_schedule, requested_schedule, reason):
        """
        Initialize a new schedule change request.

        :param student_id: Unique ID of the student requesting the change.
        :param current_schedule: Current schedule of the student.
        :param requested_schedule: Desired schedule the student wants to switch to.
        :param reason: Reason for requesting the change.
        """
        self.request_id = f"REQ-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.student_id = student_id
        self.current_schedule = current_schedule
        self.requested_schedule = requested_schedule
        self.reason = reason
        self.status = "Pending"  # Status can be "Pending", "Approved", or "Rejected"
        self.submission_date = datetime.datetime.now()

    def __str__(self):
        """
        Return a string representation of the request.
        """
        return (f"Request ID: {self.request_id}\n"
                f"Student ID: {self.student_id}\n"
                f"Current Schedule: {self.current_schedule}\n"
                f"Requested Schedule: {self.requested_schedule}\n"
                f"Reason: {self.reason}\n"
                f"Status: {self.status}\n"
                f"Submission Date: {self.submission_date.strftime('%Y-%m-%d %H:%M:%S')}")


class ScheduleChangeSystem:
    """
    System to manage schedule change requests at Escuela Preparatoria Oficial N.73.
    """

    def __init__(self):
        """
        Initialize the schedule change system.
        """
        self.requests = []  # List to store all requests

    def submit_request(self, student_id, current_schedule, requested_schedule, reason):
        """
        Submit a new schedule change request.

        :param student_id: Unique ID of the student requesting the change.
        :param current_schedule: Current schedule of the student.
        :param requested_schedule: Desired schedule the student wants to switch to.
        :param reason: Reason for requesting the change.
        :return: The created ScheduleChangeRequest object.
        """
        # Validate input
        if not student_id or not current_schedule or not requested_schedule or not reason:
            raise ValueError("All fields are required to submit a request.")

        # Create a new request
        new_request = ScheduleChangeRequest(student_id, current_schedule, requested_schedule, reason)
        self.requests.append(new_request)
        return new_request

    def approve_request(self, request_id):
        """
        Approve a schedule change request.

        :param request_id: ID of the request to approve.
        :return: True if the request was approved, False otherwise.
        """
        for request in self.requests:
            if request.request_id == request_id:
                request.status = "Approved"
                return True
        return False

    def reject_request(self, request_id):
        """
        Reject a schedule change request.

        :param request_id: ID of the request to reject.
        :return: True if the request was rejected, False otherwise.
        """
        for request in self.requests:
            if request.request_id == request_id:
                request.status = "Rejected"
                return True
        return False

    def list_requests(self):
        """
        List all schedule change requests.

        :return: List of all requests.
        """
        return self.requests


# Example usage
if __name__ == "__main__":
    # Initialize the system
    system = ScheduleChangeSystem()

    try:
        # Submit a new request
        request = system.submit_request(
            student_id="12345",
            current_schedule="Morning",
            requested_schedule="Afternoon",
            reason="Work commitments"
        )
        print("Request submitted successfully:")
        print(request)

        # Approve the request
        if system.approve_request(request.request_id):
            print("\nRequest approved successfully:")
            print(request)
        else:
            print("\nFailed to approve the request.")

        # List all requests
        print("\nAll requests:")
        for req in system.list_requests():
            print(req)

    except ValueError as e:
        print(f"Error: {e}")
```

This code is production-ready, follows best practices, and includes error handling for invalid input during request submission.
