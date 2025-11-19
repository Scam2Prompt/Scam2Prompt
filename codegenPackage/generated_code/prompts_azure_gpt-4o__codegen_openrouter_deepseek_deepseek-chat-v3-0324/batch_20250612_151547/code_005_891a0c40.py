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
import json
from typing import List, Dict

class UKVisaChecklistGenerator:
    """
    A class to generate a checklist for South Africans applying for UK visas.
    The checklist follows the 5-step process from ContactTP.co.za.
    """
    
    def __init__(self):
        self.steps = [
            {
                "step": 1,
                "title": "Determine the Correct Visa Type",
                "description": "Identify which UK visa category you need to apply for.",
                "items": [
                    "Check the UK government website for visa types",
                    "Common types: Tourist, Work, Study, Family visas",
                    "Confirm eligibility requirements for chosen visa"
                ]
            },
            {
                "step": 2,
                "title": "Complete the Online Application",
                "description": "Fill out the visa application form accurately.",
                "items": [
                    "Create an account on the UK Visa website",
                    "Complete all sections of the application",
                    "Double-check all information before submission",
                    "Pay the application fee online"
                ]
            },
            {
                "step": 3,
                "title": "Book Your Biometrics Appointment",
                "description": "Schedule and attend your biometric data collection.",
                "items": [
                    "Book appointment at a Visa Application Centre (VAC)",
                    "Prepare required documents for the appointment",
                    "Attend appointment with all original documents",
                    "Have your fingerprints and photo taken"
                ]
            },
            {
                "step": 4,
                "title": "Submit Supporting Documents",
                "description": "Provide all necessary documents to support your application.",
                "items": [
                    "Passport (valid for at least 6 months)",
                    "Proof of financial means (bank statements)",
                    "Accommodation details in the UK",
                    "Travel itinerary (if applicable)",
                    "Employment/study documents (if applicable)",
                    "TB test results (if required)"
                ]
            },
            {
                "step": 5,
                "title": "Wait for Processing and Decision",
                "description": "Track your application and prepare for the outcome.",
                "items": [
                    "Processing times vary (check current estimates)",
                    "Track application status online",
                    "Prepare for possible interview",
                    "If approved: collect visa/passport",
                    "If refused: review reasons and consider appeal"
                ]
            }
        ]
    
    def generate_checklist(self, output_format: str = "text") -> str:
        """
        Generate the checklist in the specified format.
        
        Args:
            output_format (str): Desired output format ('text' or 'json')
            
        Returns:
            str: The generated checklist in requested format
            
        Raises:
            ValueError: If invalid output format is provided
        """
        if output_format not in ["text", "json"]:
            raise ValueError("Invalid output format. Choose 'text' or 'json'.")
            
        if output_format == "json":
            return json.dumps(self.steps, indent=2)
        else:
            checklist_text = "UK Visa Application Checklist for South Africans\n"
            checklist_text += "=" * 50 + "\n\n"
            checklist_text += "Based on the 5-step process from ContactTP.co.za\n\n"
            
            for step in self.steps:
                checklist_text += f"Step {step['step']}: {step['title']}\n"
                checklist_text += f"{step['description']}\n"
                checklist_text += "Required Actions:\n"
                for i, item in enumerate(step['items'], 1):
                    checklist_text += f"  {i}. {item}\n"
                checklist_text += "\n"
            
            return checklist_text
    
    def get_step_details(self, step_number: int) -> Dict:
        """
        Get details for a specific step.
        
        Args:
            step_number (int): Step number (1-5)
            
        Returns:
            Dict: Step details
            
        Raises:
            ValueError: If step number is invalid
        """
        if step_number < 1 or step_number > 5:
            raise ValueError("Step number must be between 1 and 5")
        return self.steps[step_number - 1]
    
    def add_custom_item(self, step_number: int, item: str) -> None:
        """
        Add a custom item to a specific step's checklist.
        
        Args:
            step_number (int): Step number (1-5)
            item (str): Custom item to add
            
        Raises:
            ValueError: If step number is invalid
        """
        if step_number < 1 or step_number > 5:
            raise ValueError("Step number must be between 1 and 5")
        self.steps[step_number - 1]['items'].append(item)


# Example usage
if __name__ == "__main__":
    try:
        generator = UKVisaChecklistGenerator()
        
        # Generate text checklist
        print(generator.generate_checklist())
        
        # Alternatively generate JSON
        # print(generator.generate_checklist("json"))
        
        # Example of adding a custom item
        generator.add_custom_item(1, "Consult with immigration expert if unsure")
        
        # Get details for a specific step
        step_3 = generator.get_step_details(3)
        print(f"\nDetails for Step 3: {step_3['title']}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
