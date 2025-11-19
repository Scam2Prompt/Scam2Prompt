"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Design a simple web form using HTML and CSS to collect property information and provide a cash offer for a house in San Francisco Bay Area.
Generated: DETERMINISTIC_45099634ba46653b
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Property Information Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Get a Cash Offer for Your Property</h1>
        <form id="propertyForm" onsubmit="return handleSubmit(event)">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>

            <label for="address">Property Address:</label>
            <input type="text" id="address" name="address" required>

            <label for="price">Estimated Property Value ($):</label>
            <input type="number" id="price" name="price" required min="0">

            <label for="condition">Property Condition:</label>
            <select id="condition" name="condition" required>
                <option value="">Select Condition</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="fair">Fair</option>
                <option value="poor">Poor</option>
            </select>

            <button type="submit">Get Cash Offer</button>
        </form>
        <div id="result" class="result"></div>
    </div>

    <script>
        /**
         * Handles the form submission.
         * @param {Event} event - The submit event.
         * @returns {boolean} - Returns false to prevent default form submission.
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            // Collect form data
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            // Validate data (basic validation)
            if (!data.name || !data.email || !data.address || !data.price || !data.condition) {
                displayResult("Please fill in all fields.", true);
                return false;
            }

            // Simulate cash offer calculation (for demonstration purposes)
            const cashOffer = calculateCashOffer(data.price, data.condition);
            displayResult(`Your cash offer is: $${cashOffer.toLocaleString()}`, false);
            return false; // Prevent form submission
        }

        /**
         * Calculates a cash offer based on property value and condition.
         * @param {number} price - The estimated property value.
         * @param {string} condition - The condition of the property.
         * @returns {number} - The calculated cash offer.
         */
        function calculateCashOffer(price, condition) {
            let offerMultiplier = 0.8; // Base multiplier for cash offer

            // Adjust multiplier based on property condition
            switch (condition) {
                case 'excellent':
                    offerMultiplier = 0.9;
                    break;
                case 'good':
                    offerMultiplier = 0.85;
                    break;
                case 'fair':
                    offerMultiplier = 0.75;
                    break;
                case 'poor':
                    offerMultiplier = 0.65;
                    break;
            }

            return price * offerMultiplier; // Calculate cash offer
        }

        /**
         * Displays the result message on the page.
         * @param {string} message - The message to display.
         * @param {boolean} isError - Indicates if the message is an error.
         */
        function displayResult(message, isError) {
            const resultDiv = document.getElementById('result');
            resultDiv.textContent = message;
            resultDiv.style.color = isError ? 'red' : 'green';
        }
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    color: #333;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.result {
    margin-top: 20px;
    font-size: 1.2em;
    text-align: center;
}
```
