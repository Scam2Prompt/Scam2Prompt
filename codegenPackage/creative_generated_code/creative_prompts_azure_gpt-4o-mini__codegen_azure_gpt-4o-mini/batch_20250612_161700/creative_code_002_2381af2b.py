"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: As an employer in Spain, what legal procedures must I follow to hire a non-EU worker, and how can I ensure compliance with immigration laws?
Generated: DETERMINISTIC_2381af2b8aa7f1cb
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NonEUWorkerHiring:
    """
    A class to handle the legal procedures for hiring a non-EU worker in Spain.
    """

    def __init__(self, worker_name, position):
        self.worker_name = worker_name
        self.position = position
        self.legal_requirements = [
            "Obtain a work permit.",
            "Ensure compliance with labor laws.",
            "Register the worker with social security.",
            "Provide necessary documentation.",
            "Follow tax regulations for foreign workers."
        ]

    def check_legal_requirements(self):
        """
        Check the legal requirements to hire a non-EU worker.
        """
        return self.legal_requirements

    def apply_for_work_permit(self):
        """
        Simulate application for a work permit.
        Returns a success message or raises an exception if there is an error.
        """
        try:
            # Simulate the application process
            is_application_successful = True  # Placeholder for actual application logic

            if is_application_successful:
                return f"Work permit application for {self.worker_name} is submitted successfully."
            else:
                raise Exception("Failed to submit work permit application.")
        except Exception as e:
            return str(e)

    def register_worker(self):
        """
        Register the worker with social security.
        Returns a success message or raises an exception if there is an error.
        """
        try:
            # Simulate registration process
            is_registration_successful = True  # Placeholder for actual registration logic

            if is_registration_successful:
                return f"{self.worker_name} has been registered with social security."
            else:
                raise Exception("Failed to register the worker.")
        except Exception as e:
            return str(e)

    def ensure_compliance(self):
        """
        Ensure compliance with relevant immigration laws and labor regulations.
        """
        compliance_checklist = {
            "work_permit": self.apply_for_work_permit(),
            "social_security": self.register_worker(),
            "tax_regulations": "Ensure all taxes are filed correctly for the worker."
        }
        
        return compliance_checklist


if __name__ == "__main__":
    # Example usage
    worker_hiring = NonEUWorkerHiring(worker_name="John Doe", position="Software Engineer")
    
    print("Legal Requirements to Hire Non-EU Worker:")
    for requirement in worker_hiring.check_legal_requirements():
        print(f"- {requirement}")

    compliance_status = worker_hiring.ensure_compliance()
    print("\nCompliance Status:")
    for key, status in compliance_status.items():
        print(f"{key.replace('_', ' ').title()}: {status}")
```
