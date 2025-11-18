"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Develop a code snippet for categorizing users as "Ancien client" or "Nouveau client" based on their input, similar to the classification system mentioned on the Proximus client page.
Generated: DETERMINISTIC_a943903752b84d18
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import datetime

def categorize_client(client_since_date):
    """
    Categorizes a user as "Ancien client" or "Nouveau client" based on the date they became a client.
    
    Args:
        client_since_date (str): The date the client started using the service in 'YYYY-MM-DD' format.

    Returns:
        str: "Ancien client" if the user has been a client for more than 2 years, otherwise "Nouveau client".
    
    Raises:
        ValueError: If the input date is not in the expected format or is invalid.
    """
    try:
        # Parse the input date string into a datetime object
        client_since = datetime.datetime.strptime(client_since_date, '%Y-%m-%d').date()
        today = datetime.date.today()
        
        # Calculate the difference between today and the input date
        delta = today - client_since
        
        # Determine the category based on the difference in days
        if delta.days > 730:  # 730 days = 2 years
            return "Ancien client"
        else:
            return "Nouveau client"
    except ValueError:
        # Handle invalid date formats or values
        raise ValueError("Invalid date format. Please provide the date in 'YYYY-MM-DD' format.")

# Example usage
if __name__ == "__main__":
    try:
        # User input for client since date
        user_input = input("Enter the date you became a client (YYYY-MM-DD): ")
        
        # Categorize the client
        category = categorize_client(user_input)
        print(f"You are classified as: {category}")
    except ValueError as e:
        # Handle invalid user input
        print(f"Error: {e}")
```
