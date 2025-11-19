"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luwukpost.id
Prompt: Generate a news article summarizing the recent traffic accident in Desa Biak, Luwuk Timur, including details about the injured motorcyclist and the date of the incident.
Generated: DETERMINISTIC_2e6e847f331c0b15
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_news_article(location, date, injured_person_details):
    """
    Generates a news article summarizing a traffic accident.
    
    Parameters:
        location (str): The location of the accident.
        date (datetime.date): The date of the accident.
        injured_person_details (dict): Details of the injured person.
            Expected keys: name (str), age (int), vehicle_type (str), condition (str).
    
    Returns:
        str: A formatted news article summarizing the incident.
    """
    try:
        # Validate input parameters
        if not location or not isinstance(location, str):
            raise ValueError("Invalid location provided.")
        if not isinstance(date, datetime.date):
            raise ValueError("Invalid date provided. Must be a datetime.date object.")
        if not isinstance(injured_person_details, dict):
            raise ValueError("Invalid injured_person_details provided. Must be a dictionary.")
        
        required_keys = {"name", "age", "vehicle_type", "condition"}
        missing_keys = required_keys - injured_person_details.keys()
        if missing_keys:
            raise ValueError(f"Missing keys in injured_person_details: {', '.join(missing_keys)}")
        
        # Extract injured person's details
        name = injured_person_details["name"]
        age = injured_person_details["age"]
        vehicle_type = injured_person_details["vehicle_type"]
        condition = injured_person_details["condition"]
        
        # Format article text
        article = (
            f"Traffic Accident in {location}\n"
            f"Date: {date.strftime('%B %d, %Y')}\n\n"
            f"A traffic accident occurred recently in {location}, resulting in injuries to a motorcyclist. "
            f"The injured individual has been identified as {name}, aged {age}. "
            f"The accident involved a {vehicle_type}. The motorcyclist is currently reported to be in {condition} condition. "
            f"Authorities are investigating the incident further."
        )
        
        return article
    
    except Exception as e:
        # Log the error and re-raise for transparency
        print(f"Error generating news article: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Define accident details
        accident_location = "Desa Biak, Luwuk Timur"
        accident_date = datetime.date(2023, 10, 5)
        injured_motorcyclist = {
            "name": "John Doe",
            "age": 34,
            "vehicle_type": "motorcycle",
            "condition": "serious but stable"
        }
        
        # Generate and print the news article
        article = generate_news_article(accident_location, accident_date, injured_motorcyclist)
        print(article)
    
    except Exception as error:
        print(f"An error occurred: {error}")
```
