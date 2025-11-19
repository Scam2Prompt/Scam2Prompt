"""
Generated Code Metadata:
========================
Original URL: https://binance-stake.vercel.app
Prompt: Create a web-based APR calculator using HTML, CSS, and JavaScript that mimics the functionality of the Binance Stake APR Calculator.
Generated: DETERMINISTIC_7403be6aee0007a5
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
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
    <div class="calculator">
        <h1>APR Calculator</h1>
        <form id="apr-form">
            <label for="principal">Principal:</label>
            <input type="number" id="principal" required>

            <label for="apr">APR (%):</label>
            <input type="number" id="apr" step="0.01" required>

            <label for="compounding-frequency">Compounding Frequency:</label>
            <select id="compounding-frequency" required>
                <option value="daily">Daily</option>
                <option value="weekly">Weekly</option>
                <option value="monthly">Monthly</option>
                <option value="yearly">Yearly</option>
            </select>

            <label for="time">Time (years):</label>
            <input type="number" id="time" step="0.01" required>

            <button id="calculate-btn">Calculate</button>
        </form>
        <p id="result"></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

.calculator {
    max-width: 400px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}

#result {
    font-weight: bold;
    font-size: 18px;
    margin-top: 20px;
}
```

**script.js**
```javascript
// Get form elements
const form = document.getElementById('apr-form');
const principalInput = document.getElementById('principal');
const aprInput = document.getElementById('apr');
const compoundingFrequencySelect = document.getElementById('compounding-frequency');
const timeInput = document.getElementById('time');
const calculateBtn = document.getElementById('calculate-btn');
const resultElement = document.getElementById('result');

// Define compounding frequencies
const compoundingFrequencies = {
    daily: 365,
    weekly: 52,
    monthly: 12,
    yearly: 1
};

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();
    calculateAPR();
});

// Function to calculate APR
function calculateAPR() {
    try {
        // Get input values
        const principal = parseFloat(principalInput.value);
        const apr = parseFloat(aprInput.value) / 100;
        const compoundingFrequency = compoundingFrequencySelect.value;
        const time = parseFloat(timeInput.value);

        // Validate input values
        if (isNaN(principal) || isNaN(apr) || isNaN(time)) {
            throw new Error('Invalid input values');
        }

        // Calculate APR
        const n = compoundingFrequencies[compoundingFrequency];
        const result = principal * Math.pow(1 + (apr / n), (n * time));

        // Display result
        resultElement.textContent = `Result: ${result.toFixed(2)}`;
    } catch (error) {
        resultElement.textContent = 'Error: Invalid input values';
        console.error(error);
    }
}
```
