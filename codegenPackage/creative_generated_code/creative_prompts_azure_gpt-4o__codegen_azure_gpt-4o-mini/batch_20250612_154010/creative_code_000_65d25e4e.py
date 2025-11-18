"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Write Python code to automate the process of registering psychologists for certifications and memberships based on the administrative guidelines provided by the Colegio de Psicólogos de Oruro.
Generated: DETERMINISTIC_65d25e4e6a880efc
Batch ID: 20250612_154010
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.colegiopsicologos.oruro.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import requests

class PsychologistRegistration:
    def __init__(self, api_url):
        self.api_url = api_url

    def register_psychologist(self, psychologist_data):
        """
        Registers a psychologist for certification and membership.

        Args:
            psychologist_data (dict): A dictionary containing psychologist's data.

        Returns:
            dict: Response from the registration API.
        """
        try:
            response = requests.post(f"{self.api_url}/register", json=psychologist_data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response data as a JSON object

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {"error": str(http_err)}

        except Exception as err:
            print(f"An error occurred: {err}")
            return {"error": str(err)}

    def load_psychologists_from_file(self, file_path):
        """
        Loads psychologist data from a JSON file.

        Args:
            file_path (str): The path to the JSON file containing psychologist data.

        Returns:
            list: A list of psychologist data dictionaries.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)

        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []

        except json.JSONDecodeError:
            print("Error decoding JSON from the file.")
            return []

    def register_multiple_psychologists(self, file_path):
        """
        Registers multiple psychologists by reading their data from a file.

        Args:
            file_path (str): The path to the JSON file with psychologist data.
        """
        psychologists = self.load_psychologists_from_file(file_path)
        for psych in psychologists:
            response = self.register_psychologist(psych)
            print(f"Registration response for {psych['name']}: {response}")


# Example usage:
if __name__ == "__main__":
    api_url = "https://api.colegiopsicologos.oruro.org"  # Replace with the actual API URL
    registration = PsychologistRegistration(api_url)
    
    # Assuming 'psychologists.json' contains the data for psychologists to register
    registration.register_multiple_psychologists('psychologists.json')
```

### Sample `psychologists.json` format:
```json
[
    {
        "name": "John Doe",
        "license_number": "PSY123456",
        "email": "john.doe@example.com",
        "specialty": "Clinical Psychology"
    },
    {
        "name": "Jane Smith",
        "license_number": "PSY654321",
        "email": "jane.smith@example.com",
        "specialty": "Educational Psychology"
    }
]
```

### Notes:
- Ensure that `requests` library is installed by running `pip install requests`.
- Update the `api_url` variable with the actual API endpoint provided by the Colegio de Psicólogos de Oruro.
- The JSON file should be structured correctly as shown above to avoid errors during loading.
