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
import datetime
import json

class FundRecoveryActionPlan:
    """
    Class to generate an action plan for fund recovery based on scam details.
    """

    def __init__(self, scam_details):
        """
        Initializes the FundRecoveryActionPlan with user-provided scam details.

        Args:
            scam_details (dict): Details about the scam including the type,
                                 amount lost, date of occurrence, and any 
                                 other relevant information.
        """
        self.scam_details = scam_details
        self.action_plan = {
            "report_date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "steps": []
        }

    def validate_scam_details(self):
        """
        Validates the scam details provided by the user.

        Raises:
            ValueError: If any required field is missing or invalid.
        """
        required_fields = ['scam_type', 'amount_lost', 'date_occurred']
        for field in required_fields:
            if field not in self.scam_details or not self.scam_details[field]:
                raise ValueError(f"Missing required field: {field}")

        # Ensure amount lost is a positive number
        if not isinstance(self.scam_details['amount_lost'], (int, float)) or self.scam_details['amount_lost'] <= 0:
            raise ValueError("Amount lost must be a positive number.")

        # Verify date format is valid
        try:
            datetime.datetime.strptime(self.scam_details['date_occurred'], "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date occurred must be in YYYY-MM-DD format.")

    def generate_action_plan(self):
        """
        Generates an action plan based on the scam details.

        Returns:
            dict: A structured action plan for recovery.
        """
        self.validate_scam_details()

        # Step 1: Report to authorities
        self.action_plan["steps"].append("Report to local authorities and file a report.")
        
        # Step 2: Contact your bank/credit card provider
        self.action_plan["steps"].append("Contact your bank or credit card provider to dispute the charge.")
        
        # Step 3: Gather documentation
        self.action_plan["steps"].append("Gather all documentation related to the scam.")

        # Step 4: Report to consumer protection agencies
        self.action_plan["steps"].append("Report the scam to consumer protection agencies.")

        # Step 5: Monitor accounts
        self.action_plan["steps"].append("Monitor your financial accounts for any suspicious activity.")

        # Step 6: Seek legal advice if necessary
        self.action_plan["steps"].append("Consider seeking legal advice if substantial amounts are involved.")

        return self.action_plan

def main():
    """
    Main function to execute the fund recovery action plan generation.
    """
    # Example scam details provided by the user
    user_input = {
        "scam_type": "Online Investment Scam",
        "amount_lost": 5000,
        "date_occurred": "2023-09-15"
    }

    try:
        recovery_plan = FundRecoveryActionPlan(user_input)
        action_plan = recovery_plan.generate_action_plan()
        
        # Output the action plan in JSON format for better readability
        print(json.dumps(action_plan, indent=4))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
