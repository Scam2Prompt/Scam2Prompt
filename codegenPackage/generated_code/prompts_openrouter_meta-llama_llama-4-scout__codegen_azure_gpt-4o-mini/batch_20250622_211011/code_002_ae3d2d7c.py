"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Generate a JavaScript code snippet for a simple calculator that estimates the cash offer for a house in San Francisco Bay Area based on user input.
Generated: DETERMINISTIC_ae3d2d7c542b2778
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Simple Calculator for Estimating Cash Offer for a House in San Francisco Bay Area

// Function to calculate cash offer based on user input
function calculateCashOffer(propertyValue, condition, locationFactor) {
    // Validate input values
    if (typeof propertyValue !== 'number' || propertyValue <= 0) {
        throw new Error("Property value must be a positive number.");
    }
    if (typeof condition !== 'number' || condition < 0 || condition > 1) {
        throw new Error("Condition must be a number between 0 (poor) and 1 (excellent).");
    }
    if (typeof locationFactor !== 'number' || locationFactor <= 0) {
        throw new Error("Location factor must be a positive number.");
    }

    // Calculate the cash offer
    const baseOffer = propertyValue * condition * locationFactor;
    return baseOffer.toFixed(2); // Return the offer rounded to two decimal places
}

// Event listener for form submission
document.getElementById('offerForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get user input values
    const propertyValue = parseFloat(document.getElementById('propertyValue').value);
    const condition = parseFloat(document.getElementById('condition').value);
    const locationFactor = parseFloat(document.getElementById('locationFactor').value);

    try {
        // Calculate the cash offer
        const cashOffer = calculateCashOffer(propertyValue, condition, locationFactor);
        // Display the result
        document.getElementById('result').innerText = `Estimated Cash Offer: $${cashOffer}`;
    } catch (error) {
        // Handle errors and display error message
        document.getElementById('result').innerText = `Error: ${error.message}`;
    }
});
```

```html
<!-- HTML Structure for the Calculator -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cash Offer Calculator</title>
</head>
<body>
    <h1>Cash Offer Calculator for San Francisco Bay Area</h1>
    <form id="offerForm">
        <label for="propertyValue">Property Value ($):</label>
        <input type="number" id="propertyValue" required>
        <br>
        <label for="condition">Condition (0 to 1):</label>
        <input type="number" id="condition" min="0" max="1" step="0.01" required>
        <br>
        <label for="locationFactor">Location Factor:</label>
        <input type="number" id="locationFactor" required>
        <br>
        <button type="submit">Calculate Offer</button>
    </form>
    <div id="result"></div>

    <script src="calculator.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
