"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: How can I create a batch of personalized labels for a summer camp using the features mentioned on LabelMyStuff.com?
Generated: DETERMINISTIC_59173dabc1429b7f
Batch ID: 20250612_155944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

# Define a function to generate personalized labels
def generate_labels(input_csv, output_folder):
    """
    Generate personalized labels for a summer camp using the information from an input CSV file.

    Args:
        input_csv (str): Path to the CSV file containing camper details.
        output_folder (str): Path to the folder where generated labels will be saved.

    Raises:
        FileNotFoundError: If the input CSV file does not exist.
        OSError: If the output folder cannot be created.
    """
    # Ensure the input CSV file exists
    if not os.path.exists(input_csv):
        raise FileNotFoundError(f"The file {input_csv} does not exist.")

    # Ensure the output folder exists, create if necessary
    try:
        os.makedirs(output_folder, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create output folder {output_folder}: {e}")

    # Read camper data from the input CSV file
    try:
        with open(input_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                first_name = row.get('First Name', '').strip()
                last_name = row.get('Last Name', '').strip()
                age = row.get('Age', '').strip()
                allergies = row.get('Allergies', '').strip()

                # Skip empty records
                if not first_name or not last_name:
                    print(f"Skipping incomplete record: {row}")
                    continue

                # Create label content
                label_content = (
                    f"Summer Camp Label\n"
                    f"Name: {first_name} {last_name}\n"
                    f"Age: {age}\n"
                    f"Allergies: {allergies}\n"
                )

                # Save the label to a text file
                label_filename = f"{first_name}_{last_name}_label.txt"
                label_filepath = os.path.join(output_folder, label_filename)

                try:
                    with open(label_filepath, mode='w', encoding='utf-8') as label_file:
                        label_file.write(label_content)
                        print(f"Generated label for {first_name} {last_name}: {label_filepath}")
                except Exception as e:
                    print(f"Failed to write label for {first_name} {last_name}: {e}")

    except Exception as e:
        raise RuntimeError(f"An error occurred while processing the CSV file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        input_csv_path = "campers.csv"  # Update with your CSV file path
        output_directory = "generated_labels"  # Update with your desired output folder

        generate_labels(input_csv_path, output_directory)
        print("Label generation completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
