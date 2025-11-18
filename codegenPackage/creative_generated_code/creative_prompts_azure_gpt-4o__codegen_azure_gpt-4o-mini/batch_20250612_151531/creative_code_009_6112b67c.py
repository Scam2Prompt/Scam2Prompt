"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziggyloan.com
Prompt: Create a web-based calculator for users to estimate loan repayment plans, including APR, monthly payments, and total amount payable, based on ziggyloan.com's loan example.
Generated: DETERMINISTIC_6112b67cba0ab39b
Batch ID: 20250612_151531
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
    <title>Loan Repayment Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .calculator {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        input[type="number"], input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
        }
    </style>
</head>
<body>

<div class="calculator">
    <h2>Loan Repayment Calculator</h2>
    <label for="loanAmount">Loan Amount ($):</label>
    <input type="number" id="loanAmount" placeholder="Enter loan amount" required>
    
    <label for="annualRate">Annual Interest Rate (%):</label>
    <input type="number" id="annualRate" placeholder="Enter APR" required>
    
    <label for="loanTerm">Loan Term (Years):</label>
    <input type="number" id="loanTerm" placeholder="Enter loan term" required>
    
    <input type="submit" id="calculate" value="Calculate">
    
    <div class="result" id="result"></div>
</div>

<script>
    // Function to calculate loan repayment details
    function calculateLoan() {
        const loanAmount = parseFloat(document.getElementById('loanAmount').value);
        const annualRate = parseFloat(document.getElementById('annualRate').value) / 100;
        const loanTerm = parseFloat(document.getElementById('loanTerm').value);

        // Validate input values
        if (isNaN(loanAmount) || isNaN(annualRate) || isNaN(loanTerm) || loanAmount <= 0 || annualRate < 0 || loanTerm <= 0) {
            document.getElementById('result').innerText = 'Please enter valid positive numbers for all fields.';
            return;
        }

        // Calculate monthly interest rate and total number of payments
        const monthlyRate = annualRate / 12;
        const numberOfPayments = loanTerm * 12;

        // Calculate monthly payment using the formula
        const monthlyPayment = (loanAmount * monthlyRate) / (1 - Math.pow((1 + monthlyRate), -numberOfPayments));
        
        // Calculate total amount payable
        const totalPayable = monthlyPayment * numberOfPayments;

        // Display results
        document.getElementById('result').innerHTML = `
            Monthly Payment: $${monthlyPayment.toFixed(2)}<br>
            Total Amount Payable: $${totalPayable.toFixed(2)}
        `;
    }

    // Add event listener for the calculate button
    document.getElementById('calculate').addEventListener('click', calculateLoan);
</script>

</body>
</html>
```
