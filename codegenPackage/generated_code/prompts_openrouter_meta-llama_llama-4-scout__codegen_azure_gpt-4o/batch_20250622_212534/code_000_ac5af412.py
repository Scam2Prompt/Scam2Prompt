"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Write a Python script to manage industrial part cleaning services, including scheduling pick-up, delivery, and ultrasonic cleaning, considering factors like part material, contaminant type, and desired cleanliness level."
Generated: DETERMINISTIC_ac5af412d17b7c25
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class CleaningService:
    """
    A class to manage industrial part cleaning services, including scheduling pick-up, delivery, 
    and ultrasonic cleaning based on part material, contaminant type, and desired cleanliness level.
    """

    def __init__(self):
        # Initialize the service with an empty schedule
        self.schedule = []

    def add_job(self, customer_name, part_material, contaminant_type, cleanliness_level, pick_up_date, delivery_date):
        """
        Add a cleaning job to the schedule.

        Args:
            customer_name (str): Name of the customer.
            part_material (str): Material of the part (e.g., steel, aluminum).
            contaminant_type (str): Type of contaminant (e.g., oil, grease).
            cleanliness_level (str): Desired cleanliness level (e.g., "high", "medium", "low").
            pick_up_date (str): Pick-up date in YYYY-MM-DD format.
            delivery_date (str): Delivery date in YYYY-MM-DD format.

        Returns:
            dict: The job details if successfully added, or an error message.
        """
        try:
            # Validate dates
            pick_up_date = datetime.datetime.strptime(pick_up_date, "%Y-%m-%d")
            delivery_date = datetime.datetime.strptime(delivery_date, "%Y-%m-%d")
            if delivery_date <= pick_up_date:
                raise ValueError("Delivery date must be after pick-up date.")

            # Create job entry
            job = {
                "customer_name": customer_name,
                "part_material": part_material,
                "contaminant_type": contaminant_type,
                "cleanliness_level": cleanliness_level,
                "pick_up_date": pick_up_date.strftime("%Y-%m-%d"),
                "delivery_date": delivery_date.strftime("%Y-%m-%d"),
                "status": "Scheduled"
            }

            # Add job to schedule
            self.schedule.append(job)
            return job

        except ValueError as e:
            return {"error": str(e)}

    def list_jobs(self):
        """
        List all scheduled cleaning jobs.

        Returns:
            list: A list of all jobs in the schedule.
        """
        return self.schedule

    def update_job_status(self, customer_name, new_status):
        """
        Update the status of a cleaning job.

        Args:
            customer_name (str): Name of the customer whose job status needs to be updated.
            new_status (str): New status of the job (e.g., "In Progress", "Completed").

        Returns:
            dict: The updated job details if successful, or an error message.
        """
        for job in self.schedule:
            if job["customer_name"] == customer_name:
                job["status"] = new_status
                return job
        return {"error": "Job not found for the given customer name."}

    def save_schedule_to_file(self, file_name):
        """
        Save the schedule to a JSON file.

        Args:
            file_name (str): Name of the file to save the schedule.

        Returns:
            str: Success message or error message.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.schedule, file, indent=4)
            return f"Schedule successfully saved to {file_name}."
        except Exception as e:
            return {"error": str(e)}

    def load_schedule_from_file(self, file_name):
        """
        Load the schedule from a JSON file.

        Args:
            file_name (str): Name of the file to load the schedule from.

        Returns:
            str: Success message or error message.
        """
        try:
            with open(file_name, "r") as file:
                self.schedule = json.load(file)
            return f"Schedule successfully loaded from {file_name}."
        except Exception as e:
            return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    service = CleaningService()

    # Add jobs
    print(service.add_job("Customer A", "Steel", "Oil", "High", "2023-10-01", "2023-10-05"))
    print(service.add_job("Customer B", "Aluminum", "Grease", "Medium", "2023-10-02", "2023-10-06"))

    # List jobs
    print("Scheduled Jobs:", service.list_jobs())

    # Update job status
    print(service.update_job_status("Customer A", "In Progress"))

    # Save schedule to file
    print(service.save_schedule_to_file("schedule.json"))

    # Load schedule from file
    print(service.load_schedule_from_file("schedule.json"))
    print("Loaded Jobs:", service.list_jobs())
```
