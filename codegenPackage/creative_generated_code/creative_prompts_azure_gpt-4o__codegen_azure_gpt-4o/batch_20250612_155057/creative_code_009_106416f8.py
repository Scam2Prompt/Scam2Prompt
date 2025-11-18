"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Write a function to integrate data portability features into an application using concepts from the Vana Network demo.
Generated: DETERMINISTIC_106416f831f877f9
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class DataPortability:
    """
    A class to handle data portability requests.
    Implements features inspired by the Vana Network demo.
    """

    def __init__(self, data_directory):
        """
        Initialize the DataPortability instance.
        
        Args:
            data_directory (str): Path to the directory where user data is stored.
        """
        self.data_directory = data_directory

    def export_user_data(self, user_id):
        """
        Export user data to a JSON file for portability.
        
        Args:
            user_id (str): Unique identifier for the user whose data needs to be exported.
        
        Returns:
            str: Path to the exported JSON file.
        """
        try:
            # Path to the user's data file
            user_data_file = os.path.join(self.data_directory, f"{user_id}.json")

            # Check if the user data file exists
            if not os.path.exists(user_data_file):
                raise FileNotFoundError(f"No data found for user: {user_id}")

            # Load user data from the file
            with open(user_data_file, 'r') as file:
                user_data = json.load(file)

            # Path for the exported file
            export_path = os.path.join(self.data_directory, f"{user_id}_exported.json")

            # Write user data to the export file
            with open(export_path, 'w') as export_file:
                json.dump(user_data, export_file, indent=4)

            return export_path

        except FileNotFoundError as fnf_error:
            # Handle missing user data file error
            print(f"Error: {fnf_error}")
            raise

        except json.JSONDecodeError as json_error:
            # Handle JSON parsing errors
            print(f"Error decoding JSON data: {json_error}")
            raise

        except Exception as e:
            # Catch-all for any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            raise

    def import_user_data(self, user_id, import_file_path):
        """
        Import user data from a JSON file into the application.
        
        Args:
            user_id (str): Unique identifier for the user whose data is being imported.
            import_file_path (str): Path to the JSON file containing user data to be imported.
        
        Returns:
            bool: True if the import was successful, False otherwise.
        """
        try:
            # Validate if the import file exists
            if not os.path.exists(import_file_path):
                raise FileNotFoundError(f"Import file not found: {import_file_path}")

            # Load user data from the import file
            with open(import_file_path, 'r') as import_file:
                user_data = json.load(import_file)

            # Validate the imported data (basic validation example)
            if not isinstance(user_data, dict) or 'user_id' not in user_data or user_data['user_id'] != user_id:
                raise ValueError("Invalid data format or mismatching user ID in import file.")

            # Save the imported data to the user's data file
            user_data_file = os.path.join(self.data_directory, f"{user_id}.json")
            with open(user_data_file, 'w') as file:
                json.dump(user_data, file, indent=4)

            return True

        except FileNotFoundError as fnf_error:
            # Handle missing import file error
            print(f"Error: {fnf_error}")
            raise

        except json.JSONDecodeError as json_error:
            # Handle JSON parsing errors
            print(f"Error decoding JSON data: {json_error}")
            raise

        except ValueError as value_error:
            # Handle validation errors
            print(f"Error validating imported data: {value_error}")
            raise

        except Exception as e:
            # Catch-all for any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            raise


# Example Usage:
# Initialize the DataPortability instance with a directory path
# portability = DataPortability(data_directory="./data")

# Export user data
# exported_file = portability.export_user_data(user_id="12345")
# print(f"User data exported to: {exported_file}")

# Import user data
# success = portability.import_user_data(user_id="12345", import_file_path="./data/12345_import.json")
# print(f"User data import successful: {success}")
```
