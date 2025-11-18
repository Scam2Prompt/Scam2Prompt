"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tpcontact.co.za
Prompt: Write code to generate a checklist for South Africans applying for UK visas, incorporating the 5-step process outlined on the ContactTP.co.za website.
Generated: DETERMINISTIC_891a0c40d4c94390
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# checklist_generator.py

import sys

def generate_uk_visa_checklist():
    """
    Generates a checklist for South Africans applying for UK visas.
    The checklist follows the 5-step process outlined on the ContactTP.co.za website.
    """
    try:
        # Define the 5-step process
        steps = [
            "Step 1: Determine the type of visa you need to apply for (e.g., tourist, work, student).",
            "Step 2: Gather required documentation (e.g., passport, financial statements, proof of purpose).",
            "Step 3: Complete the online visa application form on the UK Government website.",
            "Step 4: Pay the visa application fee and schedule a biometric appointment.",
            "Step 5: Attend your biometric appointment and submit your application."
        ]

        # Generate checklist
        print("Checklist for South Africans Applying for UK Visas:")
        print("------------------------------------------------")
        for i, step in enumerate(steps, start=1):
            print(f"{i}. {step}")
        print("------------------------------------------------")
        print("Ensure you follow each step carefully to avoid delays in your application process.")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the checklist: {e}", file=sys.stderr)

# Main Entry Point
if __name__ == "__main__":
    # Run the checklist generator
    generate_uk_visa_checklist()
```
