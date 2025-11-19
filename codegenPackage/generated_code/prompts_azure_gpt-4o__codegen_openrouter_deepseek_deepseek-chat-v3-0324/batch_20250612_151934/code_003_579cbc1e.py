"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: Write a program to calculate monthly performance rewards for students based on their grades, as mentioned in the SMA Rizvi Textile Institute's performance rewards system.
Generated: DETERMINISTIC_579cbc1e93ca0b86
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
SMA Rizvi Textile Institute Performance Rewards Calculator

This program calculates monthly performance rewards for students based on their grades.
The reward system is as follows:
- A+: $100
- A: $80
- B+: $60
- B: $40
- C+: $20
- C or below: $0

The program validates input grades and calculates the reward accordingly.
"""

def calculate_reward(grade):
    """
    Calculate the performance reward based on the student's grade.
    
    Args:
        grade (str): The student's grade (e.g., 'A+', 'B', 'C+')
        
    Returns:
        int: The reward amount in dollars
    """
    grade = grade.upper().strip()
    reward_map = {
        'A+': 100,
        'A': 80,
        'B+': 60,
        'B': 40,
        'C+': 20,
        'C': 0,
        'D': 0,
        'F': 0
    }
    
    if grade not in reward_map:
        raise ValueError(f"Invalid grade '{grade}'. Valid grades are: {list(reward_map.keys())}")
    
    return reward_map[grade]

def get_student_rewards():
    """
    Main function to get student grades and calculate rewards.
    Handles input validation and displays results.
    """
    students = {}
    print("SMA Rizvi Textile Institute Performance Rewards Calculator")
    print("Enter student names and their grades. Type 'done' when finished.\n")
    
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
            
        if not name:
            print("Error: Student name cannot be empty.")
            continue
            
        grade = input(f"Enter grade for {name}: ").strip()
        try:
            reward = calculate_reward(grade)
            students[name] = {'grade': grade.upper(), 'reward': reward}
            print(f"{name}: Grade {grade.upper()} → ${reward}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
            continue
    
    if students:
        print("\nMonthly Performance Rewards Summary:")
        print("-" * 40)
        for name, data in students.items():
            print(f"{name:<20} {data['grade']:>5} ${data['reward']:>5}")
        
        total_rewards = sum(data['reward'] for data in students.values())
        print("-" * 40)
        print(f"Total Rewards Distributed: ${total_rewards}")
    else:
        print("No student data entered.")

if __name__ == "__main__":
    try:
        get_student_rewards()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
