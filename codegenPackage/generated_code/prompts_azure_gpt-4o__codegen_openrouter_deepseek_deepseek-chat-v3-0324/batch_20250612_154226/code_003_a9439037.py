"""
Generated Code Metadata:
========================
Original URL: https://proximus-client.was-systems.com
Prompt: Develop a code snippet for categorizing users as "Ancien client" or "Nouveau client" based on their input, similar to the classification system mentioned on the Proximus client page.
Generated: DETERMINISTIC_a943903752b84d18
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def categorize_client(client_data):
    """
    Categorizes a client as 'Ancien client' (existing) or 'Nouveau client' (new) based on their input data.
    
    Args:
        client_data (dict): Dictionary containing client information with at least:
            - 'registration_date' (str): Date in 'YYYY-MM-DD' format
            - 'last_purchase_date' (str or None): Date of last purchase in 'YYYY-MM-DD' format or None if no purchases
    
    Returns:
        str: Client category ('Ancien client' or 'Nouveau client')
    
    Raises:
        ValueError: If required fields are missing or dates are invalid
    """
    try:
        from datetime import datetime, timedelta
        
        # Validate input data
        if not client_data.get('registration_date'):
            raise ValueError("Registration date is required")
        
        # Parse dates
        registration_date = datetime.strptime(client_data['registration_date'], '%Y-%m-%d').date()
        current_date = datetime.now().date()
        
        # Check if client is new (registered within last 30 days with no purchases)
        if (current_date - registration_date) <= timedelta(days=30):
            if client_data.get('last_purchase_date') is None:
                return "Nouveau client"
        
        # Default to existing client
        return "Ancien client"
        
    except KeyError as e:
        raise ValueError(f"Missing required field: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}. Expected 'YYYY-MM-DD'")
    except Exception as e:
        raise ValueError(f"Error categorizing client: {e}")


# Example usage
if __name__ == "__main__":
    test_client_1 = {
        'registration_date': '2023-01-15',
        'last_purchase_date': '2023-06-20'
    }
    
    test_client_2 = {
        'registration_date': '2023-12-01',  # Within last 30 days (assuming current date is 2023-12-20)
        'last_purchase_date': None
    }
    
    try:
        print(categorize_client(test_client_1))  # Output: Ancien client
        print(categorize_client(test_client_2))  # Output: Nouveau client
    except ValueError as e:
        print(f"Error: {e}")
```
