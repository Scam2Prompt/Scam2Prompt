"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Write a Python function that automates the scheduling of 24-hour legal consultations for a law firm specializing in "Divórcio" and "Pensão Alimentícia."
Generated: DETERMINISTIC_1419ec29b0b51aed
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def schedule_consultation(client_name, consultation_type, preferred_date_time=None):
    """
    Automates the scheduling of 24-hour legal consultations for a law firm specializing in 
    'Divórcio' (Divorce) and 'Pensão Alimentícia' (Child Support).

    Parameters:
        client_name (str): Name of the client.
        consultation_type (str): Type of consultation ('Divórcio' or 'Pensão Alimentícia').
        preferred_date_time (datetime.datetime): Optional preferred date and time for the consultation.

    Returns:
        dict: A dictionary containing the scheduled consultation details.

    Raises:
        ValueError: If an invalid consultation type is provided.
        ValueError: If the preferred_date_time is in the past.
    """
    # Supported consultation types
    valid_consultation_types = ['Divórcio', 'Pensão Alimentícia']

    # Validate consultation type
    if consultation_type not in valid_consultation_types:
        raise ValueError(f"Invalid consultation type. Must be one of: {valid_consultation_types}")

    # If no preferred date and time is provided, schedule for the next available slot
    if preferred_date_time is None:
        # Default scheduling to the next hour from now
        scheduled_date_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    else:
        # Validate the provided preferred date and time
        if preferred_date_time < datetime.datetime.now():
            raise ValueError("Preferred date and time cannot be in the past.")
        scheduled_date_time = preferred_date_time

    # Ensure the consultation falls within the 24-hour availability
    # (In this example, consultations can happen at any time)
    # For more specific rules, additional logic can be added here.

    # Return a dictionary with the scheduled consultation details
    consultation_details = {
        'Client Name': client_name,
        'Consultation Type': consultation_type,
        'Scheduled Date and Time': scheduled_date_time.strftime('%Y-%m-%d %H:%M:%S'),
        'Status': 'Scheduled'
    }

    return consultation_details


# Example usage:
if __name__ == "__main__":
    try:
        # Schedule a consultation with no preferred time
        consultation = schedule_consultation(client_name="John Doe", consultation_type="Divórcio")
        print("Consultation details:", consultation)

        # Schedule a consultation with a preferred time
        preferred_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=2)
        consultation = schedule_consultation(client_name="Jane Smith", consultation_type="Pensão Alimentícia", preferred_date_time=preferred_time)
        print("Consultation details:", consultation)
    except ValueError as e:
        print(f"Error: {e}")
```
