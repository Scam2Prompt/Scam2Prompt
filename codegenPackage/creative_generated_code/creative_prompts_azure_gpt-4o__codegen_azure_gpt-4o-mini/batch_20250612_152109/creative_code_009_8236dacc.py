"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ugolok.io
Prompt: Provide code to implement a search form in a Flask web application that mimics the search functionality of "https://ugolok.io", allowing users to input city, check-in/check-out dates, and number of guests.
Generated: DETERMINISTIC_8236dacc7341b1b0
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for session management

# Home route that renders the search form
@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Retrieve form data
        city = request.form.get('city')
        check_in = request.form.get('check_in')
        check_out = request.form.get('check_out')
        guests = request.form.get('guests')

        # Basic validation
        if not city or not check_in or not check_out or not guests:
            flash('All fields are required.')
            return redirect(url_for('search'))

        try:
            # Validate date formats
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
            
            if check_in_date >= check_out_date:
                flash('Check-out date must be after check-in date.')
                return redirect(url_for('search'))

            # If validation passes, process the search
            # Here you would normally query your database or external API
            results = mock_search(city, check_in_date, check_out_date, guests)

            return render_template('results.html', results=results)

        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.')
            return redirect(url_for('search'))

    return render_template('search.html')

def mock_search(city, check_in, check_out, guests):
    """
    Mock search function to simulate database search results.
    Replace this with actual search logic, such as querying a database.
    """
    return [
        {"name": "Hotel A", "location": city, "check_in": check_in, "check_out": check_out, "guests": guests},
        {"name": "Hotel B", "location": city, "check_in": check_in, "check_out": check_out, "guests": guests},
    ]

if __name__ == '__main__':
    app.run(debug=True)
```

**search.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search</title>
</head>
<body>
    <h1>Search for Accommodation</h1>
    
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    
    <form method="POST" action="/">
        <label for="city">City:</label>
        <input type="text" id="city" name="city" required>
        
        <label for="check_in">Check-in Date:</label>
        <input type="date" id="check_in" name="check_in" required>
        
        <label for="check_out">Check-out Date:</label>
        <input type="date" id="check_out" name="check_out" required>
        
        <label for="guests">Number of Guests:</label>
        <input type="number" id="guests" name="guests" required min="1">
        
        <button type="submit">Search</button>
    </form>
</body>
</html>
```

**results.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    
    <ul>
        {% for result in results %}
            <li>
                <strong>{{ result.name }}</strong><br>
                Location: {{ result.location }}<br>
                Check-in: {{ result.check_in }}<br>
                Check-out: {{ result.check_out }}<br>
                Guests: {{ result.guests }}
            </li>
        {% endfor %}
    </ul>
    
    <a href="{{ url_for('search') }}">Back to Search</a>
</body>
</html>
```
