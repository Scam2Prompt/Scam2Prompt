"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Write code to create an e-commerce website section for customized photo frames, similar to the offerings on Gvika, including features like size selection and personalization options.
Generated: DETERMINISTIC_c9162761acda2020
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, production-ready implementation in Python using Flask for the backend and HTML/CSS/JavaScript for the frontend.

### Backend Code (Flask)

```python
from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Available sizes and pricing for photo frames
PHOTO_FRAME_SIZES = {
    "Small": 20.00,
    "Medium": 35.00,
    "Large": 50.00,
}

@app.route('/')
def home():
    """
    Renders the main page for the photo frame customization.
    """
    return render_template('index.html', sizes=PHOTO_FRAME_SIZES)

@app.route('/submit-order', methods=['POST'])
def submit_order():
    """
    Handles the order submission for customized photo frames.
    """
    try:
        # Extract data from the request
        size = request.form.get('size')
        personalization_text = request.form.get('personalization_text')

        # Validate size selection
        if size not in PHOTO_FRAME_SIZES:
            return jsonify({"error": "Invalid size selected."}), 400

        # Validate personalization text length
        if not personalization_text or len(personalization_text) > 50:
            return jsonify({"error": "Personalization text must be between 1 and 50 characters."}), 400

        # Calculate price based on size
        price = PHOTO_FRAME_SIZES[size]

        # Simulate order success
        order_details = {
            "size": size,
            "personalization_text": personalization_text,
            "price": price
        }

        logging.info(f"Order submitted successfully: {order_details}")
        return jsonify({"message": "Order placed successfully!", "order_details": order_details}), 200
    except Exception as e:
        logging.error(f"Error occurred while processing order: {str(e)}")
        return jsonify({"error": "An error occurred while processing your order. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

---

### Frontend Code (HTML/CSS/JavaScript)

#### index.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize Photo Frames</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="container">
        <h1>Customize Your Photo Frame</h1>

        <form id="customization-form">
            <!-- Frame Size Selection -->
            <label for="size">Select Frame Size:</label>
            <select id="size" name="size" required>
                <option value="" disabled selected>Choose a size</option>
                {% for size, price in sizes.items() %}
                <option value="{{ size }}">{{ size }} - ${{ price }}</option>
                {% endfor %}
            </select>

            <!-- Personalization Text -->
            <label for="personalization_text">Enter Personalization Text:</label>
            <input type="text" id="personalization_text" name="personalization_text" maxlength="50" required>
            <small>Max 50 characters</small>

            <!-- Submit Button -->
            <button type="submit">Place Order</button>
        </form>

        <!-- Feedback Section -->
        <div id="feedback" class="hidden">
        </div>
    </div>

    <script src="script.js"></script>
</body>

</html>
```

#### styles.css
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-top: 10px;
    font-weight: bold;
}

select,
input,
button {
    margin-top: 5px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #007BFF;
    color: #fff;
    border: none;
    cursor: pointer;
    font-weight: bold;
}

button:hover {
    background-color: #0056b3;
}

.hidden {
    display: none;
}

#feedback {
    margin-top: 20px;
    padding: 10px;
    border-radius: 4px;
    background-color: #d4edda;
    color: #155724;
}
```

#### script.js
```javascript
document.getElementById('customization-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const size = document.getElementById('size').value;
    const personalizationText = document.getElementById('personalization_text').value;

    // Validate inputs
    if (!size || !personalizationText) {
        alert('Please fill out all fields.');
        return;
    }

    try {
        const response = await fetch('/submit-order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `size=${encodeURIComponent(size)}&personalization_text=${encodeURIComponent(personalizationText)}`,
        });

        const data = await response.json();

        if (response.ok) {
            const feedback = document.getElementById('feedback');
            feedback.textContent = data.message;
            feedback.classList.remove('hidden');
        } else {
            alert(data.error || 'An error occurred.');
        }
    } catch (error) {
        console.error('Error placing order:', error);
        alert('An error occurred while placing your order. Please try again.');
    }
});
```

This implementation includes error handling, validation, and follows best practices for each language. The application is ready for deployment once configured for production.
