"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Generate a sample corporate media training plan for a Kenyan company, using expert services from Cara Productions.
Generated: DETERMINISTIC_59c8a690212c3d4e
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Corporate Media Training Plan Generator
This script generates a sample corporate media training plan for a Kenyan company,
leveraging expert services from Cara Productions.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import datetime

def generate_training_plan(company_name, training_date, location, participants):
    """
    Generates a corporate media training plan.

    Args:
        company_name (str): Name of the company.
        training_date (str): Date of the training in 'YYYY-MM-DD' format.
        location (str): Location of the training.
        participants (list): List of participant names.

    Returns:
        dict: A structured training plan.
    """
    try:
        # Validate inputs
        if not company_name or not isinstance(company_name, str):
            raise ValueError("Invalid company name. It must be a non-empty string.")
        
        if not training_date or not isinstance(training_date, str):
            raise ValueError("Invalid training date. It must be a string in 'YYYY-MM-DD' format.")
        
        # Parse and validate the training date
        training_date_obj = datetime.datetime.strptime(training_date, "%Y-%m-%d")
        if training_date_obj < datetime.datetime.now():
            raise ValueError("Training date cannot be in the past.")
        
        if not location or not isinstance(location, str):
            raise ValueError("Invalid location. It must be a non-empty string.")
        
        if not participants or not isinstance(participants, list) or not all(isinstance(p, str) for p in participants):
            raise ValueError("Invalid participants list. It must be a list of non-empty strings.")
        
        # Define the training plan structure
        training_plan = {
            "Company Name": company_name,
            "Training Date": training_date_obj.strftime("%Y-%m-%d"),
            "Location": location,
            "Participants": participants,
            "Training Provider": "Cara Productions",
            "Agenda": [
                {"Time": "09:00 AM", "Activity": "Introduction to Media Training"},
                {"Time": "10:00 AM", "Activity": "Effective Communication Strategies"},
                {"Time": "11:30 AM", "Activity": "Handling Media Interviews"},
                {"Time": "01:00 PM", "Activity": "Lunch Break"},
                {"Time": "02:00 PM", "Activity": "Crisis Communication Techniques"},
                {"Time": "03:30 PM", "Activity": "Practical Media Simulation"},
                {"Time": "05:00 PM", "Activity": "Closing Remarks and Feedback"}
            ]
        }
        
        return training_plan
    
    except ValueError as ve:
        # Handle validation errors
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample input data
    company_name = "Kenya Tech Solutions"
    training_date = "2023-12-15"
    location = "Nairobi, Kenya"
    participants = ["Alice Mwangi", "John Kamau", "Grace Otieno", "Peter Njoroge"]

    # Generate the training plan
    training_plan = generate_training_plan(company_name, training_date, location, participants)

    # Display the training plan
    if training_plan:
        print("Corporate Media Training Plan:")
        for key, value in training_plan.items():
            if key == "Agenda":
                print(f"{key}:")
                for item in value:
                    print(f"  - {item['Time']}: {item['Activity']}")
            else:
                print(f"{key}: {value}")
```
