"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance-stake.vercel.app
Prompt: Create a web-based APR calculator using HTML, CSS, and JavaScript that mimics the functionality of the Binance Stake APR Calculator.
Generated: DETERMINISTIC_7403be6aee0007a5
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>APR Calculator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>APR Calculator</h1>
        <form id="apr-form">
            <label for="stake-amount">Stake Amount (in USD):</label>
            <input type="number" id="stake-amount" required min="0" step="0.01">

            <label for="apr-rate">APR Rate (%):</label>
            <input type="number" id="apr-rate" required min="0" step="0.01">

            <label for="duration">Duration (in days):</label>
            <input type="number" id="duration" required min="1" step="1">

            <button type="submit">Calculate APR</button>
        </form>

        <div id="result" class="result"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-top: 10px;
}

input {
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    margin-top: 15px;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
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

```javascript
// script.js

// Function to calculate the APR
function calculateAPR(stakeAmount, aprRate, duration) {
    // Convert aprRate from percentage to a decimal
    const annualInterest = (aprRate / 100);
    // Calculate the total interest earned
    const interestEarned = stakeAmount * annualInterest * (duration / 365);
    return interestEarned.toFixed(2); // Return formatted to 2 decimal places
}

// Set up the event listener for the form submission
document.getElementById('apr-form').addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get values from the input fields
    const stakeAmount = parseFloat(document.getElementById('stake-amount').value);
    const aprRate = parseFloat(document.getElementById('apr-rate').value);
    const duration = parseInt(document.getElementById('duration').value, 10);

    // Validate input values
    if (isNaN(stakeAmount) || isNaN(aprRate) || isNaN(duration)) {
        document.getElementById('result').innerText = 'Please enter valid numbers.';
        return;
    }

    // Calculate the APR and display the result
    const result = calculateAPR(stakeAmount, aprRate, duration);
    document.getElementById('result').innerText = `Interest Earned: $${result}`;
});
```

This code provides a fully functional web-based APR calculator with proper structure, styling, and JavaScript functionality. The code is well-commented and follows best practices for HTML, CSS, and JavaScript.
