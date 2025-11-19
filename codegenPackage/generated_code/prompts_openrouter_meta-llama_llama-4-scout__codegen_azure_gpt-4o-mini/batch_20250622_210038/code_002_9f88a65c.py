"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: "Generate a JavaScript code for a website feature that allows users to get a free quote for UPVC window and door systems, including calculations for total cost based on size and design."
Generated: DETERMINISTIC_9f88a65cee424be8
Batch ID: 20250622_210038
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
    <title>UPVC Window and Door Quote Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .result {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Get a Free Quote for UPVC Windows and Doors</h1>
    <form id="quoteForm">
        <label for="width">Width (in meters):</label>
        <input type="number" id="width" name="width" required min="0" step="0.01"><br><br>

        <label for="height">Height (in meters):</label>
        <input type="number" id="height" name="height" required min="0" step="0.01"><br><br>

        <label for="design">Design Type:</label>
        <select id="design" name="design" required>
            <option value="standard">Standard</option>
            <option value="premium">Premium</option>
            <option value="luxury">Luxury</option>
        </select><br><br>

        <button type="submit">Get Quote</button>
    </form>

    <div class="result" id="result"></div>
</div>

<script>
    // Constants for pricing per square meter based on design type
    const pricing = {
        standard: 100, // Price per square meter for standard design
        premium: 150,  // Price per square meter for premium design
        luxury: 200    // Price per square meter for luxury design
    };

    // Function to calculate the total cost based on user input
    function calculateQuote(width, height, design) {
        const area = width * height; // Calculate area in square meters
        const costPerSquareMeter = pricing[design]; // Get cost based on design
        return area * costPerSquareMeter; // Total cost
    }

    // Event listener for form submission
    document.getElementById('quoteForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Retrieve user input values
        const width = parseFloat(document.getElementById('width').value);
        const height = parseFloat(document.getElementById('height').value);
        const design = document.getElementById('design').value;

        // Validate input values
        if (isNaN(width) || isNaN(height) || width <= 0 || height <= 0) {
            document.getElementById('result').innerText = 'Please enter valid dimensions.';
            return;
        }

        // Calculate the quote
        const totalCost = calculateQuote(width, height, design);

        // Display the result
        document.getElementById('result').innerText = `Total Cost: $${totalCost.toFixed(2)}`;
    });
</script>

</body>
</html>
```
