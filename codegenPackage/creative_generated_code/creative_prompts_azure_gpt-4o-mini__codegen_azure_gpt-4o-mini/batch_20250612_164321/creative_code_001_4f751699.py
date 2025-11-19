"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuotaschevrolet.com.ar
Prompt: Can you provide code examples for integrating a financing calculator for Chevrolet cars on a website?
Generated: DETERMINISTIC_4f751699cc9125a0
Batch ID: 20250612_164321
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
    <title>Chevrolet Financing Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .calculator {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .calculator input {
            width: 100%;
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .calculator button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .calculator button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="calculator">
    <h2>Chevrolet Financing Calculator</h2>
    <label for="loanAmount">Loan Amount ($):</label>
    <input type="number" id="loanAmount" placeholder="Enter loan amount" required>

    <label for="interestRate">Interest Rate (%):</label>
    <input type="number" id="interestRate" placeholder="Enter interest rate" required>

    <label for="loanTerm">Loan Term (Years):</label>
    <input type="number" id="loanTerm" placeholder="Enter loan term" required>

    <button id="calculateBtn">Calculate Monthly Payment</button>
    <div class="result" id="result"></div>
</div>

<script>
    // Function to calculate monthly payment
    function calculateMonthlyPayment(principal, interestRate, years) {
        // Validate input
        if (principal <= 0 || interestRate <= 0 || years <= 0) {
            throw new Error("All input values must be greater than zero.");
        }

        // Convert annual interest rate to monthly and decimal
        const monthlyRate = (interestRate / 100) / 12;
        const numberOfPayments = years * 12;

        // Calculate monthly payment using the formula
        const monthlyPayment = (principal * monthlyRate) / (1 - Math.pow((1 + monthlyRate), -numberOfPayments));

        return monthlyPayment.toFixed(2); // Return payment rounded to 2 decimal places
    }

    // Event listener for button click
    document.getElementById("calculateBtn").addEventListener("click", function() {
        try {
            // Get input values
            const loanAmount = parseFloat(document.getElementById("loanAmount").value);
            const interestRate = parseFloat(document.getElementById("interestRate").value);
            const loanTerm = parseFloat(document.getElementById("loanTerm").value);

            // Calculate the monthly payment
            const monthlyPayment = calculateMonthlyPayment(loanAmount, interestRate, loanTerm);

            // Display the result
            document.getElementById("result").innerText = `Monthly Payment: $${monthlyPayment}`;
        } catch (error) {
            // Handle errors and display to user
            document.getElementById("result").innerText = `Error: ${error.message}`;
        }
    });
</script>

</body>
</html>
```
