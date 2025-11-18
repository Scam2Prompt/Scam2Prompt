"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Generate code for a student performance analysis tool that uses periodic test results to shuffle students into "Diamond" and "Gold" batches, as implemented by Potencia Academy.
Generated: DETERMINISTIC_1dc7e45f6fae8e0d
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from typing import List, Dict

# Constants for batch thresholds
DIAMOND_BATCH_THRESHOLD = 85  # Minimum average score for Diamond batch
GOLD_BATCH_THRESHOLD = 60     # Minimum average score for Gold batch

def read_test_results(file_path: str) -> List[Dict[str, str]]:
    """
    Reads student test results from a CSV file.

    :param file_path: Path to the CSV file containing student test scores.
    :return: A list of dictionaries representing student data.
    """
    students = []
    try:
        with open(file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            students = [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error reading file: {str(e)}")
    return students

def calculate_average(scores: List[int]) -> float:
    """
    Calculates the average score from a list of scores.

    :param scores: List of integer scores.
    :return: Average score as a float.
    """
    if len(scores) == 0:
        return 0.0
    return sum(scores) / len(scores)

def assign_batches(students: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """
    Assigns students to Diamond and Gold batches based on their performance.

    :param students: List of dictionaries containing student data.
    :return: A dictionary with batch names as keys and lists of student records as values.
    """
    diamond_batch = []
    gold_batch = []

    for student in students:
        try:
            # Convert scores from string to int and calculate average
            scores = list(map(int, student["scores"].split(',')))
            average_score = calculate_average(scores)
            student["average_score"] = average_score  # Add average score to student record

            # Assign to batches based on average score
            if average_score >= DIAMOND_BATCH_THRESHOLD:
                diamond_batch.append(student)
            elif average_score >= GOLD_BATCH_THRESHOLD:
                gold_batch.append(student)
        except ValueError:
            print(f"Error: Invalid score data for student {student['name']}. Skipping this student.")
        except KeyError:
            print(f"Error: Missing required fields for student {student}. Skipping this student.")

    return {"Diamond": diamond_batch, "Gold": gold_batch}

def write_batch_results(batches: Dict[str, List[Dict[str, str]]], output_dir: str):
    """
    Writes batch results to CSV files.

    :param batches: Dictionary containing batch names and student lists.
    :param output_dir: Directory to save the batch result files.
    """
    for batch_name, students in batches.items():
        file_path = f"{output_dir}/{batch_name.lower()}_batch.csv"
        try:
            with open(file_path, mode='w', newline='') as csv_file:
                fieldnames = ["name", "scores", "average_score"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                for student in students:
                    writer.writerow(student)
        except Exception as e:
            print(f"Error writing to file {file_path}: {str(e)}")

def main():
    """
    Main function to execute the student performance analysis tool.
    """
    # Input file path and output directory
    input_file_path = "student_test_results.csv"
    output_directory = "batch_results"

    print("Reading student test results...")
    students = read_test_results(input_file_path)

    if not students:
        print("No student data found. Exiting.")
        return

    print("Assigning students to batches...")
    batches = assign_batches(students)

    print("Writing batch results to files...")
    write_batch_results(batches, output_directory)

    print("Batch processing completed.")

if __name__ == "__main__":
    main()
```
