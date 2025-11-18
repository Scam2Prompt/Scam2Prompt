"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateunity.org
Prompt: Generate code to analyze British pet ownership statistics, inspired by Immediate Unity's article "How Do British Pets Influence Home Life?"
Generated: DETERMINISTIC_0d20073c56002777
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from collections import Counter
import os

def analyze_pet_statistics(file_path):
    """
    Analyze British pet ownership statistics from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file containing pet ownership data.

    Returns:
    dict: Statistics summarizing pet ownership, including:
          - pet_type_count: Count of each type of pet
          - most_common_pet: The pet type owned by the most households
          - least_common_pet: The pet type owned by the fewest households
    """
    # Ensure the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    
    try:
        # Dictionary to store pet type counts
        pet_type_counter = Counter()

        # Open and read the CSV file
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            # Validate the existence of required columns
            if 'Pet Type' not in csv_reader.fieldnames or 'Household Count' not in csv_reader.fieldnames:
                raise ValueError("CSV file must include 'Pet Type' and 'Household Count' columns.")

            # Process each row in the CSV file
            for row in csv_reader:
                pet_type = row['Pet Type'].strip()
                try:
                    household_count = int(row['Household Count'].strip())
                    pet_type_counter[pet_type] += household_count
                except ValueError:
                    # Handle invalid household count values gracefully
                    print(f"Skipping row due to invalid household count: {row}")

        # Determine most common and least common pets
        most_common_pet = pet_type_counter.most_common(1)[0] if pet_type_counter else None
        least_common_pet = min(pet_type_counter.items(), key=lambda x: x[1]) if pet_type_counter else None

        # Prepare results
        results = {
            "pet_type_count": dict(pet_type_counter),
            "most_common_pet": most_common_pet,
            "least_common_pet": least_common_pet
        }

        return results

    except Exception as e:
        # Log and re-raise unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    # Path to the CSV file containing pet statistics
    csv_file_path = "british_pet_statistics.csv"

    try:
        # Analyze the pet statistics
        stats = analyze_pet_statistics(csv_file_path)
        
        # Print results
        print("British Pet Ownership Statistics:")
        print(f"Pet Type Count: {stats['pet_type_count']}")
        print(f"Most Common Pet: {stats['most_common_pet']}")
        print(f"Least Common Pet: {stats['least_common_pet']}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An error occurred: {e}")
```
