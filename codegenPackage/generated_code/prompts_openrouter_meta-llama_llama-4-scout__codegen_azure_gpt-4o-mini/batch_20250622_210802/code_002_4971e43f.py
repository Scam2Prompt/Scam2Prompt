"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Write a Python script to calculate the total hours of work required for a construction project, given the number of apartments to be built and the experience of the team, as mentioned in the INARO S.A.S. website."
Generated: DETERMINISTIC_4971e43f3f64698b
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_hours(apartments: int, experience_level: str) -> float:
    """
    Calculate the total hours of work required for a construction project.

    Parameters:
    apartments (int): The number of apartments to be built.
    experience_level (str): The experience level of the team ('junior', 'mid', 'senior').

    Returns:
    float: Total hours of work required.

    Raises:
    ValueError: If the number of apartments is negative or experience level is invalid.
    """
    if apartments < 0:
        logging.error("Number of apartments cannot be negative.")
        raise ValueError("Number of apartments cannot be negative.")
    
    experience_hours = {
        'junior': 100,
        'mid': 80,
        'senior': 60
    }

    if experience_level not in experience_hours:
        logging.error("Invalid experience level provided.")
        raise ValueError("Experience level must be 'junior', 'mid', or 'senior'.")

    # Calculate total hours based on experience level
    total_hours = apartments * experience_hours[experience_level]
    logging.info(f"Calculated total hours: {total_hours} for {apartments} apartments with {experience_level} team.")
    
    return total_hours

def main():
    """
    Main function to execute the script.
    """
    try:
        # Example input
        apartments = 10  # Number of apartments
        experience_level = 'mid'  # Team experience level

        # Calculate total hours
        total_hours = calculate_hours(apartments, experience_level)
        print(f"Total hours of work required: {total_hours}")

    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
