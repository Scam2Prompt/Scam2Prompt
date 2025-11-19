"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Illustrate how to implement a loan calculator in a web application that mimics the settlement loan calculator from Rhino Finance.
Generated: DETERMINISTIC_17c69edf181995a6
Batch ID: 20250612_155712
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
    <title>Loan Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            max-width: 600px;
            background-color: #f4f4f4;
        }
        input, button {
            margin: 10px 0;
            padding: 10px;
            width: calc(100% - 22px);
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background-color: #e0ffe0;
            border: 1px solid #b2ffb2;
        }
    </style>
</head>
<body>

    <h1>Loan Calculator</h1>
    <form id="loan-form">
        <label for="amount">Loan Amount:</label>
        <input type="number" id="amount" required>

        <label for="interest">Annual Interest Rate (%):</label>
        <input type="number" id="interest" required>

        <label for="years">Loan Term (Years):</label>
        <input type="number" id="years" required>

        <button type="submit">Calculate</button>
    </form>

    <div class="result" id="result" style="display:none;"></div>

    <script>
        // Function to calculate monthly payment
        function calculateMonthlyPayment(principal, interest, years) {
            // Convert annual interest rate to monthly and decimal
            const monthlyInterest = interest / 100 / 12;
            const numberOfPayments = years * 12;

            // Calculate monthly payment using formula
            const monthlyPayment = (principal * monthlyInterest) / 
                (1 - Math.pow((1 + monthlyInterest), -numberOfPayments));

            return monthlyPayment;
        }

        // Event listener for form submission
        document.getElementById('loan-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form from submitting

            // Get user inputs
            const amount = parseFloat(document.getElementById('amount').value);
            const interest = parseFloat(document.getElementById('interest').value);
            const years = parseInt(document.getElementById('years').value, 10);

            // Validate inputs
            if (isNaN(amount) || amount <= 0 || 
                isNaN(interest) || interest <= 0 || 
                isNaN(years) || years <= 0) {
                alert('Please enter valid positive numbers for all fields.');
                return;
            }

            // Calculate monthly payment
            const monthlyPayment = calculateMonthlyPayment(amount, interest, years).toFixed(2);

            // Display the result
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = `Monthly Payment: $${monthlyPayment}`;
        });
    </script>

</body>
</html>
```
