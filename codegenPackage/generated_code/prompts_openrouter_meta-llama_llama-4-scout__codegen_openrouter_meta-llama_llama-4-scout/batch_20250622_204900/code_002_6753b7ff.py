"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Generate JavaScript code for a simple EMI calculator that takes loan amount, interest rate, and tenure as inputs.
Generated: DETERMINISTIC_6753b7ff08596b84
Batch ID: 20250622_204900
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the EMI for a loan based on the loan amount, interest rate, and tenure.
 * 
 * @param {number} loanAmount The loan amount.
 * @param {number} interestRate The annual interest rate (in percent).
 * @param {number} tenure The loan tenure (in years).
 * @returns {number} The calculated EMI.
 */
function calculateEmi(loanAmount, interestRate, tenure) {
    // Check for invalid inputs
    if (loanAmount <= 0 || interestRate <= 0 || tenure <= 0) {
        throw new Error("Loan amount, interest rate, and tenure must be positive numbers.");
    }

    // Convert interest rate from percent to a decimal
    const monthlyInterestRate = (interestRate / 100) / 12;
    // Calculate the number of monthly installments
    const numberOfMonths = tenure * 12;

    // Calculate EMI using the formula: EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
    // Where P is the loan amount, r is the monthly interest rate, and n is the number of months
    const emi = loanAmount * monthlyInterestRate * Math.pow((1 + monthlyInterestRate), numberOfMonths) / (Math.pow((1 + monthlyInterestRate), numberOfMonths) - 1);

    return emi.toFixed(2); // Round to 2 decimal places
}

// Example usage
try {
    const loanAmount = 100000; // Loan amount
    const interestRate = 10; // Interest rate (in percent)
    const tenure = 5; // Tenure (in years)

    const emi = calculateEmi(loanAmount, interestRate, tenure);
    console.log(`The EMI for a loan of ₹${loanAmount} at ${interestRate}% interest for ${tenure} years is: ₹${emi}`);
} catch (error) {
    console.error(error.message);
}

// Create a simple EMI calculator interface
class EMICalculator {
    constructor() {
        this.loanAmountInput = document.getElementById('loan-amount');
        this.interestRateInput = document.getElementById('interest-rate');
        this.tenureInput = document.getElementById('tenure');
        this.emiOutput = document.getElementById('emi-output');
        this.calculateButton = document.getElementById('calculate-button');

        this.calculateButton.addEventListener('click', () => this.calculateAndDisplayEmi());
    }

    calculateAndDisplayEmi() {
        try {
            const loanAmount = parseFloat(this.loanAmountInput.value);
            const interestRate = parseFloat(this.interestRateInput.value);
            const tenure = parseFloat(this.tenureInput.value);

            if (isNaN(loanAmount) || isNaN(interestRate) || isNaN(tenure)) {
                throw new Error("Please enter valid numbers for loan amount, interest rate, and tenure.");
            }

            const emi = calculateEmi(loanAmount, interestRate, tenure);
            this.emiOutput.textContent = `EMI: ₹${emi}`;
        } catch (error) {
            this.emiOutput.textContent = `Error: ${error.message}`;
        }
    }
}

// Initialize the EMI calculator interface
document.addEventListener('DOMContentLoaded', () => {
    new EMICalculator();
});
```

```html
<!-- Simple HTML interface for EMI calculator -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EMI Calculator</title>
    <style>
        /* Basic styling for the interface */
        body {
            font-family: Arial, sans-serif;
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input {
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        #emi-output {
            font-weight: bold;
            font-size: 18px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h2>EMI Calculator</h2>
    <label for="loan-amount">Loan Amount:</label>
    <input type="number" id="loan-amount" required>

    <label for="interest-rate">Interest Rate (%):</label>
    <input type="number" id="interest-rate" required>

    <label for="tenure">Tenure (years):</label>
    <input type="number" id="tenure" required>

    <button id="calculate-button">Calculate EMI</button>

    <div id="emi-output"></div>

    <script src="emi-calculator.js"></script>
</body>
</html>
```
