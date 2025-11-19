"""
Generated Code Metadata:
========================
Original URL: https://shrimohinirajdevasthan.com
Prompt: Generate a code snippet to create a web application that displays information about the Mohiniraj Temple, including its history and daily programs.
Generated: DETERMINISTIC_e6d2d55c0c5f718e
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

# Define temple information
temple_info = {
    'name': 'Mohiniraj Temple',
    'location': 'Kothanur, Bangalore, India',
    'history': '''
    The Mohiniraj Temple is a sacred Hindu temple dedicated to Lord Vishnu, 
    located in Kothanur, Bangalore. The temple is famous for its stunning 
    architecture and beautiful carvings. According to legend, the temple was 
    built in the 9th century AD and is one of the oldest temples in the region.
    ''',
    'daily_programs': '''
    The temple conducts various daily programs, including:
    - Abhishekam (6:00 AM - 7:00 AM)
    - Archana (7:00 AM - 8:00 AM)
    - Pooja (8:00 AM - 9:00 AM)
    - Sahasranama Archana (6:00 PM - 7:00 PM)
    '''
}

@app.route('/')
@cache.cached(timeout=60)  # cache for 1 minute
def index():
    try:
        return render_template('index.html', temple_info=temple_info)
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mohiniraj Temple</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>{{ temple_info['name'] }}</h1>
        <p>Location: {{ temple_info['location'] }}</p>
    </header>
    <main>
        <section>
            <h2>History</h2>
            <p>{{ temple_info['history'] }}</p>
        </section>
        <section>
            <h2>Daily Programs</h2>
            <p>{{ temple_info['daily_programs'] }}</p>
        </section>
    </main>
</body>
</html>
```

```css
/* static/style.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
}

p {
    margin-bottom: 1em;
}
```

```html
<!-- templates/error.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
</body>
</html>
```

```python
# requirements.txt

Flask
Flask-Caching
```
