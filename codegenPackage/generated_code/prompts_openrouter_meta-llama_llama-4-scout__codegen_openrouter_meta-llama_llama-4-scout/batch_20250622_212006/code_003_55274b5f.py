"""
Generated Code Metadata:
========================
Original URL: https://prospectlimited.com
Prompt: "Design a simple investment calculator in HTML and CSS that takes into account the different investment plans offered by Prospect Limited, including the Starter, Standard, Premium, Gold, and Executive plans."
Generated: DETERMINISTIC_55274b5f69ef8618
Batch ID: 20250622_212006
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
    <title>Prospect Limited Investment Calculator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Prospect Limited Investment Calculator</h1>
    <form id="investment-form">
        <label for="investment-plan">Select Investment Plan:</label>
        <select id="investment-plan" name="investment-plan">
            <option value="starter">Starter (5% interest)</option>
            <option value="standard">Standard (7% interest)</option>
            <option value="premium">Premium (10% interest)</option>
            <option value="gold">Gold (12% interest)</option>
            <option value="executive">Executive (15% interest)</option>
        </select>
        <br><br>
        <label for="investment-amount">Investment Amount:</label>
        <input type="number" id="investment-amount" name="investment-amount" required>
        <br><br>
        <label for="investment-term">Investment Term (years):</label>
        <input type="number" id="investment-term" name="investment-term" required>
        <br><br>
        <button id="calculate-btn">Calculate</button>
    </form>
    <div id="result"></div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

form {
    width: 50%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
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
    width: 50%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```

**script.js**
```javascript
// Get elements
const form = document.getElementById('investment-form');
const investmentPlanSelect = document.getElementById('investment-plan');
const investmentAmountInput = document.getElementById('investment-amount');
const investmentTermInput = document.getElementById('investment-term');
const calculateBtn = document.getElementById('calculate-btn');
const resultDiv = document.getElementById('result');

// Define investment plans
const investmentPlans = {
    starter: 0.05,
    standard: 0.07,
    premium: 0.10,
    gold: 0.12,
    executive: 0.15
};

// Add event listener to calculate button
calculateBtn.addEventListener('click', (e) => {
    e.preventDefault();

    try {
        // Get input values
        const investmentPlan = investmentPlanSelect.value;
        const investmentAmount = parseFloat(investmentAmountInput.value);
        const investmentTerm = parseInt(investmentTermInput.value);

        // Validate input values
        if (isNaN(investmentAmount) || investmentAmount <= 0) {
            throw new Error('Invalid investment amount');
        }

        if (isNaN(investmentTerm) || investmentTerm <= 0) {
            throw new Error('Invalid investment term');
        }

        // Calculate investment return
        const interestRate = investmentPlans[investmentPlan];
        const investmentReturn = investmentAmount * Math.pow(1 + interestRate, investmentTerm);
        const totalReturn = investmentReturn.toFixed(2);

        // Display result
        resultDiv.innerHTML = `
            <h2>Investment Result</h2>
            <p>Investment Plan: ${investmentPlan.charAt(0).toUpperCase() + investmentPlan.slice(1)}</p>
            <p>Investment Amount: $${investmentAmount.toFixed(2)}</p>
            <p>Investment Term: ${investmentTerm} years</p>
            <p>Total Return: $${totalReturn}</p>
        `;
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: red">${error.message}</p>`;
    }
});
```
