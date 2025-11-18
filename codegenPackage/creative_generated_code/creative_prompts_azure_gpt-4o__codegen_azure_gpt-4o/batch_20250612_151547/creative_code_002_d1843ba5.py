"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Generate code to automate the registration process for a gliding club, including handling parental authorization forms and medical certificates.
Generated: DETERMINISTIC_d1843ba53194a4da
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import datetime

class GlidingClubRegistration:
    """
    Class to handle the registration process for a gliding club.
    """

    def __init__(self, data_directory="registrations"):
        """
        Initializes the registration system.

        Args:
          data_directory (str): Directory to store registration data.
        """
        self.data_directory = data_directory
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

    def collect_registration_data(self):
        """
        Collects registration data from the user.
        
        Returns:
          dict: A dictionary containing registration data.
        """
        print("=== Gliding Club Registration ===")
        registration_data = {}

        # Basic Information
        registration_data["first_name"] = input("First Name: ").strip()
        registration_data["last_name"] = input("Last Name: ").strip()
        registration_data["age"] = int(input("Age: ").strip())
        registration_data["email"] = input("Email Address: ").strip()
        registration_data["phone"] = input("Phone Number: ").strip()

        # Parental Authorization (if user is under 18)
        if registration_data["age"] < 18:
            print("\nParental Authorization Required:")
            registration_data["parent_name"] = input("Parent/Guardian Name: ").strip()
            registration_data["parent_phone"] = input("Parent/Guardian Phone: ").strip()
            registration_data["parent_authorization"] = input("Parent Authorization Form Path: ").strip()
            if not os.path.exists(registration_data["parent_authorization"]):
                print("Error: Parental Authorization Form not found.")
                raise FileNotFoundError("Parental Authorization Form is missing.")

        # Medical Certificate
        print("\nMedical Certificate Required:")
        registration_data["medical_certificate"] = input("Medical Certificate Path: ").strip()
        if not os.path.exists(registration_data["medical_certificate"]):
            print("Error: Medical Certificate not found.")
            raise FileNotFoundError("Medical Certificate is missing.")

        return registration_data

    def save_registration(self, registration_data):
        """
        Saves registration data to a file.

        Args:
          registration_data (dict): Registration data to save.
        """
        file_name = f"{registration_data['first_name']}_{registration_data['last_name']}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        file_path = os.path.join(self.data_directory, file_name)

        with open(file_path, "w") as file:
            json.dump(registration_data, file, indent=4)
        
        print(f"\nRegistration successfully saved to {file_path}")

    def run(self):
        """
        Main method to run the registration process.
        """
        try:
            registration_data = self.collect_registration_data()
            self.save_registration(registration_data)
        except FileNotFoundError as e:
            print(f"\nRegistration failed: {e}")
        except ValueError:
            print("\nError: Invalid input. Please try again.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    registration_system = GlidingClubRegistration()
    registration_system.run()
```
