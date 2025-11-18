"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Write a program to generate an efficient action plan for fund recovery based on user-provided scam details, inspired by The Legato's recovery process.
Generated: DETERMINISTIC_8f351ff3b1b456f7
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for the application
import datetime
import json

class FundRecoveryPlanGenerator:
    """
    A class to generate an action plan for fund recovery based on user-provided scam details.
    """

    def __init__(self):
        # Initialize the recovery plan generator
        self.action_plan = []

    def gather_details(self):
        """
        Gather details from the user about the scam.
        """
        try:
            print("Please provide details about the scam.")
            scam_details = {
                "victim_name": input("Victim's Full Name: ").strip(),
                "contact_email": input("Contact Email: ").strip(),
                "amount_lost": float(input("Amount Lost (in USD): ")),
                "scammer_name": input("Scammer's Name (if known): ").strip(),
                "scammer_contact": input("Scammer's Contact Info (if known): ").strip(),
                "scam_description": input("Brief Description of the Scam: ").strip(),
                "incident_date": input("Date of Incident (YYYY-MM-DD): ").strip(),
                "reported_to_authorities": input("Reported to Authorities? (yes/no): ").strip().lower() == "yes"
            }
            
            # Validate date format
            scam_details["incident_date"] = self.validate_date(scam_details["incident_date"])

            return scam_details
        
        except ValueError as ve:
            print(f"Error: Invalid input. Please ensure numeric values for the amount lost. Details: {ve}")
            return None
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return None

    def validate_date(self, date_str):
        """
        Validate the format of the date provided.
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as ve:
            print(f"Error: Invalid date format. Details: {ve}")
            return None

    def generate_plan(self, scam_details):
        """
        Generate an action plan based on the provided scam details.
        """
        if not scam_details:
            print("Unable to generate action plan due to missing or invalid details.")
            return []

        # Step 1: Notify law enforcement if not already done
        if not scam_details["reported_to_authorities"]:
            self.action_plan.append(
                "Contact local law enforcement and file an official report regarding the scam."
            )

        # Step 2: Gather evidence
        self.action_plan.append("Collect and organize all evidence related to the scam (emails, receipts, chat logs, etc.).")

        # Step 3: Contact financial institutions
        self.action_plan.append(
            "Notify your bank or payment service provider about the fraudulent transaction. "
            "Request a chargeback or freeze on the affected account."
        )

        # Step 4: Perform online reputation checks on the scammer
        if scam_details["scammer_name"] or scam_details["scammer_contact"]:
            self.action_plan.append(
                f"Perform online searches and reputation checks on '{scam_details['scammer_name']}' "
                f"or '{scam_details['scammer_contact']}' to aid in identification."
            )

        # Step 5: Utilize recovery services
        self.action_plan.append(
            "Engage professional fund recovery services (e.g., The Legato) for assistance in recovering lost funds."
        )

        # Step 6: Educate yourself and others
        self.action_plan.append(
            "Educate yourself about common scam tactics to avoid future incidents. "
            "Share your experience to warn others."
        )

        return self.action_plan

    def display_plan(self):
        """
        Display the generated action plan step by step.
        """
        print("\n--- Fund Recovery Action Plan ---")
        for step, action in enumerate(self.action_plan, 1):
            print(f"Step {step}: {action}")

    def save_plan_to_file(self, scam_details):
        """
        Save the generated action plan and scam details to a JSON file.
        """
        try:
            file_name = f"recovery_plan_{scam_details['victim_name'].replace(' ', '_')}.json"
            data = {
                "scam_details": scam_details,
                "action_plan": self.action_plan
            }
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
            print(f"\nAction plan saved to file: {file_name}")
        except Exception as e:
            print(f"Error saving the plan to file: {e}")

def main():
    """
    Main function to execute the program.
    """
    print("Welcome to the Fund Recovery Plan Generator!")
    frpg = FundRecoveryPlanGenerator()

    # Step 1: Gather scam details from the user
    scam_details = frpg.gather_details()
    if scam_details is None:
        print("Exiting due to invalid input.")
        return

    # Step 2: Generate an action plan
    frpg.generate_plan(scam_details)

    # Step 3: Display the action plan
    frpg.display_plan()

    # Step 4: Save the plan to a file
    frpg.save_plan_to_file(scam_details)

# Execute the program
if __name__ == "__main__":
    main()
```
