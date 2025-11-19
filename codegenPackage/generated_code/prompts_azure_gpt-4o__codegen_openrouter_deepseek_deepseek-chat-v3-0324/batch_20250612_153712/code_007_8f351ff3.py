"""
Generated Code Metadata:
========================
Original URL: https://legatoltd.net
Prompt: Write a program to generate an efficient action plan for fund recovery based on user-provided scam details, inspired by The Legato's recovery process.
Generated: DETERMINISTIC_8f351ff3b1b456f7
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple

class ScamType(Enum):
    PHISHING = auto()
    INVESTMENT = auto()
    ROMANCE = auto()
    IMPERSONATION = auto()
    OTHER = auto()

class RecoveryStep:
    def __init__(self, description: str, priority: int, deadline: Optional[datetime] = None):
        self.description = description
        self.priority = priority
        self.deadline = deadline

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "priority": self.priority,
            "deadline": self.deadline.isoformat() if self.deadline else None
        }

class RecoveryPlan:
    def __init__(self):
        self.steps: List[RecoveryStep] = []
    
    def add_step(self, step: RecoveryStep) -> None:
        self.steps.append(step)
        self.steps.sort(key=lambda x: x.priority)
    
    def to_dict(self) -> Dict:
        return {
            "steps": [step.to_dict() for step in self.steps]
        }
    
    def save_to_file(self, filename: str) -> None:
        try:
            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
        except IOError as e:
            raise Exception(f"Failed to save recovery plan: {str(e)}")

def get_scam_details() -> Tuple[ScamType, Dict]:
    print("Please provide details about the scam:")
    
    # Get scam type
    print("\nSelect scam type:")
    for i, scam_type in enumerate(ScamType):
        print(f"{i+1}. {scam_type.name}")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= len(ScamType):
                scam_type = list(ScamType)[choice-1]
                break
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get additional details
    details = {}
    details["amount_lost"] = float(input("Enter amount lost (in USD): "))
    details["date_occurred"] = input("Enter date scam occurred (YYYY-MM-DD): ")
    details["payment_method"] = input("Enter payment method used: ")
    details["scammer_details"] = input("Enter any known scammer details: ")
    
    return scam_type, details

def generate_recovery_plan(scam_type: ScamType, details: Dict) -> RecoveryPlan:
    plan = RecoveryPlan()
    
    # Immediate actions (high priority)
    plan.add_step(RecoveryStep(
        "Contact your bank or payment provider to report the fraud and request a chargeback",
        1,
        datetime.now()
    ))
    
    plan.add_step(RecoveryStep(
        "File a report with your local law enforcement agency",
        2,
        datetime.now()
    ))
    
    # Type-specific steps
    if scam_type == ScamType.PHISHING:
        plan.add_step(RecoveryStep(
            "Change all passwords and enable two-factor authentication on affected accounts",
            3
        ))
        plan.add_step(RecoveryStep(
            "Report the phishing attempt to the relevant platform (e.g., email provider, social media)",
            4
        ))
    elif scam_type == ScamType.INVESTMENT:
        plan.add_step(RecoveryStep(
            "Gather all communication and documentation related to the investment",
            3
        ))
        plan.add_step(RecoveryStep(
            "Report to financial regulatory authorities in your jurisdiction",
            4
        ))
    elif scam_type == ScamType.ROMANCE:
        plan.add_step(RecoveryStep(
            "Preserve all communication with the scammer (emails, messages, etc.)",
            3
        ))
        plan.add_step(RecoveryStep(
            "Report the profile to the dating/social platform where you met the scammer",
            4
        ))
    
    # Common follow-up steps
    plan.add_step(RecoveryStep(
        "Monitor your financial accounts for suspicious activity",
        5
    ))
    
    plan.add_step(RecoveryStep(
        "Consider consulting with a legal professional specializing in fraud cases",
        6
    ))
    
    return plan

def main():
    try:
        print("Fund Recovery Action Plan Generator")
        print("Inspired by The Legato's recovery process\n")
        
        scam_type, details = get_scam_details()
        recovery_plan = generate_recovery_plan(scam_type, details)
        
        filename = f"recovery_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        recovery_plan.save_to_file(filename)
        
        print(f"\nRecovery plan generated successfully! Saved to {filename}")
        print("Please follow the steps in order of priority.")
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please try again or seek professional assistance.")

if __name__ == "__main__":
    main()
```
