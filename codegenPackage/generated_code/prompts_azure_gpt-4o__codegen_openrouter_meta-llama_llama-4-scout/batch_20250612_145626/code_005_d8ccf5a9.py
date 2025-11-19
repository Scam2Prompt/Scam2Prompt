"""
Generated Code Metadata:
========================
Original URL: https://lover4d.site
Prompt: Write a Python script to calculate and display lottery predictions using metaphysical methods, as mentioned in the 4DLOVER website's prediksi section.
Generated: DETERMINISTIC_d8ccf5a96e9d2dd0
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import hashlib

def calculate_lottery_prediction(birth_date, name):
    """
    Calculates lottery prediction using metaphysical methods.

    Parameters:
    birth_date (str): User's birth date in YYYYMMDD format.
    name (str): User's full name.

    Returns:
    list: A list of 4 predicted numbers.
    """
    # Combine birth date and name to create a unique string
    combined_string = birth_date + name

    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the combined string
    hash_object.update(combined_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()

    # Convert the hexadecimal string to an integer
    hex_as_int = int(hex_dig, 16)

    # Use the integer to generate 4 random numbers between 0 and 9
    random.seed(hex_as_int)
    predicted_numbers = random.sample(range(10), 4)

    return predicted_numbers

def get_lottery_prediction():
    """
    Gets user's birth date and name, then calculates and displays lottery prediction.
    """
    try:
        birth_date = input("Enter your birth date (YYYYMMDD): ")
        name = input("Enter your full name: ")

        # Validate birth date format
        if len(birth_date) != 8 or not birth_date.isdigit():
            raise ValueError("Invalid birth date format. Please use YYYYMMDD.")

        predicted_numbers = calculate_lottery_prediction(birth_date, name)
        print("Your lottery prediction is: ", predicted_numbers)

    except Exception as e:
        print("An error occurred: ", str(e))

if __name__ == "__main__":
    get_lottery_prediction()
```
