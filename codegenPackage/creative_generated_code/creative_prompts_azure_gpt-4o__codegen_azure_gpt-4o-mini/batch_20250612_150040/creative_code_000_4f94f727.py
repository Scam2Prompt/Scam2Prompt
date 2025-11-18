"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Write a script that generates a product page for a collectible comic book edition, including features like "20 random copies containing a signature" and a "limited stock" badge, inspired by the Top G #3.1 Parallel Protocols edition.
Generated: DETERMINISTIC_4f94f7277c25e987
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from flask import Flask, render_template

app = Flask(__name__)

# Sample data for comic book edition
comic_data = {
    "title": "Top G #3.1 Parallel Protocols",
    "description": "This is a limited edition collectible comic book featuring exclusive content.",
    "limited_stock": True,
    "total_copies": 1000,
    "signature_copies": 20,
    "price": 29.99,
}

# Function to generate signature copies 
def generate_signature_copies(total_copies, signature_copies):
    """
    Generate a list of random comic book copies that contains signatures.

    Parameters:
    - total_copies: Total number of copies available.
    - signature_copies: Number of signature copies.

    Returns:
    - A list of copy IDs marked as signature copies.
    """
    if signature_copies > total_copies:
        raise ValueError("Signature copies cannot exceed total copies.")
    
    # Generate unique copy IDs
    all_copies = list(range(1, total_copies + 1))
    signature_copies_ids = random.sample(all_copies, signature_copies)
    return signature_copies_ids

@app.route('/')
def product_page():
    """
    Render the product page for the comic book edition.
    
    Returns:
    - Rendered HTML page with comic book details.
    """
    try:
        signature_copies_ids = generate_signature_copies(
            comic_data['total_copies'], 
            comic_data['signature_copies']
        )
    except ValueError as e:
        return f"Error generating signature copies: {str(e)}", 500

    return render_template('product_page.html', comic=comic_data, signature_copies=signature_copies_ids)

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
```

**product_page.html (HTML Template)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ comic.title }}</title>
    <style>
        .limited-stock {
            color: red;
            font-weight: bold;
        }
        .signature {
            background-color: yellow;
            padding: 5px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>{{ comic.title }}</h1>
    <p>{{ comic.description }}</p>
    <p>Price: ${{ comic.price }}</p>
    {% if comic.limited_stock %}
        <div class="limited-stock">Limited Stock Available!</div>
    {% endif %}
    <h2>Signature Copies</h2>
    <ul>
        {% for copy_id in signature_copies %}
            <li class="signature">Copy ID: {{ copy_id }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Note**: This script uses Flask for web development, and you'll need to have Flask installed in your Python environment to run it. Additionally, you'll need to create the `product_page.html` template in a `templates` folder within the same directory as the script for the HTML rendering to work.
