"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anywhere-adventure.com
Prompt: Write a script to automate the process of generating quotes for tailored travel packages, specifically for adventure sports and wildlife safaris in Kenya.
Generated: DETERMINISTIC_2cda3e59ad14f913
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from datetime import datetime

# Constants for pricing and package details
ADVENTURE_SPORTS_BASE_PRICE = 1500  # Base price in USD
WILDLIFE_SAFARI_BASE_PRICE = 2000  # Base price in USD
DISCOUNT_THRESHOLD = 5  # Number of people for group discount
DISCOUNT_RATE = 0.1  # 10% group discount

# Function to validate input data
def validate_input(data):
    required_fields = ["name", "email", "phone", "package_type", "travel_dates", "num_people"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    if data["package_type"] not in ["Adventure Sports", "Wildlife Safari"]:
        raise ValueError("Invalid package type. Must be 'Adventure Sports' or 'Wildlife Safari'.")
    if not isinstance(data["num_people"], int) or data["num_people"] <= 0:
        raise ValueError("Number of people must be a positive integer.")
    return True

# Function to calculate package price
def calculate_price(package_type, num_people):
    if package_type == "Adventure Sports":
        base_price = ADVENTURE_SPORTS_BASE_PRICE
    elif package_type == "Wildlife Safari":
        base_price = WILDLIFE_SAFARI_BASE_PRICE
    else:
        raise ValueError("Invalid package type.")
    
    total_price = base_price * num_people
    
    # Apply group discount if applicable
    if num_people >= DISCOUNT_THRESHOLD:
        total_price -= total_price * DISCOUNT_RATE
    
    return total_price

# Function to generate a unique quote ID
def generate_quote_id():
    return str(uuid.uuid4())

# Function to create a quote
def generate_quote(data):
    try:
        # Validate input data
        validate_input(data)
        
        # Calculate price
        price = calculate_price(data["package_type"], data["num_people"])
        
        # Generate quote details
        quote = {
            "quote_id": generate_quote_id(),
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "package_type": data["package_type"],
            "travel_dates": data["travel_dates"],
            "num_people": data["num_people"],
            "price": price,
            "generated_at": datetime.now().isoformat()
        }
        
        return quote
    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}

# Entry point for the script (example usage)
if __name__ == "__main__":
    # Example request data
    request_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+123456789",
        "package_type": "Adventure Sports",
        "travel_dates": "2023-12-10 to 2023-12-20",
        "num_people": 6
    }
    
    # Generate quote
    quote = generate_quote(request_data)
    
    # Print the quote in JSON format
    print(json.dumps(quote, indent=4))
```
