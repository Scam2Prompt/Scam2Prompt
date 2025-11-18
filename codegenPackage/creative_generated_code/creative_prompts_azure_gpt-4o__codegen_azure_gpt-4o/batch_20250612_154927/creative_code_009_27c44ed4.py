"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Write a script to analyze student performance data for technical programs such as "Mecatrónica Automotriz," using the educational focus described on the Instituto Pangoa site.
Generated: DETERMINISTIC_27c44ed47cdc7231
Batch ID: 20250612_154927
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

def load_student_data(file_path):
    """
    Load student performance data from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file containing student performance data.

    Returns:
        list[dict]: A list of dictionaries where each dictionary represents a student's data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    student_data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_data.append(row)
    except Exception as e:
        raise Exception(f"Error reading CSV file: {e}")
    
    return student_data


def calculate_statistics(student_data):
    """
    Calculate performance statistics for students.

    Parameters:
        student_data (list[dict]): A list of dictionaries containing student data.

    Returns:
        dict: A dictionary containing performance statistics.
    """
    program_stats = {}
    try:
        for student in student_data:
            program = student.get("Program", "").strip()
            grade = float(student.get("Grade", "0"))
            
            if program not in program_stats:
                program_stats[program] = {
                    "total_students": 0,
                    "total_grades": 0.0,
                    "highest_grade": float('-inf'),
                    "lowest_grade": float('inf'),
                }
            
            program_stats[program]["total_students"] += 1
            program_stats[program]["total_grades"] += grade
            program_stats[program]["highest_grade"] = max(
                program_stats[program]["highest_grade"], grade
            )
            program_stats[program]["lowest_grade"] = min(
                program_stats[program]["lowest_grade"], grade
            )

        # Compute average grades for each program
        for program in program_stats:
            stats = program_stats[program]
            stats["average_grade"] = (
                stats["total_grades"] / stats["total_students"]
                if stats["total_students"] > 0
                else 0.0
            )
    except Exception as e:
        raise Exception(f"Error calculating statistics: {e}")

    return program_stats


def display_statistics(statistics):
    """
    Display program performance statistics.

    Parameters:
        statistics (dict): A dictionary containing performance statistics for each program.
    """
    print("Performance Statistics:")
    print("-" * 30)
    for program, stats in statistics.items():
        print(f"Program: {program}")
        print(f"  Total Students: {stats['total_students']}")
        print(f"  Average Grade: {stats['average_grade']:.2f}")
        print(f"  Highest Grade: {stats['highest_grade']}")
        print(f"  Lowest Grade: {stats['lowest_grade']}")
        print("-" * 30)


def main():
    """
    Main function to load data, analyze statistics, and display the results.
    """
    # Path to the CSV file containing student performance data
    file_path = "student_performance.csv"

    try:
        # Load student performance data
        student_data = load_student_data(file_path)

        # Calculate statistics based on the loaded data
        statistics = calculate_statistics(student_data)

        # Display the calculated statistics
        display_statistics(statistics)
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
