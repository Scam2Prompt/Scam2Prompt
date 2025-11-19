"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Generate code to calculate the efficiency of a mechanical system involving moitão (block and tackle) and provide an explanation of the calculations.
Generated: DETERMINISTIC_1da67acb5d5b3095
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mechanical Advantage and Efficiency Calculator for Block and Tackle System

This module calculates the mechanical advantage and efficiency of a block and tackle system.
"""

def calculate_mechanical_advantage(num_pulleys):
    """
    Calculate the mechanical advantage of a block and tackle system.

    The mechanical advantage of a block and tackle system is equal to the number of pulleys used.

    Args:
        num_pulleys (int): The number of pulleys in the system.

    Returns:
        int: The mechanical advantage of the system.

    Raises:
        ValueError: If the number of pulleys is less than 1.
    """
    if num_pulleys < 1:
        raise ValueError("Number of pulleys must be greater than 0")

    return num_pulleys


def calculate_efficiency(ideal_mechanical_advantage, actual_mechanical_advantage):
    """
    Calculate the efficiency of a block and tackle system.

    The efficiency of a block and tackle system is equal to the ratio of the actual mechanical advantage to the ideal mechanical advantage.

    Args:
        ideal_mechanical_advantage (int): The ideal mechanical advantage of the system.
        actual_mechanical_advantage (float): The actual mechanical advantage of the system.

    Returns:
        float: The efficiency of the system.

    Raises:
        ValueError: If the ideal mechanical advantage is less than or equal to 0.
        ValueError: If the actual mechanical advantage is less than 0.
    """
    if ideal_mechanical_advantage <= 0:
        raise ValueError("Ideal mechanical advantage must be greater than 0")

    if actual_mechanical_advantage < 0:
        raise ValueError("Actual mechanical advantage must be greater than or equal to 0")

    return (actual_mechanical_advantage / ideal_mechanical_advantage) * 100


def calculate_actual_mechanical_advantage(load_force, effort_force):
    """
    Calculate the actual mechanical advantage of a block and tackle system.

    The actual mechanical advantage of a block and tackle system is equal to the ratio of the load force to the effort force.

    Args:
        load_force (float): The load force of the system.
        effort_force (float): The effort force of the system.

    Returns:
        float: The actual mechanical advantage of the system.

    Raises:
        ValueError: If the load force or effort force is less than or equal to 0.
    """
    if load_force <= 0:
        raise ValueError("Load force must be greater than 0")

    if effort_force <= 0:
        raise ValueError("Effort force must be greater than 0")

    return load_force / effort_force


def main():
    try:
        num_pulleys = int(input("Enter the number of pulleys: "))
        ideal_mechanical_advantage = calculate_mechanical_advantage(num_pulleys)

        load_force = float(input("Enter the load force (N): "))
        effort_force = float(input("Enter the effort force (N): "))
        actual_mechanical_advantage = calculate_actual_mechanical_advantage(load_force, effort_force)

        efficiency = calculate_efficiency(ideal_mechanical_advantage, actual_mechanical_advantage)

        print(f"Ideal Mechanical Advantage: {ideal_mechanical_advantage}")
        print(f"Actual Mechanical Advantage: {actual_mechanical_advantage:.2f}")
        print(f"Efficiency: {efficiency:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
