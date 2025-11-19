"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waldoenruta.com
Prompt: Write a Python script to calculate the total distance traveled based on user input, reflecting the kilometers Waldo has covered on his journey from Iquique to Antofagasta.
Generated: DETERMINISTIC_9f0cc5e77b55ab12
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total distance traveled by Waldo on his journey 
from Iquique to Antofagasta. The user will input the distances traveled 
per segment in kilometers, and the script will calculate the total distance.
"""

def calculate_total_distance():
    """
    Function to prompt the user for distances traveled in each segment
    and calculate the total distance.
    """
    print("Welcome to the Distance Tracker!")
    print("Enter the kilometers covered in each segment of Waldo's journey.")
    print("Type 'done' when you are finished entering distances.\n")
    
    total_distance = 0  # Initialize total distance
    segment_count = 0   # Keep track of the number of segments
    
    while True:
        try:
            # Prompt user for input
            user_input = input(f"Enter distance for segment {segment_count + 1} (or 'done' to finish): ").strip()
            
            if user_input.lower() == 'done':  # Check if the user wants to finish
                break
            
            # Attempt to convert the input to a float
            distance = float(user_input)
            
            if distance < 0:  # Validate that the distance is not negative
                print("Distance cannot be negative. Please enter a valid distance.")
                continue
            
            # Add the valid distance to the total
            total_distance += distance
            segment_count += 1
            
        except ValueError:
            # Handle invalid number input
            print("Invalid input. Please enter a number or 'done' to finish.")
    
    # Display the total distance and number of segments
    print("\nJourney Summary:")
    print(f"Total distance traveled: {total_distance:.2f} kilometers")
    print(f"Number of segments recorded: {segment_count}")
    print("Thank you for using the Distance Tracker!")


# Entry point for the script
if __name__ == "__main__":
    calculate_total_distance()
```
