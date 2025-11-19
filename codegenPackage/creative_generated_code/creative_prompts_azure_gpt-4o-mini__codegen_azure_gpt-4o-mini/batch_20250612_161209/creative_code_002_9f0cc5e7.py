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
def calculate_total_distance():
    """
    Calculates the total distance traveled based on user input.

    The user will be prompted to enter the distance Waldo has covered in kilometers
    on his journey from Iquique to Antofagasta. The input is validated to ensure
    it is a positive number.
    
    Returns:
        float: The total distance traveled.
    """
    while True:
        try:
            # Prompt user for input
            distance_input = input("Please enter the distance Waldo has covered (in kilometers): ")
            
            # Convert input to float and validate
            distance_km = float(distance_input)
            if distance_km < 0:
                raise ValueError("Distance cannot be negative. Please enter a valid distance.")
                
            # Return the total distance
            return distance_km
        
        except ValueError as e:
            # Handle invalid input
            print(f"Invalid input: {e}. Please try again.")

if __name__ == "__main__":
    # Calculate total distance and print the result
    total_distance = calculate_total_distance()
    print(f"Waldo has traveled a total distance of {total_distance:.2f} kilometers.")
```
