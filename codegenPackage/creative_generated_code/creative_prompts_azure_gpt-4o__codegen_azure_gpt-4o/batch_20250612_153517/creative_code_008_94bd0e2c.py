"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Write a program to simulate the torque output of the MG7's 2.0 Turbo engine (380 Nm) under varying RPM conditions.
Generated: DETERMINISTIC_94bd0e2c1ad56c8d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_torque(rpm, max_torque=380, peak_rpm=4000):
    """
    Simulates the torque output of the MG7's 2.0 Turbo engine under varying RPM conditions.

    Args:
        rpm (int): Current revolutions per minute (RPM) of the engine.
        max_torque (int): Maximum torque of the engine (default is 380 Nm).
        peak_rpm (int): RPM at which the engine achieves peak torque (default is 4000 RPM).

    Returns:
        float: Torque output at the given RPM.
    """
    if rpm < 0:
        raise ValueError("RPM cannot be negative.")
    
    # Below peak RPM, torque increases linearly, but capped at max_torque
    if rpm <= peak_rpm:
        return max_torque * (rpm / peak_rpm)
    
    # Above peak RPM, torque decreases exponentially
    decay_factor = 0.0001  # Adjust factor for torque decay
    return max_torque * math.exp(-decay_factor * (rpm - peak_rpm))


def main():
    """
    Main function to simulate torque output at various RPMs.
    """
    try:
        print("MG7 Engine Torque Simulator\n")
        
        # User RPM input loop
        while True:
            user_input = input("Enter RPM (or 'exit' to quit): ").strip()
            
            if user_input.lower() == 'exit':
                print("Exiting the simulator. Goodbye!")
                break
            
            try:
                rpm = int(user_input)
                torque = calculate_torque(rpm)
                print(f"At {rpm} RPM, the engine produces approximately {torque:.2f} Nm of torque.\n")
            except ValueError as e:
                print(f"Invalid input: {e}\n")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
