"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staklngstoryfoundatlon.org
Prompt: Create a script to display validator details in a paginated format, similar to the Story Staking Dashboard.
Generated: DETERMINISTIC_438d0f25ee12bf1f
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Validator:
    """
    Represents a validator with details.
    """
    def __init__(self, id, name, stake, commission_rate):
        self.id = id
        self.name = name
        self.stake = stake
        self.commission_rate = commission_rate

def paginate(data, page, page_size):
    """
    Paginates the given data.

    Args:
        data (list): List of items to paginate.
        page (int): Current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        dict: A dictionary containing paginated data, current page, total pages, and total items.
    """
    total_items = len(data)
    total_pages = math.ceil(total_items / page_size)
    
    # Ensure valid page number
    if page < 1 or page > total_pages:
        raise ValueError(f"Invalid page number. Must be between 1 and {total_pages}.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return {
        "data": data[start_index:end_index],
        "current_page": page,
        "total_pages": total_pages,
        "total_items": total_items
    }

def display_validators(validators, page, page_size):
    """
    Displays validator details in a paginated format.

    Args:
        validators (list): List of Validator objects.
        page (int): Current page number (1-indexed).
        page_size (int): Number of validators per page.
    """
    try:
        paginated_result = paginate(validators, page, page_size)
        print(f"Page {paginated_result['current_page']} of {paginated_result['total_pages']}")
        print("ID | Name         | Stake       | Commission Rate")
        print("-" * 50)
        for validator in paginated_result["data"]:
            print(f"{validator.id:2} | {validator.name:12} | {validator.stake:10} | {validator.commission_rate:15}")
        print(f"Total Validators: {paginated_result['total_items']}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Sample validator data
validators = [
    Validator(1, "Validator A", 1000, "10%"),
    Validator(2, "Validator B", 2000, "12%"),
    Validator(3, "Validator C", 1500, "8%"),
    Validator(4, "Validator D", 2500, "14%"),
    Validator(5, "Validator E", 3000, "9%"),
    Validator(6, "Validator F", 1700, "13%")
]

# User input for page navigation
PAGE = 1      # Change this to test different pages
PAGE_SIZE = 2 # Change this to test different page sizes

# Display validators in paginated format
display_validators(validators, PAGE, PAGE_SIZE)
```
