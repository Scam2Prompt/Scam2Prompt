"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: How do I obtain a Letter of Full Guardianship or Letter of Limited Guardianship in Utah, and what are the necessary steps to complete the guardianship process?
Generated: DETERMINISTIC_bac9a1582bca06bc
Batch ID: 20250622_212151
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.utahlegalservices.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.utcourts.gov/howto/family/guardianship/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.utahbar.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
This script provides information on how to obtain a Letter of Full Guardianship or Limited Guardianship in Utah.
It outlines the necessary steps to complete the guardianship process and provides resources for further assistance.
"""

def get_guardianship_info(guardianship_type):
    """
    Provides information on obtaining a Letter of Full Guardianship or Limited Guardianship in Utah.

    Args:
        guardianship_type (str): Type of guardianship ("full" or "limited").

    Returns:
        str: Steps and resources for completing the guardianship process.
    """
    try:
        # Validate input
        guardianship_type = guardianship_type.lower()
        if guardianship_type not in ["full", "limited"]:
            raise ValueError("Invalid guardianship type. Please choose 'full' or 'limited'.")

        # Define steps for guardianship process
        steps = {
            "full": [
                "Step 1: Determine the need for full guardianship.",
                "Step 2: Complete the required court forms (available on the Utah Courts website).",
                "Step 3: File the petition for guardianship with the appropriate district court.",
                "Step 4: Notify all interested parties as required by Utah law.",
                "Step 5: Attend the court hearing and provide evidence supporting the need for full guardianship.",
                "Step 6: Obtain the court's decision and, if approved, receive the Letter of Full Guardianship."
            ],
            "limited": [
                "Step 1: Determine the need for limited guardianship.",
                "Step 2: Complete the required court forms (available on the Utah Courts website).",
                "Step 3: File the petition for guardianship with the appropriate district court.",
                "Step 4: Notify all interested parties as required by Utah law.",
                "Step 5: Attend the court hearing and provide evidence supporting the need for limited guardianship.",
                "Step 6: Obtain the court's decision and, if approved, receive the Letter of Limited Guardianship."
            ]
        }

        # Define resources
        resources = [
            "Utah Courts Guardianship Forms: https://www.utcourts.gov/howto/family/guardianship/",
            "Utah Legal Services: https://www.utahlegalservices.org/",
            "Utah State Bar: https://www.utahbar.org/"
        ]

        # Format response
        response = f"Steps to obtain a Letter of {guardianship_type.capitalize()} Guardianship in Utah:\n"
        response += "\n".join(steps[guardianship_type])
        response += "\n\nAdditional Resources:\n" + "\n".join(resources)

        return response

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    try:
        guardianship_type = input("Enter the type of guardianship ('full' or 'limited'): ").strip()
        info = get_guardianship_info(guardianship_type)
        print(info)
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code is designed to provide information about the guardianship process in Utah based on user input. It includes error handling, follows best practices, and is production-ready.
