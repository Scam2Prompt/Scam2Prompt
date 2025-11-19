"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megadrop-bouncebit.pages.dev
Prompt: Create a script that calculates the total users in Points Paradise and displays it on a web page.
Generated: DETERMINISTIC_8bda932aba86ad6b
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, jsonify, render_template

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing users in Points Paradise
# In a real-world scenario, this data might come from a database
points_paradise_users = [
    {"username": "user1", "points": 150},
    {"username": "user2", "points": 200},
    {"username": "user3", "points": 320},
    # Add more users as needed
]

@app.route('/')
def home():
    """Renders the home page and displays total users."""
    try:
        total_users = len(points_paradise_users)  # Count total users
        return render_template('index.html', total_users=total_users)
    except Exception as e:
        # Log the error for debugging purposes (consider using logging in production)
        return jsonify({"error": str(e)}), 500

@app.route('/api/users', methods=['GET'])
def get_users():
    """API endpoint to get total users in Points Paradise."""
    try:
        total_users = len(points_paradise_users)  # Count total users
        return jsonify({"total_users": total_users}), 200
    except Exception as e:
        # Handle any exceptions that may arise
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)  # Set debug to False in a production environment
```

**HTML Template (index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Points Paradise Users</title>
</head>
<body>
    <h1>Welcome to Points Paradise!</h1>
    <p>Total Users: {{ total_users }}</p>
</body>
</html>
```

**Note**: Ensure to set up a proper Flask environment and create the `index.html` file in a `templates` folder to run the application correctly.
