"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://denshaven.com
Prompt: Write a Python script to create a webpage showcasing the amenities of Dens Haven villas, including features like a swimming pool, clubhouse, landscaped garden, and CCTV monitoring system.
Generated: DETERMINISTIC_af39486e0fd1bb50
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template_string

# Initialize the Flask application
app = Flask(__name__)

# HTML template for the webpage
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dens Haven Villas</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        main {
            padding: 2rem;
        }
        .amenities {
            display: flex;
            flex-wrap: wrap;
            gap: 1.5rem;
        }
        .amenity {
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 1rem;
            text-align: center;
            flex: 1 1 200px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Dens Haven Villas</h1>
        <p>Experience Luxury Living</p>
    </header>
    <main>
        <h2>Our Amenities</h2>
        <div class="amenities">
            <div class="amenity">
                <h3>Swimming Pool</h3>
                <p>Relax and unwind in our sparkling swimming pool.</p>
            </div>
            <div class="amenity">
                <h3>Clubhouse</h3>
                <p>Enjoy community events and gatherings in our modern clubhouse.</p>
            </div>
            <div class="amenity">
                <h3>Landscaped Garden</h3>
                <p>Take a stroll through our beautifully designed gardens.</p>
            </div>
            <div class="amenity">
                <h3>CCTV Monitoring System</h3>
                <p>Your safety is our priority with 24/7 CCTV surveillance.</p>
            </div>
        </div>
    </main>
</body>
</html>
"""

@app.route('/')
def homepage():
    """
    Route to serve the homepage showcasing Dens Haven Villas amenities.
    """
    try:
        # Render the HTML template and return it
        return render_template_string(html_template)
    except Exception as e:
        # Log and handle errors gracefully
        error_message = f"An error occurred: {str(e)}"
        return f"<h1>Error</h1><p>{error_message}</p>", 500

# Main block to run the Flask application
if __name__ == "__main__":
    # Best practice: Avoid hardcoding production port in code
    app.run(debug=True, host="0.0.0.0", port=5000)
```
