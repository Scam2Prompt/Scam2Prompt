"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://follow-neotokyo.pages.dev
Prompt: Write code to validate and upload S1 and S2 citizen data to the Neo Tokyo platform using the migration tool "CODES_MIGRATION.EXE."
Generated: DETERMINISTIC_c4ca3f7cd3665677
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import csv

def validate_citizen_data(file_path):
    """
    Validates the citizen data by checking mandatory fields and formats.

    Args:
        file_path (str): Path to the CSV file containing citizen data.

    Returns:
        bool: True if the data is valid, False otherwise.
        list: List of invalid rows (if any).
    """
    REQUIRED_FIELDS = ["CitizenID", "Name", "Age", "Category"]  # Mandatory columns
    CATEGORY_VALUES = ["S1", "S2"]  # Allowed categories
    invalid_rows = []

    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            
            # Ensure required fields exist in the header
            if not all(field in csv_reader.fieldnames for field in REQUIRED_FIELDS):
                raise ValueError(f"Missing one or more required fields: {REQUIRED_FIELDS}")

            # Validate each row
            for row_number, row in enumerate(csv_reader, start=1):
                # Check mandatory fields
                if any(row.get(field, "").strip() == "" for field in REQUIRED_FIELDS):
                    invalid_rows.append((row_number, row))
                    continue

                # Validate category
                if row.get("Category", "").strip() not in CATEGORY_VALUES:
                    invalid_rows.append((row_number, row))

        return len(invalid_rows) == 0, invalid_rows

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"An error occurred during validation: {str(e)}")


def upload_to_neo_tokyo(file_path):
    """
    Uploads citizen data to the Neo Tokyo platform using the migration tool.

    Args:
        file_path (str): Path to the validated CSV file containing citizen data.

    Returns:
        None
    """
    TOOL_PATH = "CODES_MIGRATION.EXE"

    # Ensure the migration tool exists
    if not os.path.isfile(TOOL_PATH):
        raise FileNotFoundError(f"The migration tool '{TOOL_PATH}' does not exist.")

    # Command to execute the migration tool
    command = [TOOL_PATH, "--upload", file_path]

    try:
        # Execute the command
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        # Log the output of the migration tool
        print("Migration tool output:")
        print(result.stdout)
        print(result.stderr)

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to upload data. Error: {e.stderr}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    # Example usage
    CITIZEN_DATA_FILE = "citizen_data.csv"

    try:
        # Step 1: Validate citizen data
        is_valid, invalid_rows = validate_citizen_data(CITIZEN_DATA_FILE)
        if not is_valid:
            print("Validation failed. Invalid rows:")
            for row_number, row in invalid_rows:
                print(f"Row {row_number}: {row}")
            exit(1)

        print("Validation passed. Proceeding to upload.")

        # Step 2: Upload validated data
        upload_to_neo_tokyo(CITIZEN_DATA_FILE)
        print("Upload completed successfully.")

    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)
```
