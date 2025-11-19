"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: What are the steps to apply for Spanish nationality, and what specific requirements must I meet based on residency or marriage?
Generated: DETERMINISTIC_fe08bcad1f7458fc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to provide steps and requirements to apply for Spanish nationality.
The program is structured as a function-based design to ensure clarity and modularity.
"""

def spanish_nationality_info():
    """
    Provides information about the steps to apply for Spanish nationality
    and the specific requirements based on residency or marriage.
    Returns:
        dict: A dictionary containing information about the process and requirements.
    """
    try:
        # General steps for applying for Spanish nationality
        steps = [
            "Step 1: Gather required documents such as passport, proof of residency, marriage certificate (if applicable), etc.",
            "Step 2: Obtain and fill out the Spanish nationality application form.",
            "Step 3: Submit the application form and accompanying documents to the relevant government office.",
            "Step 4: Pay the application fee (if applicable).",
            "Step 5: Attend an interview or fulfill additional requirements (e.g., language test, cultural knowledge test).",
            "Step 6: Wait for the decision from the Spanish authorities."
        ]

        # Requirements based on residency
        residency_requirements = {
            "Standard Residency": "You must have legally resided in Spain for at least 10 years.",
            "Reduced Residency Periods": [
                "5 years for refugees.",
                "2 years for citizens from Ibero-American countries, Andorra, Philippines, Equatorial Guinea, or Sephardic Jews.",
                "1 year for individuals born in Spain, married to a Spanish citizen, widowed from a Spanish spouse, or those who did not exercise their right to apply for nationality after being under Spanish guardianship."
            ]
        }

        # Requirements based on marriage
        marriage_requirements = [
            "You must have been married to a Spanish citizen for at least 1 year.",
            "You must prove continuous cohabitation during the marriage.",
            "You must meet the residency requirement: 1 year of legal residency in Spain."
        ]

        # Return the compiled information in a structured format
        return {
            "Steps": steps,
            "Requirements": {
                "Residency": residency_requirements,
                "Marriage": marriage_requirements
            }
        }

    except Exception as e:
        # Handle any unexpected errors
        return {"Error": f"An unexpected error occurred: {str(e)}"}


def display_nationality_info():
    """
    Fetches and displays the Spanish nationality application information
    in a user-friendly format.
    """
    try:
        # Get the nationality information
        info = spanish_nationality_info()

        # Display the steps to apply
        print("Steps to Apply for Spanish Nationality:")
        for step in info["Steps"]:
            print(f"- {step}")

        # Display the requirements based on residency
        print("\nRequirements Based on Residency:")
        for key, value in info["Requirements"]["Residency"].items():
            if isinstance(value, list):
                print(f"{key}:")
                for item in value:
                    print(f"  - {item}")
            else:
                print(f"{key}: {value}")

        # Display the requirements based on marriage
        print("\nRequirements Based on Marriage:")
        for requirement in info["Requirements"]["Marriage"]:
            print(f"- {requirement}")

    except Exception as e:
        # Graceful error handling in case of display issues
        print(f"An error occurred while displaying nationality information: {str(e)}")


if __name__ == "__main__":
    """
    Main function to execute the program. 
    This ensures the above functions run only when the file is executed directly.
    """
    display_nationality_info()
```
