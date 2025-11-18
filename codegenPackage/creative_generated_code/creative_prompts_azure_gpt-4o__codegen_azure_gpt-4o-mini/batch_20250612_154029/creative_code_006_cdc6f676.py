"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haggis.vercel.app
Prompt: Develop a script to restrict access to the HAGGIS Hunt campaign for users from specific jurisdictions, as outlined in the legal terms on the website.
Generated: DETERMINISTIC_cdc6f67614d60d52
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, abort
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)

# List of restricted jurisdictions
RESTRICTED_JURISDICTIONS = [
    'JurisdictionA',
    'JurisdictionB',
    'JurisdictionC'
]

def is_restricted_jurisdiction(jurisdiction):
    """
    Check if the given jurisdiction is in the list of restricted jurisdictions.
    
    Args:
        jurisdiction (str): The jurisdiction to check.
        
    Returns:
        bool: True if restricted, False otherwise.
    """
    return jurisdiction in RESTRICTED_JURISDICTIONS

def jurisdiction_required(f):
    """
    Decorator to restrict access based on user jurisdiction.
    
    Args:
        f (function): The function to be wrapped.
    
    Returns:
        function: The wrapped function with jurisdiction check.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the user's jurisdiction from request headers
        jurisdiction = request.headers.get('X-Jurisdiction')
        
        if jurisdiction is None:
            # Abort if jurisdiction is not provided
            abort(400, description="Jurisdiction header is missing.")
        
        if is_restricted_jurisdiction(jurisdiction):
            # Abort if user is from a restricted jurisdiction
            abort(403, description="Access denied for users from restricted jurisdictions.")
        
        return f(*args, **kwargs)
    
    return decorated_function

@app.route('/haggis-hunt', methods=['GET'])
@jurisdiction_required
def haggis_hunt():
    """
    Endpoint for the HAGGIS Hunt campaign.
    
    Returns:
        str: A message indicating access to the HAGGIS Hunt campaign.
    """
    return "Welcome to the HAGGIS Hunt campaign!"

if __name__ == '__main__':
    # Run the application on localhost with debug mode disabled
    app.run(host='0.0.0.0', port=5000, debug=False)
```
