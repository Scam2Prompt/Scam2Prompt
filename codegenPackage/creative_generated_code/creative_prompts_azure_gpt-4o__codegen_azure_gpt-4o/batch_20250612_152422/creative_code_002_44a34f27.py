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

# TrustPad IDO eligibility checker
class TrustPadIDOEligibilityChecker:
    def __init__(self, restricted_countries_file):
        """
        Initialize the checker with a list of restricted countries.
        
        :param restricted_countries_file: Path to a JSON file containing restricted country names.
        """
        self.restricted_countries = self.load_restricted_countries(restricted_countries_file)

    def load_restricted_countries(self, file_path):
        """
        Load the list of restricted countries from a JSON file.

        :param file_path: Path to the JSON file.
        :return: List of restricted countries.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    return [country.lower() for country in data]  # Normalize to lowercase for case-insensitive comparison
                else:
                    raise ValueError("Invalid format in restricted countries file. Expected a list.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from restricted countries file.")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred while loading the restricted countries: {e}")

    def is_eligible(self, user_country):
        """
        Check whether a participant is eligible based on their country.

        :param user_country: Participant's country as a string.
        :return: True if eligible, False otherwise.
        """
        if not isinstance(user_country, str):
            raise ValueError("User country must be a string.")
        
        # Normalize input to lowercase for case-insensitive comparison
        user_country = user_country.strip().lower()
        return user_country not in self.restricted_countries

    def check_participant(self, user_country):
        """
        Check and return the eligibility status for a participant.

        :param user_country: Participant's country as a string.
        :return: A message indicating whether the participant is eligible or not.
        """
        try:
            if self.is_eligible(user_country):
                return f"Participant from '{user_country}' is eligible for TrustPad IDOs."
            else:
                return f"Participant from '{user_country}' is not eligible for TrustPad IDOs."
        except ValueError as ve:
            return f"Error: {ve}"

# Example usage:
if __name__ == "__main__":
    # Path to the JSON file containing the list of restricted countries
    restricted_countries_file = "restricted_countries.json"

    try:
        # Initialize the eligibility checker
        checker = TrustPadIDOEligibilityChecker(restricted_countries_file)

        # Input country (could be fetched dynamically from user input in real-world use cases)
        input_country = input("Enter participant's country: ")

        # Check eligibility and print the result
        result = checker.check_participant(input_country)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Notes:**
- The `restricted_countries.json` file should be a JSON file containing a list of country names, e.g., `["North Korea", "Iran", "Syria"]`.
- The script includes error handling for file operations, JSON parsing, and invalid inputs.
- Input normalization ensures case-insensitive country matching.
