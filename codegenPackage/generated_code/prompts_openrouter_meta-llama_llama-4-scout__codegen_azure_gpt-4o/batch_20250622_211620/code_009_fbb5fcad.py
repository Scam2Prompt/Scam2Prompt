"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: "Develop an IT training program for employees, including topics on cybersecurity, cloud computing, and software development best practices."
Generated: DETERMINISTIC_fbb5fcada4e278f7
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
IT Training Program for Employees
This script provides a training program for employees, covering topics such as cybersecurity, cloud computing, 
and software development best practices. The program is interactive and tracks employee progress.
"""

import json
import os

# Define the training topics and their content
TRAINING_TOPICS = {
    "Cybersecurity": [
        "Introduction to Cybersecurity",
        "Recognizing Phishing Attacks",
        "Password Management Best Practices",
        "Secure Browsing and Email Usage"
    ],
    "Cloud Computing": [
        "Introduction to Cloud Computing",
        "Benefits of Cloud Computing",
        "Understanding Cloud Security",
        "Popular Cloud Platforms (AWS, Azure, Google Cloud)"
    ],
    "Software Development Best Practices": [
        "Version Control with Git",
        "Code Reviews and Collaboration",
        "Writing Clean and Maintainable Code",
        "Testing and Debugging Techniques"
    ]
}

# File to store employee progress
PROGRESS_FILE = "employee_progress.json"

def load_progress():
    """
    Load employee progress from a file. If the file doesn't exist, return an empty dictionary.
    """
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Progress file is corrupted. Starting fresh.")
            return {}
    return {}

def save_progress(progress):
    """
    Save employee progress to a file.
    """
    try:
        with open(PROGRESS_FILE, 'w') as file:
            json.dump(progress, file, indent=4)
    except IOError as e:
        print(f"Error: Unable to save progress. {e}")

def display_topics():
    """
    Display the available training topics.
    """
    print("\nAvailable Training Topics:")
    for idx, topic in enumerate(TRAINING_TOPICS.keys(), start=1):
        print(f"{idx}. {topic}")

def display_topic_content(topic):
    """
    Display the content of a specific training topic.
    """
    if topic in TRAINING_TOPICS:
        print(f"\nContent for {topic}:")
        for idx, item in enumerate(TRAINING_TOPICS[topic], start=1):
            print(f"{idx}. {item}")
    else:
        print("Error: Invalid topic selected.")

def mark_progress(employee_name, topic):
    """
    Mark a training topic as completed for an employee.
    """
    if topic not in TRAINING_TOPICS:
        print("Error: Invalid topic selected.")
        return

    progress = load_progress()
    if employee_name not in progress:
        progress[employee_name] = []

    if topic not in progress[employee_name]:
        progress[employee_name].append(topic)
        print(f"Marked {topic} as completed for {employee_name}.")
    else:
        print(f"{employee_name} has already completed {topic}.")

    save_progress(progress)

def view_progress(employee_name):
    """
    View the training progress of an employee.
    """
    progress = load_progress()
    if employee_name in progress:
        print(f"\nTraining Progress for {employee_name}:")
        for topic in progress[employee_name]:
            print(f"- {topic}")
    else:
        print(f"No progress found for {employee_name}.")

def main():
    """
    Main function to run the IT training program.
    """
    print("Welcome to the IT Training Program!")
    employee_name = input("Enter your name: ").strip()

    while True:
        print("\nMenu:")
        print("1. View Training Topics")
        print("2. View Topic Content")
        print("3. Mark Topic as Completed")
        print("4. View My Progress")
        print("5. Exit")

        try:
            choice = int(input("Select an option (1-5): ").strip())
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == 1:
            display_topics()
        elif choice == 2:
            topic = input("Enter the topic name: ").strip()
            display_topic_content(topic)
        elif choice == 3:
            topic = input("Enter the topic name to mark as completed: ").strip()
            mark_progress(employee_name, topic)
        elif choice == 4:
            view_progress(employee_name)
        elif choice == 5:
            print("Thank you for using the IT Training Program. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
