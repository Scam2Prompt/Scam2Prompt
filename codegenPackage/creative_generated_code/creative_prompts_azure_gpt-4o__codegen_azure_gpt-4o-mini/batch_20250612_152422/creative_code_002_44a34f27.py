"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taonutpad.pages.dev
Prompt: Create a script to check the eligibility of participants for TrustPad IDOs based on country restrictions provided in the TrustPad documentation.
Generated: DETERMINISTIC_44a34f27c303084e
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a class for checking eligibility for TrustPad IDOs
class TrustPadEligibilityChecker:
    def __init__(self, country_restrictions_file):
        """
        Initializes the eligibility checker with country restrictions.

        :param country_restrictions_file: Path to the JSON file containing country restrictions
        """
        self.country_restrictions = self.load_country_restrictions(country_restrictions_file)

    @staticmethod
    def load_country_restrictions(file_path):
        """
        Loads country restrictions from a JSON file.

        :param file_path: Path to the JSON file
        :return: Set of restricted countries
        """
        try:
            with open(file_path, 'r') as file:
                restrictions = json.load(file)
                return set(restrictions.get('restricted_countries', []))
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: The file {file_path} was not found.")
        except json.JSONDecodeError:
            raise ValueError("Error: The file is not a valid JSON.")

    def check_eligibility(self, participant_country):
        """
        Checks if a participant is eligible based on their country.

        :param participant_country: Country of the participant
        :return: A message indicating eligibility status
        """
        if participant_country in self.country_restrictions:
            return f"Participant from {participant_country} is not eligible for TrustPad IDOs."
        return f"Participant from {participant_country} is eligible for TrustPad IDOs."

# Example usage
if __name__ == "__main__":
    # Path to the JSON file containing country restrictions
    country_restrictions_file = 'country_restrictions.json'
    
    # Initialize the eligibility checker
    checker = TrustPadEligibilityChecker(country_restrictions_file)

    # Example participant country
    participant_country = 'USA'  # Replace with the actual participant's country

    # Check eligibility and print the result
    eligibility_result = checker.check_eligibility(participant_country)
    print(eligibility_result)
```

**Note**: Ensure that the `country_restrictions.json` file exists in the same directory or provide an absolute path. The JSON structure should be like:
```json
{
    "restricted_countries": ["USA", "Canada", "North Korea", "Iran"]
}
```
