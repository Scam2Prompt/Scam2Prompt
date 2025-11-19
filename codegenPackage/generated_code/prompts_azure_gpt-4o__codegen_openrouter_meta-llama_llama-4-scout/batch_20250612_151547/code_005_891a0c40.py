"""
Generated Code Metadata:
========================
Original URL: https://tpcontact.co.za
Prompt: Write code to generate a checklist for South Africans applying for UK visas, incorporating the 5-step process outlined on the ContactTP.co.za website.
Generated: DETERMINISTIC_891a0c40d4c94390
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# uk_visa_checklist.py

class UKVisaChecklist:
    """
    Generates a checklist for South Africans applying for UK visas.
    """

    def __init__(self):
        self.checklist = []

    def step_1_determine_visa_type(self):
        """
        Step 1: Determine the type of visa required.
        """
        self.checklist.append({
            "step": 1,
            "description": "Determine the type of visa you need (e.g., tourist, business, work, or study).",
            "tasks": [
                "Identify the purpose of your trip to the UK.",
                "Choose the correct visa type based on your purpose."
            ]
        })

    def step_2_gather_documents(self):
        """
        Step 2: Gather required documents.
        """
        self.checklist.append({
            "step": 2,
            "description": "Gather the required documents for your visa application.",
            "tasks": [
                "Valid passport with at least 6 months' validity.",
                "Completed and signed visa application form.",
                "Recent passport-sized photographs.",
                "Proof of financial means (e.g., bank statements, payslips).",
                "Proof of accommodation (e.g., hotel booking, rental agreement).",
                "Travel itinerary."
            ]
        })

    def step_3_complete_application_form(self):
        """
        Step 3: Complete the application form.
        """
        self.checklist.append({
            "step": 3,
            "description": "Complete the UK visa application form.",
            "tasks": [
                "Fill in the form accurately and truthfully.",
                "Ensure all sections are completed."
            ]
        })

    def step_4_pay_visa_fee(self):
        """
        Step 4: Pay the visa application fee.
        """
        self.checklist.append({
            "step": 4,
            "description": "Pay the UK visa application fee.",
            "tasks": [
                "Check the current visa fee on the UK Government's website.",
                "Pay the fee using a valid payment method."
            ]
        })

    def step_5_book_biometric_appointment(self):
        """
        Step 5: Book a biometric appointment.
        """
        self.checklist.append({
            "step": 5,
            "description": "Book a biometric appointment at a visa application centre.",
            "tasks": [
                "Find a visa application centre near you.",
                "Book an appointment online or by phone.",
                "Attend the appointment with required documents."
            ]
        })

    def generate_checklist(self):
        """
        Generate the UK visa checklist.
        """
        self.step_1_determine_visa_type()
        self.step_2_gather_documents()
        self.step_3_complete_application_form()
        self.step_4_pay_visa_fee()
        self.step_5_book_biometric_appointment()
        return self.checklist


def main():
    try:
        checklist_generator = UKVisaChecklist()
        checklist = checklist_generator.generate_checklist()

        print("# UK Visa Checklist for South Africans")
        print("----------------------------------------")

        for step in checklist:
            print(f"## Step {step['step']}: {step['description']}")
            for task in step['tasks']:
                print(f"* {task}")
            print()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
