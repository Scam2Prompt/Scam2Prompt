"""
Generated Code Metadata:
========================
Original URL: https://albemarle.devindex.net
Prompt: Create a code snippet to enable JavaScript for an investment strategy application similar to Albemarle's, assuming it uses a web-based interface.
Generated: DETERMINISTIC_3ecca4c3cf1dbd4c
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Investment Strategy Application - JavaScript Code Snippet

// Function to calculate the expected return of an investment
/**
 * Calculates the expected return based on the investment amount, 
 * expected annual return rate, and investment duration.
 * 
 * @param {number} investmentAmount - The initial amount invested.
 * @param {number} annualReturnRate - The expected annual return rate (in decimal).
 * @param {number} years - The number of years the money is invested for.
 * @returns {number} - The expected return after the specified duration.
 * @throws {Error} - Throws an error if any parameter is invalid.
 */
function calculateExpectedReturn(investmentAmount, annualReturnRate, years) {
    // Input validation
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error('Invalid investment amount. It must be a positive number.');
    }
    if (typeof annualReturnRate !== 'number' || annualReturnRate < 0) {
        throw new Error('Invalid annual return rate. It must be a non-negative number.');
    }
    if (typeof years !== 'number' || years <= 0) {
        throw new Error('Invalid duration. It must be a positive number.');
    }

    // Calculate the expected return using compound interest formula
    const expectedReturn = investmentAmount * Math.pow((1 + annualReturnRate), years);
    return expectedReturn;
}

// Function to display the investment strategy results
/**
 * Displays the expected return in the web interface.
 * 
 * @param {number} expectedReturn - The expected return to display.
 */
function displayExpectedReturn(expectedReturn) {
    const resultElement = document.getElementById('result');
    if (resultElement) {
        resultElement.textContent = `Expected Return: $${expectedReturn.toFixed(2)}`;
    } else {
        console.error('Result element not found in the DOM.');
    }
}

// Event listener for the form submission
document.getElementById('investmentForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Retrieve input values
    const investmentAmount = parseFloat(document.getElementById('investmentAmount').value);
    const annualReturnRate = parseFloat(document.getElementById('annualReturnRate').value) / 100; // Convert percentage to decimal
    const years = parseInt(document.getElementById('years').value, 10);

    try {
        // Calculate expected return
        const expectedReturn = calculateExpectedReturn(investmentAmount, annualReturnRate, years);
        // Display the result
        displayExpectedReturn(expectedReturn);
    } catch (error) {
        console.error('Error calculating expected return:', error.message);
        alert('An error occurred: ' + error.message);
    }
});
```

```html
<!-- HTML Structure for the Investment Strategy Application -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Strategy Application</title>
</head>
<body>
    <h1>Investment Strategy Calculator</h1>
    <form id="investmentForm">
        <label for="investmentAmount">Investment Amount ($):</label>
        <input type="number" id="investmentAmount" required min="0.01" step="0.01"><br>

        <label for="annualReturnRate">Expected Annual Return Rate (%):</label>
        <input type="number" id="annualReturnRate" required min="0" step="0.01"><br>

        <label for="years">Investment Duration (years):</label>
        <input type="number" id="years" required min="1"><br>

        <button type="submit">Calculate Expected Return</button>
    </form>

    <div id="result"></div>

    <script src="investmentStrategy.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
