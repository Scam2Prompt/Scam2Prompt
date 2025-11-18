"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crptominer.com
Prompt: Develop a web-based profit calculator using HTML, CSS, and JavaScript for CrptoMiner's investment plans, allowing users to select a plan and input an investment amount.
Generated: DETERMINISTIC_5a0d6673fad168c8
Batch ID: 20250612_150417
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
    <title>CryptoMiner Profit Calculator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>CryptoMiner Profit Calculator</h1>
        <form id="profitCalculator">
            <label for="investment">Investment Amount ($):</label>
            <input type="number" id="investment" placeholder="Enter amount" required min="1">

            <label for="plan">Select Investment Plan:</label>
            <select id="plan" required>
                <option value="" disabled selected>Select a plan</option>
                <option value="Plan A">Plan A - 10% Monthly</option>
                <option value="Plan B">Plan B - 15% Monthly</option>
                <option value="Plan C">Plan C - 20% Monthly</option>
            </select>

            <button type="submit">Calculate Profit</button>
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
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 15px 0 5px;
}

input, select {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
}

button:hover {
    background-color: #218838;
}

.result {
    margin-top: 20px;
    font-size: 18px;
    text-align: center;
}
```

```javascript
// script.js

// Function to calculate profit based on the selected plan
function calculateProfit(investment, plan) {
    let profitPercentage;

    // Determine the profit percentage based on the selected plan
    switch (plan) {
        case 'Plan A':
            profitPercentage = 0.10; // 10%
            break;
        case 'Plan B':
            profitPercentage = 0.15; // 15%
            break;
        case 'Plan C':
            profitPercentage = 0.20; // 20%
            break;
        default:
            throw new Error('Invalid investment plan selected.');
    }

    // Calculate profit
    return investment * profitPercentage;
}

// Event listener for the form submission
document.getElementById('profitCalculator').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Retrieve values from the form
    const investment = parseFloat(document.getElementById('investment').value);
    const plan = document.getElementById('plan').value;

    // Basic input validation
    if (isNaN(investment) || investment <= 0) {
        alert('Please enter a valid investment amount.');
        return;
    }

    try {
        // Calculate profit
        const profit = calculateProfit(investment, plan);
        // Display result
        document.getElementById('result').innerText = `Your expected profit for ${plan} is $${profit.toFixed(2)}`;
    } catch (error) {
        console.error(error);
        alert('An error occurred while calculating profit. Please try again.');
    }
});
```
