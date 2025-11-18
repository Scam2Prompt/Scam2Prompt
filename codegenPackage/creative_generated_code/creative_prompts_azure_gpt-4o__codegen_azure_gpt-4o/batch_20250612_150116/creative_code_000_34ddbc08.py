"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Write Python code to create a subscription-based e-book access system similar to Digielearning, including features for different subscription plans (e.g., Basic, Standard, Premium) and secure user authentication.
Generated: DETERMINISTIC_34ddbc089c80d331
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import uuid
import datetime

# A dictionary to store user data in-memory for demonstration purposes
# In production, use a database like PostgreSQL, MySQL, or MongoDB
users = {}

# A dictionary to define subscription plans and their features
subscription_plans = {
    "Basic": {
        "price": 5.99,
        "max_books": 5
    },
    "Standard": {
        "price": 12.99,
        "max_books": 10
    },
    "Premium": {
        "price": 19.99,
        "max_books": 20
    }
}

# Function to securely hash passwords
def hash_password(password):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password, salt

# Function to verify hashed passwords
def verify_password(stored_password, stored_salt, provided_password):
    return stored_password == hashlib.sha256((provided_password + stored_salt).encode()).hexdigest()

# Function to register a new user
def register_user(username, password, subscription_plan):
    if username in users:
        raise ValueError("Username already exists.")
    
    if subscription_plan not in subscription_plans:
        raise ValueError("Invalid subscription plan.")
    
    hashed_password, salt = hash_password(password)
    
    # Store user data
    users[username] = {
        "password": hashed_password,
        "salt": salt,
        "subscription_plan": subscription_plan,
        "subscription_start_date": datetime.datetime.now(),
    }
    print(f"User '{username}' registered successfully!")

# Function to authenticate a user
def authenticate_user(username, password):
    user = users.get(username)
    if not user:
        raise ValueError("Invalid username or password.")
    
    if not verify_password(user["password"], user["salt"], password):
        raise ValueError("Invalid username or password.")
    
    print(f"User '{username}' authenticated successfully!")
    return True

# Function to get user subscription details
def get_subscription_details(username):
    user = users.get(username)
    if not user:
        raise ValueError("User not found.")
    
    subscription_details = subscription_plans[user["subscription_plan"]]
    print(f"Subscription details for '{username}': {subscription_details}")
    return subscription_details

# Function to upgrade a user's subscription plan
def upgrade_subscription(username, new_plan):
    user = users.get(username)
    if not user:
        raise ValueError("User not found.")
    
    if new_plan not in subscription_plans:
        raise ValueError("Invalid subscription plan.")
    
    if user["subscription_plan"] == new_plan:
        raise ValueError(f"User is already on the '{new_plan}' plan.")
    
    user["subscription_plan"] = new_plan
    user["subscription_start_date"] = datetime.datetime.now()
    print(f"User '{username}' upgraded to the '{new_plan}' plan!")

# Example usage
if __name__ == "__main__":
    try:
        # Register users
        register_user("john_doe", "secure_password123", "Basic")
        register_user("jane_smith", "password456", "Standard")
        
        # Authenticate users
        authenticate_user("john_doe", "secure_password123")
        
        # Get subscription details
        get_subscription_details("john_doe")
        
        # Upgrade subscription
        upgrade_subscription("john_doe", "Premium")
        
        # Get updated subscription details
        get_subscription_details("john_doe")
    except Exception as e:
        print(f"Error: {e}")
```
